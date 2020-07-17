# -*- coding: utf-8 -*-
import os, sys
import json
import datetime
import time
import os.path

#просто выписка в жсон по 10 кам 

now=datetime.datetime.now()
#print (str(now))
#print (now.strftime("%d-%m-%y %H:%M"))
dataw=now.strftime("%d.%m.%y") 
timen=now.strftime("%H:%M") 
#print (dataw)
#print (timen)
link=done=""
oldsbsfer=subsfer=oldsfer=sfer=""
#выбор папки
basepa="./"
osnpa="vps/"
npa=input("путь ("+osnpa+")").strip()
if npa!="":
	osnpa=npa
fpath=basepa+osnpa
print(os.path.exists(fpath))
if os.path.exists(fpath):
	print(os.path.exists(fpath))
else:
	try:
		os.mkdir(npa)
	except OSError:
		print ("Создать директорию %s не удалось" % fpath)
	
for t in range(10):
	#inp = raw_input("текст: ")
	inp =  input("текст: ")
	inpj = inp.strip() + '.json'
	

	check_file = os.path.exists(fpath+inp) 
	
	if check_file:
		inp =  input("есть такой - назови по другому: ")
		inpj = inp + '.json'
	print(inpj)
	#price =  input("Цена ")

	oldsfer=sfer
	sfer =  input("Сфера("+oldsfer+")? ")
	if sfer=="":
		sfer=oldsfer

	oldsbsfer=subsfer
	subsfer =  input("Подсфера("+oldsbsfer+")? ")
	if subsfer=="":
		subsfer=oldsbsfer

	#price = raw_input("Цена ")
	#sfer = raw_input("Сфера ")
	#subsfer = raw_input("Подсфера ")

	 
	data='{\n"text":\"'+inp+'\",\n'
	#data+='"price":\"'+price+'\",\n'
	data+='"sfer":\"'+sfer+'\",\n'
	data+='"subsfer":\"'+subsfer+'\",\n'
	data+='"dadd":\"'+dataw+'\",\n'
	data+='"tadd":\"'+timen+'\",\n'
	#data+='"link":\"'+link+'\",\n'
	data+='"done":\"'+done+'\"\n}'
	

	#data+='"dbye":"",\n'
	#data+='"dget":"",\n'
	#data+='"name":""\n}'

	my_file = open(fpath+inpj, 'w')
	my_file.write(data)
	my_file.close()
	
	print(inpj)
	print(sfer)
	print(subsfer)

	#data2 = json.loads(data)
	#with open(inpj, "w") as write_file:
	#	json.dump(data, write_file,ensure_ascii=False)
		#encoding="utf-8"
	print("")	
	time.sleep(1)
