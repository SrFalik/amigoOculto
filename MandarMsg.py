from pywhatkit import sendwhatmsg_instantly
from pyautogui import click
from pyautogui import hotkey
from pyautogui import press
from time import sleep
from Sortear import sortear


def mandarMsg():
    listaResultado = sortear()
    for i in range(len(listaResultado)):
        sendwhatmsg_instantly(listaResultado[i]["r"]["numero"], 'Você tirou: ' + listaResultado[i]["r2"]["nome"])
        click(2944, 983)
        sleep(2)
        press('enter')
        sleep(2)
        hotkey('ctrl', 'w')

