from web3 import Web3


##For connecting to ganache##
w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))
chain_id = 1337
caller = "0x90F8bf6A479f320ead074411a4B0e7944Ea8c9C1"
private_key = "0x4f3edf983ac636a65a842ce7c78d9aa706d3b113bce9c46f30d7d21715b23b1d" # leaving the private key like this is very insecure if you are working on real world project


##Initialize smart contract and account##
# Initialize address nonce
nonce = w3.eth.get_transaction_count(caller)

# Initialize contract ABI and address
abi = '[{"inputs":[],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"balanceLeft","type":"uint256"}],"name":"balance","type":"event"},{"inputs":[{"internalType":"address payable","name":"recipient","type":"address"}],"name":"destroy","outputs":[],"stateMutability":"nonpayable","type":"function"}'

contract_address = "0xe78a0f7e598cc8b0bb87894b0f60dd2a88d6a8ab"



##Call functions and transactions##
# Create smart contract instance
contract = w3.eth.contract(address=contract_address, abi=abi)

# initialize the chain id, we need it to build the transaction for replay protection
Chain_id = w3.eth.chain_id

# Call your function
call_function = contract.functions.testFunc().buildTransaction({"chainId": Chain_id, "from": caller, "nonce": nonce})

# Sign transaction
signed_tx = w3.eth.account.sign_transaction(call_function, private_key=private_key)

# Send transaction
send_tx = w3.eth.send_raw_transaction(signed_tx.rawTransaction)

# Wait for transaction receipt
tx_receipt = w3.eth.wait_for_transaction_receipt(send_tx)
# print(tx_receipt) # Optional