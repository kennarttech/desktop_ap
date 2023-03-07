from flask import Flask, json, jsonify, redirect, render_template
from flask_restful import Resource, Api



app = Flask(__name__)


app.config['SECRETE_KEY'] = 'http://127.0.0.1:5000/'
api = Api(app)



puppies = []

class Hompage(Resource):
    def get(self):
        return {'Hello word': 22}
    


class PuppyNames(Resource):
    def get(self, name):
        for pup in puppies:
            if pup['name'] == name:
                return pup 
        return {'name': None}, 404



    def post(self, name):
        pup = {"name": name}
        puppies.append(pup)
        return pup



    def delete(self, name):
        for ind, pup in enumerate(puppies):
            if pup['name'] == name:
                deleted = puppies.pop(ind)
                print(f'Hey the {deleted} was deleted succesful')
                return {'note': 'delete success'}



class AllNames(Resource):
    def get(self):
        return {'puppies':puppies}



api.add_resource(Hompage, '/')
api.add_resource(PuppyNames, '/puppy/<string:name>')
api.add_resource(AllNames, '/puppies')



567


if __name__ == '__main__':
    app.run(debug=True)