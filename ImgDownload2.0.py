
# -*- coding: utf-8 -*-
from tkinter import *
import threading
from urllib.request import Request, urlopen, urlretrieve
from urllib.error import URLError, HTTPError
import os
import re
import time
window=Tk()
window.title('图片批量下载')
window.geometry('700x300')






# urlfront='https://t1.onvshen.com:85/gallery/21501/23542/'
def img_save():

	urlfront=var_urlfront.get()
	urlfront=re.findall('(.*?)0\d*\d*.jpg',urlfront)[0]
	print(urlfront)
	path_dir=var_path.get()
	a=[]
	a.append(urlfront+'0.jpg')
	for i in range(1,10):
		a.append(urlfront+'00'+str(i)+'.jpg')
	for i in range(10,60):

		a.append(urlfront+'0'+str(i)+'.jpg')
	
	os.mkdir(path_dir)
	m=len(a)//3
	def fun01():
		x=0
		for imgurl in a[:m]:
			
			req = Request(imgurl)
			try:
			    response = urlopen(req)
			except HTTPError as e:
			    break
			except URLError as e:
			    break
			else:

			    urlretrieve(imgurl,path_dir+'/%s.jpg' % str(x+1))
			    print(str(x+1))
			    x+=1
			    print('fun01 in working!')
			    # l.config(text='正在下载第%s张图片'% str(x))
			    # window.update_idletasks()
	def fun02():
		x=m
		for imgurl in a[m:m*2]:
			
			req = Request(imgurl)
			try:
			    response = urlopen(req)
			except HTTPError as e:
			    break
			except URLError as e:
			    break
			else:

			    urlretrieve(imgurl,path_dir+'/%s.jpg' % str(x+1))
			    print(str(x+1))
			    x+=1
			    print('fun02 in working!')
			    # l.config(text='正在下载第%s张图片'% str(x))
			    # window.update_idletasks()
	def fun03():
		x=m*2
		for imgurl in a[m*2:]:
			
			req = Request(imgurl)
			try:
			    response = urlopen(req)
			except HTTPError as e:
			    break
			except URLError as e:
			    break
			else:

			    urlretrieve(imgurl,path_dir+'/%s.jpg' % str(x+1))
			    print(str(x+1))
			    x+=1
			    print('fun03 in working!')
	def fun04():
		while t03.isAlive() or t02.isAlive() or t01.isAlive():
			l.config(text='多线程下载中.\n请稍等')
			window.update_idletasks()
			time.sleep(1)
			l.config(text='多线程下载中..\n请稍等')
			window.update_idletasks()
			time.sleep(1)
			l.config(text='多线程下载中...\n请稍等')
			window.update_idletasks()
			time.sleep(1)		    
	# t01 =threading.Thread(target=fun01)
	# t02 =threading.Thread(target=fun02)
	# t03 =threading.Thread(target=fun03)
	# t04 =threading.Thread(target=fun04)
	# t04.setDaemon(True)
	# t01.start()
	# t02.start()
	# t03.start()
	# t04.start()
	# t01.join()
	t01 =threading.Thread(target=fun01)
	t02 =threading.Thread(target=fun02)
	t03 =threading.Thread(target=fun03)
	t04 =threading.Thread(target=fun04)
	t01.start()
	t02.start()
	t03.start()
	t04.start()
	t01.join()

	
	t02.join()
	t03.join()
	t04.join()
	l.config(text='下载完成 共%d张图片\n已经保存在%s/下' % (len(os.listdir(path_dir)),path_dir))
	window.update_idletasks()
	time.sleep(1)

	# l.config(text='共%d张图片\n已经保存在%s/下' % (x,path_dir))

def func1():
	global t
	t =threading.Thread(target=img_save)
	t.setDaemon(True)#设置线程为后台线程
	t.start()


var_urlfront = StringVar()
var_urlfront.set('https://t1.onvshen.com:85/gallery/21501/23542/002.jpg')
var_path = StringVar()
var_path.set('DonwoadIm0')
Label(window,text='图片URL:').place(x=100,y=60)
Label(window,text='文件夹名称:').place(x=100,y=100)
l=Label(window,bg='#000',fg = 'white',width=31,height = 3,text='输入可迭代的图片URL\n然后点击提交 → → →')
l.place(x=130,y=140)
# l.config(text='输入可迭代的图片URL\n然后点击提交 →')
# time.sleep(0.3)
# window.update_idletasks()
# l.config(text='输入可迭代的图片URL\n然后点击提交 → →')
# time.sleep(0.3)
# window.update_idletasks()
# l.config(text='输入可迭代的图片URL\n然后点击提交 → → →')
# time.sleep(0.3)
# window.update_idletasks()
Entry(window,textvariable = var_urlfront,width = 60).place(x=175,y=60)
Entry(window,textvariable = var_path).place(x=175,y=100)
b=Button(window,text = '提交',command = func1,height=3,width = 8)
b.place(x = 400, y = 140)
window.mainloop()
# https://img.onvshen.com:85/gallery/21501/17266/005.jpg