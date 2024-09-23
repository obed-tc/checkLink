

from colorama import Fore, Style, init
import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
import os
import time
import whois
import socket
init(autoreset=True)


validos=[]
keyAbstract="6fa7808152de443d9c5e4ad272aeb108"
keyMailBox="ZVHI28XNZSRWE59KJ0PA"
def clearMonitor():
    if (os.name=="nt"):
        os.system("cls")
    else:
        os.system("clear")


def banner():
    clearMonitor()
    print(f"""{Fore.GREEN}
 ::::::::  :::    ::: ::::::::::  ::::::::  :::    ::: :::        ::::::::::: ::::    ::: :::    ::: 
:+:    :+: :+:    :+: :+:        :+:    :+: :+:   :+:  :+:            :+:     :+:+:   :+: :+:   :+:  
+:+        +:+    +:+ +:+        +:+        +:+  +:+   +:+            +:+     :+:+:+  +:+ +:+  +:+   
+#+        +#++:++#++ +#++:++#   +#+        +#++:++    +#+            +#+     +#+ +:+ +#+ +#++:++    
+#+        +#+    +#+ +#+        +#+        +#+  +#+   +#+            +#+     +#+  +#+#+# +#+  +#+   
#+#    #+# #+#    #+# #+#        #+#    #+# #+#   #+#  #+#            #+#     #+#   #+#+# #+#   #+#  
 ########  ###    ### ##########  ########  ###    ### ########## ########### ###    #### ###    ###
          
                                                                                    {Fore.RESET} Version 1.0
  {Fore.YELLOW} ▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌{Fore.RED}     [ {Fore.CYAN}Tool Created by obed-tc{Fore.RED} ]       {Fore.YELLOW}▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌
    """)
def menuBanner():
    print(f"""    {Fore.RED}[{Fore.RESET}01{Fore.RED}] {Fore.YELLOW} Grupo de whatsapp            {Fore.RED}[{Fore.RESET}06{Fore.RED}] {Fore.YELLOW} Perfil de instagram
    {Fore.RED}[{Fore.RESET}02{Fore.RED}] {Fore.YELLOW} Grupo de telegram            {Fore.RED}[{Fore.RESET}07{Fore.RED}] {Fore.YELLOW} DNS
    {Fore.RED}[{Fore.RESET}03{Fore.RED}] {Fore.YELLOW} Correo electronico           {Fore.RED}[{Fore.RESET}08{Fore.RED}] {Fore.YELLOW} Sitios web
    {Fore.RED}[{Fore.RESET}04{Fore.RED}] {Fore.YELLOW} Número de telefono           {Fore.RED}[{Fore.RESET}09{Fore.RED}] {Fore.YELLOW} URl de zoom
    {Fore.RED}[{Fore.RESET}05{Fore.RED}] {Fore.YELLOW} Perfil de facebook           {Fore.RED}[{Fore.RESET}10{Fore.RED}] {Fore.YELLOW} URl de google meet   
""")
def fetch_data(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json() 
        else:
            return f'Error: {response.status_code}'
    except Exception as e:
        return f'Exception: {str(e)}'
def selectOption(option):
    if (option=="1"):
        jobGroupWhatsapp()
    elif (option=="2"):
        jobGroupTelegram()
    elif (option=="3"):
        verifyEmail()
    elif (option=="4"):
        print("Pronto")
        input("")
    elif (option=="5"):
        jobUrlFacebook()
    elif (option=="6"):
        jobUrlInstagram()
    elif (option=="7"):
        jobDns()
    elif (option=="8"):
        jobWebsite()
    elif (option=="9"):
        print("Proximamente")
        input("")
    elif (option=="10"):
        print("Proximamente")
        input("")
    else:
        print(f"{Fore.LIGHTRED_EX}\n           :( Opcion incorrecta")
        time.sleep(2)

def jobDns():
    clearMonitor()
    print(f"""{Fore.LIGHTGREEN_EX}
VERIFICAR DISPONIBILIDAD DE DOMINIOS
          
    {Fore.RED}[{Fore.RESET}01{Fore.RED}] {Fore.YELLOW} Verificacion individual       
    {Fore.RED}[{Fore.RESET}02{Fore.RED}] {Fore.YELLOW} Verificacion masiva         (File TXT required)
""")
    option=str(input(f"{Fore.RED}[{Fore.RESET}-{Fore.RED}]{Fore.LIGHTYELLOW_EX} Select an option: {Fore.RESET} "))
    if (option=="1"):
        url=str(input(f"\n{Fore.RED}[{Fore.RESET}-{Fore.RED}]{Fore.LIGHTYELLOW_EX} Enter domain: {Fore.RESET}"))
        verify_dns(url)
        input(f"\n\n{Fore.LIGHTYELLOW_EX}Presione {Fore.YELLOW}ENTER{Fore.LIGHTYELLOW_EX} para volver al Menu principal")

    elif(option=="2"):
        path=str(input(f"\n{Fore.RED}[{Fore.RESET}-{Fore.RED}]{Fore.LIGHTYELLOW_EX} Enter path file (example.txt): {Fore.RESET}"))
        readTxt(path,"dns")
        input(f"\n\n{Fore.LIGHTYELLOW_EX}Presione {Fore.YELLOW}ENTER{Fore.LIGHTYELLOW_EX} para volver al Menu principal")

    else:
        print(f"{Fore.LIGHTRED_EX}\n           :( Opcion incorrecta")
        time.sleep(2)

def jobWebsite():
    clearMonitor()
    print(f"""{Fore.LIGHTGREEN_EX}
VERIFICAR SITIOS WEB
          
    {Fore.RED}[{Fore.RESET}01{Fore.RED}] {Fore.YELLOW} Verificacion individual       
    {Fore.RED}[{Fore.RESET}02{Fore.RED}] {Fore.YELLOW} Verificacion masiva         (File TXT required)
""")
    option=str(input(f"{Fore.RED}[{Fore.RESET}-{Fore.RED}]{Fore.LIGHTYELLOW_EX} Select an option: {Fore.RESET} "))
    if (option=="1"):
        url=str(input(f"\n{Fore.RED}[{Fore.RESET}-{Fore.RED}]{Fore.LIGHTYELLOW_EX} Enter url website: {Fore.RESET}"))
        verify_website(url)
        input(f"\n\n{Fore.LIGHTYELLOW_EX}Presione {Fore.YELLOW}ENTER{Fore.LIGHTYELLOW_EX} para volver al Menu principal")

    elif(option=="2"):
        path=str(input(f"\n{Fore.RED}[{Fore.RESET}-{Fore.RED}]{Fore.LIGHTYELLOW_EX} Enter path file (example.txt): {Fore.RESET}"))
        readTxt(path,"website")
        input(f"\n\n{Fore.LIGHTYELLOW_EX}Presione {Fore.YELLOW}ENTER{Fore.LIGHTYELLOW_EX} para volver al Menu principal")

    else:
        print(f"{Fore.LIGHTRED_EX}\n           :( Opcion incorrecta")
        time.sleep(2)

def jobGroupWhatsapp():
    clearMonitor()
    print(f"""{Fore.LIGHTGREEN_EX}
VALIDAR GRUPO DE WHATSAPP
          
    {Fore.RED}[{Fore.RESET}01{Fore.RED}] {Fore.YELLOW} Validacion individual       
    {Fore.RED}[{Fore.RESET}02{Fore.RED}] {Fore.YELLOW} Validación masiva         (File TXT required)
""")
    option=str(input(f"{Fore.RED}[{Fore.RESET}-{Fore.RED}]{Fore.LIGHTYELLOW_EX} Select an option: {Fore.RESET} "))
    if (option=="1"):
        url=str(input(f"\n{Fore.RED}[{Fore.RESET}-{Fore.RED}]{Fore.LIGHTYELLOW_EX} Enter url group whatsapp: {Fore.RESET}"))
        verifyUrlGroupWhatsapp(url)
        input(f"\n\n{Fore.LIGHTYELLOW_EX}Presione {Fore.YELLOW}ENTER{Fore.LIGHTYELLOW_EX} para volver al Menu principal")

    elif(option=="2"):
        path=str(input(f"\n{Fore.RED}[{Fore.RESET}-{Fore.RED}]{Fore.LIGHTYELLOW_EX} Enter path file (example.txt): {Fore.RESET}"))
        readTxt(path,"whatsapp")
        input(f"\n\n{Fore.LIGHTYELLOW_EX}Presione {Fore.YELLOW}ENTER{Fore.LIGHTYELLOW_EX} para volver al Menu principal")

    else:
        print(f"{Fore.LIGHTRED_EX}\n           :( Opcion incorrecta")
        time.sleep(2)

def jobGroupTelegram():
    clearMonitor()
    print(f"""{Fore.LIGHTCYAN_EX}
VALIDAR GRUPO DE TELEGRAM
          
    {Fore.RED}[{Fore.RESET}01{Fore.RED}] {Fore.YELLOW} Validacion individual       
    {Fore.RED}[{Fore.RESET}02{Fore.RED}] {Fore.YELLOW} Validación masiva         (File TXT required)
""")
    option=str(input(f"{Fore.RED}[{Fore.RESET}-{Fore.RED}]{Fore.LIGHTYELLOW_EX} Select an option: {Fore.RESET} "))
    if (option=="1"):
        url=str(input(f"\n{Fore.RED}[{Fore.RESET}-{Fore.RED}]{Fore.LIGHTYELLOW_EX} Enter url group telegram: {Fore.RESET}"))
        verifyUrlGroupTelegram(url)
        input(f"\n\n{Fore.LIGHTYELLOW_EX}Presione {Fore.YELLOW}ENTER{Fore.LIGHTYELLOW_EX} para volver al Menu principal")

    elif(option=="2"):
        path=str(input(f"\n{Fore.RED}[{Fore.RESET}-{Fore.RED}]{Fore.LIGHTYELLOW_EX} Enter path file (example.txt): {Fore.RESET}"))
        readTxt(path,"telegram")
        input(f"\n\n{Fore.LIGHTYELLOW_EX}Presione {Fore.YELLOW}ENTER{Fore.LIGHTYELLOW_EX} para volver al Menu principal")

    else:
        print(f"{Fore.LIGHTRED_EX}\n           :( Opcion incorrecta")
        time.sleep(2)

def jobUrlFacebook():
    clearMonitor()
    print(f"""{Fore.LIGHTBLUE_EX}
VALIDAR PERFIL DE FACEBOOK
          
    {Fore.RED}[{Fore.RESET}01{Fore.RED}] {Fore.YELLOW} Validacion individual       
    {Fore.RED}[{Fore.RESET}02{Fore.RED}] {Fore.YELLOW} Validación masiva         (File TXT required)
""")
    option=str(input(f"{Fore.RED}[{Fore.RESET}-{Fore.RED}]{Fore.LIGHTYELLOW_EX} Select an option: {Fore.RESET} "))
    if (option=="1"):
        url=str(input(f"\n{Fore.RED}[{Fore.RESET}-{Fore.RED}]{Fore.LIGHTYELLOW_EX} Enter url profile facebook: {Fore.RESET}"))
        verifyUrlFacebook(url)
        input(f"\n\n{Fore.LIGHTYELLOW_EX}Presione {Fore.YELLOW}ENTER{Fore.LIGHTYELLOW_EX} para volver al Menu principal")

    elif(option=="2"):
        path=str(input(f"\n{Fore.RED}[{Fore.RESET}-{Fore.RED}]{Fore.LIGHTYELLOW_EX} Enter path file (example.txt): {Fore.RESET}"))
        readTxt(path,"facebook")
        input(f"\n\n{Fore.LIGHTYELLOW_EX}Presione {Fore.YELLOW}ENTER{Fore.LIGHTYELLOW_EX} para volver al Menu principal")

    else:
        print(f"{Fore.LIGHTRED_EX}\n           :( Opcion incorrecta")
        time.sleep(2)

def jobUrlInstagram():
    clearMonitor()
    print(f"""{Fore.LIGHTRED_EX}
VALIDAR PERFIL DE INSTAGRAM
          
    {Fore.RED}[{Fore.RESET}01{Fore.RED}] {Fore.YELLOW} Validacion individual       
    {Fore.RED}[{Fore.RESET}02{Fore.RED}] {Fore.YELLOW} Validación masiva         (File TXT required)
""")
    option=str(input(f"{Fore.RED}[{Fore.RESET}-{Fore.RED}]{Fore.LIGHTYELLOW_EX} Select an option: {Fore.RESET} "))
    if (option=="1"):
        url=str(input(f"\n{Fore.RED}[{Fore.RESET}-{Fore.RED}]{Fore.LIGHTYELLOW_EX} Enter url profile instagram: {Fore.RESET}"))
        verifyUrlInstagram(url)
        input(f"\n\n{Fore.LIGHTYELLOW_EX}Presione {Fore.YELLOW}ENTER{Fore.LIGHTYELLOW_EX} para volver al Menu principal")

    elif(option=="2"):
        path=str(input(f"\n{Fore.RED}[{Fore.RESET}-{Fore.RED}]{Fore.LIGHTYELLOW_EX} Enter path file (example.txt): {Fore.RESET}"))
        readTxt(path,"instagram")
        input(f"\n\n{Fore.LIGHTYELLOW_EX}Presione {Fore.YELLOW}ENTER{Fore.LIGHTYELLOW_EX} para volver al Menu principal")

    else:
        print(f"{Fore.LIGHTRED_EX}\n           :( Opcion incorrecta")
        time.sleep(2)



def readTxt(file,type):
    global validos
    with open(file, 'r', encoding='utf-8') as archivo:
        lineas = archivo.readlines()
        
        for linea in lineas:
            url=linea.strip()
            if (type=="whatsapp"):
                verifyUrlGroupWhatsapp(str(url))
            elif (type=="telegram"):
                verifyUrlGroupTelegram(str(url))
            elif (type=="facebook"):
                verifyUrlFacebook(str(url))
            elif (type=="instagram"):
                verifyUrlFacebook(str(url))
            elif (type=="dns"):
                verify_dns(str(url))
            elif (type=="website"):
                verify_website(str(url))
    print(f"{Fore.GREEN}\n====================={Fore.RESET} RESULTADOS{Fore.GREEN} ===========================")
    print(f"\n{Fore.CYAN}[{Fore.RESET}*{Fore.CYAN}]{Fore.LIGHTCYAN_EX} Links revisados ",len(lineas))
    
    print(f"\n{Fore.CYAN}[{Fore.RESET}*{Fore.CYAN}]{Fore.LIGHTCYAN_EX} Links validos ",len(validos))
    
    if (len(validos)>=1):
        if (type=="whatsapp"):
            print(f"\n{Fore.RESET}[{Fore.GREEN}OK{Fore.RESET}]{Fore.RESET} Guardado Valid_WhatsappGroups.txt")
            saveTxt(validos,"Valid_Whatsapp_Groups")
        elif (type=="telegram"):
            print(f"\n{Fore.RESET}[{Fore.GREEN}OK{Fore.RESET}]{Fore.RESET} Guardado Valid_TelegramGroups.txt")
            saveTxt(validos,"Valid_Telegram_Groups")
        elif (type=="facebook"):
            print(f"\n{Fore.RESET}[{Fore.GREEN}OK{Fore.RESET}]{Fore.RESET} Guardado Valid_Facebook_Profiles.txt")
            saveTxt(validos,"Valid_Facebook_Profiles")
        elif (type=="instagram"):
            print(f"\n{Fore.RESET}[{Fore.GREEN}OK{Fore.RESET}]{Fore.RESET} Guardado Valid_Instagram_Profiles.txt")
            saveTxt(validos,"Valid_Instagram_Profiles")
        elif (type=="dns"):
            print(f"\n{Fore.RESET}[{Fore.GREEN}OK{Fore.RESET}]{Fore.RESET} Guardado Valid_DNS.txt")
            saveTxt(validos,"Valid_DNS")
        elif (type=="website"):
            print(f"\n{Fore.RESET}[{Fore.GREEN}OK{Fore.RESET}]{Fore.RESET} Guardado Valid_Websites.txt")
            saveTxt(validos,"Valid_Websites")
        validos=[]
    
def saveTxt(mi_lista,nameFile):
    with open(nameFile+'.txt', 'w', encoding='utf-8') as archivo:
        for elemento in mi_lista:
            archivo.write(elemento + '\n') 
def verifyUrlGroupWhatsapp(url):
    global validos
    print("________________________________________________________")
    print(Fore.CYAN+"\n[URL] "+Fore.YELLOW+url)

    print(f"\n{Fore.CYAN}[{Fore.RESET}-{Fore.CYAN}]{Fore.LIGHTCYAN_EX} Verificando formato url...")

    if ("https://chat.whatsapp.com" not in url):
        print("[x] FORMATO NO VALIDO")
        input()
        return
    print(f"{Fore.CYAN}[{Fore.RESET}-{Fore.CYAN}]{Fore.LIGHTCYAN_EX} Verificando url...")
    page = urlopen(url)
    html = page.read().decode("utf-8")
    soup = BeautifulSoup(html, "html.parser")

    name_group=(soup.find_all("h3")[1]).text

    if (len(name_group)<1):
        print(F"\n{Fore.YELLOW}[{Fore.RED}!{Fore.YELLOW}]{Fore.LIGHTRED_EX} Url no valida")
    else:
        print(f"\n{Fore.RESET}[{Fore.GREEN}OK{Fore.RESET}]{Fore.RESET} Grupo de whatsapp valido")
        print(f"{Fore.RESET}[{Fore.GREEN}OK{Fore.RESET}]{Fore.CYAN} Nombre del grupo :{Fore.RESET} {name_group}")
        print(f"{Fore.RESET}[{Fore.GREEN}OK{Fore.RESET}]{Fore.CYAN} URL: {Fore.RESET} {url}")

        validos.append(url)

def verifyUrlGroupTelegram(url):
    global validos
    print("________________________________________________________")
    print(Fore.CYAN+"\n[URL] "+Fore.YELLOW+url)

    print(f"\n{Fore.CYAN}[{Fore.RESET}-{Fore.CYAN}]{Fore.LIGHTCYAN_EX} Verificando formato url...")

    if ("https://t.me/" not in url):
        print("[x] FORMATO NO VALIDO")
        return
    print(f"{Fore.CYAN}[{Fore.RESET}-{Fore.CYAN}]{Fore.LIGHTCYAN_EX} Verificando url...")
    page = urlopen(url)
    html = page.read().decode("utf-8")
    soup = BeautifulSoup(html, "html.parser")

    classgroup=soup.find_all(class_="tgme_page_title")
    name_group=""
    if (len(classgroup)!=0):
        name_group=((classgroup[0]).find("span")).text

    if (len(name_group)<1):
        print(F"\n{Fore.YELLOW}[{Fore.RED}!{Fore.YELLOW}]{Fore.LIGHTRED_EX} Url no valida")
    else:
        print(f"\n{Fore.RESET}[{Fore.GREEN}OK{Fore.RESET}]{Fore.RESET} Grupo de Telegram valido")
        print(f"{Fore.RESET}[{Fore.GREEN}OK{Fore.RESET}]{Fore.CYAN} Nombre del grupo :{Fore.RESET} {name_group}")
        print(f"{Fore.RESET}[{Fore.GREEN}OK{Fore.RESET}]{Fore.CYAN} URL: {Fore.RESET} {url}")

        validos.append(url)

def verifyUrlFacebook(url):
    global validos
    print("________________________________________________________")
    print(Fore.CYAN+"\n[URL] "+Fore.YELLOW+url)

    print(f"\n{Fore.CYAN}[{Fore.RESET}-{Fore.CYAN}]{Fore.LIGHTCYAN_EX} Verificando formato url...")

    if ("https://www.facebook.com/" not in url):
        print("[x] FORMATO NO VALIDO")

        return
    print(f"{Fore.CYAN}[{Fore.RESET}-{Fore.CYAN}]{Fore.LIGHTCYAN_EX} Verificando url...")
    
        
    page = urlopen(url)
    html = page.read().decode("utf-8")
    soup = BeautifulSoup(html, "html.parser")
    name_group=soup.title.string
    if (len(name_group)<1 or name_group=="Facebook"):
        print(F"\n{Fore.YELLOW}[{Fore.RED}!{Fore.YELLOW}]{Fore.LIGHTRED_EX} Url no valida")
    else:
        print(f"\n{Fore.RESET}[{Fore.GREEN}OK{Fore.RESET}]{Fore.RESET} Url de facebook valido")
        print(f"{Fore.RESET}[{Fore.GREEN}OK{Fore.RESET}]{Fore.CYAN} Nombre :{Fore.RESET} {name_group}")
        print(f"{Fore.RESET}[{Fore.GREEN}OK{Fore.RESET}]{Fore.CYAN} URL: {Fore.RESET} {url}")
        validos.append(url)

def verifyUrlInstagram(url):
    global validos
    print("________________________________________________________")
    print(Fore.CYAN+"\n[URL] "+Fore.YELLOW+url)

    print(f"\n{Fore.CYAN}[{Fore.RESET}-{Fore.CYAN}]{Fore.LIGHTCYAN_EX} Verificando formato url...")
    if ("https://www.instagram.com/" not in url):
        print("[x] FORMATO NO VALIDO")
        return
    print(f"{Fore.CYAN}[{Fore.RESET}-{Fore.CYAN}]{Fore.LIGHTCYAN_EX} Verificando url...")
    page = urlopen(url)
    html = page.read().decode("utf-8")
    soup = BeautifulSoup(html, "html.parser")
    name_group=soup.title.string
    if (len(name_group)<1 or name_group=="Instagram" ):
        print(F"\n{Fore.YELLOW}[{Fore.RED}!{Fore.YELLOW}]{Fore.LIGHTRED_EX} Url no valida")
    else:
        print(f"\n{Fore.RESET}[{Fore.GREEN}OK{Fore.RESET}]{Fore.RESET} Url de instagram valido")
        print(f"{Fore.RESET}[{Fore.GREEN}OK{Fore.RESET}]{Fore.CYAN} Nombre :{Fore.RESET} {name_group.split(' ')[0]} {name_group.split(' ')[1]}")
        print(f"{Fore.RESET}[{Fore.GREEN}OK{Fore.RESET}]{Fore.CYAN} URL: {Fore.RESET} {url}")
        validos.append(url)

def verify_dns(dominio):
    try:
        global validos
        print("________________________________________________________")
        print(Fore.CYAN + "\n[DNS] " + Fore.YELLOW + dominio)
        
        info_dominio = whois.whois(dominio)
        if info_dominio.get("creation_date") is None:
            print(f"\n{Fore.RESET}[{Fore.GREEN}OK{Fore.RESET}] El dominio {dominio} está disponible.")
            validos.append(dominio)

        else:
            print(f"\n{Fore.YELLOW}[{Fore.RED}!{Fore.YELLOW}] {Fore.LIGHTRED_EX}El dominio ya está registrado.")
            creation_date = info_dominio.get("creation_date")
            if isinstance(creation_date, list):
                creation_date = creation_date[0]
            print(f"\n{Fore.RESET}[{Fore.GREEN}-{Fore.RESET}] Fecha de creación: {creation_date}")
            expiration_date = info_dominio.get("expiration_date")
            if isinstance(expiration_date, list):
                expiration_date = expiration_date[0]
            print(f"{Fore.RESET}[{Fore.GREEN}-{Fore.RESET}] Fecha de expiración: {expiration_date}")
            registrant = info_dominio.get("registrar")
            if registrant:
                print(f"{Fore.RESET}[{Fore.GREEN}-{Fore.RESET}] Registrante: {registrant}")
            name_servers = info_dominio.get("name_servers")
            if name_servers:
                print(f"{Fore.RESET}[{Fore.GREEN}-{Fore.RESET}] Servidores de nombres (DNS): {', '.join(name_servers)}")
            emails = info_dominio.get("emails")
            if emails:
                print(f"{Fore.RESET}[{Fore.GREEN}-{Fore.RESET}] Correo(s) de contacto: {''.join(emails)}")
            
    except Exception as e:
        if "No match for" in str(e):
            print(f"\n{Fore.RESET}[{Fore.GREEN}OK{Fore.RESET}] El dominio {dominio} está disponible.")
            validos.append(dominio)

        else:
            print(f"Error al consultar el dominio {dominio}: {e}")


def verifyEmail():
    clearMonitor()
    print(f"""{Fore.LIGHTRED_EX}
Select option:
          
    {Fore.RED}[{Fore.RESET}01{Fore.RED}] {Fore.YELLOW} Abstract Api
    {Fore.RED}[{Fore.RESET}02{Fore.RED}] {Fore.YELLOW} MailBox
""")
    option=str(input(f"{Fore.RED}[{Fore.RESET}-{Fore.RED}]{Fore.LIGHTYELLOW_EX} Select an option: {Fore.RESET} "))
    email=str(input(f"{Fore.RED}[{Fore.RESET}-{Fore.RED}]{Fore.LIGHTYELLOW_EX} Enter email: {Fore.RESET} "))
    
    if (option=="1"):
        getAbstractEmail(email)
    elif (option=="2"):
        getMailBox(email)
    
    input(f"\n\n{Fore.LIGHTYELLOW_EX}Presione {Fore.YELLOW}ENTER{Fore.LIGHTYELLOW_EX} para volver al Menu principal")
def verifyGmail():
    print("Use a mechanize")
def getMailBox(email):
    global keyMailBox
    data=fetch_data(f"https://api.mailboxvalidator.com/v2/validation/single?email={email}&key={keyMailBox}")
    if 'error' in data:
        print(data['error'])
    else:
        email_address = data.get('email_address')
        domain = data.get('domain')
        is_free = data.get('is_free')
        is_syntax = data.get('is_syntax')
        is_smtp = data.get('is_smtp')
        is_verified = data.get('is_verified')


        print(f"\n{Fore.RESET}[{Fore.GREEN}OK{Fore.RESET}]{Fore.CYAN} Email: {Fore.RESET}{email_address}")
        print(f"{Fore.RESET}[{Fore.GREEN}OK{Fore.RESET}]{Fore.CYAN} Dominio: {Fore.RESET}{domain}")

        print(f'{Fore.RESET}[{Fore.GREEN+"OK" if is_syntax else Fore.RED+"!"}{Fore.RESET}]{Fore.CYAN} Formato:{Fore.RESET} {"Valido" if is_syntax else "Invalido"}')
        
        print(f"{Fore.RESET}[{Fore.GREEN}OK{Fore.RESET}]{Fore.CYAN} Tipo:{Fore.RESET} {'Gratuito' if is_free else 'Pago'}")
        print(f"{Fore.RESET}[{Fore.GREEN}OK{Fore.RESET}]{Fore.CYAN} Verificado:{Fore.RESET} {'Si' if is_verified else 'No'}")
        print(f"\n{Fore.RESET}[{Fore.GREEN+'OK' if is_smtp else Fore.RED+'!'}{Fore.RESET}]{Fore.GREEN if is_smtp else Fore.RED} El correo electronico {'Existe' if is_smtp else 'No existe'}")

def getAbstractEmail(email):
    global keyAbstract
    data=fetch_data(f"https://emailvalidation.abstractapi.com/v1/?api_key={keyAbstract}&email={email}")
    if 'error' in data:
        print(data['error'])
    else:
        email = data.get('email')
        
        is_valid_format = data.get('is_valid_format', {}).get('value')
        is_free_email = data.get('is_free_email', {}).get('value')
        is_mx_found = data.get('is_mx_found', {}).get('value')
        is_smtp_valid = data.get('is_smtp_valid', {}).get('value')

        print(f"\n{Fore.RESET}[{Fore.GREEN}OK{Fore.RESET}]{Fore.CYAN} Email: {Fore.RESET}{email}")
        print(f'{Fore.RESET}[{Fore.GREEN+"OK" if is_valid_format else Fore.RED+"!"}{Fore.RESET}]{Fore.CYAN} Formato:{Fore.RESET} {"Valido" if is_valid_format else "Invalido"}')
        
        print(f"{Fore.RESET}[{Fore.GREEN}OK{Fore.RESET}]{Fore.CYAN} Tipo:{Fore.RESET} {'Gratuito' if is_free_email else 'Pago'}")
        print(f"{Fore.RESET}[{Fore.GREEN}OK{Fore.RESET}]{Fore.CYAN} Dominio:{Fore.RESET} {'Valido' if is_mx_found else 'Invalido'}")
        print(f"\n{Fore.RESET}[{Fore.GREEN+'OK' if is_smtp_valid else Fore.RED+'!'}{Fore.RESET}]{Fore.GREEN if is_smtp_valid else Fore.RED} El correo electronico {'Existe' if is_smtp_valid else 'No existe'}")

def verify_website(url):
    global validos

    print("________________________________________________________")
    print(Fore.CYAN+"\n[URL] "+Fore.YELLOW+url)
    if url.startswith('http://'):
        url_sin_protocolo = url.replace('http://', '')
    elif url.startswith('https://'):
        url_sin_protocolo = url.replace('https://', '')
    else:
        url_sin_protocolo = url
    
    for protocolo in ['https://', 'http://']:
        try:
            url_completa = protocolo + url_sin_protocolo
            
            response = requests.get(url_completa, timeout=5)
            
            if response.status_code == 200:
                ip_address = socket.gethostbyname(url_sin_protocolo.split('/')[0])
                validos.append(protocolo+url_sin_protocolo)
                print(f"\n{Fore.RESET}[{Fore.GREEN}OK{Fore.RESET}] El sitio web está activo con {protocolo}. \n{Fore.GREEN}Dirección IP:{Fore.YELLOW} {ip_address}")
            else:
                print(f"\n{Fore.YELLOW}[{Fore.RED}!{Fore.YELLOW}]{Fore.LIGHTRED_EX} El sitio web no existe o no está accesible con {protocolo}")

        except requests.ConnectionError:
            print("Error")
    

def startScript():
    try:
        while True:
            banner()
            menuBanner()
            option=str(input(f"{Fore.RED}[{Fore.RESET}-{Fore.RED}]{Fore.LIGHTGREEN_EX} Select an option{Fore.RED} : {Fore.LIGHTCYAN_EX}"))
            selectOption(option)
    except:
        
        print(f"{Fore.RED}\n\n[!] Cerrando checkLink")

if __name__=="__main__":
    startScript()