lista=[]
nev=" "
def bekér():
    nev=input("Adja meg a nevét: ")
    lista.append(nev)
    if nev!="":
        print("A név/nevek:", lista)
        return bekér()

bekér()
