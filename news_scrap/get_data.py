import requests
import datetime
from datetime import datetime, timedelta
from bs4 import BeautifulSoup
from selenium import webdriver


def get_soup(url) :
	# options = webdriver.ChromeOptions()
	# options.headless = True
	# options.add_argument('window-size=1920x1080')

	# browser = webdriver.Chrome(r'C:\Users\PC\Documents\simbyungki\git\autoplus\chromedriver.exe', options=options)
	# browser.maximize_window()

	# browser.get(url)
	

	headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'}
	res = requests.get(url, headers=headers)
	res.raise_for_status()
	soup = BeautifulSoup(res.text, 'lxml')
	return soup



def daum_news(keyword) : 
	today_date = datetime.now().strftime('%Y년%m월%d일')
	now_date_time = datetime.now().strftime('%Y%m%d%H%M%S')
	yesterday_time = (datetime.now() - timedelta(days=1)).strftime('%Y%m%d%H%M%S')

	url = f'https://search.daum.net/search?w=news&nil_search=btn&DA=STC&enc=utf8&cluster=y&cluster_page=1&q={keyword}&period=d&sd={yesterday_time}&ed={now_date_time}'
	print(url)
	soup = get_soup(url)
	
	try :
		news_list = soup.find('ul', attrs={'id': 'newsResultUL'}).find_all('li', limit = cnt)
		print('-'* 100)
		print()
		print(f'[다음 "{keyword}" 검색결과 >> 최신]')
		print()
		for idx, news in enumerate(news_list) :
			title = news.find('a', attrs={'class': 'f_link_b'}).get_text()
			link = news.find('a', attrs={'class': 'f_link_b'})['href']
			get_created = news.find('span', attrs={'class': 'f_nb date'}).contents
			
			date = get_created[0].strip()
			media = get_created[2].strip()

			print(f'{str(idx +1).zfill(2)}. [{date}] [{media}]')
			print(f'    {title}')
			print(f'    {link}')
		
		print()
	except Exception as e :
		print(f'{today_date}에 등록된 \'{keyword}\' 관련 뉴스가 없습니다.')
	
	

	


# def naver_news() :
# 	keyword = '오토플러스'
# 	url = f'https://search.naver.com/search.naver?where=news&query={keyword}sm=tab_opt&sort=0&photo=0&field=0&reporter_article=&pd=4&ds=&de=&docid=&nso=so%3Ar%2Cp%3A1d%2Ca%3Aall&mynews=0&refresh_start=0&related=0'
# 	soup = get_soup(url)

# 	news_items = soup.find('div', attrs={'class': 'api_subject_bx'}).find_all('div', attrs={'class': 'api_ani_send'})
# 	print('모든 데이터 로드 완료')
# 	print(soup.find('div', attrs={'class': 'api_subject_bx'}))

# 	# for idx, news_item in enumerate(news_items) :
# 	# 	press = news.find('div', attrs={'class': 'news_info'}).find('a', attrs={'class': 'info press'}).get_text().strip()
# 	# 	title = news.find('a', attrs={'class': 'news_tit'})['title']
# 	# 	link = news.find('a', attrs={'class': 'news_tit'})['href']
# 	# 	summary = news.find('div', attrs={'class': 'dsc_wrap'}).get_text().strip()

# 	# 	print(f'{idx} {press} {title}')
# 	# 	print(f'{summary}')
# 	# 	print(f'{link}')



if __name__ == '__main__' : 
	daum_news('오토플러스')
	