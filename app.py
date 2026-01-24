from flask import Flask, render_template, request
from datetime import datetime, timedelta

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    resultado = None
    if request.method == 'POST':
        data_str = request.form['data']
        dias = int(request.form['dias'])
        operacao = request.form['operacao']
        
        data_obj = datetime.strptime(data_str, '%Y-%m-%d')
        
        if operacao == 'somar':
            calculo = data_obj + timedelta(days=dias)
        else:
            calculo = data_obj - timedelta(days=dias)
            
        resultado = calculo.strftime('%d/%m/%Y')
        
    return render_template('index.html', resultado=resultado)

if __name__ == '__main__':
    app.run(debug=True)