#!/usr/bin/env python3
from web3 import Web3
# import os
# import sys
import time
import statistics

from scapy.all import *

#Importa cabeçalho agregação
from myIoT_agg_header import iot_agregacao

ultimo_tempo = time.time()
count = 0
countbloco = 0
list_tempos = []
tempo_passado_total = 0
tempo_transacao = 0
tempo_atual = 0

##For connecting to Ethereum ganache##
w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:7545"))
chain_id = 5777
caller = "0x6547d934479F6dB68875ADc8eCd28cDFaF4048d5"
private_key = "0xd69e807fa59dc504dbcac4e7c206ced69c8465eb8b4ddcc3c73e4a2441c56747" # leaving the private key like this is very insecure if you are working on real world project
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
contract_address = "0xFFf8D6bE5045884c23B9A51bf5d5b44A3048160A"
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
    global count
    global countbloco
    global iot_leituras
    global ultimo_tempo
    global tempo_atual
    global file
    global file2
    global tempo_passado_desde_ultimo
    global tempo_passado_total
    global tempo_transacao
    global tempo_rec_pkt
    global tempo_rec_transacao
    # global tamanho_total
    # global tempo_atual
    # global ultimo_tempo
    
    # Armazena varíavel qualquer para mandar baseline para BC
    # iot_leituras = pkt[TCP].dport
    #Detecta se pacote é MQTT para testar baseline
    # if pkt[TCP].dport == 1883:
    

	# Detecta se cabeçalho de agregação está no pacote             
    if iot_agregacao in pkt:
        # Armazena varíavel agregação para mandar para BC
        iot_leituras = pkt[iot_agregacao].iot_agg
        # pkt.show2()

        #  count = count + 1
        #  countpkt = open("1-total_pkt_recebido_agg.txt","w")
        #  countpkt.write(str(count))
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
        tempo_rec_pkt = time.time()
		# Wait for transaction receipt
        w3.eth.wait_for_transaction_receipt(send_store_contact)
        # print(tx_receipt) # Optional
        # print(contact_list.functions.retrieve().call())
        # Tempo da transação
        tempo_rec_transacao = time.time()
		
		#Escreve nr de blocos gerados
        countbloco = countbloco + 1
        countblc = open("1_blocos_rec_baseline","a")
        countblc.write(str(countbloco))
        countblc.write('\n')
        
		#Escreve tempo passado em segundos
        tempo_atual = time.time()
        tempo_passado_desde_ultimo = tempo_atual - ultimo_tempo
        ultimo_tempo = tempo_atual
        tempo_passado_total = tempo_passado_desde_ultimo + tempo_passado_total
        file = open("1_tempo_passado_seg", "a")
        file.write(str(tempo_passado_total))
        file.write('\n')
        
		#Escreve quanto durou para efetuar cada transação
        tempo_transacao = tempo_rec_transacao - tempo_rec_pkt
        file2 = open("1_tempo_transacao_seg", "a")
        file2.write(str(tempo_transacao))
        file2.write('\n')
         							
# sys.stdout.flush()
def main():
    # ifaces = [i for i in os.listdir('/sys/class/net/') if 'eth' in i]
    iface = 's1-eth42'
    print("sniffing on %s" % iface)
    # sys.stdout.flush()
    sniff(iface = iface,
          prn = lambda x: handle_pkt(x))

if __name__ == '__main__':
    main()
