import random
from termcolor import colored, cprint
import sys
import time
import shutil

def check_validity_num(num_comp,num_essais_MAX):    
    """Fonction qui vérifie si le nombre de l'utilisateur est supérieur/inférieur/égal au nombre de l'ordinateur.

    Args:
        num_comp (int): nombre aléatoire de l'ordinateur
    """
    validity = False
    
    num_essais = 1
    
    num_user = int(input(colored("Veuillez entrer un nombre : ","light_magenta")))
    
    while(validity == False):
        if(num_user < num_comp):
            validity = False
            print(colored("Trop faible ! ","white","on_blue"))
            num_essais +=1
            if(num_essais >= num_essais_MAX):
                validity = True
                print(colored("Nombre essaies DÉPASSÉ ! ","white","on_light_red",attrs=["bold", "blink"]))
                print(colored(f"Voici le nombre de l'ordinateur : {num_comp} ","white","on_light_red",attrs=["bold", "blink"]))
            if(num_essais < num_essais_MAX):
                num_user = int(input(colored("Veuillez entrer un nombre : ","light_magenta")))
        if(num_user == num_comp):
            validity = True
            print(colored("Vous avez trouvé le nombre mystère !!! ","white","on_light_green"))
        if(num_user > num_comp):
            validity = False
            print(colored("Trop grand ! ","white","on_red"))
            num_essais +=1
            if(num_essais >= num_essais_MAX):
                validity = True
                print(colored("Nombre essaies DÉPASSÉ ! ","white","on_light_red",attrs=["bold", "blink"]))
                print(colored(f"Voici le nombre de l'ordinateur : {num_comp} ","white","on_light_red",attrs=["bold", "blink"]))
            if(num_essais < num_essais_MAX):
                num_user = int(input(colored("Veuillez entrer un nombre : ","light_magenta")))
        
            
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
    print(colored(banner.center(cols), "light_yellow", attrs=["bold"]))         

print_banner()

def print_menu():
    print(colored("\nVeuillez choisir votre mode de jeu :","blue"))
    print(colored("- 1) Facile : Votre nombre est compris entre 0 et 100 (30 essais MAX)","blue"))
    print(colored("- 2) Moyen : Votre nombre est compris entre 0 et 100 (15 essais MAX)","blue"))
    print(colored("- 3) Difficile : Votre nombre est compris entre 0 et 100 (5 essais MAX)","blue"))
    print(colored("- 4) Hardcore : Votre nombre est compris entre 0 et 100 (1 essai MAX)","blue"))
    print("")
    choix = int(input(colored("Veuillez entrer votre choix : ","light_blue")))
    return choix

playing = True

while(playing = True):
    
    
