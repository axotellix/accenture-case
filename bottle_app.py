from bottle import default_app, route, response, template, run
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

@route('/')
def hello_world():
    return 'Hello world'

@route('/api/userinfo/<username>')
def userinfo(username):
	response.add_header('Access-Control-Allow-Origin', '*')
	if(username == 'user1' or username == 'user2' or username == 'user3'):
		user = cursor.execute("SELECT user_id,fullname,invest_type FROM users WHERE username='" + username + "';").fetchall()[0]
		user_assets = cursor.execute("SELECT stocks,count FROM assets WHERE user_id=" + str(user[0])).fetchall()
		user1 = {"name": user[1], "stocks": {i[0]: i[1] for i in user_assets}, "type": user[2]}
		return template('{{data}}', data=user1)
	else:
		return 'Username not found'

@route('/api/rebalance/<username>')
def rebalance(username):
	response.add_header('Access-Control-Allow-Origin', '*')
	if(username == 'user1' or username == 'user2' or username == 'user3'):
		# Ребалансировка портфеля (рекомендации)
		user = cursor.execute("SELECT user_id,fullname,invest_type FROM users WHERE username='" + username + "';").fetchall()[0]
		user_assets = cursor.execute("SELECT stocks,count FROM assets WHERE user_id=" + str(user[0])).fetchall()
		user1 = {"name": user[1], "stocks": {i[0]: i[1] for i in user_assets}, "type": user[2]}

		if(True):
			other_count = 0
			return_data = ""
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
			return_data += ("Портфель состоит на " + str(obligs_percent) + "% из облигаций и из акций на " + str(100 - obligs_percent) + "%")
			
			sell_list = []
			i = 0 # счетчик размера рекомендаций
			if(user1['type'] == 1):
				# Ультраконсервативный тип инвестора
				if(other_count > 1000):
					# Если есть значимое число акций
					return 'Рекомендуем оставить в портфеле только облигации для минимизации рисков.' + return_data

			elif(user1['type'] == 2):
				# Консервативный тип инвестора
				while(int(100*((i + obligs_count)/(other_count + obligs_count))) < 80):
					# Считаем насколько портфель не соответствует типу профиля
					i += 5
				min_different = int(0.05 * (other_count + obligs_count) ) # минимальная разница, которую имеет смысл учитывать - 5% для консервативных
				if(i//1000 > 0 and i > min_different): # ~1000 - цена облигаций  ОФЗ и многих других
					return_data += ("Закупка " + str(i//1000) + " облигаций ОФЗ обеспечит диверсификацию портфеля, снизит риски и позволит поднять аллокацию облигаций до рекомендуемого уровня ~80%.")
					return_data += ("К покупке рекомендованы облигации государственного типа, т.к. гарантия сбережения денег доказывается при каждом кризисе. Только государственные облигации не упали в цене, а наоборот продолжили расти в течение кризисов последних лет.")
					return_data += ("Также можно продать какие-либо акции на " + str(i) + " руб.")
					
					# Выбираем акции для продажи (фиксация прибыли)
					for company_name in company_names:
						if(company_name != "OFZ"):
							prices_month = json.loads(requests.get("https://investcab.ru/api/chistory?symbol=" + company_name + "&resolution=D&from=" + str(start_time) + "&to=" + str(end_time)).json())['c'][-30:] # график за месяц
							increase = int((prices_month[-1] / prices_month[0] - 1) * 100) # изменение за месяц в процентах
							if(increase > 8):
								return_data += (company_name + " (" + str(increase) + "%)")
								sell_list.append(company_name)
					if(increase > 8):
						return_data += ("Перечисленные акции предложены к продаже, так как достигнут стратегический максимум поднятия цены 8-15%.")
						return_data += ("Данный максимум сигнализирует о возможной переоценнености акции и ее будущей потере в цене.")
						return template('{\"to_buy\": {\"bonds\": 1, \"stocks\": 1},\"{{data}}\","bonds": {{list_bonds}}, "stocks": ["OFZ"], "status": 0}',data=return_data,list_bonds=sell_list)
						#if(input("Продать данные акции? [Y/n] ") == "Y"):
						#	for i in sell_list:
						#		cursor.execute("DELETE FROM assets WHERE user_id=" + str(user[0]) + " AND stocks=\"" + i + "\";")
						#		connect.commit()
				else:
					i = 0
					while(int(100*((i + other_count)/(other_count + obligs_count))) < 20):
						i += 5
					if(i > min_different):
						return_data += ("Для увеличения доходности можно докупить акций на ~" + str(i) + " руб., что также позволит поднять аллокацию акций до рекомендуемого уровня ~20%")
						
						# Рекомендации по докупке
						low_risk = []
						for company_name in company_names:
							if(company_name != "OFZ"):
								data = cursor.execute("SELECT stocks, volatility, caps FROM stocks WHERE stocks=\"" + company_name + "\"").fetchall()[0]
								if('T' in data[2]):
									# Если у акций большая капитализации
									cap = True 
								else:
									# если нет
									cap = False
								volatility = float(data[1]) # берем волатильность
								if(volatility < 12 and cap == True):
									# Если низкая волатильность и большая капитализация, то низкий уровень рисков. Рекомендуем для текущего (консервативного) профиля
									low_risk.append(company_name)

						if(len(low_risk) > 0):
							return_data += ("В соответствии с вашим риск-профилем рекомендуем")
							return_data += (low_risk)
							return_data += ("Поскольку данные акции обладают большой капитализацией и низкой волатильностью.")
							return template('{{data}}',data=return_data)
						elif(max_target > 0):
							return 'Лучшие прогнозы в портфеле у компании ' + max_target_name + '. В среднем ожидается рост ' + str(100-int(max_target*100)) + '%'
					else:
						return 'Ваш портфель в порядке.'

			elif(user1['type'] == 3):
				# Умеренный тип инвестора
				while(int(100*((i + obligs_count)/(other_count + obligs_count))) < 50):
					i += 5
				min_different = int(0.1 * (other_count + obligs_count) ) # минимальная разница, которую имеет смысл учитывать - 10% для умеренных
				if(i//1000 > 0 and i > min_different): # ~1000 - цена облигаций ОФЗ и многих других
					return_data += ("Закупка " + str(i//1000) + " облигаций ОФЗ обеспечит диверсификацию портфеля, снизит риски и позволит поднять аллокацию облигаций до рекомендуемого уровня ~50%.")
					return_data += ("К покупке рекомендованы облигации государственного типа, т.к. гарантия сбережения денег доказывается при каждом кризисе. Только государственные облигации не упали в цене, а наоборот продолжили расти в течение кризисов последних лет.")
					return_data += ("Также можно продать какие-либо акции на " + str(i) + " руб.")
					
					# Выбираем акции для продажи (фиксация прибыли)
					for company_name in company_names:
						if(company_name != "OFZ"):
							prices_month = json.loads(requests.get("https://investcab.ru/api/chistory?symbol=" + company_name + "&resolution=D&from=" + str(start_time) + "&to=" + str(end_time)).json())['c'][-30:] # график за месяц
							increase = int((prices_month[-1] / prices_month[0] - 1) * 100) # изменение за месяц в процентах
							if(increase > 8):
								return_data += (company_name + " (" + str(increase) + "%)")
					if(increase > 8):
						return_data += ("Перечисленные акции предложены к продаже, так как достигнут стратегический максимум поднятия цены 8-15%.")
						return_data += ("Данный максимум сигнализирует о возможной переоценнености акции и ее будущей потере в цене.")
						return template('{{data}}',data=return_data)
						#if(input("Продать 50% акций? [Y/n] ") == "Y"):
							#for i in sell_list:
							#	cursor.execute("DELETE FROM assets WHERE user_id=" + str(user[0]) + " AND stocks=\"" + i + "\";")
							#	cursor.execute("INSERT INTO assets VALUES (null, " + str(user[0]) + ", \"" + i + "\", " + user1['stocks'][i] // 2 + "\")")
							#	connect.commit()
				else:
					i = 0
					while(int(100*((i + other_count)/(other_count + obligs_count))) < 50):
						i += 5
					if(i > min_different):
						return_data += ("Для увеличения доходности можно докупить акций на ~" + str(i) + " руб., что также позволит поднять аллокацию акций до рекомендуемого уровня ~50%")
						return_data += ("Лучшие прогнозы в портфеле у компании " + max_target_name + ". В среднем ожидается рост " + str(100-int(max_target*100)) + "%")
						return template('{{data}}',data=return_data)
					else:
						return 'Ваш портфель в порядке.'

			elif(user1['type'] == 4):
				# Агрессивный тип инвестора
				while(int(100*((i + obligs_count)/(other_count + obligs_count))) < 20):
					i += 5
				min_different = int(0.15 * (other_count + obligs_count) ) # минимальная разница, которую имеет смысл учитывать - 15% для агрессивных
				if(i//1000 > 0 and i > min_different): # ~1000 - цена облигаций ОФЗ и многих других
					return_data += ("Закупка " + str(i//1000) + " облигаций ОФЗ обеспечит диверсификацию портфеля, снизит риски и позволит поднять аллокацию облигаций до рекомендуемого уровня ~20%.")
					return_data += ("К покупке рекомендованы облигации государственного типа, т.к. гарантия сбережения денег доказывается при каждом кризисе. Только государственные облигации не упали в цене, а наоборот продолжили расти в течение кризисов последних лет.")
					return_data += ("Также можно продать какие-либо акции на " + str(i) + " руб.")

					# Выбираем акции для продажи (фиксация прибыли)
					for company_name in company_names:
						if(company_name != "OFZ"):
							prices_month = json.loads(requests.get("https://investcab.ru/api/chistory?symbol=" + company_name + "&resolution=D&from=" + str(start_time) + "&to=" + str(end_time)).json())['c'][-30:] # график за месяц
							increase = int((prices_month[-1] / prices_month[0] - 1) * 100) # изменение за месяц в процентах
							if(increase > 8):
								print(company_name + " (" + str(increase) + "%)")
					if(increase > 8):
						# Предлагаем частичную фиксацию прибыли, т.к. агрессивный риск-профиль
						return_data += ("Перечисленные акции предложены к продаже, так как достигнут стратегический максимум поднятия цены 8-15%.")
						return_data += ("Данный максимум сигнализирует о возможной переоценнености акции и ее будущей потере в цене.")
						return template('{{data}}',data=return_data)
						#if(input("Продать 50% акций? [Y/n] ") == "Y"):
						#	for i in sell_list:
						#		cursor.execute("DELETE FROM assets WHERE user_id=" + str(user[0]) + " AND stocks=\"" + i + "\";")
						#		cursor.execute("INSERT INTO assets VALUES (null, " + str(user[0]) + ", \"" + i + "\", " + user1['stocks'][i] // 2 + "\")")
						#		connect.commit()
				else:
					i = 0
					while(int(100*((i + other_count)/(other_count + obligs_count))) < 80):
						i += 5
					if(i > min_different):
						return_data += ("Для увеличения доходности можно докупить акций на ~" + str(i) + " руб., что также позволит поднять аллокацию акций до рекомендуемого уровня ~80%")
						return_data += ("Лучшие прогнозы в портфеле у компании " + max_target_name + ". В среднем ожидается рост " + str(100-int(max_target*100)) + "%" )
						return template('{{data}}',data=return_data)
					else:
						return 'Ваш портфель в порядке.'

			elif(user1['type'] == 5):
				# Ультраагресивный тип инвестора
				if(obligs_count > 1000):
					# Если есть значимое число облигаций
					return 'Рекомендуем оставить в портфеле только акции и фонды для повышения доходности.'
	else:
		return 'Username not found'
	
run(host='localhost', port=1337)