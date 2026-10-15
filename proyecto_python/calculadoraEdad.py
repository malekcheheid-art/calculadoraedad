def es_bisiesto(anio):
    return (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0)


def es_fecha_valida(d, m, a, diaA, mesA, anioA):
    if a < 1900 or a > 2026:
        return False

    if m < 1 or m > 12:
        return False

    if d < 1 or d > 31:
        return False

    if m in [4, 6, 9, 11] and d > 30:
        return False

    if m == 2:
        if es_bisiesto(a):
            if d > 29:
                return False
        else:
            if d > 28:
                return False

    if (a, m, d) > (anioA, mesA, diaA):
        return False

    return True


print("=====================================================")
print("    CALCULADORA EN PYTHON DE: Malek Cheheid    ")
print("=====================================================")

try:
    diaN = int(input("Ingrese Dia de nacimiento: "))
    mesN = int(input("Ingrese Mes de nacimiento: "))
    anioN = int(input("Ingrese Anio de nacimiento: "))

    diaA, mesA, anioA = 8, 7, 2026

    if not es_fecha_valida(diaN, mesN, anioN, diaA, mesA, anioA):
        print("[ERROR] La fecha ingresada no es valida.")
    else:
        edad = anioA - anioN

        if mesN > mesA or (mesN == mesA and diaN > diaA):
            edad = edad - 1

        print(f"\n[SISTEMA] Fecha de hoy: {diaA}/{mesA}/{anioA}")
        print(f"[SISTEMA] Edad calculada: {edad} anos.")

except ValueError:
    print("[ERROR] Deben ingresar numeros enteros.")

except EOFError:
    print("")
    print("[ERROR] No se pudo leer la entrada: estas ejecutando el archivo")
    print("con doble clic o con el boton Run, que no permiten escribir.")
    print("")
    print("Ejecutalo desde la TERMINAL de VS Code:")
    print("    cd proyecto_python")
    print("    python calculadoraEdad.py")