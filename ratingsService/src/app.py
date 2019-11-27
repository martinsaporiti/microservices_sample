from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from flask_cors import CORS


app = Flask(__name__)
api = Api(app)
CORS(app)


@app.route('/')
def hello_world():
    return 'Hello, Ratings!'




class Ratings(Resource):
    
    ratings = [
            {
                'id': 1,
                'rating' : 700
            },
            {
                'id': 2,
                'rating' : 123
            },
            {
                'id': 3,
                'rating' : 3456
            },
            {
                'id': 4,
                'rating' : 3453549
            },
            {
                'id': 5,
                'rating' : 1123
            },
            
    ]

    def get(self, obra_id):
        return self.ratings[int(obra_id) -1]

api.add_resource(Ratings, '/ratingsService/api/v1/obra/<obra_id>')

if __name__ == '__main__':
     app.run(host='0.0.0.0', port='5000')
