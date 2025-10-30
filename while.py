def mostrar_menu():
    """Muestra las opciones disponibles en el menú."""
    print("\n==================================================")
    print("--- Menú de Opciones del Sistema de Empleados ---")
    print("==================================================")
    print("1. **Ingresar datos del empleado**")
    print("2. **Calcular bono**")
    print("3. **Mostrar resumen**")
    print("4. **Salir del sistema**")
    print("--------------------------------------------------")

def main():
    """Función principal del programa para controlar el flujo."""
    
    ejecutando = True 
    
    while ejecutando:
        mostrar_menu()
        
        opcion = input("Ingrese el número de la opción deseada (1-4): ").strip()
        
        try:
            opcion = int(opcion)
        except ValueError:
            print("\n❌ *Error*: Por favor, ingrese un **número** válido (1, 2, 3, o 4).")
            continue 

        if opcion == 1:
            ingresar_datos()
            
        elif opcion == 2:
            calcular_bono()
            
        elif opcion == 3:
            mostrar_resumen()
            
        elif opcion == 4:
            print("\n👋 *Opción 4 seleccionada*: Saliendo del sistema. ¡Hasta pronto!")
            ejecutando = False 
            sys.exit(0) # Salida limpia
            
        else:
            print(f"\n❌ *Error*: Opción '{opcion}' no válida. Por favor, elija una opción entre 1 y 4.")

# --- Punto de Entrada del Programa ---

if __name__ == "__main__":
    main()






