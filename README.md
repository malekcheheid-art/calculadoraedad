# Calculadora de Edad — Python & C++

> **Actividad 1 — De Revisión Integral (Python & C++)**
> EEST N.º 1 "Eduardo Ader" — Laboratorio de Programación (LPR) — 5° 3° A
> Profesor: Yamil Ganduglia — 1° Cuatrimestre 2026
> **Autor:** Malek Cheheid


---

##  Descripción

Programa que calcula la **edad exacta** de una persona a partir de su fecha de
nacimiento, verificando que la fecha ingresada exista realmente en el calendario
(bisiestos y cantidad de días de cada mes).

La actividad consiste en resolver **el mismo algoritmo en dos lenguajes** —
Python (alto nivel) y C++ (lenguaje estructurado de bajo nivel) — para luego
comparar cómo se expresa la misma lógica en cada uno.

**Fecha actual de referencia:** 8 de julio de 2026 (fija, según el enunciado).

---

##  Requisitos del algoritmo

El programa debe cumplir estas condiciones:

1. **Cálculo base:** `edad = anioActual - anioNacimiento`
2. **Ajuste:** descontar 1 año si la persona **todavía no cumplió** años en el
   mes o día actual.
3. **Validación:** rechazar fechas imposibles (día 35, mes 13, 29 de febrero en
   años no bisiestos, año 20900, etc.).
4. **Fecha futura:** en la versión de Python también se rechazan las fechas de
   nacimiento posteriores a la fecha de referencia.

### El condicional central (la parte a completar)

```c
if (mesN > mesA || (mesN == mesA && diaN > diaA))
    edad = edad - 1;
```

Equivalente en Python:

```python
if mesN > mesA or (mesN == mesA and diaN > diaA):
    edad = edad - 1
```

**Regla de los años bisiestos** (implementada en `esBisiesto`):

```
(anio % 4 == 0 && anio % 100 != 0) || (anio % 400 == 0)
```

---

## Estructura de carpetas

```
/calculadoraedad/
├── .gitignore <-- Archivo para que Git ignore los archivos pesados
├── README.md <-- Descripción breve del ejercicio de revisión
├── LICENSE <-- Descripción breve de la licencia
├── docs/ <-- Carpeta exclusiva para documentación
│ └── InformeProyectoCalculadoraEdad.pdf <-- Archivo de información del Proyecto
├── proyecto_cpp/ <-- Carpeta exclusiva para el código de C++
│ └── calculadoraEdad.cpp <-- Archivo de código en C++
└── proyecto_python/ <-- Carpeta exclusiva para el código de Python
 └── calculadoraEdad.py <-- Archivo de código en Python
```

---

##  Cómo ejecutar

### Python

No requiere instalar nada (solo Python 3).

```bash
cd proyecto_python
python calculadoraEdad.py
```

El programa pide el **día**, **mes** y **año** por separado:

```
=====================================================
    CALCULADORA EN PYTHON DE: Malek Cheheid
=====================================================
Ingrese Dia de nacimiento: 8
Ingrese Mes de nacimiento: 7
Ingrese Anio de nacimiento: 2008

[SISTEMA] Fecha de hoy: 8/7/2026
[SISTEMA] Edad calculada: 18 anos.
```

Si lo ejecutás con doble clic o con el botón **Run** de VS Code no vas a poder
escribir nada: el archivo detecta esa situación y te explica cómo correrlo
desde la terminal.

### C++

**Opción 1 — Local (Windows con MSYS2 / MinGW):**

```bash
g++ -std=c++17 -O2 proyecto_cpp/calculadoraEdad.cpp -o proyecto_cpp/calculadoraEdad.exe
proyecto_cpp/calculadoraEdad.exe
```

**Opción 2 — Online (OnlineGDB, sin instalar nada):**

1. Entrá a <https://www.onlinegdb.com/online_c++_compiler>
2. Pegá el contenido de `proyecto_cpp/calculadoraEdad.cpp`
3. Presioná **Run** y capturá la salida

> La versión C++ pide día, mes y año **en una sola línea**, separados por
> espacios: `8 7 2008`

---

##  Casos de prueba verificados

| Caso | Entrada | Resultado esperado |
|---|---|---|
| Cumple años **hoy mismo** (8/7/2008) | `8 7 2008` | 18 años |
| Cumple años **mañana** (9/7/2008) | `9 7 2008` | 17 años *(ajustado)* |
| Cumple años **ayer** (7/7/2008) | `7 7 2008` | 18 años |
| Mes posterior, día anterior (7/8/2008) | `7 8 2008` | 17 años *(ajustado)* |
| Mes anterior (8/6/2008) | `8 6 2008` | 18 años |
| 29 de febrero **bisiesto** (29/2/2008) | `29 2 2008` | 18 años |
| 29 de febrero **no bisiesto** (29/2/2007) | `29 2 2007` | ❌ Fecha inválida |
| 1900 **no** es bisiesto (29/2/1900) | `29 2 1900` | ❌ Fecha inválida |
| 2000 **sí** es bisiesto (29/2/2000) | `29 2 2000` | 26 años |
| 31 de abril | `31 4 2000` | ❌ Fecha inválida |
| Mes 13 | `1 13 2000` | ❌ Fecha inválida |
| Día 0 | `0 1 2000` | ❌ Fecha inválida |
| Año 20900 | `1 1 20900` | ❌ Fecha inválida |
| Límite inferior (1/1/1900) | `1 1 1900` | 126 años |
| Nacimiento el mismo día de hoy | `8 7 2026` | 0 años |
| Fecha futura | `9 7 2027` | ❌ Fecha inválida *(solo Python)* |
| Texto en vez de número | `abc` | ❌ Error de tipo *(solo Python)* |

---

##  Diferencias entre Python y C++

| Aspecto | Python | C++ |
|---|---|---|
| **Declaración de variables** | Dinámica (no se declara ni se tipa) | Estática: `int diaN, mesN, anioN;` |
| **Entrada por teclado** | `int(input("..."))` | `cin >> diaN >> mesN >> anioN;` |
| **Salida por pantalla** | `print(f"...")` | `cout << "..." << endl;` |
| **Conectores lógicos** | `and`, `or`, `not` | `&&`, `||`, `!` |
| **Devolver valores** | `return` (sin tipo) | `bool esFechaValida(...)` (con tipo) |
| **Verdadero/Falso** | `True` / `False` | `true` / `false` |
| **Namespaces** | Módulos e importaciones | `using namespace std;` |
| **Manejo de errores** | `try / except ValueError / EOFError` | No hay equivalente nativo; `cin` falla silenciosamente |
| **Fin de Sentencia** | No requiere `;` | Requiere `;` |

**Observación importante:** el bloque `try/except` de la versión Python no tiene
un equivalente directo en C++. Ahí, `cin >> anio` deja la variable en un estado
de error si la entrada no es numérica, y el programa continúa con un valor
indeterminado. Esta es una de las ventajas que Python ofrece frente a la
gestión manual de C++.

Por la misma razón, la validación de fechas futuras existe solo en la versión de
Python: en C++ no hay forma cómoda de detectar que la entrada no era numérica.

---

##  Documentación

El informe completo en formato **APA v7** se encuentra en:

```
docs/InformeProyectoCalculadoraEdad.pdf
```

---

##  Licencia

Proyecto con fines educativos bajo la licencia [MIT](LICENSE).