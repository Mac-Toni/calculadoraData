from flask import Flask, render_template, request
from datetime import datetime, timedelta

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    resultado = None
    # Pega a data e hora atual para o rodapé
    agora = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
    
    if request.method == 'POST':
        # Caso 1: Diferença entre duas datas (Aba Intervalo)
        if 'data_fim' in request.form:
            d1 = datetime.strptime(request.form['data_ini'], '%Y-%m-%d')
            d2 = datetime.strptime(request.form['data_fim'], '%Y-%m-%d')
            diff = abs((d2 - d1).days)
            resultado = f"{diff} dias de diferença"
        
        # Caso 2: Somar ou Subtrair (Aba Prazos)
        elif 'data' in request.form:
            data_str = request.form['data']
            dias = int(request.form['dias'])
            operacao = request.form['operacao']
            data_obj = datetime.strptime(data_str, '%Y-%m-%d')
            
            if operacao == 'somar':
                calculo = data_obj + timedelta(days=dias)
            else:
                calculo = data_obj - timedelta(days=dias)
            
            resultado = f"Data: {calculo.strftime('%d/%m/%Y')}"
        
    return render_template('index.html', resultado=resultado, agora=agora)

if __name__ == '__main__':
    app.run(debug=True)