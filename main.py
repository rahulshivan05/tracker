import requests
from bs4 import BeautifulSoup


# print(dir(requests))

URL = 'https://www.amazon.in/AMD-Ryzen-3600-Processor-100000031BOX/dp/B07STGGQ18/ref=sr_1_7?dchild=1&keywords=AMD+Ryzen+5&qid=1607067791&s=electronics&sr=1-7'


headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'}

def check_price():
	page = requests.get(URL, headers=headers)

	soup = BeautifulSoup(page.content, 'html.parser')

	title = soup.find(id="productTitle").get_text()
	price = soup.find(id="priceblock_ourprice").get_text()
	converted_price = price[0:8]

	if (converted_price < ₹ 16,750):
		send_mail() # not work because not implement. 
		

	print(converted_price)



	print(title.strip())
# Not implemented.
# def send_mail():
		
