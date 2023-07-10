def dico(val,liste):
    debut=0
    n=len(liste)
    fin=n
    while debut<fin:
        m=(debut+fin)//2
        if liste[m]==val:
            return f"L'élément {val} est le {m+1}e nombre de la liste. "
        elif liste[m]>val:
            fin=m-1
        else:
            debut=m+1
    return "L'élément n'est pas présent dans la liste."


print(dico(12,[1,2,12]))