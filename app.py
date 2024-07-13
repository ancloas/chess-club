from flask import Flask, request, jsonify, render_template
from dotenv import load_dotenv
import os
from pymongo import MongoClient

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# Get the MongoDB URI from environment variables
mongodb_uri = os.getenv("MONGODB_URI")
client = MongoClient(mongodb_uri)

# Get the database with the name chess_club
db = client['chess_club'] 

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/join', methods=['POST'])
def join():
    data = request.get_json()
    app.logger.info(f'Received data: {data}')  # Log the received data
    name = data.get('name')
    email = data.get('email')
    phone = data.get('phone')

    result = db.members.insert_one({
        "name": name,
        "email": email,
        "phone": phone
    })

    return jsonify({"message": "Successfully joined!", "id": str(result.inserted_id)}), 201

if __name__ == '__main__':
    app.run(debug=True)
