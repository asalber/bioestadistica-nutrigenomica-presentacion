"""Convierte las presentaciones revealjs en capítulos de libro e inserta la narración."""
import re, sys, importlib.util, pathlib

raiz = pathlib.Path(sys.argv[1])
spec = importlib.util.spec_from_file_location("narrativa", pathlib.Path(__file__).with_name("narrativa.py"))
nar = importlib.util.module_from_spec(spec); spec.loader.exec_module(nar)

CONFIG_PDF = '''```{r}
#| include: false
#| cache: false
knitr::opts_chunk$set(dev = "cairo_pdf", fig.pos = "H", out.width = "100%")
# Tablas LaTeX simples (sin longtable) en el PDF
kable <- function(...) knitr::kable(..., format = "latex", booktabs = TRUE, linesep = "")
```
'''

def convertir(origen, destino, capitulo):
    n = nar.CAPITULOS[capitulo]
    lineas = (raiz / origen).read_text().split("\n")
    # Quitar cabecera YAML
    assert lineas[0] == "---"
    fin = lineas.index("---", 1)
    lineas = lineas[fin + 1:]
    out = [f"# {n['titulo']} {{#sec-{capitulo}}}", "", n["intro"].strip(), ""]
    pila = []          # pila de divs abiertos: True si se conserva
    en_main_title = False
    i = 0
    while i < len(lineas):
        l = lineas[i]
        s = l.strip()
        # Inclusión de la configuración
        if s.startswith("{{< include _configuracion-r.qmd"):
            out += ["{{< include _configuracion-r.qmd >}}", "", CONFIG_PDF]
            i += 1; continue
        # Diapositivas de sección: ## {background-color= .myblue} + main-title
        if s.startswith("## {background-color"):
            # buscar el título en el bloque main-title siguiente
            j = i + 1
            while not lineas[j].strip().startswith(":::{.main-title}"):
                j += 1
            titulo = lineas[j + 1].strip()
            out += [f"## {titulo}", ""]
            if titulo in n["secciones"]:
                out += [n["secciones"][titulo].strip(), ""]
            i = j + 3  # salta :::{.main-title}, título y :::
            continue
        # Cabeceras de diapositiva
        m = re.match(r"^(#{2,3}) (.+?)(\s*\{[^}]*\})?$", l)
        if m and not pila:
            nivel = len(m.group(1)) + 1
            titulo = m.group(2).strip()
            clave = titulo
            if clave in n.get("antes", {}):
                out += [n["antes"][clave].strip(), ""]
            out += ["#" * nivel + " " + titulo, ""]
            if clave in n["diapositivas"]:
                out += [n["diapositivas"][clave].strip(), ""]
            i += 1; continue
        # Separadores de diapositiva
        if s == "---":
            i += 1; continue
        # details/summary -> callout de solución
        if s == "<details>":
            out += ["::: {.callout-tip}", "## Solución"]
            i += 2  # salta <summary>
            continue
        if s == "</details>":
            out += [":::"]
            i += 1; continue
        # Divs
        if s.startswith(":::"):
            resto = s.lstrip(":").strip()
            if resto:  # apertura
                quitar = any(c in resto for c in ["{.columns}", ".column", "{.centered}", "{.destacado}"])
                tipo = "teorema" if re.match(r"\{#(def|thm|exm|exr)-", resto) else "otro"
                pila.append((not quitar, tipo))
                # Texto narrativo antes de ejercicios, ejemplos, etc.
                mid = re.match(r"\{#([\w-]+)\}", resto)
                if mid and mid.group(1) in n.get("antes_bloque", {}):
                    out += [n["antes_bloque"][mid.group(1)].strip(), ""]
                if not quitar:
                    out.append(l)
                i += 1
                if mid and mid.group(1) in n.get("despues_bloque", {}):
                    # se inserta al cerrar este bloque
                    pila[-1] = (pila[-1][0], pila[-1][1], mid.group(1))
                continue
            else:  # cierre
                abierto = pila.pop()
                if abierto[0]:
                    out.append(l)
                if len(abierto) == 3:
                    out += ["", n["despues_bloque"][abierto[2]].strip()]
                i += 1; continue
        # Gráficos: los de media anchura más estrechos
        if s.startswith("#| fig-width: 6"):
            out += [l, "#| out-width: 60%"]
            i += 1; continue
        out.append(l)
        i += 1
    out += ["", n["cierre"].strip(), ""]
    texto = "\n".join(out)
    texto = re.sub(r"\n{3,}", "\n\n", texto)
    (raiz / "libro" / destino).write_text(texto)

convertir("01-distribuciones.qmd", "01-distribuciones.qmd", "distribuciones")
convertir("02-estimacion.qmd", "02-estimacion.qmd", "estimacion")
convertir("03-contrastes.qmd", "03-contrastes.qmd", "contrastes")
print("ok")
