from web3 import Web3

w3 = Web3(Web3.HTTPProvider('https://ropsten.infura.io/v3/1f0ea7097c8d4613b7016dc744e6411e'))
account = w3.eth.account.create()
privateKey = account.privateKey.hex()
address = account.address

print(f"Your address: {address}\nYour key: {privateKey}")