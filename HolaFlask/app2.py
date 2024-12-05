from flask import Flask

app=Flask(__name__)

app.route("/")
def HolaFlask():
    return "<h1> ¡Hola Flask!</h1> <hr>"

## definimos la segunda ruta
app.route("/ruta2")
def ruta2():
    return "<strong> estamos en la segunda ruta </strong> <hr>"

## definimos una tecera ruta
app.route("/ruta3")
def ruta3():
    return "<em> estamos en a tercera ruta </em> <hr>"

if __name__ == '__main__':
    app.run(debug=True)