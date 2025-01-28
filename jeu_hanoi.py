# Initialisation des tableaux
tableau1 = [6, 5, 4, 3, 2, 1]  # Les disques initialement empilés
tableau2 = []  # Tableau vide
tableau3 = []  # Tableau vide

def afficher_jeu():
    """
    Affiche les trois tableaux avec des représentations graphiques des disques.
    """
    max_height = max(len(tableau1), len(tableau2), len(tableau3))
    for i in range(max_height, 0, -1):
        ligne1 = dessiner_disque(tableau1[i - 1]) if i <= len(tableau1) else " " * 15
        ligne2 = dessiner_disque(tableau2[i - 1]) if i <= len(tableau2) else " " * 15
        ligne3 = dessiner_disque(tableau3[i - 1]) if i <= len(tableau3) else " " * 15
        print(f"{ligne1}   {ligne2}   {ligne3}")
    print("___________   ___________   ___________")
    print("  Tableau 1     Tableau 2     Tableau 3")

def dessiner_disque(taille):
    """
    Retourne une chaîne représentant un disque de la taille donnée.
    """
    espace = " " * (7 - taille)
    disque = "=" * (taille * 2 - 1)
    return f"{espace}{disque}{espace}"

def deplacer_disque(source, cible):
    """
    Déplace un disque d'un tableau source vers un tableau cible.
    """
    if not source:
        print("Le tableau source est vide !")
        return False
    if cible and cible[-1] < source[-1]:
        print("Mouvement invalide : un disque plus grand ne peut pas être placé sur un plus petit.")
        return False
    cible.append(source.pop())
    return True

def verifier_victoire():
    """
    Vérifie si tous les disques ont été déplacés dans le tableau 2 ou 3.
    """
    return len(tableau2) == 6 or len(tableau3) == 6

# Boucle principale du jeu
print("Bienvenue au jeu de Hanoï !")
print("Le but est de déplacer tous les disques de Tableau 1 vers Tableau 2 ou Tableau 3.")
print("Règles : Un disque plus grand ne peut jamais être placé sur un plus petit.")
while True:
    afficher_jeu()
    try:
        source = int(input("Choisissez le tableau source (1, 2 ou 3) : "))
        cible = int(input("Choisissez le tableau cible (1, 2 ou 3) : "))
        if source not in [1, 2, 3] or cible not in [1, 2, 3]:
            print("Veuillez entrer des numéros de tableau valides (1, 2 ou 3).")
            continue

        tableaux = [tableau1, tableau2, tableau3]
        if deplacer_disque(tableaux[source - 1], tableaux[cible - 1]):
            if verifier_victoire():
                afficher_jeu()
                print("Félicitations, vous avez gagné le jeu des tours de Hanoï !")
                break
    except ValueError:
        print("Veuillez entrer un numéro valide.")
