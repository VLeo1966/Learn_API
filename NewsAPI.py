#импортируем Flask и библиотеку Request
from flask import Flask, render_template, request
import requests

#импортируем объект класса Flask
app = Flask(__name__)

#формируем путь и методы GET и POST
@app.route('/', methods=['GET', 'POST'])
def index():
   weather = None
   news = None
   if request.method == 'POST':
       city = request.form['city']
       weather = get_weather(city)
       news = get_news()
   return render_template("index1.html", weather=weather, news=news)

def get_weather(city):
   api_key = "69b5c0453341a541b802c116ad211f8f"
   #адрес, по которомы мы будем отправлять запрос. Не забываем указывать f строку.
   url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&unit=metric"
   #для получения результата нам понадобится модуль requests
   response = requests.get(url)
   #прописываем формат возврата результата
   return response.json()

#в функции прописываем город, который мы будем вводить в форме
def get_news():
   api_key = "33e2464bfed448ffa6cdf6b395f4f81d"
   url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}"
   response = requests.get(url)
   return response.json().get('articles', [])

if __name__ == '__main__':
   app.run(debug=True)