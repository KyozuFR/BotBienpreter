from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
try:
    from module.NTFY.ntfy import notify
except:
    print("the 'NTFY' module has not been activated")
# navigateur = webdriver.Firefox(service=Service("geckodriver.exe"))

print("""
BotBienpreter  Copyright (C) 2023  Linares Julien
This program comes with ABSOLUTELY NO WARRANTY; for details look at readme.md and LICENSE files.
This is free software, and you are welcome to redistribute it
under certain conditions; for details look at readme.md and LICENSE files.""")



with open("mdp.txt", "r") as mdp:
    email, mdp = mdp.readlines(0)[0].split("|")

def connection(lienproj):
    #Est appelé si l'utilisateur n'est pas connecté
    for button in navigateur.find_elements(By.TAG_NAME, "a"):
         if button.get_property('href') == "https://www.bienpreter.com/connexion":
             button.click()
             break
    navigateur.find_element(By.NAME, "user_login[email]").send_keys(email)
    navigateur.find_element(By.NAME, "user_login[password]").send_keys(mdp)
    testvar = 0
    while testvar == 0:
        for bouton in navigateur.find_elements(By.TAG_NAME, "button"):
            if bouton.text == "Se connecter":
                bouton.click()
                testvar = 1
                break
    testvar = 0
    while testvar == 0:
        for menu in navigateur.find_elements(By.TAG_NAME, "a"):
            if menu.get_property('href') == "https://www.bienpreter.com/projets":
                menu.click()
                testvar = 1
                break
    testvar = 0
    while testvar == 0:
        for menu in navigateur.find_elements(By.TAG_NAME, "a"):
            if menu.get_property('href') == lienproj:
                menu.click()
                testvar = 1
                break
    print("connected")


def BUYFONC(lien, mont):
    #Cette fonction attend que le timer défini par la page (et donc le projet) se termine. Elle a pour résultat grace à ses 2 entrée que sont le lien et le montant d'investir dans le projet souhaité.
    navigateur.get(lien)
    testvar = 0
    while testvar == 0:
        for texte in navigateur.find_elements(By.TAG_NAME, "em"):
            if texte.text == "VOUS DEVEZ ÊTRE CONNECTÉ(E) POUR PRÊTER DE L'ARGENT":
                connection(lien)
                testvar = 1
                break
            else:
                for texte in navigateur.find_elements(By.TAG_NAME, "a"):
                    if texte.text == "Le projet":
                        if texte.get_attribute('class').__contains__("disabled") is False:
                            testvar = 1
                            break
    print("Waiting")
    testvar = 0
    while testvar == 0:
        for menu in navigateur.find_elements(By.TAG_NAME, "a"):
            if menu.text == "PRÊTER" and "disabled" not in menu.get_attribute('class'):
                menu.click()
                testvar = 1
                break
    navigateur.find_element(By.NAME, "project_lend_money[amount]").send_keys(mont)
    testvar = 0
    while testvar == 0:
        for menu in navigateur.find_elements(By.TAG_NAME, "button"):
            if menu.text == "PRÊTER":
                menu.click()
                testvar = 1
                break
    navigateur.find_element(By.NAME, "project_lend_money_confirm[contractAccepted]").click()
    testvar = 0
    while testvar == 0:
        for menu in navigateur.find_elements(By.TAG_NAME, "button"):
            if menu.text == "Confirmer le prêt":
                menu.click()
                testvar = 1
                break
    print("successfully completed purchase")

navigateur = webdriver.Firefox(service=Service("geckodriver.exe"))
navigateur.implicitly_wait(20)
with open("lien.txt", "r+") as file:
    for i in file.readlines():
        lienause, nbmont = i.split("|")
        print("lien:", lienause, "montant:",nbmont)
        BUYFONC(lienause, int(nbmont))
        try:
            notify(lienause, nbmont)
        except:
            print("the 'NTFY' module has not been activated")