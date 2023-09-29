print "hola mundo"

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Error: No puedes dividir por cero."
    else:
        return a / b

while True:
    try:
        # Solicitar al usuario que ingrese dos números
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))

        # Mostrar opciones de operación
        opciones = """
            Opciones de operación:
            1. Suma
            2. Resta
            3. Multiplicación
            4. División
            5. Salir
        """
        print(opciones)

        # Solicitar al usuario que elija una opción
        opcion = int(input("Seleccione una opción (1/2/3/4/5): "))

        if opcion == 1:
            resultado = suma(num1, num2)
        elif opcion == 2:
            resultado = resta(num1, num2)
        elif opcion == 3:
            resultado = multiplicacion(num1, num2)
        elif opcion == 4:
            resultado = division(num1, num2)
        elif opcion == 5:
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida.")
            continue

        print(f"El resultado es: {resultado}")

    except ValueError:
        print("Error: Ingrese valores numéricos válidos.")
    except Exception as e:
        print(f"Error: {str(e)}")

