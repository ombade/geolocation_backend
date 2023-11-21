# from flask import Flask, request, jsonify, render_template, session
# from flask_bcrypt import Bcrypt
# from math import sin, cos, sqrt, atan2, radians
# from flask_cors import CORS
# from bson import ObjectId 
# import pymongo
# import json
# # from flask import Flask, request, jsonify, render_template
# # from flask import Flask, request, jsonify, render_template
# # from flask_bcrypt import Bcrypt
# # from bson import ObjectId
# # from flask_cors import CORS
# # import pymongo
# class CustomJSONEncoder(json.JSONEncoder):
#     def default(self, obj):
#         if isinstance(obj, ObjectId):
#             return str(obj)
#         return super().default(obj)


# app = Flask(__name__)
# CORS(app, resources={r"/*": {"origins": "*"}}, supports_credentials=True)
# app.json_encoder = CustomJSONEncoder 

# client = pymongo.MongoClient("mongodb+srv://ombade364:Pass123@cluster0.qlwkzo3.mongodb.net/")
# db = client['GEOlocation']
# info = db["users"]
# messages_collection = db["messages"]
# location_collection = db["location"]




# # @app.route("/", methods=[ "POST"])
# # def hello_world():
# #     if request.method == "POST":
# #         # Assuming the data is sent as JSON in the request body
# #         data = request.json
# #         uid = data.get('uid', '')
# #         # Process the uid as needed
# #         return jsonify({"message": "UID received successfully"})
# #     else:
# #         uid = request.args.get('uid', '')
# #         return render_template("index2.html", uid=uid)
# # @app.route("/dashboard", methods=["PUT"])
# @app.route("/dashboard", methods=["GET"])
# def handle_get_request():
#     uid = request.args.get('uid', '')
#     # Process the uid as needed
#     return render_template("index2.html", uid=uid)
# @app.route("/signup", methods=["POST"])
# def signup():
#     email = request.json["email"]
#     password = request.json["repeatpassword"]
#     user_id = request.json["uid"]

#     # Check if the email already exists in MongoDB
#     if info.find_one({"email": email}):
#         return jsonify({"error": "Email already exists"}), 409

#     # Insert the new user data into MongoDB
#     data = {
#         "email": email,
#         "password": password,  # Note: In a production scenario, hash the password
#         "user": user_id
#     }
#     info.insert_one(data)

#     return jsonify({
#         "email": email,
#         "user": user_id
#     })

# @app.route("/login", methods=["POST"])
# def login_user():
#     email = request.json["email"]
#     password = request.json["password"]

#     # Query MongoDB to find the user by email
#     user = info.find_one({"email": email})

#     # Check if the user exists and the password matches (insecure, use bcrypt in production)
#     if user and user["password"] == password:
#         return jsonify({
#             "email": user["email"],
#             "user": user["user"]
#         })
#     else:
#         return jsonify({"error": "Unauthorized Access"}), 401



# # routes form the location alert 




# def haversine(lat1, lon1, lat2, lon2):
#     R = 6371.0  # approximate radius of the Earth in kilometers

#     dlat = radians(lat2 - lat1)
#     dlon = radians(lon2 - lon1)

#     a = sin(dlat / 2) ** 2 + cos(radians(lat1)) * cos(radians(lat2)) * sin(dlon / 2) ** 2
#     c = 2 * atan2(sqrt(a), sqrt(1 - a))

#     distance = R * c

#     return distance

# def check_within_area(center_lat, center_lon, check_lat, check_lon, radius):
#     distance = haversine(center_lat, center_lon, check_lat, check_lon)
#     return distance <= radius

# # Add the following import at the beginning of your Python code
# from flask import render_template

# # ...





# @app.route('/alertdata', methods=['POST'])
# def receive_alert_data():
#     content = request.get_json()

#     # Extract data from the request
#     target_latitude = content.get('latitude', '')
#     target_longitude = content.get('longitude', '')
#     message = content.get('message', '')
#     uid = content.get('uid', '')
#     range_value = content.get('radius', '')  # Assuming the range is sent from the frontend
#     # print(target_latitude+ " !target_longitude! "+target_longitude+message+"uid id " +uid)

#     # Print received data (optional)
#     print(f"Received target location data. Latitude: {target_latitude}, Longitude: {target_longitude}, Message: {message}, UID: {uid}, Range: {range_value}")

#     # Store data in MongoDB
#     data_to_insert = {
#         'latitude': target_latitude,
#         'longitude': target_longitude,
#         'message': message,
#         'uid': uid,
#         'range': range_value  # Include the range in the data
#     }
#     result = location_collection.insert_one(data_to_insert)

#     # Check if data was inserted successfully (optional)
#     if result.inserted_id:
#         print(f"Data successfully inserted with _id: {result.inserted_id}")

#     return jsonify({'message': 'Data received and stored in MongoDB'})


# @app.route('/submit_form', methods=['POST'])
# def submit_form():
#     data = request.json  # Assuming the data is sent as JSON

#     # Print the received data
#     print("Received data:", data)

#     # Create a new message record
#     new_message = {
#         'name': data.get('name'),
#         'email': data.get('email'),
#         'message': data.get('message')
#     }

#     # Add the new message record to the 'messages' collection
#     messages_collection.insert_one(new_message)

#     # Add your logic to process the form data here

#     # For demonstration purposes, just echoing back the received data
#     return jsonify(data)



# @app.route("/get_user/<email>", methods=["GET"])
# def get_user(email):
#     # Fetch user data from MongoDB based on the user_id
#     user = info.find_one({"email": email})
#     if user:
#         return jsonify(user)
#     else:
#         return jsonify({"error": "User not found"}), 404

# # Route to edit user information
# # Route to edit user information using email as the key
# @app.route("/edit_user/<email>", methods=["PUT"])
# def edit_user(email):
#     # Get the updated user information from the request body
#     data = request.json
#     new_email = data.get('email', '')
#     password = data.get('password', '')
#     user = data.get('user', '')
#     # Update the user information in MongoDB based on the email
#     result = info.update_one(
#         {"email": email},
#         {"$set": {"email": new_email, "password": password, "user": user}}
#     )
#     if result.modified_count > 0:
#         return jsonify({"message": "User updated successfully"})
#     else:
#         return jsonify({"error": "User not found or no changes made"}), 404

# @app.route("/delete/<email>", methods=["DELETE"])
# def delete_user(email):
#     # Handle user deletion in MongoDB
#     result = info.delete_one({"email": email})
#     if result.deleted_count > 0:
#         return jsonify({"message": "User deleted successfully"})
#     else:
#         return jsonify({"error": "User not found"}), 404

# @app.route('/get_messages', methods=['GET'])
# def get_messages():
#     # Fetch all messages from the "messages" collection
#     messages_cursor = messages_collection.find()

#     # Convert ObjectId to string in each document
#     messages_list = [
#         {
#             'name': message['name'],
#             'email': message['email'],
#             'message': message['message'],
#             '_id': str(message['_id'])
#         }
#         for message in messages_cursor
#     ]

#     return jsonify(messages_list)

# @app.route('/delete_message/<message_id>', methods=['DELETE'])
# def delete_message(message_id):
#     # Delete a message from the "messages" collection based on the message_id
#     result = messages_collection.delete_one({"_id": ObjectId(message_id)})

#     if result.deleted_count > 0:
#         return jsonify({"message": "Message deleted successfully"})
#     else:
#         return jsonify({"error": "Message not found"}), 404




# @app.route('/get_locations', methods=['GET'])
# def location_table():
#     locations_cursor = location_collection.find()
#     locations_list = [
#         {
#             'latitude': location['latitude'],
#             'longitude': location['longitude'],
#             'message': location['message'],
#             'uid': location['uid'],
#             'range': location['range'],
#             '_id': str(location['_id'])
#         }
#         for location in locations_cursor
#     ]
    
# #     return jsonify(locations_list)


# @app.route('/location_table', methods=['GET'])
# def render_location_table():
#     # locations_cursor = location_collection.find()
#     # locations_list = [
#     #     {
#     #         'latitude': location['latitude'],
#     #         'longitude': location['longitude'],
#     #         'message': location['message'],
#     #         'uid': location['uid'],
#     #         'range': location['range'],
#     #         '_id': str(location['_id'])
#     #     }
#     #     for location in locations_cursor
#     # ]
#     return render_template('location_table.html',)
# from flask import jsonify

# # Add this route to your existing backend code
# @app.route('/delete_location/<location_id>', methods=['DELETE'])
# def delete_location(location_id):
#     # Handle location deletion in MongoDB
#     result = location_collection.delete_one({"_id": ObjectId(location_id)})
#     if result.deleted_count > 0:
#         return jsonify({"message": "Location deleted successfully"})
#     else:
#         return jsonify({"error": "Location not found"}), 404




# if __name__ == "__main__":
#     app.run(host="0.0.0.0", debug=True)


from flask import Flask, request, jsonify, render_template
from flask_bcrypt import Bcrypt
from math import sin, cos, sqrt, atan2, radians
from flask_cors import CORS
from bson import ObjectId 
import pymongo
import json

class CustomJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, ObjectId):
            return str(obj)
        return super().default(obj)

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}}, supports_credentials=True)
app.json_encoder = CustomJSONEncoder 

client = pymongo.MongoClient("mongodb+srv://ombade364:Pass123@cluster0.qlwkzo3.mongodb.net/")
db = client['GEOlocation']
info = db["users"]
messages_collection = db["messages"]
location_collection = db["location"]
# target_latitude =0.0
# target_longitude =0.0
# radius = 0.0 

# @app.route('/alertdata', methods=['POST'])
# def receive_alert_data( ):
#     global target_latitude, target_longitude, radius
#     content = request.get_json()

#     # Extract data from the request
#     target_latitude = content.get('latitude', '')
#     target_longitude = content.get('longitude', '')
#     message = content.get('message', '')
#     message = content.get('radius', '')
#     uid = content.get('uid', '')# Assuming the range is sent from the frontend

#     # Create a document to be inserted into the MongoDB collection
#     location_data = {
#         "latitude": target_latitude,
#         "longitude": target_longitude,
#         "message": message,
#         "uid": uid,
#         "range": radius
#     }

#     # Insert the document into the MongoDB collection
#     location_collection.insert_one(location_data)

#     print(f"Received target location data. Latitude: {target_latitude}, Longitude: {target_longitude}, Message: {message}, UID: {uid}, Range: {range_value}")

#     return jsonify({"status": "success", "message": "Data stored successfully"}), 201

# @app.route('/currdata', methods=['POST'])
# def receive_curr_data( ):
#     global target_latitude, target_longitude, radius
#     content = request.get_json()
#     # if isinstance(content, list):
#     #     content = content[0]
#     current_latitude = content['latitude']
#     current_longitude = content['longitude']
#     # current_latitude = request.json.latitude
#     # current_longitude = request.json.longitude
#     print(f"Received current location data. Latitude: {current_latitude}, Longitude: {current_longitude}")



#     if check_within_area(target_latitude, target_longitude, current_latitude, current_longitude, radius):
#         print("Alert: The current location is within the specified area.")
#         # Send a request to the frontend for the alert
#         # Add your code here to send a request to the frontend

#     return jsonify({'message': 'Data received'})


@app.route('/alertdata', methods=['POST'])
def receive_alert_data():
    global target_latitude, target_longitude, radius
    content = request.get_json()

    # Extract data from the request
    target_latitude = content.get('latitude', '')
    target_longitude = content.get('longitude', '')
    message = content.get('message', '')
    radius = content.get('radius', '')  # Assuming the radius is sent from the frontend
    uid = content.get('uid', '')

    # Create a document to be inserted into the MongoDB collection
    location_data = {
        "latitude": target_latitude,
        "longitude": target_longitude,
        "message": message,
        "uid": uid,
        "range": radius
    }

    # Insert the document into the MongoDB collection
    location_collection.insert_one(location_data)

    print(f"Received target location data. Latitude: {target_latitude}, Longitude: {target_longitude}, Message: {message}, UID: {uid}, Range: {radius}")

    return jsonify({"status": "success", "message": "Data stored successfully"}), 201

@app.route('/currdata', methods=['POST'])
def receive_curr_data():
    global target_latitude, target_longitude, radius
    content = request.get_json()

    current_latitude = content['latitude']
    current_longitude = content['longitude']
    print(f"Received current location data. Latitude: {current_latitude}, Longitude: {current_longitude}")

    if check_within_area(target_latitude, target_longitude, current_latitude, current_longitude, radius):
        print("Alert: The current location is within the specified area.")
        
        # Retrieve the message stored in MongoDB at the target location
        location_data = location_collection.find_one(
            {'latitude': target_latitude, 'longitude': target_longitude}
        )
        
        if location_data:
            message_from_mongo = location_data.get('message', '')
            response_data = {
                'message': f'Alert: The current location is within the specified area. Message: {message_from_mongo}',
                'alert': True
            }
            return jsonify(response_data)

    return jsonify({'message': 'Data received'})



@app.route("/dashboard", methods=["GET"])
def handle_get_request():
    uid = request.args.get('uid', '')
    # Process the uid as needed
    return render_template("index2.html", uid=uid)

#login form data and maluplation 

@app.route("/signup", methods=["POST"])
def signup():
    email = request.json["email"]
    password = request.json["repeatpassword"]
    user_id = request.json["uid"]

    if info.find_one({"email": email}):
        return jsonify({"error": "Email already exists"}), 409

    data = {
        "email": email,
        "password": password,  # Note: In a production scenario, hash the password
        "user": user_id
    }
    info.insert_one(data)

    return jsonify({
        "email": email,
        "user": user_id
    })

@app.route("/login", methods=["POST"])
def login_user():
    email = request.json["email"]
    password = request.json["password"]

    user = info.find_one({"email": email})

    if user and user["password"] == password:
        return jsonify({
            "email": user["email"],
            "user": user["user"]
        })
    else:
        return jsonify({"error": "Unauthorized Access"}), 401


@app.route('/get_user_locations/<uid>', methods=['GET'])
def get_user_locations(uid):
    user_locations_cursor = location_collection.find({"uid": uid})
    user_locations_list = [
        {
            'latitude': location['latitude'],
            'longitude': location['longitude'],
            'message': location['message'],
            'range': location['range'],
            '_id': str(location['_id'])
        }
        for location in user_locations_cursor
    ]

    return jsonify(user_locations_list)


def haversine(lat1, lon1, lat2, lon2):
    R = 6371.0

    dlat = radians(lat2 - lat1)
    dlon = radians(lon2 - lon1)

    a = sin(dlat / 2) ** 2 + cos(radians(lat1)) * cos(radians(lat2)) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = R * c

    return distance

def check_within_area(center_lat, center_lon, check_lat, check_lon, radius):
    distance = haversine(center_lat, center_lon, check_lat, check_lon)
    return distance <= radius

@app.route('/submit_form', methods=['POST'])
def submit_form():
    data = request.json

    print("Received data:", data)

    new_message = {
        'name': data.get('name'),
        'email': data.get('email'),
        'message': data.get('message')
    }

    messages_collection.insert_one(new_message)

    return jsonify(data)

@app.route("/get_user/<email>", methods=["GET"])
def get_user(email):
    # Fetch user data from MongoDB based on the user_id
    user = info.find_one({"email": email})
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404



@app.route("/edit_user/<email>", methods=["PUT"])
def edit_user(email):
    # Get the updated user information from the request body
    data = request.json
    new_email = data.get('email', '')
    password = data.get('password', '')
    user = data.get('user', '')
    # Update the user information in MongoDB based on the email
    result = info.update_one(
        {"email": email},
        {"$set": {"email": new_email, "password": password, "user": user}}
    )
    if result.modified_count > 0:
        return jsonify({"message": "User updated successfully"})
    else:
        return jsonify({"error": "User not found or no changes made"}), 404

@app.route("/delete/<email>", methods=["DELETE"])
def delete_user(email):
    # Handle user deletion in MongoDB
    result = info.delete_one({"email": email})
    if result.deleted_count > 0:
        return jsonify({"message": "User deleted successfully"})
    else:
        return jsonify({"error": "User not found"}), 404

from flask import jsonify

@app.route('/GET_User_data', methods=['GET'])
def GET_User_data():
    user_cursor = info.find()

    user_list = [
        {
            '_id': str(user['_id']),
            'email': user['email'],
            'password': user['password'],
            'user': user['user']
        }
        for user in user_cursor
    ]

    return jsonify(user_list)

# messge table maluplation

@app.route('/get_messages', methods=['GET'])
def get_messages():
    messages_cursor = messages_collection.find()

    messages_list = [
        {
            'name': message['name'],
            'email': message['email'],
            'message': message['message'],
            '_id': str(message['_id'])
        }
        for message in messages_cursor
    ]

    return jsonify(messages_list)

@app.route('/delete_message/<message_id>', methods=['DELETE'])
def delete_message(message_id):
    result = messages_collection.delete_one({"_id": ObjectId(message_id)})

    if result.deleted_count > 0:
        return jsonify({"message": "Message deleted successfully"})
    else:
        return jsonify({"error": "Message not found"}), 404

# location table manuplation 

@app.route('/get_locations', methods=['GET'])
def location_table():
    locations_cursor = location_collection.find()
    locations_list = [
        {
            'latitude': location['latitude'],
            'longitude': location['longitude'],
            'message': location['message'],
            'uid': location['uid'],
            'range': location['range'],
            '_id': str(location['_id'])
        }
        for location in locations_cursor
    ]
    
    return jsonify(locations_list)

@app.route('/delete_location/<location_id>', methods=['DELETE'])
def delete_location(location_id):
    result = location_collection.delete_one({"_id": ObjectId(location_id)})
    if result.deleted_count > 0:
        return jsonify({"message": "Location deleted successfully"})
    else:
        return jsonify({"error": "Location not found"}), 404

#  rendering the admin templtes code        
@app.route('/location_table', methods=['GET'])
def render_location_table():
    return render_template('location_table.html')
@app.route('/message_table', methods=['GET'])
def render_message_table():
    return render_template('message_table.html')
@app.route("/user_table" , methods=['GET'])
def admin():
    return render_template("user_table.html")
@app.route("/" , methods=['GET'])
def index():
    return render_template("index.html")
from flask import render_template, request

@app.route("/admii", methods=['POST'])
def admii():
    # Assuming the UID is part of the request data
    uid = request.form.get('uid')  # You might need to adjust this depending on how the UID is sent

    # Check if UID is "om"
    if uid == 'om':
        return render_template("index.html")
    else:
        # Handle the case where UID is not "om", you can redirect or return an error message
        return "Invalid UID. Access denied."

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)

