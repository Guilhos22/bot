from tkinter import Tk, messagebox


def mostrar_erro_popup(titulo, msg):
    root = Tk()
    root.withdraw()
    messagebox.showerror(titulo, msg)
    root.destroy()

def mostrar_popup(titulo, msg):
    root = Tk()
    root.withdraw()
    messagebox.showinfo(titulo, msg)
    root.destroy()



def continuar():
    return messagebox.askyesno("Reiniciar", "Deseja processar outro lote de CTE's?")

def criar_excel():
    return messagebox.askyesno("CRIAR", "Deseja criar uma nova planilha?")
