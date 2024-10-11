from colorama import Fore, Style, init

# Inicializa o colorama no Windows (em outros sistemas operacionais, ele já funciona normalmente)
init(autoreset=True)

def menu():
    print(Fore.YELLOW + "____________________________")
    print(Fore.GREEN + "Bem-vindo à sua calculadora")
    print(Fore.CYAN + "Aqui está o menu de opções")
    
    print(Fore.MAGENTA + "1. Somar")
    print(Fore.MAGENTA + "2. Subtrair")
    print(Fore.MAGENTA + "3. Multiplicar")
    print(Fore.MAGENTA + "4. Dividir")
    print(Fore.RED + "0. Sair")
    
    print(Fore.YELLOW + "____________________________")
