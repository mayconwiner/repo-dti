import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import pyautogui
import os
import webbrowser
from time import sleep

def begin(usuario,senha):
    pyautogui.PAUSE = 4
    webbrowser.open('https://nossahepta.com.br')
    pyautogui.click(349,535,clicks=2,duration=0.1)
    sleep(3)
    pyautogui.click(349,535,clicks=2,duration=0.1)
    pyautogui.PAUSE = 2
    pyautogui.write(usuario,interval=0.1)
    pyautogui.click(321,583,duration=1) 
    pyautogui.write(senha,interval=1)
    pyautogui.press('enter')
    pyautogui.PAUSE = 2
    opcao()
sleep(3)

def folhaPonto():
    #Entra no folha de ponto 
    pyautogui.click(669,142,duration=1)
    pyautogui.PAUSE = 2
    pyautogui.click(461,462,duration=1)
    sleep(2)
    pyautogui.click(506,639,duration=1)
    sleep(3)
    pyautogui.click(1395,469)
    pyautogui.PAUSE = 4
    pyautogui.press('enter')

def visitas():
    #Entra no visitas 
    pyautogui.click(669,142,duration=1)
    pyautogui.PAUSE = 2
    pyautogui.click(461,462,duration=1)
    sleep(2)
    pyautogui.click(510,782,duration=1)
    sleep(2)
    pyautogui.click(1417,435,duration=1)

    

def opcao():
    resposta = pyautogui.confirm(
        text='Qual funcionalidade deseja acessar?',
        title='Sistema de Acesso',
        buttons=['Visitas', 'Folha de Ponto', 'Repetir Procedimento']

    )

    if resposta == 'Visitas':
        visitas()
    elif resposta == 'Folha de Ponto':
        folhaPonto()
    elif resposta == 'Repetir Procedimento':
        begin()
    else:
        pyautogui.alert('Opção Invalida')
        exit()

sleep(3)

class DataEntryForm(ttk.Frame):

    def __init__(self, master):
        super().__init__(master, padding=(20, 10))
        self.pack(fill=BOTH, expand=YES)

        # Variaveis do formulário
        self.name = ttk.StringVar(value="")
        self.password = ttk.StringVar(value="")

        # cabeçalho do formulário
        hdr_txt = "Entre com seu usuário e senha para inicializar o sistema" 
        hdr = ttk.Label(master=self, text=hdr_txt, width=50)
        hdr.pack(fill=X, pady=10)

        # Entradas do formulário
        self.create_form_entry("Usuário", self.name)
        self.create_form_entry("Senha", self.password, show="*")
        self.create_buttonbox()

    def create_form_entry(self, label, variable, show=None):
        """Cria o formulário de entrada"""
        container = ttk.Frame(self)
        container.pack(fill=X, expand=YES, pady=5)

        lbl = ttk.Label(master=container, text=label.title(), width=10)
        lbl.pack(side=LEFT, padx=5)

        ent = ttk.Entry(master=container, textvariable=variable, show=show)
        ent.pack(side=LEFT, padx=5, fill=X, expand=YES)

    def create_buttonbox(self):
        """Cria os botões de submissão e cancelamento."""
        container = ttk.Frame(self)
        container.pack(fill=X, expand=YES, pady=(15, 10))

        sub_btn = ttk.Button(
            master=container,
            text="Login",
            command=self.on_submit,
            bootstyle=SUCCESS,
            width=6,
        )
        sub_btn.pack(side=RIGHT, padx=5)
        sub_btn.focus_set()

        cnl_btn = ttk.Button(
            master=container,
            text="Cancelar",
            command=self.on_cancel,
            bootstyle=DANGER,
            width=6,
        )
        cnl_btn.pack(side=RIGHT, padx=5)

    def on_submit(self):
        begin(self.name.get(),self.password.get())
        self.quit()
    
       
    def on_cancel(self):
        """Fecha a aplicação."""
        self.quit()


if __name__ == "__main__":

    app = ttk.Window("Nossa Hepta", "superhero", resizable=(False, False))
    DataEntryForm(app)
    app.mainloop()

