from flask import render_template
from . import bp as app
from app.blueprints.main.models import Car



    
@app.route("/")
def home():
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
    
    