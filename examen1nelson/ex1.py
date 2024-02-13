import tkinter as tk
from tkinter import messagebox

class CuestionarioApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Cuestionario de Bienestar")
        self.respuestas = []
        self.pregunta_actual = 0

        self.preguntas = [
            "1. ¿Tienes cambios de ánimo constantes (de feliz a triste)?",
            "2. ¿Normalmente te aíslas de tu entorno (familia, hobbies o trabajo)?",
            "3. ¿Tienes dificultades para concentrarte y tomar decisiones?",
            "4. ¿Has notado cambios en la pérdida de peso o apetito?",
            "5. ¿Experimentas insomnio o somnolencia todos los días?",
            "6. ¿Sientes falta de energía?"
        ]

        self.respuestas_var = tk.IntVar()

        self.label_pregunta = tk.Label(root, text=self.preguntas[0], font=("Arial", 12), wraplength=400, justify="left")
        self.label_pregunta.pack(pady=10)

        self.radio_si = tk.Radiobutton(root, text="Sí", variable=self.respuestas_var, value=1, font=("Arial", 10))
        self.radio_si.pack(pady=5, padx=20, side=tk.LEFT)
        self.radio_no = tk.Radiobutton(root, text="No", variable=self.respuestas_var, value=2, font=("Arial", 10))
        self.radio_no.pack(pady=5, padx=20, side=tk.RIGHT)

        self.boton_siguiente = tk.Button(root, text="Siguiente", command=self.siguiente_pregunta, font=("Arial", 12))
        self.boton_siguiente.pack(pady=10)

    def siguiente_pregunta(self):
        respuesta = self.respuestas_var.get()
        if respuesta == 0:
            messagebox.showinfo("¡Alerta!", "Por favor, selecciona una respuesta.")
        else:
            self.respuestas.append(respuesta)
            self.respuestas_var.set(0)
            self.pregunta_actual += 1
            if self.pregunta_actual < len(self.preguntas):
                self.label_pregunta.config(text=self.preguntas[self.pregunta_actual])
            else:
                self.mostrar_resultados()

    def mostrar_resultados(self):
        promedio_respuestas = sum(self.respuestas) / len(self.respuestas)
        mensaje_resultados = f"Tu puntuación total es: {sum(self.respuestas)}\n"
        mensaje_resultados += f"Tu promedio es: {promedio_respuestas:.2f}\n"
        if promedio_respuestas <= 1.5:
            mensaje_resultados += "¡Considera hablar con un profesional de la salud mental!"
        else:
            mensaje_resultados += "¡Sigue cuidando tu bienestar mental!"

        messagebox.showinfo("Resultados", mensaje_resultados)
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = CuestionarioApp(root)
    root.mainloop()

