from flask import Flask
from flask_restful import Api, Resource, reqparse, abort

app = Flask(__name__)
api = Api(app)

image_post_args = reqparse.RequestParser()
image_post_args.add_argument("name", type=str, help="Image name is required", required=True)
image_post_args.add_argument("image_url", type=str, help="Image URL is required", required=True)

id_arr = {}

def abort_if_image_id_doesnt_exist(image_id):
    if image_id not in id_arr:
        abort(404, message="Could not find image")

def abort_if_image_exists(image_id):
    if image_id in id_arr:
        abort(409, message="Image already exists with that ID")

class Image(Resource):
    def get(self, image_id):
        abort_if_image_id_doesnt_exist(image_id)
        return id_arr[image_id]
    
    def post(self, image_id):
        abort_if_image_exists(image_id)
        args = image_post_args.parse_args()
        id_arr[image_id] = args
        return id_arr[image_id], 201

    def delete(self, image_id):
        abort_if_image_id_doesnt_exist(image_id)
        del id_arr[image_id]
        return '', 204

api.add_resource(Image, "/image/<int:image_id>")

if __name__ == "__main__":
    app.run(debug=True)