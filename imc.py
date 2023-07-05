def imc():
    poids=float(input("Entrez votre poids en kg : "))
    taille=float(input("Entrez votre taille en m : "))
    t=taille**2
    formule=poids/t
    print("Votre IMC est de : ",formule)
    if formule >0:
        if formule< 18.5:
            return "Vous êtes en Insuffisance pondérale."
        elif formule < 25 :
            return "Vous avez une corpulence normale."
        elif formule <30:
            return "Vous êtes en surpoids."
        elif formule < 35 :
            return "Vous êtes en obésité modérée."
        elif formule < 40 :
            return "Vous êtes en obésité sévère."
print(imc())