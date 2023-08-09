from solcx import compile_standard, install_solc
install_solc('0.8.0')
import json  #to save the output in a JSON file
from web3 import Web3

with open("ContactList.sol", "r") as file:
    contact_list_file = file.read()

compiled_sol = compile_standard(
    {
        "language": "Solidity",
        "sources": {"ContactList.sol": {"content": contact_list_file}},
        "settings": {
            "outputSelection": {
                "*": {
                    "*": ["abi", "metadata", "evm.bytecode", "evm.bytecode.sourceMap"] # output needed to interact with and deploy contract 
                }
            }
        },
    },
    solc_version="0.8.0",
)
print(compiled_sol)
with open("compiled_code.json", "w") as file:
    json.dump(compiled_sol, file)

# get bytecode
bytecode = compiled_sol["contracts"]["ContactList.sol"]["ContactList"]["evm"]["bytecode"]["object"]
# get abi
abi = json.loads(compiled_sol["contracts"]["ContactList.sol"]["ContactList"]["metadata"])["output"]["abi"]

# For connecting to ganache
w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:7545"))
chain_id = 1337
address = "0xD1010bd90A3cb6045f9B1cC7622E148BC399cC75"
private_key = "0xe552a4487eae3ac3796edadfdfa8a97482bb022de42778496f2a57f1c03d2829" # leaving the private key like this is very insecure if you are working on real world project
# Create the contract in Python
ContactList = w3.eth.contract(abi=abi, bytecode=bytecode)
# Get the number of latest transaction
nonce = w3.eth.get_transaction_count(address)

# build transaction
transaction = ContactList.constructor().build_transaction(
    {
        "chainId": chain_id,
        "gasPrice": w3.eth.gas_price,
        "from": address,
        "nonce": nonce,
    }
)
# Sign the transaction
sign_transaction = w3.eth.account.sign_transaction(transaction, private_key=private_key)
print("Deploying Contract!")
# Send the transaction
transaction_hash = w3.eth.send_raw_transaction(sign_transaction.rawTransaction)
# Wait for the transaction to be mined, and get the transaction receipt
print("Waiting for transaction to finish...")
transaction_receipt = w3.eth.wait_for_transaction_receipt(transaction_hash)
print(f"Done! Contract deployed to {transaction_receipt.contractAddress}")