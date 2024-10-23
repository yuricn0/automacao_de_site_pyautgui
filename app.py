import webbrowser
import pyautogui as gui
from time import sleep 


while True:
    # Navegar até o site 

    abrir_site = False 
    while abrir_site == False:
        try:
            webbrowser.open('https://cursoautomacao.netlify.app/?_gl=1*1oivtf5*_ga*NjA2ODQ5MDA5LjE3MjkwODc4NzU.*_ga_37GXT4VGQK*MTcyOTYzNzY0Ny45LjEuMTcyOTYzNzY3My4wLjAuMA..')
            abrir_site = True
        except Exception as e:
            gui.alert(text='Não foi possivel abrir o site. Erro {e}')
    # Pegar o nome do usuário

    nome = gui.prompt(text='Digite seu nome: ', title=('Dados pessoais'))

    # Scroll até o campo pra clicar o nome e clicar no nome

    gui.moveTo(x=-861,y=545, duration=2)
    sleep(1)
    gui.scroll(-1000)
    sleep(0.2)
    gui.moveTo(x=-361,y=565, duration=2)
    gui.click()
    sleep(0.2)

    # Digitar seu nome e apertar em alerta e depois fechar o aviso de alerta

    gui.typewrite(nome)
    gui.press('tab')
    sleep(0.4)
    gui.press('enter')
    sleep(0.4)
    gui.press('enter')
    sleep(1)

    # Scroll totalmente pra cima e depois até seção de arquivos

    gui.scroll(1000)
    sleep(1)
    gui.scroll(-1800)

    # Clicar em baixar 'Planilha Excel' e depois em 'Arquivo PDF'

    gui.click(x=-1484,y=949, duration=2)
    sleep(0.5)
    gui.click(x=-1199,y=949, duration=1)
    sleep(2)
    gui.click(x=-1199,y=824, duration=1)
    sleep(1)

    # Fechar janela

    gui.hotkey('Ctrl' , 'w')
    sleep(2)

    # Alert para avisar que a automação finalizou e se deseja continuar

    resposta = gui.confirm(text='Deseja continuar? ', title='Continuação de automação', buttons=('Sim', 'Não'))
    if resposta == 'Sim':
        continue
    else: 
        break
