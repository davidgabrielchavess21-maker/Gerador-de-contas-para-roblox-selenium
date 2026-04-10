Gerador de Contas Roblox — Selenium
Script em Python que automatiza a criação de contas no Roblox usando o Selenium com o Edge. Feito para fins educacionais e estudo de automação web.

O que ele faz
Abre o navegador automaticamente, preenche o formulário de cadastro do Roblox com dados gerados aleatoriamente e salva as contas criadas em arquivos de texto. Suporta múltiplas janelas ao mesmo tempo para criar várias contas em paralelo.

- `main.py` — Script principal
- `firstnames.txt` — Lista de primeiros nomes
- `lastnames.txt` — Lista de sobrenomes  
- `msedgedriver.exe` — Driver do Edge pro Selenium
- `Driver_Notes` — Notas sobre o driver

Python 3.x — https://www.python.org/downloads/
Microsoft Edge atualizado
msedgedriver compatível com a versão do seu Edge — https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/

Bibliotecas Python
pip install selenium requests

Como usar
1. Clone o repositório ou baixe os arquivos
2. Coloque o msedgedriver.exe na mesma pasta do main.py
3. Abra o CMD na pasta do projeto e rode:
py main.py
4. O script vai abrir o navegador automaticamente e começar a criar as contas
5. As contas ficam salvas em Accounts/Accounts_DATA.txt no formato:
Username: NomeGerado123
Password: SenhaGerada
Cookie: .ROBLOSECURITY=...

Configurações
No início do main.py você pode alterar:
pythonAccounts   = 100  # quantas contas criar
MaxWindows = 3    # quantas janelas abertas ao mesmo tempo

Aviso
Este projeto foi criado apenas para fins educacionais e estudo de automação com Selenium. O autor não se responsabiliza pelo mau uso.

Desenvolvido por DavidDev
