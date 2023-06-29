from random import*
def devine_nombre(debut : int,fin : int ,coups_max : int):
    nombre=randint(debut,fin)
    nb_coups=0
    coups_max=10
    run=True
    while run==True:
        reponse=int(input("Saisissez un nombre :"))
        if nb_coups>coups_max:
            return "Tu as perdu bouhhhh!"
        elif reponse > nombre:
            print("C'est moins !")
        elif reponse < nombre:
            print("C'est plus !")
        elif reponse==nombre:
            return "Tu as gagner !"
        nb_coups+=1
            
print(devine_nombre(1,10,4))
