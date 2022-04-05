from flask import Flask, render_template
app = Flask(__name__)

@app.route('/robots.txt')
def robots():
    return 'shctf{th1s-aster0id-1$-n0t-3ntir3ly-stable}'

@app.route('/')
@app.route('/index.html')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
