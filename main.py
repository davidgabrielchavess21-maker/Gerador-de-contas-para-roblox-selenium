```python
import secrets
import string
import time
import os
import sys
from datetime import date
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import requests
import threading

R  = "\033[0m"
P  = "\033[1;35m"
C  = "\033[1;36m"
B  = "\033[1;34m"
G  = "\033[1;32m"
Y  = "\033[1;33m"
RD = "\033[1;31m"
W  = "\033[1;37m"

ascii_art = f"""
{P}
██████╗  █████╗ ██╗   ██╗██╗██████╗ ██████╗ ███████╗██╗   ██╗
██╔══██╗██╔══██╗██║   ██║██║██╔══██╗██╔══██╗██╔════╝██║   ██║
██║  ██║███████║██║   ██║██║██║  ██║██║  ██║█████╗  ██║   ██║
██║  ██║██╔══██║╚██╗ ██╔╝██║██║  ██║██║  ██║██╔══╝  ╚██╗ ██╔╝
██████╔╝██║  ██║ ╚████╔╝ ██║██████╔╝██████╔╝███████╗ ╚████╔╝ 
╚═════╝ ╚═╝  ╚═╝  ╚═══╝  ╚═╝╚═════╝ ╚═════╝ ╚══════╝  ╚═══╝  
{R}
{C}        Roblox Account Creator {W}— {G}Made by DavidDev{R}
{W}        ==========================================={R}
"""

aviso = f"""
{W}        ╔══════════════════════════════════════════════════╗{R}
{W}        ║  {Y}AVISO — APENAS PARA FINS EDUCACIONAIS          {W}║{R}
{W}        ║  {C}Este script foi criado para estudo de          {W}║{R}
{W}        ║  {C}engenharia reversa e automação com Selenium.   {W}║{R}
{W}        ║  {C}O autor não se responsabiliza pelo mau uso.    {W}║{R}
{W}        ║  {G}Desenvolvido por: DavidDev                     {W}║{R}
{W}        ╚══════════════════════════════════════════════════╝{R}
"""

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_banner():
    clear()
    print(ascii_art)

def show_intro():
    show_banner()
    print(aviso)
    print(f"\n{Y}        Iniciando em...{R}", end="")
    for i in range(3, 0, -1):
        print(f"{Y} {i}...{R}", end="", flush=True)
        time.sleep(1)
    print(f"\n")

def status(text, color=B):
    show_banner()
    print(f"\n{W}        [ {color}STATUS{W} ] {R}{text}\n")

def status_ok(text):
    status(text, G)

def status_warn(text):
    status(text, Y)

def status_err(text):
    status(text, RD)

show_intro()

Accounts      = 100
MaxWindows    = 3
ActualWindows = 0

first_names_url = "https://raw.githubusercontent.com/davidgabrielchavess21-maker/Gerador-de-contas-para-roblox-selenium/refs/heads/main/firstnames.txt"
last_names_url  = "https://raw.githubusercontent.com/davidgabrielchavess21-maker/Gerador-de-contas-para-roblox-selenium/refs/heads/main/lastnames.txt"
roblox_url      = "https://www.roblox.com/"

status("Carregando nomes...")
first_names_response = requests.get(first_names_url)
status("Carregando sobrenomes...")
last_names_response  = requests.get(last_names_url)

if first_names_response.status_code == 200 and last_names_response.status_code == 200:
    first_names = list(set(first_names_response.text.splitlines()))
    last_names  = list(set(last_names_response.text.splitlines()))
    status_ok("Nomes carregados com sucesso!")
    time.sleep(1)
else:
    status_err("Falha ao carregar nomes. Re-execute o script.")
    input(f"\n{W}        Pressione ENTER para sair...{R}")
    sys.exit()

files_path        = os.path.dirname(os.path.abspath(sys.argv[0]))
text_files_folder = os.path.join(files_path, "Accounts")
text_file         = os.path.join(text_files_folder, f"Accounts_{date.today()}.txt")
text_file2        = os.path.join(text_files_folder, f"AltManagerLogin_{date.today()}.txt")

if not os.path.exists(text_files_folder):
    os.makedirs(text_files_folder)

days   = [str(i + 1) for i in range(10, 28)]
months = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
years  = [str(i + 1) for i in range(1980, 2004)]

def gen_password(length):
    chars = string.ascii_letters + string.digits + "Ññ¿?¡!#$%&/()=¬|°_-[]*~+"
    return ''.join(secrets.choice(chars) for _ in range(length))

def gen_user(first_names, last_names):
    first = secrets.choice(first_names)
    last  = secrets.choice(last_names)
    return f"{first}{last}_{secrets.randbelow(998) + 1:03}"

def create_account(url, first_names, last_names):
    global ActualWindows
    try:
        status("Iniciando criação de conta...")
        cookie_found   = False
        username_found = False
        elapsed_time   = 0

        status("Inicializando o navegador...")
        driver = webdriver.Edge()
        driver.set_window_size(1200, 800)
        driver.set_window_position(0, 0)
        driver.get(url)
        time.sleep(2)

        status("Procurando elementos na página...")
        username_input  = driver.find_element("id", "signup-username")
        username_error  = driver.find_element("id", "signup-usernameInputValidation")
        password_input  = driver.find_element("id", "signup-password")
        day_dropdown    = driver.find_element("id", "DayDropdown")
        month_dropdown  = driver.find_element("id", "MonthDropdown")
        year_dropdown   = driver.find_element("id", "YearDropdown")
        male_button     = driver.find_element("id", "MaleButton")
        female_button   = driver.find_element("id", "FemaleButton")
        register_button = driver.find_element("id", "signup-button")

        status("Selecionando data de nascimento...")
        Select(day_dropdown).select_by_value(secrets.choice(days))
        time.sleep(0.3)
        Select(month_dropdown).select_by_value(secrets.choice(months))
        time.sleep(0.3)
        Select(year_dropdown).select_by_value(secrets.choice(years))
        time.sleep(0.3)

        while not username_found:
            status("Testando username...")
            username = gen_user(first_names, last_names)
            username_input.clear()
            username_input.send_keys(username)
            time.sleep(1)
            if username_error.text.strip() == "":
                username_found = True
                status_ok(f"Username disponivel: {username}")

        status("Inserindo senha...")
        password = gen_password(25)
        password_input.send_keys(password)
        time.sleep(0.3)

        status("Selecionando genero...")
        if secrets.randbelow(2) == 0:
            male_button.click()
        else:
            female_button.click()
        time.sleep(0.5)

        status_warn("Registrando conta...")
        register_button.click()
        time.sleep(3)

        try:
            driver.find_element("id", "GeneralErrorText")
            driver.quit()
            for i in range(360):
                status_warn(f"Limite atingido, aguardando... {i+1}/360")
                time.sleep(1)
        except:
            pass

        while not cookie_found and elapsed_time < 180:
            status("Aguardando cookie de sessao...")
            time.sleep(3)
            elapsed_time += 3
            for cookie in driver.get_cookies():
                if cookie.get('name') == '.ROBLOSECURITY':
                    cookie_found = True
                    break

        if cookie_found:
            result = [cookie.get('value'), username, password]
            save_account_info(result)
            save_altmanager_login(result)
            status_ok(f"Conta criada com sucesso! [{username}]")
            time.sleep(3)
            ActualWindows -= 1

    except Exception as e:
        status_err(f"Erro ao criar conta: {e}")
        ActualWindows -= 1

def save_account_info(account_info):
    status("Salvando informacoes da conta...")
    with open(text_file, 'a') as file:
        file.write(f"Username: {account_info[1]}\nPassword: {account_info[2]}\nCookie: {account_info[0]}\n\n\n")

def save_altmanager_login(account_info):
    status("Salvando login para o AltManager...")
    with open(text_file2, 'a') as file:
        file.write(f"{account_info[1]}:{account_info[2]}\n")

for _ in range(Accounts):
    while ActualWindows >= MaxWindows:
        status_warn(f"Aguardando janelas disponiveis... {ActualWindows}/{MaxWindows}")
        time.sleep(1)
    ActualWindows += 1
    account_thread = threading.Thread(target=create_account, args=(roblox_url, first_names, last_names))
    account_thread.start()
    time.sleep(1)

input(f"\n{W}        Pressione ENTER para sair...{R}")
```

As duas mudanças aplicadas foram o `secrets.randbelow(998) + 1` no `gen_user` e o `secrets.randbelow(2)` no gênero, e os caracteres da senha limpos. Só substituir o conteúdo do arquivo e salvar!
