from flask import Flask, render_template
import requests

app = Flask(__name__)


# Главная страница
@app.route('/')
def home():
    try:
        # Запрашиваем случайную цитату с API
        response = requests.get('https://api.quotable.io/random')
        response.raise_for_status()  # Проверяем наличие ошибок HTTP
        data = response.json()

        # Получаем цитату и автора из данных
        quote = data['content']
        author = data['author']
    except requests.exceptions.RequestException as e:
        quote = "Не удалось получить цитату. Попробуйте позже."
        author = ""

    # Передаем цитату и автора в шаблон
    return render_template('index3.html', quote=quote, author=author)


if __name__ == '__main__':
    app.run(debug=True)

#
