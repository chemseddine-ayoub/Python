while True:
    age = int(input("Entrez votre âge : "))
    if age < 0:
        print("Veuillez entrer un âge valide.")
        continue
    else:        
        break

if age >= 0 and age <= 12:
    print("Vous êtes un enfant.")
elif age > 12 and age <= 17:
    print("Vous êtes un adolescent.")
elif age > 17 and age <= 64:
    print("Vous êtes un adulte.")
else:    print("Vous êtes un senior.")