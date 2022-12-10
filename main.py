"""

def főfüggvény()
    a = 2               átadom ezt a masikfv-nek paraméterként
    x = masikfv(a)




def masikfv(a)
    c = a*2
    return c            visszaadom ezt a főfüggvénynek

"""

abc = "AÁBCDEÉFGHIÍJKLMNOÓÖŐPQRSTUÚÜŰVWXYZ"
titkos = "XYZAÁBCDEÉFGHIÍJKLMNOÓÖŐPQRSTUÚÜŰVW"


szoveg = "Elkelkáposztástalanítottátok"



def betu_kereses(betu):
    i = 0

    while i < len(abc) and abc[i] != betu:  #  amíg nem egyenlő a betűvel fut
        i += 1

    if i >= len(abc):   #  ha nagyobb, mint az abc, nem találta meg a betűt
        i = -1          # hibás eredményt ír ki

    return i            # visszatér az ciklusváltozó értékével


def titkositas():

    szoveg = input("Mit titkosítsak?").upper()
    titkositott_szoveg = ""

    i = 0

    while i < len(szoveg):

        betu = szoveg[i]    # eltárolom betu változóba az adott karaktert
        x = betu_kereses(betu)
        if x != -1:         # -1 jöhet ki szóközre, speciális karakterekre, ezért kell ez az ág
            titkositott_szoveg += titkos[x]
        i += 1

    print(titkositott_szoveg)

titkositas()