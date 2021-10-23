import tkinter as tk;
from tkinter import ttk;
from tkinter.constants import NW;

class App:
    '''
    Clase para crear una ventana.
    '''
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Programa 1")
        self.ventana.geometry("600x300")

        s = ttk.Style()
        s.configure('My.TFrame', background='#FF5733')

        self.contenedor = ttk.Frame(self.ventana, style='My.TFrame')
        self.contenedor.place(x=0, y = 0, width=800, height=350)

        self.texto = tk.StringVar()
        self.label1 = ttk.Label(self.contenedor, textvariable=self.texto,
        anchor=NW, background="#FF5733", font=50, padding="10 10 10 10")
        self.label1.place(x = 20, y = 20, width=550, height = 200)

        self.btn_salir = ttk.Button(self.contenedor, text="Cerrar ventana", command=self.salir)
        self.btn_salir.place(x=275, y= 250)

    def print(self, datos):
        self.texto.set(str(datos))
        self.ventana.mainloop()

    def salir(self):
        self.ventana.destroy()

if __name__ == "__main__":
    app = App()
    app.print("This one")
