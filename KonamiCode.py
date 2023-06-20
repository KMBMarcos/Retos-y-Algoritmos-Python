import keyboard

codeKonami = {"Heal":["up","down", "a","b"], 
              "Atk":["up","up","a","a"],
              "Def":["down","down","b","b"]}
def verifyIsKonamiHeal():
    keyPressed = []
    for pKey in codeKonami["Heal"]:
        keyPressed.append(pKey)
    return keyPressed

def verifyIsKonamiAtk():
    keyPressed = []
    for pKey in codeKonami["Atk"]:
        keyPressed.append(pKey)
    return keyPressed

def verifyIsKonamiDef():
    keyPressed = []
    for pKey in codeKonami["Def"]:
        keyPressed.append(pKey)
    return keyPressed


def verifKonamiCode():
    while True:
        teclas = verifyIsKonami()
    if teclas:
        print('Teclas presionadas:', teclas)