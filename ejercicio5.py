articulo = int(input("cuantos articulos va a llevar : "))
valor_de_aarticulo =0
sumDearticulo = 0

for i in range(articulo):
    valor = int(input(f"valor del producto  {str(i+1)} : "))
    cantidad = int(input(f"cuantos productos lleva  {str(i+1)} : "))
    print ("---------------------------------------------")
    sumDearticulo = valor * cantidad
    if i==0:
     valor_de_aarticulo = sumDearticulo

    else:
       if i >=1:
        valor_de_aarticulo = sumDearticulo + valor_de_aarticulo

print(f"El valor a pagar por su compra es de {int(valor_de_aarticulo )}")       

