from web3 import Web3

##For connecting to ganache##
w3 = Web3(Web3.HTTPProvider("http://10.0.2.15:7545"))
chain_id = 1337
caller = "0xD1010bd90A3cb6045f9B1cC7622E148BC399cC75"
private_key = "0xe552a4487eae3ac3796edadfdfa8a97482bb022de42778496f2a57f1c03d2829" # leaving the private key like this is very insecure if you are working on real world project


##Initialize smart contract and account##
# Initialize address nonce
nonce = w3.eth.get_transaction_count(caller)

# Initialize contract ABI and address
abi = [
			{
				"inputs": [
					{
						"internalType": "string",
						"name": "_name",
						"type": "string"
					},
					{
						"internalType": "string",
						"name": "_phoneNumber",
						"type": "string"
					}
				],
				"name": "addContact",
				"outputs": [],
				"stateMutability": "nonpayable",
				"type": "function"
			},
			{
				"inputs": [
					{
						"internalType": "uint256",
						"name": "",
						"type": "uint256"
					}
				],
				"name": "contact",
				"outputs": [
					{
						"internalType": "string",
						"name": "name",
						"type": "string"
					},
					{
						"internalType": "string",
						"name": "phoneNumber",
						"type": "string"
					}
				],
				"stateMutability": "view",
				"type": "function"
			},
			{
				"inputs": [
					{
						"internalType": "string",
						"name": "",
						"type": "string"
					}
				],
				"name": "nameToPhoneNumber",
				"outputs": [
					{
						"internalType": "string",
						"name": "",
						"type": "string"
					}
				],
				"stateMutability": "view",
				"type": "function"
			},
			{
				"inputs": [],
				"name": "retrieve",
				"outputs": [
					{
						"components": [
							{
								"internalType": "string",
								"name": "name",
								"type": "string"
							},
							{
								"internalType": "string",
								"name": "phoneNumber",
								"type": "string"
							}
						],
						"internalType": "struct ContactList.Contact[]",
						"name": "",
						"type": "tuple[]"
					}
				],
				"stateMutability": "view",
				"type": "function"
			}
		]

contract_address = "0x725738B88E2127d6E270B8D1112E8B99D9ABabeC"

##Call functions and transactions##
# Create smart contract instance
contact_list = w3.eth.contract(address=contract_address, abi=abi)

#Call function
store_contact = contact_list.functions.addContact(
    "name", "+2348112398610"
).build_transaction({"from": caller, "gas": 200000, "gasPrice": w3.eth.gas_price, "nonce": nonce})

# Sign transaction
sign_store_contact = w3.eth.account.sign_transaction(store_contact, private_key=private_key)

# Send transaction
send_store_contact = w3.eth.send_raw_transaction(sign_store_contact.rawTransaction)

# Wait for transaction receipt
w3.eth.wait_for_transaction_receipt(send_store_contact)
# print(tx_receipt) # Optional
print(contact_list.functions.retrieve().call())