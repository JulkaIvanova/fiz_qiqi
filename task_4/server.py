from flask import Flask

app = Flask(__name__)


@app.route('/')
def start():
    return "Миссия Колонизация Марса"

@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести!"

@app.route('/promotion')
def promotion():
    return f"""Человечество вырастает из детства.<br>
<br>
Человечеству мала одна планета.<br>
<br>
Мы сделаем обитаемыми безжизненные пока планеты.<br>
<br>
И начнем с Марса!<br>
<br>
Присоединяйся!"""

@app.route('/image_mars')
def image_mars():
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Привет, Марс!</title>
</head>
<body>
    <h2>Жди нас, Марс!</h2>
    <img src='https://foni.papik.pro/uploads/posts/2024-09/foni-papik-pro-b9s6-p-kartinki-mars-na-prozrachnom-fone-6.png' height=300px>
    <p>Вот она какая, красная планета.</p>
</body>
</html>"""


@app.route('/promotion_image')
def promotion_image():
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Колонизация</title>
    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
</head>
<body>
    <h2>Жди нас, Марс!</h2>
    <img src='{url_for('static', filename='img/Mars.png')}' height=300px>
    <div>Человечество вырастает из детства.</div>
<div>Человечеству мала одна планета.</div>
<div>Мы сделаем обитаемыми безжизненные пока планеты.</div>
<div>И начнем с Марса!</div>
<div>Присоединяйся!</div>
</body>
</html>"""

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')