tableau1 = ("\n"
            "         _                     _                     _         ""\n"
            "        | |                   | |                   | |        ""\n"
            "        | |                   | |                   | |        ""\n"
            "        | |                   | |                   | |        ""\n"
            "        | |                   | |                   | |        ""\n"
            "        | |                   | |                   | |        ""\n"
            "        | |                   | |                   | |        ""\n"
            "        | |                   | |                   | |        ""\n"
            "        | |                   | |                   | |        ""\n"
            "        | |                   | |                   | |        ""\n"
            "        | |                   | |                   | |        ""\n"
            "        | |                   | |                   | |        ""\n"
            "        | |                   | |                   | |        ""\n"
            "        | |                   | |                   | |        ""\n"
            "        | |                   | |                   | |        ""\n"
            "        | |                   | |                   | |        ""\n"
            "        | |                   | |                   | |        ""\n"
            "        | |                   | |                   | |        ""\n"
            "        | |                   | |                   | |        ""\n"
            "        | |                   | |                   | |        ""\n"
            "        | |                   | |                   | |        ""\n"
            "___________________   ___________________   ___________________""\n"
            "|    Tableau 1    |   |    Tableau 2    |   |    Tableau 3    |""\n"
            "___________________   ___________________   ___________________""\n")
tableau2 = ()
tableau3 = ()

hor = "_"
ver = "|"

disque1 = ("_ _ _""\n"
           "| 1 |""\n"
           "_ _ _""\n")
          
disque2 = ("__ _ __""\n"
           "|  2  |""\n"
           "__ _ __""\n")

disque3 = ("___ _ ___""\n"
           "|   3   |""\n"
           "___ _ ___""\n")

disque4 = ("____ _ ____""\n"
           "|    4    |""\n"
           "____ _ ____""\n")

disque5 = ("_____ _ _____""\n"
           "|     5     |""\n"
           "_____ _ _____""\n")

disque6 = ("______ _ _____""\n"
           "|      6     |""\n"
           "______ _ _____""\n")

i = 0

while(i!=2):
    choixuser = input('''Choisi une option :
    1) Jouer au jeu d'hanoï
    2) Arreter de jouer ''')

    if(choixuser == '1'):
        print("_______________________________________________________________________________________""\n"
            "|""Le but du jeu est de faire passer les disques du premier tableau sur un autre tableau""|""\n"
            "|""en faisant en sorte que les gros disques soient sur les petits disques""               |""\n"
              "_______________________________________________________________________________________"
            "\n"
            )

    elif(choixuser == '2'):
        print("Vous quittez le jeu au revoir :)")
        i = 2
    

    else:
        print("Erreur vous devez choisir entre 1 et 2")
