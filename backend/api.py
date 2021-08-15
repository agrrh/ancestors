from flask import Flask
from flask_restplus import Resource, Api
from model.account import Account
from model.person import Person

app = Flask(__name__)
api = Api(app)


@api.route("/account/<string:account_id>")
class HandlerAccount(Resource):
    def get(self, account_id):
        return Account(id=account_id).__dict__


@api.route("/person/<string:person_id>")
class HandlerPerson(Resource):
    def get(self, person_id):
        return Person(id=person_id).__dict__


if __name__ == "__main__":
    app.run(debug=True)
