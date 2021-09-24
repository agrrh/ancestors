import os
import yaml

from flask import Flask
from flask_restplus import Resource, Api

from box import Box

from model.database import Database
from model.account import Account
from model.person import Person

config_path = os.environ.get("CONFIG_PATH", "./config.yml")

with open(config_path) as fp:
    data = yaml.load(fp, Loader=yaml.FullLoader)
    config = Box(data)

app = Flask(__name__)
api = Api(app)
database = Database(**config.database)


@api.route("/healthz")
class HandlerHealthz(Resource):
    def get(self):
        health = {
            "database": database.health(),
        }

        # fmt: off
        health_status = all([
            v.get("status", False)
            for k, v
            in health
        ])
        # fmt: on

        return health, 200 if health_status else 500


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
