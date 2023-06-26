def addition(a, b):
  return a + b

def soustraction(a, b):
  return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Erreur : Division par zéro"

def calculatrice():
    print("Bienvenue dans la calculatrice !")
    print("Veuillez choisir une opération :")
    print("1. Addition")
    print("2. Soustraction")
    print("3. Multiplication")
    print("4. Division")
    choix = input("Votre choix (1-4) : ")

    if choix == "1":
        a = float(input("Premier nombre : "))
        b = float(input("Deuxième nombre : "))
        resultat = addition(a, b)
        print("Résultat : ", resultat)
    elif choix == "2":
        a = float(input("Premier nombre : "))
        b = float(input("Deuxième nombre : "))
        resultat = soustraction(a, b)
        print("Résultat : ", resultat)
    elif choix == "3":
        a = float(input("Premier nombre : "))
        b = float(input("Deuxième nombre : "))
        resultat = multiplication(a, b)
        print("Résultat : ", resultat)
    elif choix == "4":
        a = float(input("Numérateur : "))
        b = float(input("Dénominateur : "))
        if b != 0:
            resultat = division(a, b)
            print("Résultat : ", resultat)
        else:
            print("Erreur : Division par zéro")
    else:
        print("Choix invalide.")

calculatrice()