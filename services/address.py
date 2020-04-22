import requests
from config.database import db


def create_address(header):
    url = "https://api.cryptoapis.io/v1/bc/btc/testnet/address"
    r = requests.post(url, headers=header)
    json_string = r.json()
    private_key=json_string['payload']['privateKey']
    public_key = json_string['payload']['publicKey']
    wif = json_string['payload']['wif']
    address = json_string['payload']['address']
    my_cursor = db.cursor()
    sql = "INSERT INTO address (Address,PublicKey,PrivateKey,Wif) VALUES (%s,%s,%s,%s)"
    val = (address, public_key, private_key, wif)
    my_cursor.execute(sql, val)
    db.commit()
    return json_string


def address_info(header,addressid):
    url = "https://api.cryptoapis.io/v1/bc/btc/testnet/address/"+str(addressid)
    r = requests.get(url, headers=header)
    return r.json()

def transaction_address(header,address_string,txn_type):
    if txn_type =="BASIC":
        url = "https://api.cryptoapis.io/v1/bc/btc/testnet/address/"+str(address_string)+"/basic/transactions?index=0&limit=50"
        r = requests.get(url, headers=header)
        return r.json()
    elif txn_type =="CONFIRMED":
        url = "https://api.cryptoapis.io/v1/bc/btc/testnet/address/"+str(address_string)+"/transactions?index=0&limit=50"
        r = requests.get(url, headers=header)
        return r.json()
    elif txn_type == "UNCONFIRMED":
        url = "https://api.cryptoapis.io/v1/bc/btc/testnet/address/"+str( address_string)+"/unconfirmed-transactions?index=0&limit=50"
        r = requests.get(url, headers=header)
        return r.json()

