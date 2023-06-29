def mad_libs():
    lieu=input("Entrez un lieu :")
    animal = input("Entrez une espèce d'animal :")
    nom = input("Entrez un prénom : ")
    nom_animal = input("Quel est le nom de l'animal ? ")
    adversaire = input("Qui est l'adversaire ? ")
    tresor = input("Quel est le trésor ? ")
    histoire= "Luffy et son équipage naviguaient vers " + lieu +" . Soudain, ils aperçurent un "+ animal + " géant. " + nom + " décida de l'apprivoiser et de le nommer "+ nom_animal +". Ensemble, ils affrontèrent " +adversaire +" pour protéger" + tresor +" ."

    return histoire
print(mad_libs())