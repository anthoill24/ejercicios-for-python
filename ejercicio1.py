def zoolo () :
 jovenes = 0
 adultos = 0 
 nume = 0
 animal = str (input("hola , introduce el nombre de tu animal ")) 
 if animal == "elefante" :
  nume = 5
 elif animal == "jirafa" :
  nume =  7
 elif animal == "chimpances":
   nume =  8
 else :
   print("no esta en la base de datos")
 for i in range(nume):
   edad =  int(input("que edad tiene tiene tu animal ")) + i
   if edad < 5:
    jovenes+=1
   elif edad >= 5:
    adultos+=1
      
 print("cuentas con ", jovenes , animal ,  "joven  y " , adultos , animal , "adultos")

  





  