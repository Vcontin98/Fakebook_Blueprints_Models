from flask import jsonify, request, redirect
from . import bp as app
from app.blueprints.main.models import Car
from app import db

@app.route("/")
def users():
    user_dict = {
        "lucas": {
            "eyeColor": "blue",
            "hairColor": "brown"
        },
        "joe": {
            "eyeColor": "gray",
            "hairColor": "black"
        },
        "kevin": {
            "eyeColor": "brown",
            "hairColor": "blonde"
        }
    }

    return jsonify(user_dict)


@app.route("/car-update", methods=["POST"])
def car_update():
    car_input = (request.form['carInput'])
    user = 1
    
    
    new_car = Car(make=car_input, model=car_input, year=car_input, color=car_input, price= car_input)
    
    db.session.add(new_car)
    db.session.commit()
    
    return redirect("http://127.0.0.1:5000/")




