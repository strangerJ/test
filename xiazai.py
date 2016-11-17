#!/usr/bin/env python
# coding: utf-8
import urllib
from selenium import webdriver
import time
import sys,os
reload(sys)
import re  
sys.setdefaultencoding('utf8') 
 
def Html_download(url):
    url = url.replace('&amp;','&')
    driver = webdriver.PhantomJS()
    driver.get(url)
    time.sleep(5)
    dir_m = re.search(r'sn=(.*?)&',url)
    path=r'E:\Download\%s'%dir_m.group(1)
    if not os.path.exists(path):
        os.mkdir(path)
    file_name=r'test.html'   
    dest_dir=os.path.join(path,file_name)
    urllib.urlretrieve(url , dest_dir)
    i=0
    while i<20:
        driver.execute_script("window.scrollBy(0,500)","")
        time.sleep(5)
        i+=1
    time.sleep(5)
    img_urls = driver.find_elements_by_xpath('//div[@id="js_content"]//img')
    tt=0
    for img_url in img_urls:
        url = img_url.get_attribute('src') 
        data = urllib.urlopen(url).read()
        f = open('%s\%s.png'%(path,tt),'wb')
        f.write(data)
        f.close()
        tt+=1
    redata = "var tyu=(i-1)+'.png'; images[i].src = tyu ;"
    page = open(dest_dir,'r')
    code = page.read()
    code = code.replace('images[i].src = "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAIAAACQd1PeAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAyBpVFh0WE1MOmNvbS5hZG9iZS54bXAAAAAAADw/eHBhY2tldCBiZWdpbj0i77u/IiBpZD0iVzVNME1wQ2VoaUh6cmVTek5UY3prYzlkIj8+IDx4OnhtcG1ldGEgeG1sbnM6eD0iYWRvYmU6bnM6bWV0YS8iIHg6eG1wdGs9IkFkb2JlIFhNUCBDb3JlIDUuMC1jMDYwIDYxLjEzNDc3NywgMjAxMC8wMi8xMi0xNzozMjowMCAgICAgICAgIj4gPHJkZjpSREYgeG1sbnM6cmRmPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5LzAyLzIyLXJkZi1zeW50YXgtbnMjIj4gPHJkZjpEZXNjcmlwdGlvbiByZGY6YWJvdXQ9IiIgeG1sbnM6eG1wPSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvIiB4bWxuczp4bXBNTT0iaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wL21tLyIgeG1sbnM6c3RSZWY9Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC9zVHlwZS9SZXNvdXJjZVJlZiMiIHhtcDpDcmVhdG9yVG9vbD0iQWRvYmUgUGhvdG9zaG9wIENTNSBXaW5kb3dzIiB4bXBNTTpJbnN0YW5jZUlEPSJ4bXAuaWlkOkJDQzA1MTVGNkE2MjExRTRBRjEzODVCM0Q0NEVFMjFBIiB4bXBNTTpEb2N1bWVudElEPSJ4bXAuZGlkOkJDQzA1MTYwNkE2MjExRTRBRjEzODVCM0Q0NEVFMjFBIj4gPHhtcE1NOkRlcml2ZWRGcm9tIHN0UmVmOmluc3RhbmNlSUQ9InhtcC5paWQ6QkNDMDUxNUQ2QTYyMTFFNEFGMTM4NUIzRDQ0RUUyMUEiIHN0UmVmOmRvY3VtZW50SUQ9InhtcC5kaWQ6QkNDMDUxNUU2QTYyMTFFNEFGMTM4NUIzRDQ0RUUyMUEiLz4gPC9yZGY6RGVzY3JpcHRpb24+IDwvcmRmOlJERj4gPC94OnhtcG1ldGE+IDw/eHBhY2tldCBlbmQ9InIiPz6p+a6fAAAAD0lEQVR42mJ89/Y1QIABAAWXAsgVS/hWAAAAAElFTkSuQmCC";',redata)
    page.close()
    page2 = open(dest_dir,'w')
    page2.write(code)
    page2.close()
    driver.quit()
if __name__ == '__main__':
    url='http://mp.weixin.qq.com/s?__biz=MzI4NDA2NDAxMA==&mid=2653851475&idx=1&sn=af0325327e51996254719b5274f92db0&chksm=f05b0f36c72c8620c8c5c108395557c0fc8f6ec72be4d7408fc1999f973dee89e28b5465f74c&scene=0#rd'
    Html_download(url)

