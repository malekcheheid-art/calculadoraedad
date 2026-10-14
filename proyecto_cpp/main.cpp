#include <iostream>
using namespace std;

bool esBisiesto(int anio)
{
    return (anio % 4 == 0 && anio % 100 != 0) || (anio % 400 == 0);
}

bool esFechaValida(int d, int m, int a)
{
    if (a < 1900 || a > 2026) return false;

    if (m < 1 || m > 12) return false;

    if (d < 1 || d > 31) return false;

    if ((m == 4 || m == 6 || m == 9 || m == 11) && d > 30)
        return false;

    if (m == 2)
    {
        if (esBisiesto(a))
        {
            if (d > 29)
                return false;
        }
        else
        {
            if (d > 28)
                return false;
        }
    }

    return true;
}

int main()
{
    int diaN, mesN, anioN;

    int diaA = 8, mesA = 7, anioA = 2026;

    cout << "=====================================================" << endl;
    cout << "    CALCULADORA DE EDAD DE: Malek Cheheid    " << endl;
    cout << "=====================================================" << endl;

    cout << "Ingrese Dia, Mes y Anio de nacimiento (separados por espacios): ";
    cin >> diaN >> mesN >> anioN;

    if (!esFechaValida(diaN, mesN, anioN))
    {
        cout << "[ERROR] La fecha ingresada no existe en el calendario." << endl;
        return 1;
    }

    int edad = anioA - anioN;

    if (mesN > mesA || (mesN == mesA && diaN > diaA))
    {
        edad = edad - 1;
    }

    cout << "\n[SISTEMA] Fecha de hoy: "
         << diaA << "/" << mesA << "/" << anioA << endl;
    cout << "[SISTEMA] Edad calculada: " << edad << " anos." << endl;
    cout << "=====================================================" << endl;

    return 0;
}