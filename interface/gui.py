from tkinter import *
from tkinter import messagebox
import webbrowser

def iniciar_interface():
    resultado = {}

    def confirmar():
        branch = selected_filial.get().lower().strip()
        data = caixa_data.get().strip()

        if branch == "selecione" or not data:
            messagebox.showwarning("Campos obrigatórios", "Por favor, selecione a filial e informe a data.")
            return

        resultado['branch'] = branch
        resultado['data'] = data
        janela.destroy()

    def link(event):
        webbrowser.open_new("https://github.com/Guilhos22")

    janela = Tk()
    janela.title('Aquamarine Bot')
    janela.geometry("300x300")

    label_filial = Label(janela, text="Selecione a Filial:")
    label_filial.pack(pady=10)

    selected_filial = StringVar(janela)
    selected_filial.set("Selecione")

    menu_filial = OptionMenu(janela, selected_filial, "produção", "matriz", "aromas")
    menu_filial.pack(pady=10)

    label_data = Label(janela, text='Data de lançamento CTE:')
    label_data.pack(pady=10)

    caixa_data = Entry(janela)
    caixa_data.pack(pady=10)

    btn_confirmar = Button(janela, text='Confirmar', command=confirmar)
    btn_confirmar.pack(pady=10)

    

    link_github = Label(janela, text="Visite este código em meu github!", fg="blue", cursor="hand2", font=('Arial', 10, 'underline'))
    link_github.pack()
    link_github.bind("<Button-1>", link)

    janela.mainloop()

    return resultado.get('branch'), resultado.get('data')
