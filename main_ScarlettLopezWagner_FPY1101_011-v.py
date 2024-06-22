import funciones_ScarlettLopezWagner_FPY1101_011-v as fn

NombreLibro=[]
print(NombreLibro)

while True:
    print("Bienvenido a la Biblioteca\n1.Registra libro\n2.prestar libro\n3.Lista reporte de prestamos\n4.Imprimir reporte de prestamo\n5.Salir del programa")

    opcion=int(input("ingrese su opcion:"))

    if opcion==1:
        fn.registar_NombreLibro(NombreLibro)
    elif opcion==2:
        fn.prestar_libro(NombreLibro)
        print(NombreLibro)
    elif opcion==3:
        fn.lista_reporte_prestamo(NombreLibro)
    elif opcion==4:
        fn.imprimir_lista_de_reporte(NombreLibro)
        print(NombreLibro)
    elif opcion==5:
        break
    else:
        print("opcion no valida,seleccione,nuevamente")                