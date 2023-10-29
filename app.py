

# C:\flask_dev\flaskreact\app.py
from flask import Flask, request, jsonify, render_template, session, redirect, url_for
from flask_bcrypt import Bcrypt
from flask_cors import CORS
# from flask_cors import CORS
from models import db, User
 


app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

# app = Flask(__name__)
# CORS(app) 
 
app.config['SECRET_KEY'] = 'cairocoders-ednalan'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flaskdb.db'
 
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ECHO = True
  
bcrypt = Bcrypt(app) 
CORS(app, supports_credentials=True)
db.init_app(app)
  
with app.app_context():
    db.create_all()
 
@app.route("/")
def hello_world():
    return render_template("index2.html")
@app.route("/get_users", methods=["GET"])
def get_users():
    users = User.query.all()
    user_list = [{"id": user.id, "email": user.email} for user in users]
    return jsonify(user_list)
@app.route("/user_list", methods=["GET"])
def user_list():
    return render_template("user_list.html")
 
@app.route("/signup", methods=["POST"])
def signup():
    email = request.json["email"]
    password = request.json["password"]
 
    user_exists = User.query.filter_by(email=email).first() is not None
 
    if user_exists:
        return jsonify({"error": "Email already exists"}), 409
     
    hashed_password = bcrypt.generate_password_hash(password)
    new_user = User(email=email, password=hashed_password)
    db.session.add(new_user)
    db.session.commit()
 
    session["user_id"] = new_user.id
 
    return jsonify({
        "id": new_user.id,
        "email": new_user.email
    })
 
@app.route("/login", methods=["POST"])
def login_user():
    email = request.json["email"]
    password = request.json["password"]
  
    user = User.query.filter_by(email=email).first()
  
    if user is None:
        return jsonify({"error": "Unauthorized Access"}), 401
  
    if not bcrypt.check_password_hash(user.password, password):
        return jsonify({"error": "Unauthorized"}), 401
      
    session["user_id"] = user.id
  
    return jsonify({
        "id": user.id,
        "email": user.email
    })
 
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
