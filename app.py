import os
import util
import db
from flask import Flask, json
from flask_cors import CORS
from flask_restful import Api
from resources.user import User

app = Flask(__name__)
# Allow cross domain apps to access API
CORS(app)

# Provide Mongo Atlas URI, stored in config file
app.config["MONGO_URI"] = os.getenv("MONGO_URI_MASTER")
# Set custom JSON Encoder for Mongo Object
app.json_encoder = util.MongoEncoder
db.mongo.init_app(app)
api = Api(app)

api.add_resource(User, "/user")


# Vanilla Flask route
@app.route("/", methods=["GET"])
def index():
    return "Welcome to my ZotHacks 2020 project!"


# Handles validation errors and returns JSON Object
@app.errorhandler(422)
@app.errorhandler(400)
def handle_error(err):
    messages = err.data.get("messages", ["Invalid request."])
    return json.jsonify({"errors": messages}), err.code


if __name__ == "__main__":
    app.run(port=5000,debug=True)
