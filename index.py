#coding:utf-8
from flask import Flask,render_template,request,url_for,redirect,session,escape
app=Flask(__name__)

@app.route('/login/<status>')
def login(status):
    return "loggined!"

@app.route('/admin')
def admin():
    check_login=False
    if check_login:
        return 'login success'
    else:return redirect(url_for('login'))

if __name__=='__main__':
    app.run(host='0.0.0.0',debug=True)