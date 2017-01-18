import os 
def menu():
    os.system ("clear")
    print ("\n\t\t MENU PRINCIPAL")
    print ("\t1.Vuelos\n")
    print ("\t2.Metodo de compra\n")
    print ("\t3.Promociones\n")
    print ("\t4.Descuentos\n")
    print ("\t5.Contactenos\n")
    print ("\t6.Salir\n\n")
a=0
while(1):
    menu()
    a=input ("\t\tElija un numero: ")
