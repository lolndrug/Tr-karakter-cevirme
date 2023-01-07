def ing_Cevir(eposta):
    ing_Trk = {
        "ş" : "s",
        "ç" : "c",
        "ö" : "o",
        "ı" : "i",
        "ğ" : "g",
        "ü" : "u"
    }
    liste_posta = list(eposta.lower())
    for karakter in liste_posta:
        if karakter in ing_Trk:
            liste_posta[liste_posta.index(karakter)] = ing_Trk[karakter]

    return "".join(liste_posta)

e_Posta = ["ĞĞĞĞĞ"]

s = ing_Cevir(e_Posta[0])
print(list(map(ing_Cevir,e_Posta)))

