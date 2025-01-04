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

"""

    Args:
        num_comp (): nombre aléatoire de l'ordinateur
        num_user (int): nombre choisi de l'utilisateur
    """

def check_validity_num(num_comp,num_user):    
    """Fonction qui vérifie si le nombre de l'utilisateur est supérieur/inférieur/égal au nombre de l'ordinateur.

    Args:
        num_comp (_type_): _description_
        num_user (_type_): _description_

    Returns:
        _type_: _description_
    """
    return validity