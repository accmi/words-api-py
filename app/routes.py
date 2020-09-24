from user.resource import SignUp
from word.resource import WordResource
from list.resource import ListResource, ListsResource


class Routes:
    def __init__(self, api):
        self.api = api

        self.api.add_resource(SignUp, '/api/signup')
        self.api.add_resource(ListResource, '/api/lists/<int:list_id>')
        self.api.add_resource(ListsResource, '/api/lists')
        self.api.add_resource(WordResource, '/api/words')
