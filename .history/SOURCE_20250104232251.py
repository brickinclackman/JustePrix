#------ Importations de bibliothèques ------ 
import random
from termcolor import colored, cprint
import sys
import time
import shutil

#------ Déclaration des fonctions ------

def check_validity_num(num_comp,num_essais_MAX,choix_mod):    
    """Fonction qui vérifie si le nombre de l'utilisateur est supérieur/inférieur/égal au nombre de l'ordinateur.

    Args:
        num_comp (int): nombre aléatoire de l'ordinateur
    """
    
    
    validity = False
    
    num_essais = 0
    
    num_user = int(input(colored("Veuillez entrer un nombre : ","light_magenta")))
    
    if(choix_mod == 4):
        num_essais = 1
    
    while(validity == False):
        if(num_user < num_comp):
            validity = False
            print(colored("Trop faible ! ","white","on_blue"))
            num_essais +=1
            if(num_essais > num_essais_MAX):
                validity = True
                print(colored("Nombre essaies DÉPASSÉ ! ","white","on_light_red",attrs=["bold", "blink"]))
                print(colored(f"Voici le nombre de l'ordinateur : {num_comp} ","white","on_light_red",attrs=["bold", "blink"]))
            if(num_essais < num_essais_MAX):
                print(colored(f"Encore {num_essais_MAX - num_essais} essais.","dark_grey"))
                num_user = int(input(colored("Veuillez entrer un nombre : ","light_magenta")))
        if(num_user == num_comp):
            validity = True
            print(colored("Vous avez trouvé le nombre mystère !!! ","white","on_light_green"))
        if(num_user > num_comp):
            validity = False
            print(colored("Trop grand ! ","white","on_red"))
            num_essais +=1
            if(num_essais > num_essais_MAX):
                validity = True
                print(colored("Nombre essaies DÉPASSÉ ! ","white","on_light_red",attrs=["bold", "blink"]))
                print(colored(f"Voici le nombre de l'ordinateur : {num_comp} ","white","on_light_red",attrs=["bold", "blink"]))
            if(num_essais < num_essais_MAX):
                print(colored(f"Encore {num_essais_MAX - num_essais} essais.","dark_grey"))
                num_user = int(input(colored("Veuillez entrer un nombre : ","light_magenta")))
         
def print_banner():
    """
    Affiche une bannière stylée avec animation, suivie du message "made by brickinclackman".
    """
    cols = shutil.get_terminal_size().columns
    banner = """
     ██╗██╗   ██╗███████╗████████╗███████╗    ██████╗ ██████╗ ██╗██╗  ██╗
     ██║██║   ██║██╔════╝╚══██╔══╝██╔════╝    ██╔══██╗██╔══██╗██║╚██╗██╔╝
     ██║██║   ██║███████╗   ██║   █████╗      ██████╔╝██████╔╝██║ ╚███╔╝ 
██   ██║██║   ██║╚════██║   ██║   ██╔══╝      ██╔═══╝ ██╔══██╗██║ ██╔██╗ 
╚█████╔╝╚██████╔╝███████║   ██║   ███████╗    ██║     ██║  ██║██║██╔╝ ██╗
 ╚════╝  ╚═════╝ ╚══════╝   ╚═╝   ╚══════╝    ╚═╝     ╚═╝  ╚═╝╚═╝╚═╝  ╚═╝
"""
    
    # Affichage progressif de la bannière
    for char in banner:
        print(colored(char, "light_yellow", attrs=["bold"]), end="", flush=True)
        time.sleep(0.04)  # Délai de 50ms entre chaque caractère
    
    # Affichage du message "made by brickinclackman"
    print(colored("made by brickinclackman", "cyan", attrs=["bold"]))
    time.sleep(0.5)

def print_menu():
    """Affiche le menu de choix des niveaux de manière stylée et agréable.
    
    Returns:
        int: Choix fait par l'utilisateur, concernant le niveau.
    """
    # Affichage de la bordure du menu
    print(colored("╔══════════════════════════════════════════════════════════════════════════════╗", "yellow"))
    print(colored("║            Choisissez votre mode                                             ║", "cyan"))
    print(colored("║                de jeu :                                                      ║", "cyan"))
    print(colored("╠══════════════════════════════════════════════════════════════════════════════╣", "yellow"))
    
    # Affichage des options de jeu avec des emojis et couleurs variées
    print(colored("║ 1) Facile    : 🟢 Votre nombre est compris entre 0 et 100 (30 essais MAX)    ║", "green"))
    print(colored("║ 2) Moyen     : 🟠 Votre nombre est compris entre 0 et 100 (15 essais MAX)    ║", "yellow"))
    print(colored("║ 3) Difficile : 🔴 Votre nombre est compris entre 0 et 100 (5 essais MAX)     ║", "red"))
    print(colored("║ 4) Hardcore  : 🟣 Votre nombre est compris entre 0 et 100 (1 essai MAX)      ║", "magenta"))
    
    # Affichage de la bordure du bas
    print(colored("╠══════════════════════════════════════════════════════════════════════════════╣", "yellow"))
    
    # Demande du choix avec un prompt attrayant
    choix = int(input(colored("║ Veuillez entrer votre choix : ", "light_blue") + colored("→ ", "cyan")))
    
    # Affichage d'une ligne de séparation
    print(colored("╚══════════════════════════════════════════════════════════════════════════════╝", "yellow"))
    
    return choix

def main():
    print_banner()

    playing = True

    while(playing == True):
        choix = print_menu()

        if(choix == 1):
            num_essais_MAX = 30
        if(choix == 2):
            num_essais_MAX = 15
        if(choix == 3):
            num_essais_MAX = 5
        if(choix == 4):
            num_essais_MAX = 1
        else:
            while(choix > 4 or choix < 1):
                choix = print_menu()
                if(choix == 1):
                    num_essais_MAX = 30
                if(choix == 2):
                    num_essais_MAX = 15
                if(choix == 3):
                    num_essais_MAX = 5
                if(choix == 4):
                    num_essais_MAX = 1

        num_computer = random.randint(0,100)

        check_validity_num(num_computer,num_essais_MAX,choix)
        
        replay = input(colored("Voulez-vous rejouer ? Oui/Non\n","light_cyan"))
        if(replay.upper() == "OUI"):
            playing = True
        if(replay.upper() == "NON"):
            playing = False

#------ Lancement du programme ------

main()