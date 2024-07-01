import os
os.system("cls")

menu="""BIENVENIDO A TALLER DE REPARACION 

1- registrar vehiculo
2- lista de todos los vehiculos
3- imprimir orden de reparacion
4- salir 

OPCION: """
vehiculos=[]
marcas=["toyota", "ford" , "kia"]
titulo=f"""{"LISTA DE VEHICULOS"}
{"-"*99}
{"MARCA ":<11}{"| AÑO DE FABRICACION ":<21}{"| KILOMETRAJE ":<12}{"| COSTO ESTIMADO(CLP) ":<19}{"| IMPUESTO(8%) ":<12}{"| COSTO TOTAL |":<11}
{"-"*99}
"""

def registrar():
    while True:
        try:
            os.system("cls")
            marca= input(f"Marca {marcas}: ").strip().lower()
            año=int(input("Año de fabricacion: "))
            km=float(input("Kilometraje: "))
            cost=int(input("Costo de Reparacion(clp): $"))
            imp=(cost/100)*8
            ctotal=round(cost+imp)
            if año>0 and año<=2024 and marca in marcas and km>=0 and cost>0:
                vehiculos.append([marca,año,km,cost,imp,ctotal])
                input("pedido agregado con exito!")
                break
            else:
                input("algo se ingreso incorrectamente")
        except Exception as e:
            input(f"excep al regitrar: {str(e)}")

def listatodos():
    salida=titulo
    for i in vehiculos:
        salida += f"{i[0]:<13}"
        salida += f"{i[1]:<21}"
        salida += f"{i[2]:<14}"
        salida += f"{i[3]:<22}"
        salida += f"{i[4]:<15}"
        salida += f"{i[5]:<11}"
        salida += "\n"
    return salida

def listamarca(marca):
    salida=titulo
    for i in vehiculos:
        if i[0]==marca:
            salida += f"{i[0]:<13}"
            salida += f"{i[1]:<21}"
            salida += f"{i[2]:<14}"
            salida += f"{i[3]:<22}"
            salida += f"{i[4]:<15}"
            salida += f"{i[5]:<11}"
            salida += "\n"
    return salida

def imprimir():
    os.system("cls")
    a= input(f"desea imprimir: [todos/{marcas}]: ").strip().lower()
    if a == "todos":
        with open("orden_de_reparacion.txt", "w", encoding='utf-8') as archivo:
            archivo.write(listatodos())
    elif a in marcas:
        with open(f"orden_de_reparacion_{a}.txt", "w") as archivo:
            archivo.write(listamarca(a))
    else:
        input("error al ingresar")


while True:
    try:
        os.system("cls")
        opc=input(menu)
        if opc=="4":
            break
        elif opc=="1":
            registrar()
        elif opc=="2":
            input(listatodos())
        elif opc=="3":
            imprimir()
    except Exception as e:
        input(f"excep menu: {str(e)}")