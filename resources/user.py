from flask import json
from flask_restful import Resource
from marshmallow import Schema, fields
from webargs.flaskparser import use_args
from db import mongo
from util import mongo_id_decoder, validate_user_id


class GetSchema(Schema):
    _id = fields.Function(deserialize=mongo_id_decoder)
    email = fields.Email()
    firstName = fields.Str()
    lastName = fields.Str()


class PostSchema(Schema):
    email = fields.Email(required=True)
    firstName = fields.Str(required=True)
    lastName = fields.Str(required=True)


class PutQuerySchema(Schema):
    _id = fields.Function(
        deserialize=mongo_id_decoder, validate=validate_user_id, required=True
    )


class PutBodySchema(Schema):
    email = fields.Email(required=True)
    firstName = fields.Str(required=True)
    lastName = fields.Str(required=True)


class DeleteSchema(Schema):
    _id = fields.Function(
        deserialize=mongo_id_decoder, validate=validate_user_id, required=True
    )


class User(Resource):
    @use_args(GetSchema(), location="querystring")
    def get(self, query):
        # Search for all users that match query arguments
        users = [user for user in mongo.db.user.find(query)]
        return json.jsonify(data=users)

    @use_args(PostSchema(), location="json")
    def post(self, body):
        # Create user with data from request
        mongo.db.user.insert_one(body)
        return json.jsonify(data=body)

    @use_args(PutQuerySchema(), location="querystring")
    @use_args(PutBodySchema(), location="json")
    def put(self, query, body):
        user_id = query.get("_id")
        # Update user with data from request
        mongo.db.user.update_one({"_id": user_id}, {"$set": body})
        updated_user = mongo.db.user.find_one({"_id": user_id})
        return json.jsonify(data=updated_user)

    @use_args(DeleteSchema(), location="querystring")
    def delete(self, query):
        user_id = query.get("_id")
        # Delete user based on _id
        mongo.db.user.delete_one({"_id": user_id})
        return {"message": "User was deleted"}
