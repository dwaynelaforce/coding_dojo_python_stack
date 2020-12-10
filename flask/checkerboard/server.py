from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def default_checkerboard():
    return render_template('index.html', x=8, y=8)

@app.route('/<rows>')
def checkerboardY(rows):
    return render_template('index.html', x=8, y=int(rows))

@app.route('/<rows>/<columns>')
def checkerboardXY(rows, columns):
    return render_template('index.html', x=int(columns), y=int(rows))

if __name__ == "__main__":
    app.run(debug=True)
