from maneFacultad import ManejadorFacultad

def metodo1(facultades,codigo):
    i = facultades.buscar_facultad(codigo)
    if i != -1:
        print(facultades.get_facultad(i))
        for carrera in facultades.get_facultad(i).get_Carreras():
            print(carrera)
    else:
        print("No se encontro facultad con ese codigo ")
def metodo2(facultades,nomb_carrera):
    facultades.buscar_carrera(nomb_carrera)