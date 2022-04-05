from flask import Flask, render_template, Response, request, url_for, make_response, redirect
import sys
import time

app = Flask(__name__)


#-------------------------------------------------#
# Home Page
#-------------------------------------------------#
@app.route('/')
def home():
    """Hello World"""
    response = make_response(render_template('edit.html'))
    response.set_cookie('userID', 'whoami')
    return response
        
#-------------------------------------------------#
# Getting Cookie
#-------------------------------------------------#
@app.route('/getcookie', methods = ['POST'])
def getcookie():
    """Unlocked Deserves a Flag"""
    if request.method == 'POST':
        name = request.cookies.get('userID')

        if name == 'Mudbud' or name == 'mudbud':
            return render_template('cookie.html')
        else:
            return render_template('edit.html')


#-------------------------------------------------#
# Robots Page
#-------------------------------------------------#
@app.route('/robots.txt')
def robot():
    """Wall-E"""
    return render_template('robots.html')


#-------------------------------------------------#
# edit Page
#-------------------------------------------------#
@app.route('/edit')
def edit():
    """To make it work better"""
    return redirect(url_for('setcookie'))


if __name__=='__main__':
    app.run(debug=True)

