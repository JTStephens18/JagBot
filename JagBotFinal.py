import requests
from requests.api import get
import time
import json
from web3 import Web3

#Local host for testing
ganache_url = "http://127.0.0.1:8545"
#web3 variable 
w3 = Web3(Web3.HTTPProvider(ganache_url))

#Ganache account with ETH - needs to be changed when you load Ganache
account1 = "0x0A68b5A54724c87616676c88b14BF0decC784312"
#Private key for the account
privateKey = "9b9f782534046370070a01edb0f1fe774b6387b05c341344782a5ae8663e7e5a"

#Address of the smart contract when deployed on Remix - needs to be changed when you deploy a new contract
address = "0xE845E586172EF63ae5083E856fE2aCFe2035d447"
#abi of the contract 
abi = json.loads('[{"constant":false,"inputs":[],"name":"get_price","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"priceVar","type":"uint256"}],"name":"set_price","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[],"name":"get_prediction","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[],"name":"set_prediction","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"inputs":[],"payable":false,"stateMutability":"nonpayable","type":"constructor"}]')
#bytecode of the contract
bytecode = '608060405260043610610062576000357c0100000000000000000000000000000000000000000000000000000000900463ffffffff16806311f37ceb146100675780638d7b923a1461007e5780639c16cdb5146100e4578063e059969d146100fb575b600080fd5b34801561007357600080fd5b5061007c610112565b005b34801561008a57600080fd5b506100e260048036038101908080359060200190820180359060200190808060200260200160405190810160405280939291908181526020018383602002808284378201915050505050509192919290505050610114565b005b3480156100f057600080fd5b506100f961012e565b005b34801561010757600080fd5b50610110610130565b005b565b806000908051906020019061012a929190610132565b5050565b565b565b82805482825590600052602060002090810192821561016e579160200282015b8281111561016d578251825591602001919060010190610152565b5b50905061017b919061017f565b5090565b6101a191905b8082111561019d576000816000905550600101610185565b5090565b905600a165627a7a72305820cd7cbb7fed55665401000b0f87d5f4a0e5a9b2cf61b7dcc64d7fcf396f24713c0029'
#The address, abi, and bytecode are all needed in order to write to the correct contract 

#Connect to our smart contract
Oracle = w3.eth.contract(abi=abi, bytecode=bytecode, address=address)

tx_hash = Oracle.functions.set_price(10).transact({'from': account1, 'gas': 410000})

tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)

#Array to store the price of our crypto
priceArray = [None] * 5

i = -1

#Function that queries a URL and retrieves the price of a crypto
def timePrice(i):
    print("Doing stuff...")
    for x in priceArray:
        response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
        #Saves the request in a json format
        x = response.json()
        #Need the "bpi", "USD", and "rate" to get only the price
        priceArray[i] = x["bpi"]["USD"]["rate"]
    print(priceArray)
    #Puts the program on hold so the price can be updated and we get updated price values
    time.sleep(30)

#Loop to fill the priceArray
while True:
    i = i + 1
    timePrice(i)
    if i == len(priceArray) - 1:
        break

        
# This code originates from Eugiene Kanillar and can be found here
# https://www.section.io/engineering-education/an-introduction-to-machine-learning-using-c++/

# It has been edited from C++ to Python for the sake of the project
# Final version made by Jesse White

#Set up historical data
trainingInit = [57983.0482, 57944.1349, 57970.9019, 57984.7187, 58011.3393]
trainingFollow = [57498.8083, 57446.6755, 57357.0003, 57287.0015, 57296.4418]

#Initialize an array to store error values
error = []

#Initialize values to be used in the training section of the module
devi = 0.0
b0 = 0.0
b1 = 0.0
learnRate = 0.01

#Train the system to follow a trend with historical data
for i in range(20):
    index = i % 5
    p = b0 + b1 * trainingInit[index]
    devi = p - trainingFollow[index]
    b0 = b0 - learnRate * devi
    b1 = b1 - learnRate * devi * trainingInit[index]
    error.append(devi)

#Take most recent price as input
response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
x = response.json()
recentValue = x["bpi"]["USD"]["rate"]

#Predict the next price value based on previous trends
pred = b0 + b1 * float(recentValue)

print("The value predicted by the model= " + str(pred))

#Check the prices, both the most recent and predicted prices, and determine either buying or selling
if (pred >= float(recentValue)):
    print("It is recommended that you SELL now.")
else:
    print("It is recommended that you BUY now.")
