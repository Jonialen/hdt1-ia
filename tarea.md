<!-- tarea.md (tarea.md) -->

# Task 1 - Análisis de Racionalidad y Métricas

### 1) Propongan dos (2) métricas de desempeño distintas para este agente
- Metrica A: Carros sin movimiento por más de 1 minuto
- Metrica B: Humano este esperando para cruazar por menos de 1 un minuto

### Describa un escenario específico donde el agente actuaría de manera "racional" bajo la Métrica A, pero esa acción sería considerada un desastre bajo la Métrica B
#### Metrica A
El sémaforo esta la mayor parte del tiempo en verde para el carro, priorizando que su flujo sea mayor, buscando mantener su metrica lo mas cercana a 0 lo antes posible.

#### Metrica B
Cada vez que detecta que hay un humano pone el semaforo en rojo para los carros haciendo que los humanos puedan pasar, priorizando que su metrica sea lo mas grande posbile para tener más humanos no esperando por mas de un minuto

### Basándose en la diapositiva de Incertidumbre, explique por qué este entorno de tráfico nunca podrá ser Completamente Observable y cómo la "Limitante en sensores" afecta la racionalidad de su agente.
Los sensores pueden fallar facilmente por el hecho de que por ejemplo en vista hermosa los detectores de velocidad si vas muy rapido no son capaces de detectarte haciendo que sus metricas puedan estar herradas, a su vez los sensores o el ambiente en si puede estar "engañado" al agente, por ejemplo si la calle esta en reparaciones y no hay flujo, en el escenario 1, estaria siendo eficiente porque la metrica estaria cercana a 0 (lo desable) pero el contexto del porque afecta su proposito en si, esto ya que no es completamente observable el ambiente y le "oculta" que la calle no esta siendo utilizada

# Task 2 – PEAS y Entornos
## 1) Complete la siguiente descripción del agente:
### P (Performance/Desempeño):
- Metros cuadrados limpiados por hora
- Porcentaje de efectividad de limpieza por panel
- Desgaste de utensilos de limpieza por dia

### E (Environment/Entorno):
- Lo rodea el clima, polvo, los paneles, lluvia, rieles, sus sensores, sus mecanismos internos.

### A (Actuators/Actuadores):
- Su cepillo y y agua.

### S (Sensors/Sensores):
- Que tan reflectivo es el panel

## 2) Clasifique el entorno de este robot según las 4 dimensiones vistas en clase.
### ¿Completamente o Parcialmente observable?
- Es paracialmente observable ya que el robot no puede persivir todas las cosas que pasan en su entorno ademas el clima o por ejemplo un riel roto u oxidado que impida contunar con su funcionamiento

### ¿Determinístico o Estocástico? (Considere el factor clima y suciedad)
- Es estocastico principalmente por el clima el cual es muy dificil de predecir y solo se pueden conseguir aproximaciones pero que pueden distar enormente de la realidad ademas cosas como el viento acumulando polvo es algo no predecible

### ¿Discreto o Continuo? (Analice los estados del movimiento y la suciedad)
- Es discreto, a unque se pudieran configurar lugares de limpieza las partes mecanicas son impresisas y no siempre terminarian en el mismo lugar, ademas de cosas como el oxido y polvo afectarian a la movilidad agregando posibles estados de cada cosa, como tapar sensores, aumentar el grosor de lo que hay que limpiar, etc.

### Benigno o Adverso? (¿El polvo "juega" en contra del robot intencionalmente?)
- Es beningo, a pesar de que el polvo, clima, y demas cosas afectan negativamente al robot, no estan en contra de el en el sentido de tener un adversario, el clima es indiferente si estuviera o no, solo es "hace su trabajo natural"

# Task 3 - Modelado
## Describa abstractamente cómo representaría el "estado" de un panel solar en una estructura de datos (grafo, matriz, vector, etc.).
Lo meteria en un vector donde cada entrada describe de forma analoga una carateristica por ejemplo (susiedad, daño, humedad), (0...1, 0...1, 0...1)

## Si el robot tiene un modelo del panel, ¿qué significa "inferir" la siguiente acción? Relacionarlo con: f(estado) => acción.
Significa que el robot va a ver su estado y talvez su memoria si tiene y en base a eso va a decidir lo que hara, si hay mucha suciedad y aun tiene agua suficiente, usa x cantidad de agua.

## ¿Qué parámetro del modelo debería ajustarse si el robot nota que, tras limpiar un panel muy sucio con poca agua, el panel sigue sucio?
La cantidad de agua que usa segun el nivel de suciedad que detecta en el estado, aumentar esa relacion de cantidad de agua x nivel de suciedad es el que abria que ajustar si el modelo no cumple con lo esperado.

