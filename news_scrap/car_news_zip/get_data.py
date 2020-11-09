import requests
import re
from bs4 import BeautifulSoup

def get_soup(url) :
	headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'}
	res = requests.get(url, headers=headers)
	res.raise_for_status()
	res.encoding=None
	soup = BeautifulSoup(res.text, 'lxml')
	return soup

new_car_list = []
used_car_list = []

# 오토뷰 신차
def get_autoview_new() :
	url = 'http://www.autoview.co.kr/content/news/news_new_car.asp?page=1&pageshow=1'
	soup = get_soup(url)

	h_news_list = soup.find('div', attrs={'class': 'top_article'}).find_all('li')
	news_list = soup.find('div', attrs={'class': 'section newslist'}).find_all('li')

	data_list = []
	return_data_dic = {}

	for h_news in h_news_list :
		link = h_news.find('a')['href']
		img_url = h_news.find('div', attrs={'class', 'thumb'})['style']
		subject = h_news.find('div', attrs={'class': 'tit'}).get_text().strip()
		summary = h_news.find('div', attrs={'class': 'txt'}).get_text().strip()
		date = h_news.find('div', attrs={'class': 'date'}).get_text().strip()
		data_group = {}
		data_group['link'] = link
		data_group['img_url'] = img_url[21:-1]
		data_group['subject'] = subject
		data_group['summary'] = summary
		data_group['date'] = date

		data_list.append(data_group)
	
	for news in news_list :
		link = news.find('a')['href']
		img_url = news.find('div', attrs={'class', 'thumb'})['style']
		subject = news.find('div', attrs={'class': 'tit'}).get_text().strip()
		summary = news.find('div', attrs={'class': 'txt'}).get_text().strip()
		date = news.find('div', attrs={'class': 'date'}).get_text().strip()
		data_group = {}
		data_group['link'] = link
		data_group['img_url'] = img_url[21:-1]
		data_group['subject'] = subject
		data_group['summary'] = summary
		data_group['date'] = date

		data_list.append(data_group)

	return_data_dic['autoview_new'] = data_list
	new_car_list.append(return_data_dic)

# IT조선 신차	
def get_chosun_new() :
	url = 'http://it.chosun.com/svc/list_in/list.html?catid=32&pn=1'
	soup = get_soup(url)

	h_news = soup.find('div', attrs={'class': 'thumb_big'})
	news_list = soup.select('.add_item_wrap > li')

	data_list = []
	return_data_dic = {}

	# headline
	link = h_news.find('div', attrs={'class': 'txt_wrap'}).find('a')['href']
	img_url = h_news.find('img')['src']
	subject = h_news.find('span', attrs={'class': 'tt'}).get_text().strip()
	summary = h_news.find('span', attrs={'class': 'txt'}).get_text().strip()
	date = h_news.find('span', attrs={'class': 'date'}).get_text().strip()
	data_group = {}
	data_group['link'] = link
	data_group['img_url'] = img_url
	data_group['subject'] = subject
	data_group['summary'] = summary
	data_group['date'] = date
	data_list.append(data_group)

	# normal
	for news in news_list :
		link = news.find('div', 'txt_wrap').find('a')['href']
		img_url = news.find('img')['src']
		subject = news.find('div', attrs={'class': 'txt_dot1'}).get_text().strip()
		summary = news.find('span', attrs={'class': 'txt_dot2'}).get_text().strip()
		date = news.find('span', attrs={'class': 'date'}).get_text().strip()
		data_group = {}
		data_group['link'] = link
		data_group['img_url'] = img_url
		data_group['subject'] = subject
		data_group['summary'] = summary
		data_group['date'] = date

		data_list.append(data_group)

	return_data_dic['chosun_new'] = data_list
	new_car_list.append(return_data_dic)

# 오토헤럴드 국내 신차
def get_autoh_new_k() :
	url = 'http://autotimes.hankyung.com/apps/news.sub_list?popup=0&nid=02&c1=02&c2=01&c3=&newscate=&isslide=&page=1'
	soup = get_soup(url)

	data_list = []
	return_data_dic = {}

	news_list = soup.select('.newest_list > dl')

	# normal
	for idx, news in enumerate(news_list) :
		link = news.find('dt').find('a')['href']
		img_url = news.find('dd', attrs={'class', 'thum'}).find('img')['src']
		subject = news.find('dt').find('a').get_text().strip()
		summary = news.find('dd', attrs={'class': 'txt'}).get_text().strip()
		date = news.find('dd', attrs={'class': 'date'}).get_text().strip()
		data_group = {}
		data_group['link'] = link
		data_group['img_url'] = img_url
		data_group['subject'] = subject
		data_group['summary'] = summary
		data_group['date'] = date[0:-6]

		data_list.append(data_group)

		# 상위 10개만 가져오기
		if idx == 9 :
			break


	return_data_dic['autoh_new_k'] = data_list
	new_car_list.append(return_data_dic)

# 오토헤럴드 국외 신차
def get_autoh_new_g() :
	url = 'http://autotimes.hankyung.com/apps/news.sub_list?popup=0&nid=02&c1=02&c2=02&c3=&newscate=&isslide=&page=1'
	soup = get_soup(url)

	data_list = []
	return_data_dic = {}

	news_list = soup.select('.newest_list > dl')

	# normal
	for idx, news in enumerate(news_list) :
		link = news.find('dt').find('a')['href']
		img_url = news.find('dd', attrs={'class', 'thum'}).find('img')['src']
		subject = news.find('dt').find('a').get_text().strip()
		summary = news.find('dd', attrs={'class': 'txt'}).get_text().strip()
		date = news.find('dd', attrs={'class': 'date'}).get_text().strip()
		data_group = {}
		data_group['link'] = link
		data_group['img_url'] = img_url
		data_group['subject'] = subject
		data_group['summary'] = summary
		data_group['date'] = date[0:-6]

		data_list.append(data_group)

		# 상위 10개만 가져오기
		if idx == 9 :
			break

	return_data_dic['autoh_new_g'] = data_list
	new_car_list.append(return_data_dic)

# 오토헤럴드 중고차
def get_autoh_used() : 
	url = 'http://autotimes.hankyung.com/apps/news.sub_list?popup=0&nid=05&c1=05&c2=02&c3=&newscate=&isslide=&page=1'
	soup = get_soup(url)

	data_list = []
	return_data_dic = {}

	news_list = soup.select('.newest_list > dl')

	# normal
	for idx, news in enumerate(news_list) :
		link = news.find('dt').find('a')['href']
		subject = news.find('dt').find('a').get_text().strip()
		summary = news.find('dd', attrs={'class': 'txt'}).get_text().strip()
		date = news.find('dd', attrs={'class': 'date'}).get_text().strip()
		if news.find('dd', attrs={'class', 'thum'}) :
			img_url = news.find('dd', attrs={'class', 'thum'}).find('img')['src']

		data_group = {}
		data_group['link'] = link
		data_group['img_url'] = img_url
		data_group['subject'] = subject
		data_group['summary'] = summary
		data_group['date'] = date[0:-6]

		data_list.append(data_group)

		# 상위 10개만 가져오기
		if idx == 9 :
			break

	return_data_dic['autoh_used'] = data_list
	used_car_list.append(return_data_dic)

# 데일리카 중고차
def get_daily_used() :
	url = 'http://www.dailycar.co.kr/content/news.html?type=list&sub=sell&maker=used'
	soup = get_soup(url)

	data_list = []
	return_data_dic = {}

	news_list = soup.select('.nwslistwrap > .nwslist:not(.ad)')

	# normal
	for idx, news in enumerate(news_list) :
		link = news.find('section', attrs={'class': 'nwslist_title'}).find('a')['href']
		subject = news.find('section', attrs={'class': 'nwslist_title'}).find('a').get_text().strip()
		summary = news.find('section', attrs={'class': 'nwslist_summary'}).get_text().strip()
		date = news.find('date').get_text().strip()
		img_url = news.find('div', attrs={'class', 'fixedratio'}).find('img')['src']

		data_group = {}
		data_group['link'] = 'http://www.dailycar.co.kr'+ link
		data_group['img_url'] = 'http://www.dailycar.co.kr'+ img_url
		data_group['subject'] = subject
		data_group['summary'] = summary
		data_group['date'] = date

		data_list.append(data_group)

		# 상위 10개만 가져오기
		if idx == 9 :
			break

	return_data_dic['daily_used'] = data_list
	used_car_list.append(return_data_dic)



# 신차 모음
def get_new_car() :
	get_autoview_new()
	get_chosun_new()
	get_autoh_new_k()
	get_autoh_new_g()

	print(new_car_list)

# 중고차 모음
def get_used_car() :
	# get_autoh_used()
	get_daily_used()

	print(used_car_list)

if __name__ == '__main__' : 
	# 신차 뉴스
	# get_new_car()

	# 중고차 업계 뉴스
	get_used_car()
