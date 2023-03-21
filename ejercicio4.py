Cantidad= int(input("Ingrese la cantidad de numeros : "))
numero_pequeño = 0

for i in range(Cantidad):
    numeros = int(input(f"numero {str(i+1)} : "))
   
    if i==0:
     numero_pequeño =  numeros 

    else:
        if numeros < numero_pequeño :
          numero_pequeño = numeros

   
    
print(f"El numero menor es : {int(numero_pequeño)}")           
