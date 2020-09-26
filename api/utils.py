from web3 import Web3

def sendTransaction(message):
    w3 = Web3(Web3.HTTPProvider('https://ropsten.infura.io/v3/02494498a9c74eafa6c8f80e75744634'))
    address = '0x96AFDbdf343Dbe34A28E5e3DC0387fF64aAb6D08'
    privateKey = '0xe1ad4b78f685244dd01796de2d57d99a86aee42c84336f9fd0176f41a1ca089b'
    nonce = w3.eth.getTransactionCount(address)
    gasPrice = w3.eth.gasPrice
    value = w3.toWei(0, 'ether')
    signedTx = w3.eth.account.signTransaction(dict(
        nonce = nonce,
        gasPrice = gasPrice,
        gas = 100000,
        to = '0x0000000000000000000000000000000000000000',
        value = value,
        data = message.encode('utf-8')
    ), privateKey)

    tx = w3.eth.sendRawTransaction(signedTx.rawTransaction)
    txId = w3.toHex(tx)
    return txId