from tkinter import *
from tkinter import messagebox
from tkcalendar import Calendar
import os, socket, webbrowser, keyring

user = os.getlogin()
local_hostname = socket.gethostname()
local_ip = socket.gethostbyname(local_hostname)

_SERVICE = "AquamarineBot"


def solicitar_credenciais(modo="primeiro_login", parent=None):
    resultado = {"salvo": False}

    if parent:
        win = Toplevel(parent)
        win.grab_set()
    else:
        win = Tk()

    win.focus_force()
    win.title("Aquamarine Bot - Credenciais")
    win.geometry("360x280")
    win.resizable(False, False)
    win.update_idletasks()
    w, h = 360, 280
    x = (win.winfo_screenwidth() // 2) - (w // 2)
    y = (win.winfo_screenheight() // 2) - (h // 2)
    win.geometry(f"{w}x{h}+{x}+{y}")

    titulo = "Primeiro Acesso" if modo == "primeiro_login" else "Alterar Credenciais"
    Label(win, text=titulo, font=("Arial", 12, "bold")).pack(pady=(16, 4))
    Label(win, text="Email e senha salvos no Windows Credential Manager.",
          font=("Arial", 8), fg="gray").pack(pady=(0, 10))

    frame = Frame(win)
    frame.pack(padx=20, fill="x")

    Label(frame, text="Email:", anchor="w").grid(row=0, column=0, sticky="w", pady=4)
    var_email = StringVar()
    if modo == "alterar":
        email_atual = keyring.get_password(_SERVICE, "email")
        if email_atual:
            var_email.set(email_atual)
    Entry(frame, textvariable=var_email, width=30).grid(row=0, column=1, padx=(8, 0), pady=4)

    Label(frame, text="Senha:", anchor="w").grid(row=1, column=0, sticky="w", pady=4)
    var_senha = StringVar()
    Entry(frame, textvariable=var_senha, show="*", width=30).grid(row=1, column=1, padx=(8, 0), pady=4)

    Label(frame, text="Confirmar:", anchor="w").grid(row=2, column=0, sticky="w", pady=4)
    var_confirma = StringVar()
    Entry(frame, textvariable=var_confirma, show="*", width=30).grid(row=2, column=1, padx=(8, 0), pady=4)

    def _salvar():
        email = var_email.get().strip()
        senha = var_senha.get()
        confirma = var_confirma.get()

        if not email or not senha:
            messagebox.showwarning("Obrigatorio", "Email e senha nao podem estar vazios.", parent=win)
            return
        if not email.endswith("@robertet.com"):
            messagebox.showwarning("Email invalido", "Informe um email valido.", parent=win)
            return
        if senha != confirma:
            messagebox.showerror("Senhas diferentes", "A senha e a confirmacao nao coincidem.", parent=win)
            return
        if len(senha) < 8:
            messagebox.showerror("Senha insegura", "A senha cadastrada é pequena demais!", parent=win)
            return
        

        keyring.set_password(_SERVICE, "email", email)
        keyring.set_password(_SERVICE, "password", senha)

       
        var_senha.set("")
        var_confirma.set("")
        del senha
        del confirma

        resultado["salvo"] = True
        messagebox.showinfo("Salvo!", "Credenciais armazenadas no cofre do sistema.\n Reiniciando para aplicar novas credenciais!", parent=win)
        win.destroy()
        from sys import exit
        exit(0)

    frame_btns = Frame(win)
    frame_btns.pack(pady=14)
    Button(frame_btns, text="Salvar",   command=_salvar,     width=10).pack(side="left", padx=6)
    Button(frame_btns, text="Cancelar", command=win.destroy, width=10).pack(side="left", padx=6)

    win.bind("<Return>", lambda _: _salvar())

    if parent:
        parent.wait_window(win)
    else:
        win.mainloop()

    return resultado["salvo"]


def iniciar_interface():
    resultado = {}

    def confirmar():
        branch = selected_filial.get().lower().strip()
        data = calendar.get_date()
        if branch == "selecione" or not data:
            messagebox.showwarning("Campos obrigatorios", "Por favor, selecione a filial e informe a data.")
            return
        resultado['branch'] = branch
        resultado['data'] = data
        janela.destroy()

    def link(event):
        webbrowser.open_new("https://github.com/Guilhos22/bot")

    janela = Tk()
    janela.title('Aquamarine Bot')
    janela.geometry("400x540")

    label_filial = Label(janela, text="Selecione a Filial:")
    label_filial.pack(pady=10)

    selected_filial = StringVar(janela)
    selected_filial.set("Selecione")

    menu_filial = OptionMenu(janela, selected_filial, "produção")
    menu_filial.pack(pady=10)

    label_data = Label(janela, text='Data de lancamento CTE:')
    label_data.pack(pady=10)

    calendar = Calendar(janela, date_pattern='dd/mm/yyyy')
    calendar.pack(pady=10)

    btn_confirmar = Button(janela, text='Confirmar', command=confirmar)
    btn_confirmar.pack(pady=10)

    btn_credenciais = Button(
        janela, text='Alterar Credenciais',
        command=lambda: solicitar_credenciais(modo="alterar", parent=janela),
        fg="blue", cursor="hand2"
    )
    btn_credenciais.pack(pady=4)

    texto_design = Label(janela, text=f'{user} - {local_ip}')
    texto_design.pack(pady=10)

    link_github = Label(janela, text="Visite este codigo em meu github!", fg="blue", cursor="hand2", font=('Arial', 10, 'underline'))
    link_github.pack()
    link_github.bind("<Button-1>", link)

    janela.mainloop()

    return resultado.get('branch'), resultado.get('data')