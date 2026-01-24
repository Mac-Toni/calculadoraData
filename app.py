from flask import Flask, render_template, request
from datetime import datetime, timedelta

app = Flask(__name__) # <-- ESSA LINHA É A QUE ESTÁ FALTANDO!

@app.route('/', methods=['GET', 'POST'])
def index():
    resultado = None
    if request.method == 'POST':
        # ... resto do código que mandei antes ...
        if 'data_fim' in request.form:
            d1 = datetime.strptime(request.form['data_ini'], '%Y-%m-%d')
            d2 = datetime.strptime(request.form['data_fim'], '%Y-%m-%d')
            diff = abs((d2 - d1).days)
            resultado = f"A diferença é de {diff} dias"
        else:
            data_str = request.form['data']
            dias = int(request.form['dias'])
            operacao = request.form['operacao']
            data_obj = datetime.strptime(data_str, '%Y-%m-%d')
            calculo = data_obj + timedelta(days=dias) if operacao == 'somar' else data_obj - timedelta(days=dias)
            resultado = f"Data resultante: {calculo.strftime('%d/%m/%Y')}"
        
    return render_template('index.html', resultado=resultado)

if __name__ == '__main__':
    app.run(debug=True)