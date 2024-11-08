from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/calcola', methods=['POST'])
def calcola():
    dati = request.get_json()
    num1 = data.get('num1', 0)
    num2 = data.get('num2', 0)
    return render_template('index.html')

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)