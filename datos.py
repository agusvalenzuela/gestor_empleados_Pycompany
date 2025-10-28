def ingresar_datos():
    nombre = str(input("Indique su nombre: "))
    cargo = str(input("Indique su cargo: "))
    edad = int(input("Ingrese su edad: "))
    sueldo = int(input("Ingrese su sueldo: "))
    bono = float(input("Ingrese el pocentaje de bono: "))
    datos = print(f"Su nombre es: {nombre} tiene el cargo de {cargo} su edad es: {str(edad)} tiene un sueldo de: $ {str(sueldo)}, y el porcentaje de bono es: {str(bono)} %")

ingresar_datos()
