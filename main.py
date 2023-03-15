#import of libraries needed to use the browser
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
#tries to import the optional notification module, if it does not import, then the requests module has not been correctly installed
try:
    from module.NTFY.ntfy import notify
except:
    print("the 'NTFY' module has not been activated")

#License
print("""
BotBienpreter  Copyright (C) 2023  Linares Julien
This program comes with ABSOLUTELY NO WARRANTY; for details look at readme.md and LICENSE files.
This is free software, and you are welcome to redistribute it
under certain conditions; for details look at readme.md and LICENSE files.""")


#Recovery of the login and password in the "mdp.txt" file
with open("mdp.txt", "r") as mdp:
    email, mdp = mdp.readlines(0)[0].split("|")

def connection(lienproj):
    #Is called if the user is not logged in
    #find and click the connection button
    for button in navigateur.find_elements(By.TAG_NAME, "a"):
         if button.get_property('href') == "https://www.bienpreter.com/connexion":
             button.click()
             break
    #enter the email and password
    navigateur.find_element(By.NAME, "user_login[email]").send_keys(email)
    navigateur.find_element(By.NAME, "user_login[password]").send_keys(mdp)
    #look for the button to complete the login and click on it
    testvar = 0
    while testvar == 0:
        for bouton in navigateur.find_elements(By.TAG_NAME, "button"):
            if bouton.text == "Se connecter":
                bouton.click()
                testvar = 1
                break
    #Find the list of projects
    testvar = 0
    while testvar == 0:
        for menu in navigateur.find_elements(By.TAG_NAME, "a"):
            if menu.get_property('href') == "https://www.bienpreter.com/projets":
                menu.click()
                testvar = 1
                break
    #find the project requested by the user
    testvar = 0
    while testvar == 0:
        for menu in navigateur.find_elements(By.TAG_NAME, "a"):
            if menu.get_property('href') == lienproj:
                menu.click()
                testvar = 1
                break
    print("connected")


def BUYFONC(lien, mont):
    #This function waits for the timer defined by the page (and therefore the project) to end. The result of this function is to invest in the desired project using the link and the amount.
    navigateur.get(lien)
    #Variable to skip adding amounts if the amount is already defined for the project
    SkipPriceAmount = False
    testvar = 0
    #Login check
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
    #Waiting for the end of the timer
    testvar = 0
    while testvar == 0:
        for menu in navigateur.find_elements(By.TAG_NAME, "a"):
            if menu.text.__contains__("PRÊTER") is True and "disabled" not in menu.get_attribute('class') and menu.get_attribute('class').__contains__("btn"):
                if menu.text != "PRÊTER":
                    SkipPriceAmount = True
                menu.click()
                testvar = 1
                break
    #enter the desired amount but skip it if it is already defined
    if SkipPriceAmount == False:
        navigateur.find_element(By.NAME, "project_lend_money[amount]").send_keys(mont)
    #find the button to confirm the amount but skip it if it is already defined
    testvar = 0
    while testvar == 0 and SkipPriceAmount == False:
        for menu in navigateur.find_elements(By.TAG_NAME, "button"):
            if menu.text == "PRÊTER":
                menu.click()
                testvar = 1
                break
    #check the box to accept the terms and conditions
    navigateur.find_element(By.NAME, "project_lend_money_confirm[contractAccepted]").click()
    #Confirm the loan
    testvar = 0
    while testvar == 0:
        for menu in navigateur.find_elements(By.TAG_NAME, "button"):
            if menu.text == "Confirmer le prêt":
                menu.click()
                testvar = 1
                break
    print("successfully completed purchase")

#set the browser
navigateur = webdriver.Firefox(service=Service("geckodriver.exe"))
navigateur.implicitly_wait(20)
#for all links in "lien.txt"
with open("lien.txt", "r+") as file:
    for i in file.readlines():
        lienause, nbmont = i.split("|")
        print("lien:", lienause, "montant:",nbmont)
        #use of the purchasing function
        BUYFONC(lienause, int(nbmont))
        #tries to send a notification (optional so does nothing if not setup)
        try:
            notify(lienause, nbmont)
        except:
            print("the 'NTFY' module has not been activated")