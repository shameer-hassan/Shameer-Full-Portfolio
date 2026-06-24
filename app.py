
from flask import Flask, render_template, request, redirect, url_for, flash, session
from werkzeug.security import check_password_hash, generate_password_hash
app=Flask(__name__)
app.secret_key="portfolio-secret-key"
ADMIN_USER="shameer"
ADMIN_HASH=generate_password_hash("CyberSecure2026!")
@app.route('/')
def home(): return render_template('home.html')
@app.route('/about')
def about(): return render_template('about.html')
@app.route('/projects')
def projects(): return render_template('projects.html')
@app.route('/contact',methods=['GET','POST'])
def contact():
    if request.method=='POST':
        flash('Message received!','success')
        return redirect(url_for('contact'))
    return render_template('contact.html')
@app.route('/admin',methods=['GET','POST'])
def admin():
    if request.method=='POST':
        if request.form['username']==ADMIN_USER and check_password_hash(ADMIN_HASH,request.form['password']):
            session['admin']=True
            return redirect('/dashboard')
        flash('Invalid credentials','error')
    return render_template('admin.html')
@app.route('/dashboard')
def dashboard():
    if not session.get('admin'): return redirect('/admin')
    return render_template('dashboard.html')
if __name__=='__main__': app.run(debug=True)
