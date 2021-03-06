# 爬取斗图啦表情包
# @author ahao

from urllib import request
from bs4 import BeautifulSoup
import bs4
import requests
import time
from multiprocessing.dummy import Pool as ThreadPool



def getImg(url):

    header = {
        'Accept': "*/*",
        'Accept-Language': "zh-CN,zh;q=0.9",
        'Connection': "keep-alive",
        'User-Agent': "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.79 Safari/537.36"
    }
    
    downPath = r"F:\pythonReptile\images"

    response = requests.get(url, headers=header, timeout=30)
    #print(response.headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    datas = soup.find_all(
        name="img", attrs={"class": "img-responsive lazy image_dta"})
    for data in datas:
        print("downloading:", data.attrs['data-original'])
        request.urlretrieve(
            data.attrs['data-original'], downPath+'\%s.jpg' % time.time())

if __name__ == '__main__':
    pool = ThreadPool(8)
    urls = [
        "http://www.doutula.com/photo/list/?page={}".format(str(i)) for i in range(1, 3)]
    pool.map(getImg, urls)
    pool.close()
    pool.join()
