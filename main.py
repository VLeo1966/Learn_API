import requests
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    try:
        # Отправляем запрос к API
        response = requests.get('https://api.quotable.io/random')
        response.raise_for_status()  # Проверяем на ошибки HTTP
        data = response.json()
        print(data)  # Выводим результат в консоль для проверки

        # Извлекаем цитату и автора
        quote = data.get('content')
        author = data.get('author')
    except requests.exceptions.RequestException as e:
        # Обрабатываем ошибки запроса
        quote = "Не удалось получить цитату. Попробуйте позже."
        author = ""

    return render_template('index3.html', quote=quote, author=author)


if __name__ == '__main__':
    app.run(debug=True)
