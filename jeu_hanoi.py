# Initialisation des tableaux
tableau1 = [6, 5, 4, 3, 2, 1]  # Disques en ordre décroissant
tableau2 = []
tableau3 = []

def afficher_tableaux():
    """
    Affiche les trois tableaux sous forme de piles
    """
    max_height = max(len(tableau1), len(tableau2), len(tableau3))
    for i in range(max_height, 0, -1):
        ligne1 = str(tableau1[i - 1]) if i <= len(tableau1) else " "
        ligne2 = str(tableau2[i - 1]) if i <= len(tableau2) else " "
        ligne3 = str(tableau3[i - 1]) if i <= len(tableau3) else " "
        print(f"   {ligne1:^10}   {ligne2:^10}   {ligne3:^10}")
    print("___________________   ___________________   ___________________")
    print("|    Tableau 1    |   |    Tableau 2    |   |    Tableau 3    |")
    print("___________________   ___________________   ___________________")

def deplacer_disque(source, cible):
    """
    Déplace un disque d'un tableau source vers un tableau cible
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
    Vérifie si le joueur a gagné (tous les disques sont dans le tableau 2 ou 3)
    """
    return len(tableau2) == 6 or len(tableau3) == 6

# Boucle principale
i = 0
while i != 2:
    choixuser = input('''Choisis une option :
1) Jouer au jeu d'Hanoï
2) Arrêter de jouer
> ''')

    if choixuser == '1':
        print("_______________________________________________________________________________________")
        print("| Le but du jeu est de faire passer tous les disques du premier tableau vers un autre tableau |")
        print("| en respectant les règles : un disque plus grand ne peut jamais être placé sur un plus petit.|")
        print("_______________________________________________________________________________________")

        while True:
            afficher_tableaux()
            try:
                source = int(input("Choisis le tableau source (1, 2, ou 3) : "))
                cible = int(input("Choisis le tableau cible (1, 2, ou 3) : "))
                if source not in [1, 2, 3] or cible not in [1, 2, 3]:
                    print("Veuillez entrer un numéro de tableau valide (1, 2 ou 3).")
                    continue

                tableaux = [tableau1, tableau2, tableau3]
                if deplacer_disque(tableaux[source - 1], tableaux[cible - 1]):
                    if verifier_victoire():
                        afficher_tableaux()
                        print("Félicitations, vous avez gagné !")
                        break
            except ValueError:
                print("Veuillez entrer un numéro valide.")
    elif choixuser == '2':
        print("Vous quittez le jeu. Au revoir :)")
        i = 2
    else:
        print("Erreur : vous devez choisir entre 1 et 2.")
