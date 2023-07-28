from web3 import Web3

# Initialize endpoint URL
node_url = "CHAINSTACK_NODE_URL"

# Create the node connection
web3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8545'))

# Verify if the connection is successful
if web3.is_connected():
    print("-" * 50)
    print("Connection Successful")
    print("-" * 50)
else:
    print("Connection Failed")
            
