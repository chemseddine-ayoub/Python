contact = []

while True:
    print("\nMenu:")
    print("1. Ajouter un contact a une liste")
    print("2. Afficher tous les contacts avec numérotation")   
    print("3. Quitter le programme")
    choice = int(input("Choisissez une option : "))
    if choice == 1:
        name = input("Entrez le nom du contact : ")
        contact.append(name)
    elif choice == 2:
        if not contact:
            print("Aucun contact enregistré.")
        for i, name in enumerate(contact):
            print(f"{i + 1}- {name}")
    elif choice == 3:
        print("Au revoir!")
        break
    else:
        print("Option invalide. Veuillez choisir une option valide.")
        
    