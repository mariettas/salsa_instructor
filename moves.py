import random


#  instructor
moves = ["Setenta",
         "Havana",
         "Lasso",
         "El Uno",
         "El Dos",
         "Avioneta",
         "Siete",
         "Siete con Coca Cola",
         "Siete Moderno",
         "Setenta y uno",
         "Ochenta y cuatro",
         "Cuarenta y cinco",
         "Setenta y agache",
         "El doce",
         "Moliendo café",
         "La pareja",
         "Mi Barrio",
         "Viñales",
         "Corona",
         "Corona doble",
         "Montaña",
         "El dedo",
         "Sencilla",
         "Dile que no",
         "Dile que no 180",
         "Exhíbela",
         "Exhíbela dos con una",
         "Sombrero",
         "Sombrero doble",
         "Sombrero doble"]

while True:
       instructor = input("Do you want me to give you a move? (y/n)").lower()

       if instructor == "y".lower():
              print(random.choice(moves))

       else:
              print("Sorry to hear that. Keep calm and suavecito.")





