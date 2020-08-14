import pyscreenshot as ImageGrab
from PIL import ImageOps
from PIL import Image 
import pyautogui as pg
import time
from numpy import *
import numpy as np
fil=open("dino_image_data.csv",'a')
col_name=[]
rnd=0
for rnd in range(0,45):
	col_name.append("prameter-"+str(rnd))
#print(col_name)
#fil.write(str(col_name))
def imageGrab():
	global n
	global xI
	global xII  
	n=n+1 
	box1 = (xI,273,xII,318)# 

	image1 = ImageGrab.grab(box1)
	grayImage =  ImageOps.grayscale(image1)
	validity = array(grayImage.getcolors())
	check_validity=validity.sum()
	
	data = np.asarray(grayImage)
	flatten_dataa=data
	#flatten_data = data.reshape(1,2025)
	#flatten_dataa = flatten_data.tolist()#add commas
	if(check_validity>=10000):	
		print(check_validity)
		print(n)

		np.savetxt(fil, flatten_dataa, delimiter=",")
		print(flatten_dataa)
		print(flatten_dataa.shape)		
		image1.save(str(n)+"im.png")
		image1.close()
		time.sleep(0.2)

	xI=xI+45
	xII=xII+45      

n=0    
numm=1
time.sleep(3)
print("===set===")
while(numm<=143):
	xI=475
	xII=520 
	while(xII<=1020):
		imageGrab()
	numm=numm+1
	#pg.press('right')   # press the left arrow key
	print(numm,"===Change===")	
	exit()
fil.close()
print("===END===") 
