CAPITULOS = {}

# ---------------------------------------------------------------------------
# Capítulo 1: distribuciones
# ---------------------------------------------------------------------------
CAPITULOS["distribuciones"] = dict(
    titulo="Distribuciones de probabilidad en Nutrigenómica",
    intro="""
Cualquier análisis estadístico empieza por una pregunta sencilla: ¿cómo se comportan los datos que vamos a medir? Antes de estimar la homocisteína media de un grupo de pacientes, de comparar la pérdida de peso entre genotipos o de decidir si un gen se expresa de forma diferente tras una intervención dietética, necesitamos un modelo que describa cómo se reparten los posibles valores de la variable. Ese modelo es una _distribución de probabilidad_.

En este capítulo repasamos las distribuciones que aparecen con más frecuencia en Nutrigenómica. Para cada una veremos su definición, sus principales características y en qué tipo de variables se utiliza, y la ilustraremos con un ejemplo realista en el que calcularemos probabilidades y visualizaremos su función de densidad o de probabilidad. Al final del capítulo presentamos las distribuciones de los p-valores y de los estadísticos ($\\chi^2$, $T$ y $F$), que serán la base de la estimación y de los contrastes de hipótesis de los capítulos siguientes.
""",
    secciones={
        "¿Por qué necesitamos modelos de distribución?": """
La Nutrigenómica combina datos de naturaleza muy distinta: medidas antropométricas y bioquímicas, genotipos, niveles de metilación, conteos de lecturas de secuenciación o composiciones de la microbiota. Cada tipo de dato tiene unas propiedades (si es continuo o discreto, si puede ser negativo, si está acotado, si presenta muchos ceros) que condicionan el modelo de probabilidad adecuado. La tabla de esta sección resume los tipos de datos más habituales y el modelo que suele utilizarse para cada uno; a lo largo del capítulo iremos recorriendo cada una de sus filas.
""",
        "Distribuciones continuas": """
Empezamos por las variables continuas, que pueden tomar cualquier valor dentro de un intervalo. Su comportamiento se describe mediante una _función de densidad_ $f(x)$, de manera que la probabilidad de que la variable tome valores en un intervalo es el área bajo la densidad en ese intervalo. Veremos primero la distribución normal, el modelo de referencia para variables simétricas, y después varios modelos para variables positivas y asimétricas, para proporciones y para composiciones.
""",
        "Distribuciones discretas": """
Pasamos ahora a las variables discretas, que toman valores aislados, normalmente números enteros que cuentan algo: alelos, portadores, lecturas de secuenciación o bacterias. Su comportamiento se describe mediante una _función de probabilidad_ $P(X=k)$, que asigna una probabilidad a cada valor posible. Las representaremos con diagramas de barras, en los que la altura de cada barra es la probabilidad de ese valor.
""",
        "Distribuciones de p-valores y de estadísticos": """
Las distribuciones vistas hasta ahora describen variables que medimos directamente en los individuos. En la última parte del capítulo cambiamos de perspectiva y estudiamos distribuciones que describen cantidades calculadas a partir de muestras: los p-valores de los contrastes de hipótesis y los estadísticos que se obtienen al combinar variables normales. No modelan fenotipos, pero son imprescindibles para hacer inferencia.
""",
    },
    diapositivas={
        "Distribución Normal": """
La distribución normal es, con diferencia, la más importante de la estadística. Describe bien muchas variables biológicas que resultan de la suma de muchos efectos pequeños e independientes, y además, como veremos en el capítulo de estimación, es la distribución a la que tienden las medias muestrales cuando el tamaño de la muestra es grande.
""",
        "Distribución Lognormal": """
Muchas variables bioquímicas, como la insulina o los triglicéridos, no son simétricas: solo toman valores positivos y presentan una cola larga hacia la derecha, con unos pocos individuos que alcanzan valores muy elevados. Para estas variables la normal no es un buen modelo. La forma más sencilla de modelarlas es suponer que su logaritmo sí es normal, lo que da lugar a la distribución lognormal.
""",
        "Distribución Gamma": """
La distribución Gamma es una alternativa a la lognormal para variables positivas y asimétricas. Es muy flexible gracias a su parámetro de forma y tiene la ventaja de integrarse de manera natural en los modelos lineales generalizados, por lo que es frecuente en el análisis de biomarcadores como la vitamina D o de ingestas de nutrientes.
""",
        "Distribución Beta": """
Algunas variables son proporciones y, por tanto, solo pueden tomar valores entre 0 y 1. Es el caso del nivel de metilación de un sitio CpG, que mide la proporción de copias del ADN que están metiladas. Para ellas necesitamos una distribución definida en el intervalo $(0,1)$, y la más utilizada es la distribución Beta.
""",
        "Distribución de Dirichlet": """
Cuando en lugar de una proporción tenemos varias que deben sumar 1, como las abundancias relativas de los distintos filos de la microbiota, las proporciones no son independientes: si una aumenta, alguna otra tiene que disminuir. La distribución de Dirichlet extiende la Beta a este tipo de _datos composicionales_.
""",
        "Distribución Binomial": """
La distribución binomial es el modelo básico para contar cuántas veces ocurre un suceso en un número fijo de ensayos independientes. En genética aparece de forma natural: el número de alelos de riesgo que porta una persona en un SNP es el número de «éxitos» en dos ensayos (los dos cromosomas homólogos).
""",
        "Distribución Multinomial": """
La binomial cuenta resultados de ensayos con solo dos posibilidades. Cuando cada ensayo puede dar más de dos resultados, como los tres genotipos posibles de un SNP, la distribución adecuada es la multinomial, que modela conjuntamente cuántas veces aparece cada resultado.
""",
        "Equilibrio de Hardy-Weinberg": """
Una de las aplicaciones más importantes de la distribución multinomial en genética es el equilibrio de Hardy-Weinberg, que relaciona las frecuencias alélicas con las frecuencias genotípicas esperadas en una población con apareamiento aleatorio.
""",
        "Distribución de Poisson": """
Cuando lo que contamos no es el número de éxitos en un número fijo de ensayos, sino el número de sucesos que ocurren en un intervalo de tiempo o de espacio (lecturas de secuenciación de un gen, mutaciones en una región, episodios clínicos por semana), el modelo de referencia es la distribución de Poisson. Su característica principal es que la media y la varianza coinciden.
""",
        "Distribución Binomial Negativa": """
En la práctica, los conteos biológicos casi nunca cumplen que la varianza sea igual a la media. Entre réplicas biológicas, la expresión de un gen varía de un individuo a otro, y eso añade variabilidad a la que tendría un modelo de Poisson. Este fenómeno se llama _sobredispersión_ y la distribución binomial negativa es el modelo estándar para tenerlo en cuenta.
""",
        "Modelos inflados de ceros": """
Un caso extremo de conteos difíciles de modelar se da cuando hay muchos más ceros de los que predice cualquier distribución de conteo habitual. Ocurre, por ejemplo, con bacterias de la microbiota que simplemente no están presentes en una parte de la población. Los modelos inflados de ceros distinguen entre los ceros «estructurales» (el taxón no existe en ese individuo) y los ceros «de muestreo» (el taxón existe pero no se ha detectado).
""",
        "Resumen de distribuciones en Nutrigenómica": """
La siguiente tabla reúne las distribuciones vistas hasta ahora, con sus parámetros, su media, su varianza y los ejemplos de Nutrigenómica en los que se utilizan. Es una buena referencia para elegir el modelo adecuado en cada análisis.
""",
        "Distribución Uniforme de los p-valores": """
En los estudios ómicos se realizan miles o millones de contrastes de hipótesis, uno por cada gen, SNP o sitio CpG. Para interpretar correctamente sus resultados es fundamental conocer cómo se distribuyen los p-valores cuando no hay ningún efecto real. El resultado es sorprendentemente sencillo: siguen una distribución uniforme.
""",
        "Distribución Chi-cuadrado": """
Las tres distribuciones que cierran el capítulo, la chi-cuadrado, la T de Student y la F de Fisher-Snedecor, se construyen a partir de la normal y describen el comportamiento de los estadísticos que calcularemos con las muestras. La primera de ellas surge al sumar cuadrados de variables normales estándar.
""",
        "Distribución T de Student": """
La T de Student surge al dividir una normal estándar entre la raíz de una chi-cuadrado dividida por sus grados de libertad. Esta construcción, que puede parecer artificial, es exactamente la que aparece al estandarizar la media muestral usando la desviación típica estimada en lugar de la poblacional, como veremos en el capítulo siguiente.
""",
        "Distribución F de Fisher-Snedecor": """
Por último, la F de Fisher-Snedecor es el cociente de dos chi-cuadrado divididas por sus grados de libertad. Aparece siempre que comparamos dos varianzas, ya sea directamente o, como en el análisis de la varianza, para comparar varias medias.
""",
        "Forma de las distribuciones de los estadísticos": """
La siguiente figura muestra cómo cambia la forma de estas tres distribuciones con sus grados de libertad. La chi-cuadrado y la F son asimétricas y solo toman valores positivos, mientras que la T es simétrica y, a medida que aumentan los grados de libertad, se confunde con la normal estándar.
""",
    },
    antes={},
    antes_bloque={
        "exm-normal-imc": "Veamos cómo utilizar la distribución normal para comparar el riesgo de obesidad entre dos genotipos de _FTO_.",
        "exm-normal-ldl": "El siguiente ejemplo ilustra una propiedad importante de la normal: un pequeño desplazamiento de la media produce un cambio grande en la proporción de individuos que superan un umbral clínico.",
        "exm-lognormal-trigliceridos": "En el siguiente ejemplo calculamos la proporción de personas con hipertrigliceridemia y comparamos la distribución en la escala original y en la escala logarítmica.",
        "exm-gamma-vitamina-d": "Como ejemplo, comparamos la prevalencia de deficiencia de vitamina D entre portadores y no portadores de una variante del gen _GC_.",
        "exm-beta-metilacion": "El siguiente ejemplo muestra cómo la ingesta de folato desplaza la distribución de la metilación de un CpG de _MTHFR_.",
        "exm-dirichlet-microbiota": "En el siguiente ejemplo modelamos la composición de la microbiota fecal por filos y simulamos la composición de varios voluntarios.",
        "exm-binomial-mthfr": "Veamos un ejemplo con el genotipo TT de _MTHFR_, uno de los más estudiados en nutrigenética por su relación con el metabolismo del folato.",
        "exm-hardy-weinberg": "Si conocemos la frecuencia alélica, podemos calcular cuántos individuos de cada genotipo esperamos en una muestra.",
        "exm-poisson-rnaseq": "Como ejemplo, consideramos el número de lecturas de un gen poco expresado en réplicas técnicas de RNA-seq, en las que la única variabilidad es la del propio proceso de secuenciación.",
        "exm-binomial-negativa-rnaseq": "El siguiente ejemplo compara una Poisson y una binomial negativa con la misma media y muestra las consecuencias de ignorar la sobredispersión.",
        "exm-zinb-microbiota": "Veamos cómo se comporta un modelo inflado de ceros con un taxón de la microbiota que falta en buena parte de los participantes.",
        "exm-uniforme-pvalores": "Una simulación de un estudio de expresión diferencial permite ver esta propiedad y sus consecuencias.",
        "exr-distribuciones": "## Ejercicio\n\nPara terminar el capítulo, proponemos un ejercicio que pone a prueba la capacidad de elegir el modelo de distribución adecuado para distintas variables.",
    },
    despues_bloque={},
    cierre="""
Elegir bien la distribución de cada variable es el primer paso de cualquier análisis, pero en la práctica nunca conocemos sus parámetros: no sabemos cuál es la media real del IMC de los portadores AA de _FTO_ ni la verdadera frecuencia del genotipo TT de _MTHFR_ en nuestra población. En el siguiente capítulo veremos cómo estimar esos parámetros a partir de una muestra y cómo cuantificar la precisión de las estimaciones mediante intervalos de confianza.
""",
)

# ---------------------------------------------------------------------------
# Capítulo 2: estimación
# ---------------------------------------------------------------------------
CAPITULOS["estimacion"] = dict(
    titulo="Estimación de parámetros",
    intro="""
En el capítulo anterior vimos que cada variable puede describirse mediante un modelo de distribución que depende de unos pocos parámetros: la media y la desviación típica en la normal, la proporción de éxitos en la binomial o la tasa en la Poisson. Sin embargo, en un estudio real esos parámetros son desconocidos. El objetivo de la _inferencia estadística_ es precisamente obtener conclusiones sobre ellos a partir de la información de una muestra.

Este capítulo se ocupa de la primera tarea de la inferencia: la _estimación_. Empezaremos distinguiendo entre población, muestra, parámetro y estimador, y estudiaremos cómo se distribuyen los principales estimadores (la media, la cuasivarianza y la proporción muestrales). Esas distribuciones muestrales nos permitirán después construir _intervalos de confianza_, que acompañan cada estimación de una medida de su precisión. Terminaremos con un repaso de los intervalos de confianza más utilizados para una y dos poblaciones.
""",
    secciones={
        "Estimación de parámetros": """
Antes de construir intervalos de confianza necesitamos fijar algunos conceptos básicos y entender cómo varían los estimadores de una muestra a otra.
""",
        "Intervalos de confianza": """
Conocida la distribución de los estimadores, podemos dar un paso más. En lugar de ofrecer un único valor como estimación del parámetro, daremos un intervalo de valores que, con una confianza determinada, contiene al parámetro.
""",
        "Principales intervalos de confianza": """
El razonamiento que hemos seguido para la media y la proporción se aplica a otros parámetros y a la comparación de dos poblaciones. En esta sección reunimos las fórmulas de los intervalos más habituales y las aplicamos a varios ejemplos de Nutrigenómica.
""",
    },
    diapositivas={
        "Población, muestra y parámetros": """
La _población_ es el conjunto de todos los individuos sobre los que queremos sacar conclusiones, por ejemplo, todos los adultos homocigotos TT de _MTHFR_. Como no podemos medirlos a todos, seleccionamos una _muestra_ aleatoria y calculamos en ella las cantidades que nos interesan.
""",
        "Estimador y estimación": """
Conviene distinguir entre el procedimiento que usamos para estimar un parámetro y el resultado concreto que obtenemos al aplicarlo a una muestra. Al primero lo llamamos estimador y al segundo estimación.
""",
        "Propiedades de los estimadores": """
No todos los estimadores son igual de buenos. Para elegir entre ellos se valoran tres propiedades principales.
""",
        "Distribución de la media muestral": """
La media muestral es el estimador más utilizado. Como su valor cambia de una muestra a otra, es una variable aleatoria con su propia distribución, llamada distribución muestral. El siguiente resultado describe su media y su varianza.
""",
        "Teorema central del límite": """
Muchas variables de interés en Nutrigenómica no son normales. Afortunadamente, el teorema central del límite, uno de los resultados más importantes de la estadística, garantiza que la media muestral se distribuye aproximadamente como una normal cuando la muestra es suficientemente grande, sea cual sea la distribución de la población.
""",
        "Distribución de la varianza muestral": """
Para estimar la variabilidad de una población usamos la cuasivarianza muestral $\\hat S^2$, que divide entre $n-1$ en lugar de $n$ para que el estimador sea insesgado. Su distribución está relacionada con la chi-cuadrado que vimos en el capítulo anterior.
""",
        "Distribución de la proporción muestral": """
Cuando la variable de interés es cualitativa, el parámetro es una proporción y el estimador natural es la proporción muestral. Su distribución se deduce de la binomial y, para muestras grandes, del teorema central del límite.
""",
        "Estimación puntual y por intervalos": """
Una estimación puntual, como decir que la homocisteína media de los portadores TT es de 14.44 µmol/l, es un único número que casi con seguridad no coincide exactamente con el valor real del parámetro.
""",
        "Intervalo de confianza": """
La idea es construir, a partir de la muestra, un intervalo que contenga al parámetro con una probabilidad alta fijada de antemano. Formalmente:
""",
        "Interpretación de un intervalo de confianza": """
La interpretación de los intervalos de confianza es una fuente habitual de errores, incluso en artículos científicos. Conviene tener claro qué afirmaciones son correctas y cuáles no.
""",
        "Interpretación frecuentista de un intervalo de confianza": """
La razón de que no podamos hablar de probabilidad una vez calculado el intervalo es que, en el enfoque frecuentista, el parámetro no es aleatorio. La confianza se refiere al procedimiento, y se entiende bien con una simulación.
""",
        "Intervalo para la media con varianza conocida": """
Veamos ahora cómo se construye un intervalo de confianza concreto. Empezamos por el caso más sencillo, la media de una población normal cuya desviación típica conocemos, por ejemplo, por estudios previos. Aunque es una situación poco habitual, ilustra con claridad el razonamiento que seguiremos en el resto de casos.
""",
        "Intervalo para la media con varianza desconocida": """
En la mayoría de los estudios no conocemos la desviación típica de la población y tenemos que estimarla con la misma muestra. Esto introduce una fuente adicional de incertidumbre, que se refleja en que la distribución del estadístico deja de ser normal y pasa a ser una T de Student.
""",
        "Intervalo para una proporción": """
Para variables cualitativas, como ser portador de un genotipo, el parámetro de interés es una proporción. El intervalo se construye igual que para la media, a partir de la aproximación normal de la proporción muestral.
""",
        "Intervalos de confianza para una población": """
La tabla siguiente resume los intervalos de confianza para los parámetros de una población, junto con las condiciones que deben cumplirse para poder aplicarlos.
""",
        "Intervalo para la varianza": """
El intervalo para la varianza es el único de la tabla que no es simétrico respecto a la estimación, porque la distribución chi-cuadrado no es simétrica. Es útil, por ejemplo, para valorar la precisión de un método de medida.
""",
        "Intervalos de confianza para dos poblaciones": """
En Nutrigenómica es muy frecuente comparar dos grupos: dos genotipos, dos dietas o las mediciones antes y después de una intervención. En estos casos el parámetro de interés es una diferencia de medias o de proporciones, o un cociente de varianzas.
""",
        "Diferencia de medias en muestras independientes": """
Empezamos comparando las medias de dos grupos formados por individuos distintos, en este caso los dos genotipos homocigotos de _FTO_.
""",
        "Diferencia de medias en muestras pareadas": """
Cuando medimos a los mismos individuos en dos momentos, las dos muestras no son independientes y hay que tenerlo en cuenta. El diseño pareado elimina la variabilidad entre individuos y suele dar intervalos mucho más precisos.
""",
        "Diferencia de proporciones": """
Para comparar dos proporciones, por ejemplo la proporción de respondedores a una suplementación en dos genotipos, se construye un intervalo para su diferencia.
""",
        "Cociente de varianzas": """
Por último, a veces interesa comparar la variabilidad de dos grupos y no sus medias. En ese caso se construye un intervalo para el cociente de las varianzas, basado en la distribución F.
""",
    },
    antes={},
    antes_bloque={
        "exm-tcl-insulina": "La siguiente simulación permite ver el teorema central del límite en acción con una variable muy asimétrica, la insulina en ayunas.",
        "exm-distribucion-varianza": "Podemos comprobar este resultado con una simulación.",
        "exm-proporcion-muestral": "El resultado anterior permite saber de antemano cuánto variará la frecuencia alélica estimada de una muestra a otra.",
        "exm-ic-media-varianza-conocida": "Apliquemos esta fórmula a un ejemplo con la glucosa en ayunas de los portadores del alelo de riesgo de _TCF7L2_.",
        "exm-ic-media-varianza-desconocida": "Volvamos al ejemplo de la homocisteína en los homocigotos TT de _MTHFR_, que usaremos también en el capítulo de contrastes.",
        "exm-ic-proporcion": "El siguiente ejemplo compara el intervalo de Wald con los de Wilson y Clopper-Pearson.",
        "exr-intervalos": "## Ejercicio\n\nEl siguiente ejercicio permite practicar el cálculo e interpretación de un intervalo de confianza y del tamaño muestral necesario para alcanzar una precisión determinada.",
    },
    despues_bloque={},
    cierre="""
Los intervalos de confianza nos dicen qué valores del parámetro son compatibles con los datos, pero muchas preguntas de investigación se formulan como una decisión: ¿reduce el omega-3 los triglicéridos?, ¿pierden menos peso los portadores del alelo de riesgo de _FTO_? En el siguiente capítulo veremos cómo responder a estas preguntas mediante los contrastes de hipótesis y descubriremos que están estrechamente relacionados con los intervalos de confianza.
""",
)

# ---------------------------------------------------------------------------
# Capítulo 3: contrastes
# ---------------------------------------------------------------------------
CAPITULOS["contrastes"] = dict(
    titulo="Contrastes de hipótesis",
    intro="""
La estimación responde a la pregunta «¿cuánto vale el parámetro?». Pero en investigación muchas veces la pregunta es otra: «¿es cierta esta afirmación sobre el parámetro?». ¿Supera la homocisteína media de los homocigotos TT de _MTHFR_ el umbral de 12 µmol/l? ¿Hay menos hombres que mujeres en una población? ¿Es distinta la diversidad de la microbiota según el tipo de dieta? Los _contrastes de hipótesis_ son el procedimiento estadístico para tomar este tipo de decisiones a partir de una muestra, controlando la probabilidad de equivocarnos.

En este capítulo construiremos los contrastes paso a paso. Primero definiremos las hipótesis y los dos tipos de error que podemos cometer. Después veremos cómo se usa un estadístico para dividir sus valores posibles en una región de aceptación y otra de rechazo, cómo se fija el riesgo $\\alpha$ y cómo se calcula e interpreta el p-valor. Estudiaremos a continuación el riesgo $\\beta$ y la potencia, y su relación con el tamaño del efecto y el tamaño muestral. Para ilustrar todos estos conceptos usaremos dos ejemplos que nos acompañarán a lo largo del capítulo: un contraste sobre la proporción de hombres en una población y otro sobre la homocisteína media de los homocigotos TT de _MTHFR_. Terminaremos con un repaso de los contrastes más utilizados en Nutrigenómica.
""",
    secciones={
        "Introducción a los contrastes de hipótesis": """
Todo contraste empieza por formular dos hipótesis enfrentadas sobre la población y por entender qué errores podemos cometer al decidir entre ellas.
""",
        "Estadístico del contraste y regiones de rechazo": """
Una vez formuladas las hipótesis, necesitamos una regla que nos diga, a la vista de la muestra, si rechazamos o no la hipótesis nula. Esa regla se basa en un estadístico y en la división de sus posibles valores en dos regiones.
""",
        "Riesgo alfa y p-valor": """
Al construir las regiones de rechazo hemos fijado de antemano una probabilidad máxima de error de tipo I. En esta sección formalizamos esa idea, el riesgo $\\alpha$, e introducimos el p-valor, que permite decidir sin calcular explícitamente la región de rechazo y que, además, cuantifica la evidencia en contra de la hipótesis nula.
""",
        "Riesgo beta, potencia y tamaño del efecto": """
Hasta ahora nos hemos centrado en controlar el error de tipo I. Pero un contraste que casi nunca rechaza la hipótesis nula tendría un riesgo $\\alpha$ muy pequeño y sería inútil. En esta sección estudiamos el otro error, el de tipo II, y la capacidad del contraste para detectar efectos reales, que llamamos potencia.
""",
        "Principales contrastes en Nutrigenómica": """
Con los conceptos anteriores ya podemos aplicar e interpretar cualquier contraste. En esta última sección repasamos los contrastes más utilizados en Nutrigenómica, organizados según el tipo de variable y el diseño del estudio, y resolvemos un ejemplo de cada uno.
""",
    },
    diapositivas={
        "Hipótesis estadísticas": """
Una hipótesis estadística es una afirmación sobre la distribución de una o varias variables en la población, normalmente sobre el valor de alguno de sus parámetros. En los contrastes siempre se enfrentan dos hipótesis.
""",
        "El contraste como un juicio": """
La lógica de los contrastes de hipótesis puede resultar poco intuitiva al principio, porque no tratan las dos hipótesis de forma simétrica. Una analogía muy útil es la de un juicio penal.
""",
        "Tipos de contraste": """
La forma de la hipótesis alternativa determina en qué dirección buscamos evidencia en contra de la hipótesis nula, y con ello la forma de la región de rechazo que veremos más adelante.
""",
        "Tipos de errores": """
Como la decisión se toma a partir de una muestra, y no de toda la población, siempre existe la posibilidad de equivocarse. Hay dos maneras de hacerlo.
""",
        "¿Qué error es más grave?": """
Una pregunta natural es cuál de los dos errores debemos evitar con más cuidado. No hay una respuesta general.
""",
        "Estadístico del contraste": """
Para decidir entre las dos hipótesis necesitamos resumir la información de la muestra en un único número que mida hasta qué punto los datos se apartan de lo que esperaríamos si la hipótesis nula fuese cierta.
""",
        "Regiones de aceptación y rechazo": """
La clave para decidir es conocer la distribución del estadístico cuando la hipótesis nula es cierta. Con ella podemos identificar qué valores del estadístico son «raros» si $H_0$ es cierta, y que por tanto nos llevarán a rechazarla.
""",
        "Riesgo alfa o nivel de significación": """
El nivel de significación es la probabilidad que hemos usado para construir la región de rechazo.
""",
        "p-valor": """
Fijar la región de rechazo de antemano tiene un inconveniente: la decisión es la misma tanto si el estadístico cae justo en el límite como si cae muy lejos de él, de modo que no sabemos cuánta evidencia hay en contra de la hipótesis nula. El p-valor resuelve este problema.
""",
        "Regla de decisión": """
El p-valor da lugar a una regla de decisión muy sencilla, que es la que utilizan todos los programas estadísticos.
""",
        "Interpretación del p-valor": """
El p-valor es probablemente el concepto estadístico peor interpretado de la literatura científica. Por eso conviene dejar claro qué es y qué no es.
""",
        "Relación entre contrastes e intervalos de confianza": """
Los contrastes de hipótesis y los intervalos de confianza son dos caras de la misma moneda: ambos se construyen a partir de la distribución del mismo estadístico, y por eso llevan a conclusiones coherentes.
""",
        "Riesgo beta y potencia": """
El riesgo $\\beta$ es la probabilidad de cometer un error de tipo II. Su complementario, la potencia, es la probabilidad de detectar un efecto que realmente existe.
""",
        "Relación entre el riesgo β y el tamaño del efecto": """
En el ejemplo anterior hemos calculado $\\beta$ para una única hipótesis alternativa. Pero $\\beta$ no es un valor único: cuanto mayor es la diferencia que queremos detectar, más separadas están las distribuciones del estimador bajo $H_0$ y bajo $H_1$, y más fácil es distinguirlas.
""",
        "Relación entre los riesgos α y β": """
El segundo factor que influye en $\\beta$ es el propio riesgo $\\alpha$ que fijamos al construir la región de rechazo. Si hacemos más pequeña la región de rechazo para disminuir $\\alpha$, ampliamos la región de aceptación y aumentamos $\\beta$.
""",
        "Relación entre los riesgos y el tamaño muestral": """
Si no podemos cambiar el tamaño del efecto que nos interesa ni queremos asumir un riesgo $\\alpha$ mayor, queda una tercera vía: aumentar la información, es decir, el tamaño de la muestra. Al hacerlo, las distribuciones bajo $H_0$ y $H_1$ se solapan menos.
""",
        "Curva de potencia": """
Reuniendo todo lo anterior, podemos representar la potencia de un contraste en función del verdadero valor del parámetro para distintos tamaños muestrales. Esta _curva de potencia_ resume la capacidad del contraste para detectar diferencias de distinto tamaño.
""",
        "¿De qué depende la potencia?": """
Los ejemplos anteriores muestran que la potencia depende de varios factores, algunos de los cuales están bajo el control del investigador al diseñar el estudio.
""",
        "Tamaño del efecto": """
Como el p-valor depende del tamaño muestral, no sirve para medir la magnitud de un efecto. Para eso se usa el tamaño del efecto, que además es la cantidad que necesitamos para calcular la potencia y el tamaño muestral de un estudio.
""",
        "Curvas de potencia": """
La siguiente figura muestra la potencia del contraste T para comparar dos medias en función del tamaño muestral por grupo, para tamaños del efecto pequeño, mediano y grande. Con un efecto pequeño hacen falta cientos de participantes por grupo para alcanzar una potencia del 80%.
""",
        "Cómo elegir el contraste": """
Existen muchos contrastes distintos, pero elegir el adecuado es sencillo si respondemos a unas pocas preguntas sobre los datos y el diseño del estudio.
""",
        "Resumen de contrastes paramétricos": """
La siguiente tabla resume los contrastes paramétricos más habituales, que suponen un modelo de distribución para la población (normalmente la normal), junto con sus condiciones de aplicación y un ejemplo de Nutrigenómica.
""",
        "Resumen de contrastes para datos categóricos y no paramétricos": """
Cuando la variable es cualitativa o no se cumplen las condiciones de los contrastes paramétricos, se utilizan los contrastes de la siguiente tabla. Los contrastes no paramétricos trabajan con los rangos de los datos y no suponen ninguna distribución concreta para la población.
""",
        "Contraste T para una muestra": """
Empezamos por el contraste sobre la media de una población, que ya hemos utilizado en el ejemplo de la homocisteína. En esta sección, para cada contraste mostramos un resumen de los datos y una tabla con el estadístico, sus grados de libertad, el p-valor y el intervalo de confianza asociado.
""",
        "Contraste para una proporción": """
Para contrastar si una proporción toma un determinado valor se puede usar la aproximación normal o, mejor, el contraste exacto basado en la distribución binomial, como hicimos en el ejemplo de la proporción de hombres.
""",
        "Contraste para una varianza": """
El contraste sobre la varianza de una población normal se basa en la distribución chi-cuadrado de la cuasivarianza muestral que vimos en el capítulo de estimación.
""",
        "Contraste T para dos muestras independientes": """
Para comparar las medias de dos grupos independientes se utiliza el contraste T de Student si las varianzas son iguales, o su versión de Welch si no lo son. Esta última es la opción más segura cuando hay dudas.
""",
        "Contraste T para dos muestras pareadas": """
Cuando las dos muestras están formadas por los mismos individuos, el contraste se reduce a un contraste T para una muestra aplicado a las diferencias.
""",
        "Contraste F de comparación de varianzas": """
El contraste F compara las varianzas de dos poblaciones normales. Además de su interés propio, se usaba tradicionalmente para decidir entre el contraste T de Student y el de Welch.
""",
        "ANOVA de un factor": """
Cuando queremos comparar las medias de más de dos grupos, hacer todos los contrastes T dos a dos aumentaría la probabilidad de algún falso positivo. El análisis de la varianza (ANOVA) contrasta en un solo paso si todas las medias son iguales.
""",
        "Correlación de Pearson": """
Para estudiar la relación lineal entre dos variables cuantitativas se contrasta si el coeficiente de correlación de Pearson poblacional es cero.
""",
        "Contraste de comparación de dos proporciones": """
Para comparar dos proporciones de grupos independientes se usa el contraste Z, que es equivalente al contraste chi-cuadrado de independencia en una tabla $2\\times 2$.
""",
        "Contraste chi-cuadrado de independencia": """
El contraste chi-cuadrado de independencia estudia si dos variables cualitativas están asociadas comparando las frecuencias observadas en una tabla de contingencia con las que esperaríamos si fuesen independientes.
""",
        "Contraste del equilibrio de Hardy-Weinberg": """
El contraste chi-cuadrado de bondad de ajuste permite comprobar si los genotipos observados son compatibles con el equilibrio de Hardy-Weinberg que estudiamos en el capítulo de distribuciones. Es un control de calidad habitual en los estudios de genotipado.
""",
        "Contraste exacto de Fisher": """
Cuando algunas frecuencias esperadas son pequeñas, la aproximación chi-cuadrado deja de ser fiable y es preferible el contraste exacto de Fisher, que calcula las probabilidades directamente a partir de la distribución hipergeométrica.
""",
        "Contraste U de Mann-Whitney": """
Si la variable es muy asimétrica y las muestras son pequeñas, el contraste T puede no ser adecuado. El contraste U de Mann-Whitney es su alternativa no paramétrica para dos muestras independientes.
""",
        "Contraste de Kruskal-Wallis": """
El contraste de Kruskal-Wallis generaliza el de Mann-Whitney a más de dos grupos y es la alternativa no paramétrica al ANOVA.
""",
        "Corrección por comparaciones múltiples": """
Como vimos al estudiar la distribución uniforme de los p-valores, cuando se realizan muchos contrastes a la vez el número de falsos positivos se dispara. Las correcciones por comparaciones múltiples ajustan los p-valores para controlarlo.
""",
    },
    antes={},
    antes_bloque={
        "exm-hipotesis": "Por ejemplo, en el estudio de la pérdida de peso según el genotipo de _FTO_ las hipótesis serían:",
        "exm-errores": "Un ejemplo ayuda a entender las consecuencias prácticas de cada tipo de error.",
        "exm-hombres-estadistico": "Presentamos ahora el primero de los dos ejemplos que nos acompañarán durante todo el capítulo. Es deliberadamente sencillo, porque el estadístico sigue una distribución binomial y todas las probabilidades se pueden calcular a mano.",
        "exm-estadistico-contraste": "El segundo ejemplo es más realista y utiliza un estadístico con distribución T de Student, como la mayoría de los contrastes sobre medias.",
        "exm-hombres-regiones": "Volvamos al ejemplo de la proporción de hombres para ver cómo se construye la región de rechazo cuando el estadístico es discreto.",
        "exm-regiones-homocisteina": "En el ejemplo de la homocisteína el estadístico es continuo y la región de rechazo queda determinada por un único valor crítico.",
        "exm-hombres-p-valor": "En el ejemplo de la proporción de hombres el p-valor es una probabilidad binomial que se calcula directamente.",
        "exm-p-valor": "En el ejemplo de la homocisteína el p-valor se obtiene de la distribución T de Student.",
        "exm-contraste-intervalo": "Comprobemos esta relación con los datos del estudio de suplementación con omega-3 del capítulo anterior.",
        "exm-hombres-potencia": "Para calcular $\\beta$ necesitamos concretar la hipótesis alternativa, es decir, fijar la diferencia mínima respecto a $H_0$ que consideramos relevante. Veámoslo en el ejemplo de la proporción de hombres.",
        "exm-hombres-tamano-efecto": "En el ejemplo de la proporción de hombres, si aumentamos la diferencia que queremos detectar, la potencia mejora.",
        "exm-hombres-alfa-beta": "En el ejemplo de la proporción de hombres podemos comprobar qué ocurre con $\\beta$ si estamos dispuestos a asumir un riesgo $\\alpha$ mayor.",
        "exm-hombres-tamano-muestral": "En el ejemplo de la proporción de hombres, pasar de 10 a 100 personas cambia por completo la potencia del contraste.",
        "exm-tamano-muestral": "Estas curvas son la base del cálculo del tamaño muestral, que debe hacerse siempre antes de empezar un estudio.",
        "exr-contrastes": "## Ejercicio\n\nPara terminar, el siguiente ejercicio consiste en identificar las hipótesis y el contraste adecuado en varios diseños típicos de Nutrigenómica.",
    },
    despues_bloque={},
    cierre="""
Con este capítulo completamos el recorrido por los fundamentos de la inferencia estadística: los modelos de distribución describen cómo se comportan las variables, la estimación permite cuantificar sus parámetros con una medida de precisión, y los contrastes de hipótesis permiten tomar decisiones controlando los riesgos de error. En cualquier análisis conviene usar las tres herramientas juntas: elegir el modelo adecuado para los datos, acompañar cada p-valor de la estimación del tamaño del efecto y su intervalo de confianza, y diseñar los estudios con la potencia suficiente para detectar los efectos, a menudo pequeños, de las interacciones entre genes y nutrientes.
""",
)
