from flask import Flask
from flask_RESTful import Resource,Api

app = Flask(__name__)
api = Api(app)

class student(Resource):
    def get(self,name):
        return {'student': name}
    def post(self,name):
        item = {'name' : name, 'class' : 12}
        return item,201

api.add_resource(student,"/student/<string:name>")

if __name__ == "__main__":
    app.run()