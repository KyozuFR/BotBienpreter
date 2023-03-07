from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
# navigateur = webdriver.Firefox(service=Service("geckodriver.exe"))

print("""
BotBienpreter  Copyright (C) 2023  Linares Julien
This program comes with ABSOLUTELY NO WARRANTY; for details look at readme.txt and LICENSE files.
This is free software, and you are welcome to redistribute it
under certain conditions; for details look at readme.txt and LICENSE files.""")



with open("mdp.txt", "r") as mdp:
    email, mdp = mdp.readlines(0)[0].split("|")


def timer_define(lien, mont):
    #Cette fonction sert à enregistrer le temps restant avant la fin du décompte
    navigateur.get(lien)
    testvar = 0
    while testvar == 0:
        for texte in navigateur.find_elements(By.TAG_NAME, "em"):
            if texte.text == "VOUS DEVEZ ÊTRE CONNECTÉ(E) POUR PRÊTER DE L'ARGENT":
                for button in navigateur.find_elements(By.TAG_NAME, "a"):
                    if button.get_property('href') == "https://www.bienpreter.com/connexion":
                        button.click()
                        testvar = 1
                        break
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
            if menu.get_property('href') == lien:
                menu.click()
                testvar = 1
                break
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
    print("Fin de la v0,5")

navigateur = webdriver.Firefox(service=Service("geckodriver.exe"))
navigateur.implicitly_wait(20)
with open("lien.txt", "r+") as file:
    for i in file.readlines():
        lienause, nbmont = i.split("|")
        print("lien:", lienause, "montant:",nbmont)
        timer_define(lienause, int(nbmont))