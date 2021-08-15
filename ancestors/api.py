from flask import Flask
from flask_restplus import Resource, Api
from model.person import Person

app = Flask(__name__)
api = Api(app)


@api.route("/person/<string:person>")
class HandlerPerson(Resource):
    def get(self, person):
        return Person(id=person).__dict__


if __name__ == "__main__":
    app.run(debug=True)
