from flask import redirect, render_template, redirect, url_for
from . import bp as app
from app.blueprints.main.models import Car
from flask_login import login_required, current_user



    
@app.route("/")
#@login_required
def home():
    if not current_user.is_authenticated:
        return redirect(url_for('auth.login'))
    
    
    car_info = Car.query.all()
    
    car_info.sort(key=lambda post: post.date_created, reverse=True)
    
    print(car_info)
    
    
    context = {
        "car_info": car_info,
        "user": "Victor"
    
    }
    
    return render_template('home.html', **context)
    
@app.route("/login")
def login():
    return render_template('login.html')
    
@app.route("/register")
def register():
    return render_template('register.html')
    
@app.route("/about")
def about():
    return render_template('about.html')
    
@app.route("/blog")
def blog():
    return render_template('blog.html')
    
    