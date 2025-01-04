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
    """_summary_

    Args:
        num_comp (_type_): _description_
        num_user (_type_): _description_

    Returns:
        _type_: _description_
    """
    return validity