# Interfaz de usuario para el cálculo de linea de un equipo multidiagnóstico.
from tkinter import *
from tkinter import ttk
import sys

ro20_cobre = 0.018
ro20_aluminio = 0.029
alfa_cobre = 0.00392
alfa_aluminio = 0.00403


# crear ventana
raiz = Tk()
raiz.title("Interfaz de usuario para el cálculo de linea de un equipo multidiagnóstico")
raiz.iconbitmap("cable.ico")


# Definición de la variable ro dependiente del tipo de material y de la temperatura
def ro(material, temperatura):
    if material == "cobre" or material == "Cobre":
        ro_temperatura = ro20_cobre * (1 + alfa_cobre * (temperatura - 20))
    elif material == "aluminio" or material == "Aluminio":
        ro_temperatura = ro20_aluminio * (1 + alfa_aluminio * (temperatura - 20))
    return (ro_temperatura)


#boton calcula
def codigoCalcular():

    # Obtención de los datos
    material_R3 = comboMaterialR3.get()
    material_R1 = comboMaterialR1.get()
    try:
        temperatura_R3 = float(textoTempR3.get())
        longitud_R3 = float(textoLongR3.get())
        seccion_R3 = float(textoSeccionR3.get())
        RTotal = float(textoRTotal.get())
        R0 = float(textoR0.get())
        R2 = float(textoR2.get())
        temperatura_R1 = float(textoTempR1.get())
        longitud_R1 = float(textoLongR1.get())

        # Fórmula R3
        R3 = ro(material_R3, temperatura_R3) * 2 * longitud_R3 / seccion_R3  # Se multiplica por 2 por ser ida y vuelta
        R3 = round(R3, 6)

        # Fórmula R1
        R1 = RTotal - R0 - R2 - R3
        R1 = round(R1, 6)


        # Cálculo de la sección de la línea de acometida entre el transformador y el cuadro de protección medida entre dos fases
        S1 = ro(material_R1, temperatura_R1) * 2 * longitud_R1 / R1
        S1 = round(S1, 4)

        #escribir en el texto
        PantallaR3.set(R3)
        PantallaS1.set(S1)
        if R1 >= 0:
            PantallaR1.set(R1)
        else:
            PantallaR1.set("error R1 negativo")
    except ValueError:
        PantallaS1.set("Error datos")
        PantallaR1.set("Error datos")
        PantallaR3.set("Error datos")


# creación de frame
frame = Frame()
frame.pack(fill="both", expand="True")
frame.config(width="650", height="550")
frame.config(bg="gray")
frame.config(cursor="hand2")

# Creación de label
RTotalLabel = Label(frame, text="El valor de R total en ohmios es menor que:", bg="gray")
RTotalLabel.grid(row=0, column=0, sticky="w", padx=5, pady=5)

R0Label = Label(frame, text="Valor de R0 en ohmios:", bg="gray")
R0Label.grid(row=1, column=0, sticky="w", padx=5, pady=5)

R2Label = Label(frame, text="Valor de R2 en ohmios:", bg="gray")
R2Label.grid(row=2, column=0, sticky="w", padx=5, pady=5)

materialR3Label = Label(frame, text="Material de la linea en R3:", bg="gray")
materialR3Label.grid(row=3, column=0, sticky="w", padx=5, pady=5)

tempR3Label = Label(frame, text="Temperatura en centígrados de la linea en R3:", bg="gray")
tempR3Label.grid(row=4, column=0, sticky="w", padx=5, pady=5)

seccionR3Label = Label(frame, text="Sección en milímetros cuadrados de la linea en R3:", bg="gray")
seccionR3Label.grid(row=5, column=0, sticky="w", padx=5, pady=5)

longR3Label = Label(frame, text="longitud (ida) en metros de la linea en R3:", bg="gray")
longR3Label.grid(row=6, column=0, sticky="w", padx=5, pady=5)

materialR1Label = Label(frame, text="material de la linea en R1:", bg="gray")
materialR1Label.grid(row=7, column=0, sticky="w", padx=5, pady=5)

tempR1Label = Label(frame, text="Temperatura en centígrados en R1:", bg="gray")
tempR1Label.grid(row=8, column=0, sticky="w", padx=5, pady=5)

longR1Label = Label(frame, text="longitud (ida) en metros de la linea en R1:", bg="gray")
longR1Label.grid(row=9, column=0, sticky="w", padx=5, pady=5)

resultadoR3Label = Label(frame, text=" El valor de R3 en ohmios es:", bg="gray")
resultadoR3Label.grid(row=13, column=0, sticky="w", padx=5, pady=5)

resultadoR1Label = Label(frame, text=" El valor de R1 en ohmios es menor o igual a:", bg="gray")
resultadoR1Label.grid(row=14, column=0, sticky="w", padx=5, pady=5)

resultadoS1Label = Label(frame, text=" El valor de S1 en milímetros cuadrados es:", bg="gray")
resultadoS1Label.grid(row=15, column=0, sticky="w", padx=5, pady=5)

# Creación de cuadaros de texto
textoRTotal= Entry(frame)
textoRTotal.grid(row=0, column=1)
textoRTotal.config(justify="center")

textoR0 = Entry(frame)
textoR0.grid(row=1, column=1)
textoR0.config(justify="center")

textoR2 = Entry(frame)
textoR2.grid(row=2, column=1)
textoR2.config(justify="center")

textoTempR3 = Entry(frame)
textoTempR3.grid(row=4, column=1)
textoTempR3.config(justify="center")

textoSeccionR3 = Entry(frame)
textoSeccionR3.grid(row=5, column=1)
textoSeccionR3.config(justify="center")

textoLongR3 = Entry(frame)
textoLongR3.grid(row=6, column=1)
textoLongR3.config(justify="center")

textoTempR1 = Entry(frame)
textoTempR1.grid(row=8, column=1)
textoTempR1.config(justify="center")

textoLongR1 = Entry(frame)
textoLongR1.grid(row=9, column=1)
textoLongR1.config(justify="center")

PantallaR3 = StringVar()
textoResultadoR3 = Entry(frame, state="readonly", textvariable=PantallaR3)
textoResultadoR3.grid(row=13, column=1)
textoResultadoR3.config(justify="center")

PantallaR1 = StringVar()
textoResultadoR1 = Entry(frame, state="readonly", textvariable=PantallaR1)
textoResultadoR1.grid(row=14, column=1)
textoResultadoR1.config(justify="center")

PantallaS1 = StringVar()
textoResultadoS1 = Entry(frame, state="readonly", textvariable=PantallaS1)
textoResultadoS1.grid(row=15, column=1)
textoResultadoS1.config(justify="center")

# Combobox
comboMaterialR3 = ttk.Combobox(frame)
comboMaterialR3.grid(row=3, column=1)
comboMaterialR3["values"] = ("cobre", "aluminio")
comboMaterialR3.current(0)

comboMaterialR1 = ttk.Combobox(frame)
comboMaterialR1.grid(row=7, column=1)
comboMaterialR1["values"] = ("cobre", "aluminio")
comboMaterialR1.current(0)

# Botón cálcular
botonCalcular = Button(frame, text="Cálcular", command=codigoCalcular, bg="black")
botonCalcular.grid(row=11, column=0, columnspan=2)
botonCalcular.config(fg="#03f943", justify="center")

raiz.mainloop()

