def mostrar_erro_popup(titulo, msg):
    from tkinter import Tk, messagebox
    root = Tk()
    root.withdraw()
    messagebox.showerror(titulo, msg)
    root.destroy()
