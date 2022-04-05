from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
    guess = request.args.get('flag')
    return render_template('index.html',guess=guess,flag='shctf{2_explor3_fronti3r}')

if __name__ == '__main__':
    app.run()
