#coding : utf-8
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import numpy as np
import random
import sys
import string

def drawPoint(draw,num):
	for i in range(0,num):
		length = random.randint(0,5)
		curX = random.uniform(0,96)
		curY = random.uniform(0,25)
		lineList = [(curX,curY)]
		for j in range(0,length):
			curX = min(curX+random.uniform(0,0.96),96)
			curY = min(curY+random.uniform(0,0.25),25)
			lineList.append((curX,curY))
		draw.line(lineList,fill=(10,10,10),width=1)	
def drawLine(draw,num):
	for i in range(0,num):
		length = random.randint(150,200)
		curX = random.uniform(0,96)
		curY = random.uniform(0,25)
		lineList = [(curX,curY)]
		for j in range(0,length):
			curX = min(curX+random.uniform(1.25,4.8),96)
			curY = min(curY+random.uniform(1.25,4.8),25)
			lineList.append((curX,curY))
		draw.line(lineList,fill=(10,10,10),width=1)
	

def drawNoise(draw):
	drawPoint(draw,80)
	drawLine(draw,5)

def drawPicture(name):
	img = Image.new("RGB",(96,25),(255,255,255))
	draw = ImageDraw.Draw(img)
	font = ImageFont.truetype("LBRITED.TTF", 20)
	draw.text((10, 0),name,(10,10,10),font=font)
	drawNoise(draw)
	img.save('.\pic\\'+name+'.jpg')

def genPicture():
	name = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(6))
	img = Image.new("RGB",(96,25),(255,255,255))
	draw = ImageDraw.Draw(img)
	font = ImageFont.truetype("LBRITED.TTF", 20)
	draw.text((10, 0),name,(10,10,10),font=font)
	drawNoise(draw)
	return (name,np.array(img))

def drawPictures():
	for _ in range(1000):
		drawPicture(''.join(random.choice(string.ascii_letters + string.digits) for _ in range(6)))
drawPictures()
