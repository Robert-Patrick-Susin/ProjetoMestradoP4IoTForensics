#!/usr/bin/env python3
from web3 import Web3
import os
import sys
import time
import statistics

#Importa cabeçalho myIoT com ou cabeçalhos de pré-processamento
# from no_pre_myIoT_header import iotprotocol

#Importa cabeçalho agregação
from myIoT_agg_header import iot_agregacao

from scapy.all import *


ultimo_tempo = time.time()
# Começo do experimento. Quando inicia o receptor
count = 0
tamanho_total = 0
list_tempos = []

##For connecting to Ethereum ganache##
w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:7545"))
chain_id = 1337
caller = "0xCf75D3e8CE25E91719735E6f2Bcaa3dD1cB40572"
private_key = "0x1efe0e09b0fe7dab2965f153d70fdaafbb533cfef0d2a7f0967977e77bd81ab6" # leaving the private key like this is very insecure if you are working on real world project
##Initialize smart contract and account##

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
contract_address = "0xefd5cb39840CA56aDEFFb0754b6FE22203dfc06D"
#Ethereum (Ganache) + Smart contract configuration done

# Interaction with Smart Contract on Ethereum (Ganache)
# Create smart contract instance
contact_list = w3.eth.contract(address=contract_address, abi=abi)					

def get_if():
    ifs=get_if_list()
    iface=None
    for i in get_if_list():
        if "eth0" in i:
            iface=i
            break;
    if not iface:
        print("Cannot find eth0 interface")
        exit(1)
    return iface

# evento de recepção de pacote 
def handle_pkt(pkt):
    # global count
    # global tamanho_total
    # global tempo_atual
    # global ultimo_tempo
                 
    if iot_agregacao in pkt:
        # pkt.show2()
        # Store packet header in variable to send to BC
        iot_leituras = pkt[iot_agregacao].iot_agg

    ##Call functions and transactions##

    #Get updated nonce (for everytime as its a loop)
    nonce = w3.eth.get_transaction_count(caller)

    #Call function
    store_contact = contact_list.functions.addContact(
        "name", str(iot_leituras), 
    ).build_transaction({"from": caller, "nonce": nonce})
    # ({"from": caller, "gas": 200000, "gasPrice":200000, "nonce": nonce + 1})

    # Sign transaction
    sign_store_contact = w3.eth.account.sign_transaction(store_contact, private_key=private_key)

    # Send transaction
    send_store_contact = w3.eth.send_raw_transaction(sign_store_contact.rawTransaction)

    # Wait for transaction receipt
    w3.eth.wait_for_transaction_receipt(send_store_contact)
    
	# print(tx_receipt) # Optional
    print(contact_list.functions.retrieve().call())


    # count = count + 1
    # nopre_total_pkt = open('metricas/4-teste.txt',"a")
    # nopre_total_pkt.write(str(count))
    # nopre_total_pkt.write("\n")
    # tamanho_total = tamanho_total + sys.getsizeof(pkt)
    # tamanho_total_pkt = open("3-pre_agreg_filt_tamanho_total_pkt.txt","a")
    # tamanho_total_pkt.write(str(tamanho_total))
    # tamanho_total_pkt.write("\n")
    # tempo_atual = time.time()
    # list_tempos.append(tempo_atual - ultimo_tempo)
    # ultimo_tempo = tempo_atual
    # if (count > 1):
    #     median = (statistics.median(list_tempos[1:]))
        # Abre o arquivo 4-pre_med_rec_pkt.txt e escreve a media 
        # da taxa de recebimento de count pacotes
        # pre_med_rec_pkt = open("metricas/4-pre_med_rec_pkt.txt","w")
        # pre_med_rec_pkt.write(str(median))
        # pre_med_rec_pkt.write("\n")
        # pre_med_rec_pkt.write(str(count))
							
sys.stdout.flush()
def main():
    # ifaces = [i for i in os.listdir('/sys/class/net/') if 'eth' in i]
    iface = 's1-eth42'
    print("sniffing on %s" % iface)
    sys.stdout.flush()
    sniff(iface = iface,
          prn = lambda x: handle_pkt(x))

if __name__ == '__main__':
    main()
