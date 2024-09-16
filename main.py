from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)

# Route for serving the homepage
@app.route('/')
def home():
    return render_template('index3.html')

# Route for getting a random quote
@app.route('/quote')
def get_quote():
    response = requests.get('https://api.quotable.io/random')
    if response.status_code == 200:
        data = response.json()
        return jsonify(content=data['content'], author=data['author'])
    else:
        return jsonify(content="Oops! Something went wrong.", author="Unknown")

if __name__ == '__main__':
    app.run(debug=True)
