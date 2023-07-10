from random import*


def generate(lenmdp,numbers,specials):
    letters="abcdefghijklmnopqrstuvwxyz"
    num="1234567890"
    spec="*%:/.;?,!§^=+"
    base="".join(sample(letters,lenmdp))
    if numbers == "oui":
        n="".join(sample(num,3))
        base+=n
        if specials=="oui":
            s="".join(sample(spec,1))
            base+=s
    return base
print(generate(9,"oui","oui"))