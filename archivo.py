def definir_estado():
    peso=input("ingrese el peso")
    altura=input("ingrese la altura")
    result= (float(peso)) / (float(altura)/100^2)

    if result < 16.00:
     print("delgadez severa")

    elif 16.00>= result and result <18.49:
        print("delgadez moderada")
    elif 18.49>= result and result <25.00:
        print("peso normal")
    elif 25.00>= result and result <35.00:
         print("sobrepeso")
    elif 35.00>= result:
        print("obesidad")