# -*-coding:Latin-1 -*

# INSTALL pip install colorama
# INSTALL pip install simplejson


# FONCTION SLEEP
import time
# IMPORT VARIABLE OS CLEAR
import os
# API
import json
import requests
# COULEUR TABLEAU
from colorama import Fore, Back, Style
# TABLEAU
from tabulate import tabulate


####################################################################################
api_name = requests.get("https://api.coinmarketcap.com/v1/ticker/")
name_json = api_name.json()

# CREATION LISTE ID | SORTED() POUR TRIE ALPHABET
ids = sorted([name['id'] for name in name_json]) 
 
for id in ids:
    print(id)

print ("\n\n\n\n")

####################################################################################


# INPUT STRING
coin = input("Name coin is : ")
nb_coins_string =  input("How many coins : ")
question_btc_coin = input("Do you still have bitcoins? (yes or no) : ")


# SI VIDE
if not nb_coins_string :

 os.system('cls' if os.name == 'nt' else 'clear')

 print ("\n\n")
 print (Fore.RED + "Put your coins amount or put 0")
 print ("\n\n")

 
# CONVERSION STRING INPUT EN FLOAT
nb_coins = float(nb_coins_string)


if question_btc_coin == "yes" :
	
	# SI IL RESTE DES BITCOINS, COMBIEN EN A T ON ?
	question_btc_coin = input("How many bitcoins do you have left ? : ")
	potentiel_buy = float(question_btc_coin)

	while True :

		# JSON coin
		api_coin = requests.get("https://api.coinmarketcap.com/v1/ticker/" + coin + "/?convert=EUR")
		coin_json = api_coin.json()

		# JSON BTC
		api_btc  = requests.get("https://api.coinmarketcap.com/v1/ticker/bitcoin/?convert=EUR")
		btc_json = api_btc.json()
		

		# VALEUR D'UN BITCOIN EN EURO
		cours_btc = float(btc_json[0]["price_eur"])


		# VALEUR DE LA MONNAIE EN EURO, USD, BTC
		coin_euro = round(float(coin_json[0]["price_eur"]),2)
		coin_usd  = round(float(coin_json[0]["price_usd"]),2)
		coin_btc  = float(coin_json[0]["price_btc"])

		# POURCENTAGE
		coin_percent = str(coin_json[0]["percent_change_24h"])
		# EXPLODE DE LA CHAINE POUR RECUPERER "-"
		split = coin_percent.split('.')
		
		
		# SOMME DE COINS EN BITCOIN
		total_coin_btc = float(nb_coins * coin_btc)
		# PRODUIT EN X, TOTAL DE COIN EN BTC * PRIX DU BTC EN EURO / 1
		total_coin_eur = round(float(total_coin_btc * cours_btc),2)




		#------------------COURS BTC---------------------#

		print (tabulate([[Fore.RED + str(cours_btc)  + Style.RESET_ALL]],
						  headers=['1 BTC --> Euro'], tablefmt='orgtbl'))
		print (Style.RESET_ALL)
		print ("\n\n")

		#------------------POTENTIEL---------------------#

		print (tabulate( [[Fore.RED + str(potentiel_buy / coin_btc) + Style.RESET_ALL,
						   Fore.RED + str(potentiel_buy / coin_btc + nb_coins) + Style.RESET_ALL]],
						   headers=['Achat potentiel', 'Total potentiel'], tablefmt='orgtbl'))
		print (Style.RESET_ALL)
		print ("\n\n")

		#-----------------SOMME TOTAL--------------------#

		# SI "-" EXISTE, POURENTAGE AFFICHE EN ROUGE
		if split[0][0] == "-" :

			print (tabulate([[Fore.RED + str(nb_coins) + Style.RESET_ALL,
							  Fore.RED + "{:.8f}".format(total_coin_btc) + Style.RESET_ALL,
							  Fore.RED + str(total_coin_eur) + Style.RESET_ALL,
							  Fore.RED + str(coin_percent) + Style.RESET_ALL]],
							  headers=['TOTAL', 'TOTAL BTC', 'TOTAL euros', coin +' %'], tablefmt='orgtbl'))
			print (Style.RESET_ALL)
			print ("\n\n")

		else : 

			print (tabulate([[Fore.RED + str(nb_coins) + Style.RESET_ALL,
							  Fore.RED + "{:.8f}".format(total_coin_btc) + Style.RESET_ALL,
							  Fore.RED + str(total_coin_eur) + Style.RESET_ALL, 
							  Fore.GREEN + str(coin_percent) + Style.RESET_ALL]],
							  headers=['TOTAL', 'TOTAL BTC', 'TOTAL euros', coin +' %'], tablefmt='orgtbl'))
			print (Style.RESET_ALL)
			print ("\n\n")

		#------------------COURS COINS---------------------#

		print (tabulate([[Fore.RED + str(coin_usd) + Style.RESET_ALL,
						  Fore.RED + str(coin_euro) + Style.RESET_ALL,
						  Fore.RED + "{:.8f}".format(coin_btc) + Style.RESET_ALL]],
						  headers=['Cours '+ coin +' --> $', 'Cours ' + coin + ' --> EURO', 'Cours ' + coin +' --> SATOSHIS'],tablefmt='orgtbl'))
		print (Style.RESET_ALL)
		print ("\n\n")

		# ACTUALISATION API 
		time.sleep(5)
		# CMD CLEAR
		os.system('cls' if os.name == 'nt' else 'clear')

else :

	while True :

		# JSON coin
		api_coin = requests.get("https://api.coinmarketcap.com/v1/ticker/" + coin + "/?convert=EUR")
		coin_json = api_coin.json()

		# JSON BTC
		api_btc  = requests.get("https://api.coinmarketcap.com/v1/ticker/bitcoin/?convert=EUR")
		btc_json = api_btc.json()
		

		# VALEUR D'UN BITCOIN E EURO
		cours_btc = float(btc_json[0]["price_eur"])


		# VALEUR DE LA MONNAIE EN EURO, USD, BTC
		coin_euro = round(float(coin_json[0]["price_eur"]),2)
		coin_usd  = round(float(coin_json[0]["price_usd"]),2)
		coin_btc  = float(coin_json[0]["price_btc"])

		# POURCENTAGE
		coin_percent = str(coin_json[0]["percent_change_24h"])
		# EXPLODE DE LA CHAINE POUR RECUPERER "-"
		split = coin_percent.split('.')
		
		
		# SOMME DE COINS EN BITCOIN
		total_coin_btc = float(nb_coins * coin_btc)
		# PRODUIT EN X, TOTAL DE COIN EN BTC * PRIX DU BTC EN EURO / 1
		total_coin_eur = round(float(total_coin_btc * cours_btc),2)




		#------------------COURS BTC---------------------#

		print (tabulate([[Fore.RED + str(cours_btc)  + Style.RESET_ALL]],
						  headers=['1 BTC --> Euro'], tablefmt='orgtbl'))
		print (Style.RESET_ALL)
		print ("\n\n")
		#-----------------SOMME TOTAL--------------------#

		if split[0][0] == "-" :

			print (tabulate([[Fore.RED + str(nb_coins) + Style.RESET_ALL,
							  Fore.RED + "{:.8f}".format(total_coin_btc) + Style.RESET_ALL,
							  Fore.RED + str(total_coin_eur) + Style.RESET_ALL,
							  Fore.RED + str(coin_percent) + Style.RESET_ALL]],
							  headers=['TOTAL', 'TOTAL BTC', 'TOTAL euros', coin +' %'], tablefmt='orgtbl'))
			print (Style.RESET_ALL)
			print ("\n\n")

		else : 

			print (tabulate([[Fore.RED + str(nb_coins) + Style.RESET_ALL,
							  Fore.RED + "{:.8f}".format(total_coin_btc) + Style.RESET_ALL,
							  Fore.RED + str(total_coin_eur) + Style.RESET_ALL, 
							  Fore.GREEN + str(coin_percent) + Style.RESET_ALL]],
							  headers=['TOTAL', 'TOTAL BTC', 'TOTAL euros', coin +' %'], tablefmt='orgtbl'))
			print (Style.RESET_ALL)
			print ("\n\n")

		#------------------COURS COINS---------------------#

		print (tabulate([[Fore.RED + str(coin_usd) + Style.RESET_ALL,
						  Fore.RED + str(coin_euro) + Style.RESET_ALL,
						  Fore.RED + "{:.8f}".format(coin_btc) + Style.RESET_ALL]],
						  headers=['Cours '+ coin +' --> $', 'Cours ' + coin + ' --> EURO', 'Cours ' + coin +' --> SATOSHIS'],tablefmt='orgtbl'))
		print (Style.RESET_ALL)
		print ("\n\n")

		# ACTUALISATION API 
		time.sleep(5)
		# CMD CLEAR
		os.system('cls' if os.name == 'nt' else 'clear')
