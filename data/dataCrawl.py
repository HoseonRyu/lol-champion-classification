import time

import selenium
from selenium import webdriver
from selenium.webdriver import ActionChains

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait

drv = webdriver.Chrome(executable_path='chromedriver')
ids = ["리폿하고열쇠조각"]
index = 0

def do_action(ids,driver,index):
	output = ""

	URL = "http://fow.kr/find/"+ids[index]
	driver.get(url=URL)

	aram_box = driver.find_element_by_class_name('new_recent_aram')
	ActionChains(driver).click(aram_box).perform()

	time.sleep(3)

	div = driver.find_element_by_class_name('div_recent_aram')
	table = div.find_element_by_class_name('table_recent')
	tbody = table.find_element_by_tag_name("tbody")
	rows = tbody.find_elements_by_tag_name("tr")

	print(index, "-[", ids[index],"] rows:",len(rows))
	


	for value in rows:
		elems = value.find_elements_by_tag_name("td")

		game_num = elems[11].get_attribute('onclick')
		output = output + game_num.split('(')[1].split(',')[0]

		#전적 띄우기
		ActionChains(driver).click(elems[11]).perform()
		time.sleep(1)

		tbody_ = driver.find_element_by_id('battle_detail')
		rows_ = tbody_.find_elements_by_tag_name("tr")
		
		team1 = ""
		team2 = ""

		for i in range(5):
			#print("iter",i)
			tds = rows_[i].find_elements_by_tag_name("td")
			if len(tds) != 10:
				ActionChains(driver).click(elems[11]).perform()
				time.sleep(0.5)
				ActionChains(driver).click(elems[11]).perform()
				time.sleep(0.5)
				tbody_ = driver.find_element_by_id('battle_detail')
				rows_ = tbody_.find_elements_by_tag_name("tr")

			tds = rows_[i].find_elements_by_tag_name("td")
			name = tds[1].text # summonner's name
			if name not in ids:
				ids.append(name)

			img = tds[1].find_element_by_tag_name("img")
			img_name = img.get_attribute('src')
			team1 = team1 + "," + img_name.split('/')[-1][:-4]
		
		for i in range(5):
			tds = rows_[i+7].find_elements_by_tag_name("td")
			if len(tds) != 10:
				ActionChains(driver).click(elems[11]).perform()
				time.sleep(0.5)
				ActionChains(driver).click(elems[11]).perform()
				time.sleep(0.5)
				tbody_ = driver.find_element_by_id('battle_detail')
				rows_ = tbody_.find_elements_by_tag_name("tr")

			tds = rows_[i+7].find_elements_by_tag_name("td")
			name = tds[1].text # summonner's name
			if name not in ids:
				ids.append(name)

			img = tds[1].find_element_by_tag_name("img")
			img_name = img.get_attribute('src')
			team2 = team2 + "," + img_name.split('/')[-1][:-4]

		if rows_[5].find_element_by_tag_name("td").text == "승리팀":
			output = output + team1 + team2 + "\n"
		else:
			output = output + team2 + team1 + "\n"

		ActionChains(driver).click(elems[11]).perform()
		time.sleep(0.5)
	return output


for i in range(3000):
	f = open("./output.txt",'a')
	f.write(do_action(ids,drv,index))
	f.close()

	index = index + 1

drv.close()
