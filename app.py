from colorama import Style, Fore
from random import choice

niveis_agua = ["nivel1", "nivel2", "nivel3", "nivel4", "nivel5"]

nivel__atual_agua = choice(niveis_agua)


def exibir_mensagem():
    if nivel__atual_agua == niveis_agua[0]:
        print(Fore.RED + "Muito baixo (crítico)")
    elif nivel__atual_agua == niveis_agua[1]:
        print(Fore.YELLOW + "Baixo")
    elif nivel__atual_agua == niveis_agua[2]:
        print(Fore.GREEN + "Médio")
    elif nivel__atual_agua == niveis_agua[3]:
        print(Fore.CYAN + "Alto")
    elif nivel__atual_agua == niveis_agua[4]:
        print(Fore.BLUE + "Muito alto (alerta)")

exibir_mensagem()

print(Style.RESET_ALL)
