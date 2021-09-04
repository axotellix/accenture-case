import numpy as np
import requests
import math
import json
import sqlite3
import time

fonds = ["NASDAQ Composite (IXIC)", "Nasdaq 100 (NDX)", "S&P 500 (SPX)", "Индекс Мосбиржи (IMOEX)"]
obligs = ["ОФЗ", "ВТБ", "Газпром", "Золото"]
menu = None
end_time = int(time.time())
start_time = end_time - 31104060 # год в UNIX
connect = sqlite3.connect("db.db")
cursor = connect.cursor()

while(menu != 0):
	menu = int(input("""
0 - Выход
1 - Поиск названий акций
2 - График цен акции
3 - Определение риска акции
4 - Рекомендации похожих акций
5 - Рыночная капитализация акции
6 - Долг/капитал акции
7 - Дивидендная история
8 - Целевая цена акции (средние прогнозы фондов)
9 - Ребалансировка портфеля
Ввод: """))

	if(menu == 1):
		# Поиск названий акций
		company_name = input("Поиск: ")
		names_found = json.loads(requests.get("https://investcab.ru/api/csearch?limit=30&query=" + company_name + "&type=EQF&exchange=").json())
		print("Найдены следующие акции:")
		for i in names_found:
			print(i['full_name'],end = ' ')

	elif(menu == 2):
		# Получение цен
		company_name = input("Введите название акции для получения графика: ")
		prices = json.loads(requests.get("https://investcab.ru/api/chistory?symbol=" + company_name + "&resolution=D&from=" + str(start_time) + "&to=" + str(end_time)).json())['c']
		# Вывод цен
		print("\nЦены за " + str(len(prices)) + " дней:\n", prices, end='\n\n')
		print("Цены за последний месяц:\n", prices[-30:])

	elif(menu == 3):
		# Определение риска акций
		company_name = input("Введите название акции: ")
		prices = json.loads(requests.get("https://investcab.ru/api/chistory?symbol=" + company_name + "&resolution=D&from=" + str(start_time) + "&to=" + str(end_time)).json())['c']
		volatility = math.sqrt(np.var(prices)) # Волатильность за месяц
		print("\nВолатильность\n",volatility)
		if(volatility < 12):
			print("Акция имеет низкий уровень рисков.")
		elif(volatility > 12 and volatility < 20):
			print("Акция имеет средний уровень рисков.")
		elif(volatility > 20):
			print("Акция имеет высокий уровень рисков.")

	elif(menu == 4):
		# Рекомендации
		company_name = input("Введите акцию, которой вы уже владеете: ")
		
		# Считаем её риски
		prices = json.loads(requests.get("https://investcab.ru/api/chistory?symbol=" + company_name + "&resolution=D&from=1599587468&to=1630691528").json())['c']
		volatility = math.sqrt(np.var(prices)) # Волатильность за месяц
		
		t_vols = sorted(all_vols)
		volatility = min(all_vols, key=lambda x:abs(x-volatility))
		vols = t_vols[t_vols.index(volatility):t_vols.index(volatility)+5]
		vols += t_vols[t_vols.index(volatility)-5:t_vols.index(volatility)]
		print("Рекомендуем похожие по риск-уровню акции: ")
		for i in vols:
			print(all_stocks[all_vols.index(i)],end = ' ')

	elif(menu == 5):
		# Капитализация акции
		company_name = input("Введите название акции: ").replace('@','.')
		headers = {'User-Agent': 'User agent for work'}
		cap = requests.get("https://query1.finance.yahoo.com/v7/finance/quote?formatted=true&crumb=qQMEtw/8z/0&lang=en-US&region=US&symbols=" + company_name + "&fields=marketCap&corsDomain=finance.yahoo.com", headers=headers).json()
		cap = cap['quoteResponse']['result'][0]['marketCap']['fmt']
		print(cap)

	elif(menu == 6):
		# Долг/капитал акции
		company_name = input("Введите название акции: ").replace('@','.')
		headers = {'User-Agent': 'User agent for work'}
		debt_equity = requests.get("https://finance.yahoo.com/quote/" + company_name + "/key-statistics?p=" + company_name, headers=headers)
		start = debt_equity.text.find("debtToEquity")+15
		step = debt_equity.text[start:].find(':')+1
		print("Долг/капитал: ", debt_equity.text[start+step:start+step+debt_equity.text[start+step:].find(",")])
	
	elif(menu == 7):
		# Дивидендная история акции
		company_name = input("Введите название акции: ").replace('@','.')
		headers = {'User-Agent': 'User agent for work'}
		divs = requests.get("https://query1.finance.yahoo.com/v7/finance/download/" + company_name + "?period1=" + str(end_time - 155520300) + "&period2=" + str(end_time) + "&interval=1d&events=div&includeAdjustedClose=true", headers=headers).text.split('\n')
		for i in divs:
			print(i)

	elif(menu == 8):
		# Целевая цена (прогнозы фондов)
		company_name = input("Введите название акции: ").replace('@','.')
		headers = {'User-Agent': 'User agent for work'}
		target = requests.get("https://finance.yahoo.com/quote/" + company_name + "/analysis?p=" + company_name, headers=headers).text
		start = target.find("targetMeanPrice") # ищем начало целевой цены
		step = target[start:].find("}")+1 # ищем конец параметра
		target = json.loads(target[start+17:start+step])['fmt']
		print(target)

	elif(menu == 9):
		# Ребалансировка портфеля (рекомендации)
		input_name = input("Введите username пользователя (user1, user2): ")
		user = cursor.execute("SELECT user_id,fullname,invest_type FROM users WHERE username='" + input_name + "';").fetchall()[0]
		user_assets = cursor.execute("SELECT stocks,count FROM assets WHERE user_id=" + str(user[0])).fetchall()
		user1 = {"name": user[1], "stocks": {i[0]: i[1] for i in user_assets}, "type": user[2]}
		print(user1)

		if(int(input("Запустить ребалансировку портфеля пользователя? \n1 - Да\nEnter: "))):
			other_count = 0
			obligs_count = 0
			company_names = [i for i in user1['stocks']]

			max_target = 0
			max_target_name = ""
			for company_name in company_names:
				if(company_name != "OFZ"):
					# Собираем прогнозы
					headers = {'User-Agent': 'User agent for work'}
					target = requests.get("https://finance.yahoo.com/quote/" + company_name + "/analysis?p=" + company_name, headers=headers).text
					start = target.find("targetMeanPrice") # ищем начало целевой цены
					step = target[start:].find("}")+1 # ищем конец параметра
					target = float(json.loads(target[start+17:start+step])['fmt'])

					# текущая цена
					prices = json.loads(requests.get("https://investcab.ru/api/chistory?symbol=" + company_name + "&resolution=D&from=" + str(start_time) + "&to=" + str(end_time)).json())['c']

					# отбираем лучший прогноз (% роста)
					increase = float(prices[-1]) / target
					if(increase > max_target):
						max_target = increase
						max_target_name = company_name

			if(company_names.count('OFZ') != 0):
				# Считаем, сколько занимают облигации, а сколько акции
				obligs_count = user1['stocks']['OFZ']
				for i in user1['stocks']:
					other_count += user1['stocks'][i]
				other_count -= obligs_count
				obligs_percent = int(100 * (obligs_count / (other_count + obligs_count)) )
			else:
				for i in user1['stocks']:
					other_count += user1['stocks'][i]
			print("Портфель состоит на " + str(obligs_percent) + "% из облигаций и из акций на " + str(100 - obligs_percent) + "%")
			
			i = 0 # счетчик размера рекомендаций
			if(user1['type'] == 1):
				# Ультраконсервативный тип инвестора
				if(other_count > 1000):
					# Если есть значимое число акций
					print("Рекомендуем оставить в портфеле только облигации для минимизации рисков.")

			elif(user1['type'] == 2):
				# Консервативный тип инвестора
				while(int(100*((i + obligs_count)/(other_count + obligs_count))) < 80):
					i += 5
				min_different = int(0.05 * (other_count + obligs_count) ) # минимальная разница, которую имеет смысл учитывать - 5% для консервативных
				if(i//1000 > 0 and i > min_different): # ~1000 - цена облигаций  ОФЗ и многих других
					print("Закупка " + str(i//1000) + " облигаций ОФЗ обеспечит диверсификацию портфеля и снизит риски, а также позволит поднять аллокацию облигаций до рекомендуемого уровня ~80%.")
					print("Также можно продать какие-либо акции на " + str(i) + " руб.")
					
					# Выбираем акции для продажи (фиксация прибыли)
					for company_name in company_names:
						if(company_name != "OFZ"):
							prices_month = json.loads(requests.get("https://investcab.ru/api/chistory?symbol=" + company_name + "&resolution=D&from=" + str(start_time) + "&to=" + str(end_time)).json())['c'][-30:] # график за месяц
							increase = int((prices_month[-1] / prices_month[0] - 1) * 100) # изменение за месяц в процентах
							if(increase > 8):
								print(company_name + " (" + str(increase) + "%)")
					if(increase > 8):
						print("Перечисленные акции предложены к продаже, так как достигнут стратегический максимум поднятия цены 8-15%.")
						print("Данный максимум сигнализирует о возможной переоценнености акции и ее будущей потере в цене.")
				else:
					i = 0
					while(int(100*((i + other_count)/(other_count + obligs_count))) < 20):
						i += 5
					if(i > min_different):
						print("Для увеличения доходности можно докупить акций на ~" + str(i) + " руб., что также позволит поднять аллокацию акций до рекомендуемого уровня ~20%")
						print("Лучшие прогнозы в портфеле у компании " + max_target_name + ". В среднем ожидается рост " + str(100-int(max_target*100)) + "%")
					else:
						print("Ваш портфель в порядке.")

			elif(user1['type'] == 3):
				# Умеренный тип инвестора
				while(int(100*((i + obligs_count)/(other_count + obligs_count))) < 50):
					i += 5
				min_different = int(0.1 * (other_count + obligs_count) ) # минимальная разница, которую имеет смысл учитывать - 10% для умеренных
				if(i//1000 > 0 and i > min_different): # ~1000 - цена облигаций ОФЗ и многих других
					print("Закупка " + str(i//1000) + " облигаций ОФЗ обеспечит диверсификацию портфеля и снизит риски, а также позволит поднять аллокацию облигаций до рекомендуемого уровня ~50%.")
					print("Также можно продать какие-либо акции на " + str(i) + " руб.")
					
					# Выбираем акции для продажи (фиксация прибыли)
					for company_name in company_names:
						if(company_name != "OFZ"):
							prices_month = json.loads(requests.get("https://investcab.ru/api/chistory?symbol=" + company_name + "&resolution=D&from=" + str(start_time) + "&to=" + str(end_time)).json())['c'][-30:] # график за месяц
							increase = int((prices_month[-1] / prices_month[0] - 1) * 100) # изменение за месяц в процентах
							if(increase > 8):
								print(company_name + " (" + str(increase) + "%)")
					if(increase > 8):
						print("Перечисленные акции предложены к продаже, так как достигнут стратегический максимум поднятия цены 8-15%.")
						print("Данный максимум сигнализирует о возможной переоценнености акции и ее будущей потере в цене.")
				else:
					i = 0
					while(int(100*((i + other_count)/(other_count + obligs_count))) < 50):
						i += 5
					if(i > min_different):
						print("Для увеличения доходности можно докупить акций на ~" + str(i) + " руб., что также позволит поднять аллокацию акций до рекомендуемого уровня ~50%")
						print("Лучшие прогнозы в портфеле у компании " + max_target_name + ". В среднем ожидается рост " + str(100-int(max_target*100)) + "%")
					else:
						print("Ваш портфель в порядке.")

			elif(user1['type'] == 4):
				# Агрессивный тип инвестора
				while(int(100*((i + obligs_count)/(other_count + obligs_count))) < 20):
					i += 5
				min_different = int(0.15 * (other_count + obligs_count) ) # минимальная разница, которую имеет смысл учитывать - 15% для агрессивных
				if(i//1000 > 0 and i > min_different): # ~1000 - цена облигаций ОФЗ и многих других
					print("Закупка " + str(i//1000) + " облигаций ОФЗ обеспечит диверсификацию портфеля и снизит риски, а также позволит поднять аллокацию облигаций до рекомендуемого уровня ~20%.")
					print("Также можно продать какие-либо акции на " + str(i) + " руб.")

					# Выбираем акции для продажи (фиксация прибыли)
					for company_name in company_names:
						if(company_name != "OFZ"):
							prices_month = json.loads(requests.get("https://investcab.ru/api/chistory?symbol=" + company_name + "&resolution=D&from=" + str(start_time) + "&to=" + str(end_time)).json())['c'][-30:] # график за месяц
							increase = int((prices_month[-1] / prices_month[0] - 1) * 100) # изменение за месяц в процентах
							if(increase > 8):
								print(company_name + " (" + str(increase) + "%)")
					if(increase > 8):
						print("Перечисленные акции предложены к продаже, так как достигнут стратегический максимум поднятия цены 8-15%.")
						print("Данный максимум сигнализирует о возможной переоценнености акции и ее будущей потере в цене.")
				else:
					i = 0
					while(int(100*((i + other_count)/(other_count + obligs_count))) < 80):
						i += 5
					if(i > min_different):
						print("Для увеличения доходности можно докупить акций на ~" + str(i) + " руб., что также позволит поднять аллокацию акций до рекомендуемого уровня ~80%")
						print("Лучшие прогнозы в портфеле у компании " + max_target_name + ". В среднем ожидается рост " + str(100-int(max_target*100)) + "%" )
					else:
						print("Ваш портфель в порядке.")

			elif(user1['type'] == 5):
				# Ультраагресивный тип инвестора
				if(obligs_count > 1000):
					# Если есть значимое число облигаций
					print("Рекомендуем оставить в портфеле только акции и фонды для повышения доходности.")	

				

				
				
		
		