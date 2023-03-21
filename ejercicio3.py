Ndetrabajadores = int(input("Ingrese Numero de trabajadores : "))
salario = 0
Htrabajadas = 0
for i in range(Ndetrabajadores):
    horaEx = 0
    Htrabajadas = int(input(f"Horas trabajabas  {str(i+1)} : "))
    
    if (Htrabajadas <= 40):
        salario = Htrabajadas * 20

    elif (Htrabajadas > 40):
        horaEx = Htrabajadas - 40
        salario = 40 * 20 + (horaEx * 25)   

    print(f"El salalario del trabajador es de {int(salario)}")       