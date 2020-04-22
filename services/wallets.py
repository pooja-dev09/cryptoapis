import requests

def create_wallets(header,wallet_type):
    if wallet_type == "Basic":
        url = "https://api.cryptoapis.io/v1/bc/btc/testnet/wallets"
        r = requests.post(url, headers=header)
        return r.json()
    elif wallet_type == "HD":
        url = "https://api.cryptoapis.io/v1/bc/btc/testnet/wallets/hd"
        r = requests.post(url, headers=header)
        return r.json()