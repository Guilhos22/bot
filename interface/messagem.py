from tkinter import Tk, messagebox


def mostrar_erro_popup(titulo, msg):
    root = Tk()
    root.withdraw()
    messagebox.showerror(titulo, msg)
    root.destroy()


def continuar():
    return messagebox.askyesno("Reiniciar", "Deseja processar outro lote de CTE's?")
