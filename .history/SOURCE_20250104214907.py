import random
from termcolor import colored, cprint
import shutil

num_computer = random.randint(0,100)
validity = False

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

def check_validity_num(num_comp,num_user):    
    """Fonction qui vérifie si le nombre de l'utilisateur est supérieur/inférieur/égal au nombre de l'ordinateur.

    Args:
        num_comp (int): nombre aléatoire de l'ordinateur
        num_user (int): nombre choisi de l'utilisateur

    """
    while(validity == False){
        if(num_user < num_computer):   
    }