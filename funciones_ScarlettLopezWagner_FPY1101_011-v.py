NombreLibros=['ALAS DE HIERRO','LA SOMBRA DE LA SIRENA']
NombreAutores=['REBECCA YARROS','CAMILL LACKBERG']
Publicados=[2024,2003]
codigo_sku=['ALASDE-REB-2024','LASOMB-CAM-2003']
def registro_de_libros(libros):
    titulo_libro=(input("ingresa Titulo:"))
    NombreAutor=(input("Autor del libro")).lower()
    Publicado=input("ingrese el año del  la publicacion:").lower()
    codigo_sku=int(input("ingrese el codigo sku del libro:")).lower()
try:
    for titulo_libro  in NombreLibros:
        print("nombre del libro no existe ,intente nuevamente")
        Titulo_Libro=input("ingrese el nombre del libro")
        autor=input("ingrese nombre de autor")
        sku=int(input("ingrese el codigo del libro(SKU es las 6 primeras letras del título del libro ademas de las 3 primeras letras del autor y año de publicación)" ))
        Publicado=int(input("ingrese el año que se publico"))
        Titulo_Libro=NombreAutores
        sku=codigo_sku
        todos_los_datos_del_libro=titulo_libro,autor,Publicados,sku

        NombreLibros.append({
        titulo_libro:NombreLibros,
        NombreAutores:autor,
        Publicados:Publicado,
        codigo_sku:sku
    })
except ValueError:

    def lista_libros(NombreLibros):
        print('lista_libros')
        for titulo_libro in NombreLibros:
            print(NombreLibros)

    def imprimir_lista(NombreLibro):
        autor=input("ingrese autor del libro para imprimir lista o precione enter para seleccionar todos").lower()

    if NombreLibros=="":
        libro_a_imprimir=titulo_libro
        NombreLibros="lista_de_libros.txt"
    elif autor in NombreAutores:
        libro_a_imprimir=[]
        for NombreLibro in titulo_libro:
            if NombreLibros["NombreLibro"]==NombreLibros:
                libro_a_imprimir.append(NombreLibros)
        NombreArchivo=f'lista_{NombreLibro}.txt'
    else:
        print("libro no valido")
    with open(lista_libros,'w',)as archivo:
        for Nombrelibro in libro_a_imprimir:
            archivo.write(f'NombreLibro{titulo_libro[NombreLibro]}\n')
            archivo.white(f'Nombreautor{titulo_libro[autor]}\n')
            archivo.white(f'Publicados{Publicado[Publicado]}\n')
            archivo.white(f'codigo_sku{sku[codigo_sku]}\n')        
    







