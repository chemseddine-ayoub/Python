donnees = [
    ("Sara", "Math", 12, "G1"),
    ("Sara", "Info", 14, "G1"),
    ("Ahmed", "Math", 9, "G2"),
    ("Adam", "Chimie", 18, "G1"),
    ("Sara", "Math", 11, "G1"),
    ("Bouchra", "Info", "abc", "G2"),
    ("", "Math", 10, "G1"),
    ("Yassine", "Info", 22, "G2"),
    ("Ahmed", "Info", 13, "G2"),
    ("Adam", "Math", None, "G1"),
    ("Sara", "Chimie", 16, "G1"),
    ("Adam", "Info", 7, "G1"),
    ("Ahmed", "Math", 9, "G2"),
    ("Hana", "Physique", 15, "G3"),
    ("Hana", "Math", 8, "G3"),
]

def valider(enregistrement):
    nom, matiere, note, groupe = enregistrement
    if not nom:
        return False, "raison :nom vide" 
    if not matiere:
        return False, "raison :matiere vide"
    if not groupe:
        return False, "raison :groupe vide"
    if not isinstance(note, (int, float)):
        return False, "raison :note non numérique"
    if note < 0 or note > 20:
        return False, "raison :note invalide"
    else:
        return True, ""
    
valides = []
erreurs = []
doublons_exact = set()
ligne = set()

for enregistrement in donnees:
    nom, matiere, note, groupe = enregistrement
    if enregistrement in ligne:
        doublons_exact.add(enregistrement)
        continue
    ligne.add(enregistrement)
    valide, raison = valider(enregistrement)
    if valide:
        valides.append((nom, matiere, float(note), groupe))
        doublons_exact.add(enregistrement)
    else:
        erreurs.append((enregistrement, raison))
        
matieres = set()
for nom, matiere, note, groupe in valides:
    matieres.add(matiere)
print("Les matières enseignées sont : ", matieres)

etudiants = {}

for nom, matiere, note, groupe in valides:
    if nom not in etudiants:
        etudiants[nom] = {}
    if matiere not in etudiants[nom]:
        etudiants[nom][matiere] = []
    etudiants[nom][matiere].append(note)
print("Les étudiants et leurs notes : \n", etudiants)

groupes = {}

for nom, matiere, note, groupe in valides:
    if groupe not in groupes:
        groupes[groupe] = set()
    groupes[groupe].add(nom)
print("Les groupes et leurs étudiants : \n", groupes)    

def somme(etudiant):
    if not etudiant:
        return 0
    return etudiant[0] + somme(etudiant[1:]) 

def moyenne_gen(etudiant):
    if not etudiant:
        return 0
    return somme(etudiant) / len(etudiant)    

for nom, matiere_et in etudiants.items():
    print(f"\nÉtudiant : {nom}")
    
    toutes_notes = []
    
    for matiere, notes in matiere_et.items():
        moy = moyenne_gen(notes)
        print(f"  Moyenne en {matiere} : {moy:.2f}")
        
        toutes_notes.extend(notes)
    
    moy_generale = moyenne_gen(toutes_notes)
    print(f"  Moyenne générale : {moy_generale:.2f}")
  
alertes = []  
  
for etudiant, matiere in etudiants.items():
    for matiere, notes in etudiants[etudiant].items():
        if len(notes) > 1:
            alertes.append((
                "type: doublon de notes",
                f"étudiant: {etudiant}",
                f"matière: {matiere}",
            ))
    
for etudiant, matieres_etu in etudiants.items():
    if len(matieres_etu) < len(matieres):
        alertes.append({
            "type": "profil_incomplet",
            "etudiant": etudiant
        })
        
seuil = float(input("Entrer un seuil de note :"))

for groupe, etudiants_grp in groupes.items():
    notes_groupe = []
    for etudiant in etudiants_grp:
        for matiere, notes in etudiants[etudiant].items():
            notes_groupe.extend(notes)
    if moyenne_gen(notes_groupe) < seuil:
        alertes.append((
            "type: groupe faible",
            f"groupe: {groupe}",
            f"moyenne: {moyenne_gen(notes_groupe):.2f}"
        ))
        
for etudiant, matiere_etu in etudiants.items():
    notes_etudiant = []
    
    for matiere, notes in matiere_etu.items():
        notes_etudiant.extend(notes)
    
    if notes_etudiant:
        if max(notes_etudiant) - min(notes_etudiant) >= 10:
            alertes.append((
                "type: Performances instables",
                f"étudiant: {etudiant}",
            ))

print("\n===== ALERTES DETECTÉES =====")

if not alertes:
    print("Aucune anomalie détectée.")
else:
    for alerte in alertes:
        print(alerte)    