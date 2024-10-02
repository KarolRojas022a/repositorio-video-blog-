import tkinter as tk

# Crear ventana
ventana = tk.Tk()
ventana.title("Trabajo")
ventana.iconbitmap("homepage_home_house_icon_153873.ico")
ventana.geometry("900x700+400+50")


frame1 = tk.Frame()
frame1.configure(bg="burlywood3", bd=20, width=200, height=200)
label1 = tk.Label(frame1, text="Frame 1")

frame2 = tk.Frame()
frame2.configure(bg="slategray2", bd=20, width=200, height=200)
label2 = tk.Label(frame2, text="Frame 2")

frame3 = tk.Frame()
frame3.configure(bg="purple", bd=20, width=200, height=200)

def saludar():  # Método del botón
    print("¡Hola, mundo!")

boton = tk.Button(frame3, text="Saludar", command=saludar)  # Command es para llamar al método
label3 = tk.Label(frame3, text="Frame 3")

frame4 = tk.Frame()
frame4.configure(bg="lime green", bd=20, width=200, height=200)
label4 = tk.Label(frame4, text="Frame 4")

# Configuración de la cuadrícula y empaquetado de widgets
frame1.grid(row=0, column=0)
label1.pack(pady=10)

frame2.grid(row=0, column=1)
label2.pack(pady=10)

frame3.grid(row=1, column=0)
label3.pack(pady=10)
boton.pack()

frame4.grid(row=1, column=1)
label4.pack(side=tk.LEFT, pady=10)  # Empaquetar etiqueta en frame4 a la izquierda

# Botón en el lado derecho de la etiqueta
boton_frame4 = tk.Button(frame4, text="Click Aquí", command=saludar)
boton_frame4.pack(side=tk.LEFT, padx=5, pady=10)  # Botón al lado de la etiqueta

ventana.mainloop()

