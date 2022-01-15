import requests
from requests.api import get
import time
import json
from web3 import Web3

ganache_url = "http://127.0.0.1:8545"
w3 = Web3(Web3.HTTPProvider(ganache_url))

account1 = "0x0A68b5A54724c87616676c88b14BF0decC784312"
nonce = w3.eth.getTransactionCount(account1)
privateKey = "9b9f782534046370070a01edb0f1fe774b6387b05c341344782a5ae8663e7e5a"

address = "0xE845E586172EF63ae5083E856fE2aCFe2035d447"
abi = json.loads('[{"constant":false,"inputs":[],"name":"get_price","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"priceVar","type":"uint256"}],"name":"set_price","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[],"name":"get_prediction","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[],"name":"set_prediction","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"inputs":[],"payable":false,"stateMutability":"nonpayable","type":"constructor"}]')
bytecode = '608060405260043610610062576000357c0100000000000000000000000000000000000000000000000000000000900463ffffffff16806311f37ceb146100675780638d7b923a1461007e5780639c16cdb5146100e4578063e059969d146100fb575b600080fd5b34801561007357600080fd5b5061007c610112565b005b34801561008a57600080fd5b506100e260048036038101908080359060200190820180359060200190808060200260200160405190810160405280939291908181526020018383602002808284378201915050505050509192919290505050610114565b005b3480156100f057600080fd5b506100f961012e565b005b34801561010757600080fd5b50610110610130565b005b565b806000908051906020019061012a929190610132565b5050565b565b565b82805482825590600052602060002090810192821561016e579160200282015b8281111561016d578251825591602001919060010190610152565b5b50905061017b919061017f565b5090565b6101a191905b8082111561019d576000816000905550600101610185565b5090565b905600a165627a7a72305820cd7cbb7fed55665401000b0f87d5f4a0e5a9b2cf61b7dcc64d7fcf396f24713c0029'

Oracle = w3.eth.contract(abi=abi, bytecode=bytecode, address=address)

tx_hash = Oracle.functions.set_price(10).transact({'from': account1, 'gas': 410000})

tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)

contract = w3.eth.contract(
    address=tx_receipt.contractAddress,
    abi=abi
)

priceArray = [None] * 5

i = -1

def timePrice(i):
    print("Doing stuff...")
    for x in priceArray:
        response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
        x = response.json()
        priceArray[i] = x["bpi"]["USD"]["rate"]
    print(priceArray)
    time.sleep(30)


while True:
    i = i + 1
    timePrice(i)
    if i == len(priceArray) - 1:
        break
