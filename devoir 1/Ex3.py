password = "python123"

while True:
    user_pass = input("Entrez le mot de passe : ")
    if user_pass != password:
        print("Mot de passe incorrect. Veuillez réessayer.")
        continue
    else:
        print("Mot de passe correct. Bienvenue!")
        break