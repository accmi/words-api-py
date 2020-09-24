from flask_restful import Resource, reqparse
from .model import ListModel


class ListResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name', type=str, required=True, help='Filed bane cannot be blank')

    def post(self):
        data = self.parser.parse_args()
        name = data['name']
        new_list = ListModel(name)
        list_id, err = new_list.save()

        if err:
            return {'error': err}, 400

        return {'status': 'created', 'list_id': list_id}


class ListsResource(Resource):
    def get(self):
        return {
            'lists': list(map(lambda x: x.json(), ListModel.query.all()))
        }
