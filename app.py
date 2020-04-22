from flask import Flask, jsonify
from flask_restful import Api, Resource,reqparse
from services import address,wallets
app = Flask(__name__)
api = Api(app, prefix="/api", catch_all_404s=True)
headers = {'Content-Type': 'application/json', 'X-API-Key': '9b771d5ea48a9643b336e1019ee036d1be7435d5'}


class CreateAddress(Resource):
    def get(self):
        return jsonify(address.create_address(headers))

class AddressInformation(Resource):
    def get(self,addressid):
        print(addressid)
        return jsonify(address.address_info(headers,addressid))

class AddressTransaction(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('address_string', required=True, type=str, help='address string cannot be found')
        parser.add_argument('txn_type', required=True, type=str, help='txn type cannot be found')
        args = parser.parse_args()
        address_string = args['address_string']
        txn_type = args['txn_type'].upper()
        return jsonify(address.transaction_address(headers, address_string,txn_type))

class CreateWallets(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('wallet_type', required=True, type=str, help='address string cannot be found')
        args = parser.parse_args()
        wallet_type = args['wallet_type'].upper()
        return jsonify(wallets.create_wallets(headers,wallet_type))





api.add_resource(CreateAddress, "/address/")
api.add_resource(AddressInformation, "/address/<addressid>")
api.add_resource(AddressTransaction, "/address/transactions/")
api.add_resource(CreateWallets, "/wallets/")



if __name__ == '__main__':
    app.run(port='5000', host='0.0.0.0', debug=False)