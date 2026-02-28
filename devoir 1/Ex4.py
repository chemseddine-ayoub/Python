n1 = float(input("Entrez le premier nombre: "))
n2 = float(input("Entrez le deuxième nombre: "))

print("Choisissez une opération:")
print("1. Addition")    
print("2. Soustraction")
print("3. Multiplication")
print("4. Division")
while True:
    operation = int(input("Entrez le numéro de l'opération souhaitée: "))
    if operation in [1, 2, 3, 4]:
        break
    else:
        print("Opération invalide. Veuillez choisir une opération valide.")
        continue

match operation:
    case 1:
        result = n1 + n2
        print(f"Le résultat de l'addition est: {result}")
    case 2:
        result = n1 - n2
        print(f"Le résultat de la soustraction est: {result}")
    case 3:
        result = n1 * n2
        print(f"Le résultat de la multiplication est: {result}")
    case 4:
        if n2 != 0:
            result = n1 / n2
            print(f"Le résultat de la division est: {result}")
        else:
            print("Erreur: Division par zéro n'est pas autorisée.")
    case _:
        print("Opération invalide. Veuillez choisir une opération valide.")