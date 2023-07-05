from random import*


def jeu(coups):
    score1=0
    score2=0
    liste=["pierre","feuille","ciseaux"]
    run=True
    while  run==True:
        joueur=str(input("fais ton choix "))
        adversaire=choice(liste)
        if joueur == "pierre" and adversaire == "ciseaux": 
            score1+=1
        elif joueur == "pierre" and adversaire =="feuille":
            score2+=1
        elif joueur == "feuille" and adversaire =="pierre":
            score1+=1
        elif joueur == "feuille" and adversaire =="ciseaux":
            score2+=1
        elif joueur == "ciseaux" and adversaire =="pierre":
            score2+=1
        elif joueur == "ciseaux" and adversaire =="feuille":
            score1+=1
        print (f"joueur : {score1} - Ordinateur : {score2}")
        if score1 ==coups:
            break
        elif score2==coups:
            break
    if score2==score1:
        return "Egalité !"
    elif score2>score1:
        return "Perdue !"
    return "Gagner !"

print(jeu(3))
        

