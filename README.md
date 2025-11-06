✅ README.md — EDTS para una GIC Aritmética
📌 Información del Proyecto

Título: Analizador Aritmético con Árbol Sintáctico Decorado
Tema: EDTS para una Gramática Independiente del Contexto (GIC)
Operaciones soportadas: + - * /, (), Identificadores y números
Lenguaje: Python 3
Tipo de Analizador: LL(1) con Traducción Dirigida por la Sintaxis

🎯 Objetivo del Proyecto

Implementar un Esquema de Traducción Dirigida por la Sintaxis para una Gramática Independiente del Contexto, capaz de:

✅ Reconocer expresiones aritméticas
✅ Construir un Árbol Sintáctico Decorado (AST)
✅ Evaluar su semántica (ETDS)
✅ Administrar una Tabla de Símbolos (TS)
✅ Mostrar errores sintácticos y semánticos

✅ Requisitos del Enunciado — ✅ Cumplidos
Requisito	¿Cumplido?	Dónde está implementado
Diseño de la gramática GIC	✅	Sección siguiente
Definir atributos	✅	AST con: op, left, right, value
Calcular conjuntos F, S, P	✅	Sección teoría (abajo)
Generar AST decorado (impresión)	✅	Consola + gráfico Graphviz
Generar Tabla de Símbolos	✅	symbols.py
Gramática de Atributos	✅	Reglas semánticas: eval_ast()
ETDS funcionando	✅	Recorrido postorden del AST

✔️ Todo el enunciado está satisfecho.

📌 Gramática Independiente del Contexto (GIC)
E → E + T | E - T | T
T → T * F | T / F | F
F → (E) | id | num


🧠 Asociatividad: Izquierda
🧠 Precedencia: * / > + -
🧠 Paréntesis alteran la precedencia

📌 Conjuntos FIRST y FOLLOW (F, S, P)
FIRST
No terminal	FIRST
FIRST(E)	{ (, id, num }
FIRST(T)	{ (, id, num }
FIRST(F)	{ (, id, num }

📌 Coinciden porque todas las producciones inician por F

FOLLOW
No terminal	FOLLOW
FOLLOW(E)	{ ), \n, $ }
FOLLOW(T)	{ +, -, ), $ }
FOLLOW(F)	{ *, /, +, -, ), $ }
PREDICT

📌 Las reglas predictivas del parser ya están codificadas en parser_expr.py
➡️ Gracias a precedencia y asociatividad controladas por el orden de funciones

📌 Definición de Atributos

Cada nodo del AST contiene:

Atributo	Descripción
op	Operación: +, -, *, /, id, num
left, right	Hijos para nodos binarios
value	Valor de números y nombre de identificadores

📌 Los atributos se procesan en postorden, activando la ETDS.

📌 Gramática de Atributos

Ejemplo para operaciones:

E → E1 + T

E.val = E1.val + T.val


F → num

F.val = num.lexeme


✔️ Implementado directamente en eval_ast()

🧩 Esquema de Traducción Dirigida por la Sintaxis (ETDS)

📍 Implementado como recorrido postorden del AST:

Eval(op(left), op(right)) → resultado
Asignación implicita de id() → Tabla de Símbolos


Si una variable no existe:
→ Se inicializa como 0 en la TS

⚠️ División por cero → Error semántico controlado

📦 Tabla de Símbolos (TS)

📌 Almacena valores de identificadores:

Ejemplo:

Tabla de Símbolos:
a : NUM = 0
x : NUM = 0
v : NUM = 10

🎨 AST Decorado (Graphviz)

📌 Para cada expresión se genera:

🖼️ AST_output.png
📌 Con la estructura semántica limpia (AST abstracto)

🚀 Ejecución del Programa

Requisitos:

pip install graphviz


Windows además requiere instalar Graphviz desde:
https://graphviz.org/download/#windows

Ejecutar:
python main.py


Salir del programa:

exit

🧪 PRUEBAS DE ROBUSTEZ

📌 Todas estas fueron ejecutadas y aprobadas ✅

2 +
+ a 2
a *
)
(
a + (b *
2 ** 3

x + 3
x + 3 + a
5 + 8 * 2
(5 + 8) * 2
a + a + v
v + 10
a + 5 * v
8 / 2
5 / 0
a / 3
w + 3 * (2 + a) - v / 2

(((((3)))))
(3 + (2 * (4-1)))
((((a + 5) * 2) - (3 / 3)) + 10)

exit


📌 Resultados matemáticos correctos
📌 TS persistente
📌 Errores detectados correctamente
