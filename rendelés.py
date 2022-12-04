
tipus=[]
meret=[]
feltet=[]
ar=[]

def adatbekeres(valasz):
    adat = input(valasz)
    return adat


def pizza():
    lead = "igen"
    while (lead == "igen"):
        tipus = adatbekeres("Milyen tipusú pizzát kér? 1 - sajtos, 2 - gombás, 3 - sonkás: ")
        meret = adatbekeres("Milyen méretű pizzát kér? k - kicsi, n - normál, na - nagy:")
        feltet = adatbekeres("Kér extra feltétet? i - igen, n - nem:")
        lead = adatbekeres("Szeretne még rendelést leadni? i- igen, n - nem")


        tipus.append(tipus)
        meret.append(meret)
        feltet.append(feltet)

    kiiras()

def kiiras():
    i = 0
    while (i < len(tipus)):
        print(f"{tipus[i]},{meret[i]}, {feltet[i]}")
        i = i + 1



def tipusf():
    tip = " "
    if tipus == 1:
        tip = "Sajtos"
    elif tipus == 2:
        tip = "Gombás"
    else:
        tip = "Sonkás"
    return tip

def meret():
    mer = " "
    if meret == "k":
        mer = "Kicsi"
    elif meret == "n":
        mer = "Normál"
    else:
        mer = "Nagy"
    return mer

def feltet():
    felt = " "
    if feltet == "i":
        felt ="Igen"
    else:
        felt = "Nem"
    return felt

def ar():

    plusz_feltet = 50
    normal_sajtos_ar = 1000
    normal_gombas_ar = 1100
    normal_sonkas_ar = 1200





