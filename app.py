from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/calcola', methods=['POST'])
def calcola():
    #Istruzioni per prendere le informazioni in arrivo dal front end
    dati = request.get_json()
    if dati:
        num1 = dati.get('num1')
        num2 = dati.get('num2')
        operazione = dati.get('operazione')
        #elaborazione dati
        if operazione == 'addizione':
            risultato = num1 + num2
        elif operazione == 'sottrazione':
            risultato = num1 - num2
        elif operazione == 'moltiplicazione':
            risultato = num1 * num2
        elif operazione == 'divisione':
            risultato = num1 // num2
            #restituire i dati al front end
        return jsonify(risultato = risultato)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)