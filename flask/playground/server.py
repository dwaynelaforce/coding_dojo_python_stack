from flask import Flask, render_template
app = Flask(__name__)

@app.route('/play')
def play():
    return render_template('index.html', numboxes = 3, bgcolor="aqua")

@app.route('/play/<x>')
def playx(x):
    return render_template('index.html', numboxes = int(x), bgcolor="aqua")

@app.route('/play/<x>/<color>')
def playxcolor(x, color):
    return render_template('index.html', numboxes = int(x), bgcolor=color)

if __name__ == "__main__":
    app.run(debug=True)
