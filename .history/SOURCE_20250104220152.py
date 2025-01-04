import random
from termcolor import colored, cprint
import shutil

def check_validity_num(num_comp):    
    """Fonction qui vérifie si le nombre de l'utilisateur est supérieur/inférieur/égal au nombre de l'ordinateur.

    Args:
        num_comp (int): nombre aléatoire de l'ordinateur
    """
    num_user = int(input(colored("Veuillez entrer un nombre : ","light_magenta")))
    
    while(validity == False):
        if(num_user < num_comp):
            validity = False
            print(colored("Trop faible","white","on_blue"))
        if(num_user == num_comp):
            validity = True
            print(colored("Vous avez trouvé le nombre mystère !!!","white","on_green"))
        if(num_user > num_comp):
            validity = False
            print(colored("Trop grand","white","on_red"))
      

def print_banner():
    """
    Affiche une bannière stylée.
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
    print(colored(banner.center(cols), "cyan", attrs=["bold"]))         

print_banner

print(colored("\n\nVeuillez choisir votre mode de jeu :","blue"))
print(colored("- 1) Facile : Votre nombre est compris entre 0 et 100","blue"))
print("")
choix = int(input(colored("Veuillez entrer votre choix : ","light_blue")))

if(choix == 1):
    num_computer = random.randint(0,100)
else:
    while(choix != 1):
        print(colored("\n\nVeuillez choisir votre mode de jeu :","blue"))
        print(colored("- 1) Facile : Votre nombre est compris entre 0 et 100","blue"))
        print("")
        choix = int(input(colored("Veuillez entrer votre choix : ","light_blue")))

validity = False

check_validity_num(num_computer)