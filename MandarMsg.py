import keyboard as k
from pywhatkit import sendwhatmsg
from pyautogui import click
from time import sleep

def mandarMsg():
    pywhatkit.sendwhatmsg('+5521983326343', 'Teste', 2, 17)
    pyautogui.click(2944, 983)
    time.sleep(2)
    k.press_and_release('enter')