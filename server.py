from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello"

@app.route('/play')
def boxes():
    return render_template("index.html", times=3)

@app.route('/play/<int:x>')
def play_times(x):
    return render_template("index.html", times = x, colorful = False)

@app.route('/play/<int:x>/<color>')
def play_times_colors(x, color):
    return render_template("index.html", times = x, color = color, colorful = True)

if __name__ == "__main__":
    app.run(debug = True)