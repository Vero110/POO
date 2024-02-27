from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        nombre = request.form['nombre']
        return 'Hola, {}! Gracias por enviar el formulario.'.format(nombre)
    return render_template('plantilla.html')

if __name__ == '_main_':
    app.run(debug=True)
    