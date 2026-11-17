# bioestadistica-nutrigenomica-presentacion

Presentaciones de inferencia estadística (distribuciones, estimación por intervalos y contrastes de hipótesis) con ejemplos de Nutrigenómica, para el máster en Metodología de la Investigación en Nutrigenómica y Nutrigenética.

Para generar las diapositivas: `quarto render` (se publican en `docs/`).

## Libro en PDF

La carpeta `libro/` contiene un libro de Quarto con las tres presentaciones en formato de texto, con narraciones que conectan los conceptos. El PDF publicado está en `docs/inferencia-estadistica-nutrigenomica.pdf`.

Los capítulos del libro se generan a partir de las presentaciones con `libro/scripts/convertir.py`, que elimina la sintaxis propia de las diapositivas e inserta los textos de `libro/scripts/narrativa.py`. Para regenerar el libro después de cambiar las presentaciones:

```bash
python3 libro/scripts/convertir.py .
cd libro && quarto render --to pdf
cp _book/inferencia-estadistica-nutrigenomica.pdf ../docs/
```

Requiere una instalación de LaTeX con XeLaTeX y la fuente Libertinus.

Paquetes de R necesarios: `tidyverse`, `knitr`, `svglite`, `patchwork`, `pwr`.

## Licencia

[CC BY-NC-SA 3.0 España](https://creativecommons.org/licenses/by-nc-sa/3.0/es/), Alfredo Sánchez Alberca.
