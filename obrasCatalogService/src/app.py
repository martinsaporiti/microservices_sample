import os

from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from flask_cors import CORS

app = Flask(__name__)
api = Api(app)
CORS(app)

@app.route('/')
def hello_world():
    return 'Hello, Obras!'




class Obras(Resource):

    def get(self):
        return [
            {
                'id': 1,
                'name': 'La Mona Lisa',
                'artist': 'Leonardo da Vinci',
                'price' : 345756781,
                'img' : 'http://4.bp.blogspot.com/-tX9brzE8OUU/UWxcqN4Is9I/AAAAAAAAAN0/3uhaRHRMFzE/s1600/Gioconda.jpg'
            },
            {
                'id': 2,
                'name': 'La Noche Estrellada',
                'artist': 'Vincent Van Gogh',
                'price' : 8567234,
                'img' : 'http://3.bp.blogspot.com/-LJ_NjVDSbdg/UWxfJ1lDLaI/AAAAAAAAAN8/cB1RVaQMrDA/s1600/noche+estrellada.jpg'
            },
            {
                'id': 3,
                'name': 'El Grito',
                'artist': 'Edvard Munch',
                'price' : 400,
                'img' : 'http://1.bp.blogspot.com/-q7GL6Xm6wlo/UWxhci-UeII/AAAAAAAAAOE/oE6DbZl-tkg/s1600/grito.jpg'
            },
            {
                'id': 4,
                'name': 'Guernica',
                'artist': 'Pablo Picasso',
                'price' : 523445,
                'img' : 'http://4.bp.blogspot.com/-O62dhkfR1xs/UWxjLRf8HYI/AAAAAAAAAOU/jdlNU1ocF0U/s1600/guernica.jpg'

            },
            {
                'id': 5,
                'name': 'La persistencia de la Memoria',
                'artist': 'Salvador Dalí',
                'price' : 245456,
                'img' : 'http://2.bp.blogspot.com/-LK_8zEfH1TM/UWxldDKXO4I/AAAAAAAAAOc/l1scIcESQ2w/s1600/dali.jpg'

            },
            {
                'id': 6,
                'name': 'Los tres músicos',
                'artist': 'Pablo Picasso',
                'price' : 6429789,
                'img' : 'https://1.bp.blogspot.com/-7ZYcBZuTKpA/UWxow1Z_dNI/AAAAAAAAAOk/4BYW4oP-hh8/s640/tres+musicos.jpg'
            },
        ]


api.add_resource(Obras, '/obrasCatalogService/api/v1/obras')  # Route_1

if __name__ == '__main__':
     app.run(host='0.0.0.0', port='5000')
