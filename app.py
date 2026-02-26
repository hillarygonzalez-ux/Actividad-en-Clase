from flask import Flask, request, render_template


app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('inicio.html')

@app.route('/suma', methods=['GET', 'POST'])
def sumar():
    if request.method == 'POST':
        num1 = float(request.form.get('num1'))
        num2 = float(request.form.get('num2'))
        resultado = num1 + num2
        return render_template('suma.html', resultado=resultado)

    return render_template('suma.html')

@app.route('/division', methods=['GET', 'POST'])
def dividir():
    resultado = None
    error = None

    if request.method == 'POST':
        try:
            num1 = float(request.form.get('num1'))
            num2 = float(request.form.get('num2'))

            if num2 == 0:
                error = "No se puede dividir entre 0"
            else:
                resultado = num1 / num2

        except (TypeError, ValueError):
            error = "Por favor ingresa números válidos"

    return render_template('division.html', resultado=resultado, error=error)


if __name__ == '__main__':
    app.run(debug=True)




