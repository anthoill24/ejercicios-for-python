def zoolo () :
 jovenes = 0
 adultos = 0 
 nume = 0
 animal = str (input("Introduce el nombre de tu animal : ")) 
 if animal == "elefante" :
   nume = 5
 elif animal == "jirafa" :
   nume =  7
 elif animal == "chimpances":
   nume =  8
 else :
   print("no esta en la base de datos")
 for i in range(nume):
   edad =  int(input(f"que edad tiene tiene tu animal {str(i+1)} : ")) 
   if edad <=4:
    jovenes+=1
   elif edad >= 5:
    adultos+=1
      
 print("cuentas con ", jovenes , animal ,  "jovenes  y " , adultos , animal , "adultos")



zoolo()



  