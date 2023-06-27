from flask import Flask, request, jsonify, render_template
from english_to_morse import morse_translator_eng

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/morsetoenglish',methods=['POST'])
def predict():

    a = request.form['a']

    result = basic_calculator(a)

    return render_template('index.html', prediction_text=str(result))


if __name__ == "__main__":
    app.run(debug=True)
