import tkinter as tk
from tkinter import messagebox
from datetime import datetime
from expresionesRegulares import *
from calcularTrafico import *
from leerArchivo import *
from exportarExcel import *
from maximoTrafico import *


class PROYECTO():
    def realizar_analisis(self):
        # Lee el archivo y filtra las líneas válidas
        archivo_entrada = "/home/tomas/Escritorio/UM/3ro/Automatas/Final-GH/Automatas-Gramaticas/export-2019-to-now-v4.csv"  # Reemplaza con la ruta de tu archivo de entrada
        lineas_validas = leer_archivo(archivo_entrada)

        if not lineas_validas:
            messagebox.showinfo("Error", "No se encontraron datos válidos en el archivo de entrada.")
            return

        # Obtiene las fechas de inicio y fin ingresadas por el usuario
        fecha_inicio = fecha_inicio_entry.get()
        fecha_fin = fecha_fin_entry.get()

        try:
            fecha_inicio = datetime.strptime(fecha_inicio, "%Y-%m-%d %H:%M:%S")
            fecha_fin = datetime.strptime(fecha_fin, "%Y-%m-%d %H:%M:%S")
        except ValueError:
            messagebox.showinfo("Error", "Formato de fecha incorrecto. Utilice yyyy-mm-dd HH:mm:ss.")
            return

        # Calcula el tráfico total para cada usuario en el rango de fechas
        self.trafico_por_usuario = calcular_trafico(lineas_validas, fecha_inicio, fecha_fin)

        if not self.trafico_por_usuario:
            messagebox.showinfo("Error", "No se encontraron datos en el rango de fechas especificado.")
            return

        # Encuentra el usuario con más tráfico
        self.usuario_max_trafico, self.trafico_maximo = encontrar_usuario_max_trafico(self.trafico_por_usuario)

        resultado_text.config(text=f"Usuario con más tráfico: {self.usuario_max_trafico}\nTráfico máximo: {self.trafico_maximo/100000000} Gigabytes")
        exportar_button.pack(pady=20)

    def exportar_resultados(self):
        exportar_a_excel(self.trafico_por_usuario, self.trafico_maximo)
        messagebox.showinfo("Exportar", f"Resultados exportados a 'resultados_trafico.xlsx'.")

# Crear ventana principal
pro = PROYECTO()

app = tk.Tk()
app.title("Análisis de Tráfico de Datos")
app.geometry("550x350")

etiqueta1 = tk.Label(app, text="Fecha de Inicio (yyyy-mm-dd HH:mm:ss):")
etiqueta1.pack()
fecha_inicio_entry = tk.Entry(app)
fecha_inicio_entry.pack(pady=10)

etiqueta2 = tk.Label(app, text="Fecha de Fin (yyyy-mm-dd HH:mm:ss):")
etiqueta2.pack(pady=10)
fecha_fin_entry = tk.Entry(app)
fecha_fin_entry.pack()

realizar_analisis_button = tk.Button(app, text="Realizar Análisis", command=pro.realizar_analisis)
realizar_analisis_button.pack(pady=20)

resultado_text = tk.Label(app, text="")
resultado_text.pack(pady=10)

exportar_button = tk.Button(app, text="Exportar a Excel", command=pro.exportar_resultados)
exportar_button.pack_forget()

app.mainloop()
