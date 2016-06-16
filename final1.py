#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pyglet 
import mp3play
import time
import random
from pyglet.window import mouse 
from pyglet.window import key
import speech_recognition as sr
import  sys 
reload ( sys ) 
sys . setdefaultencoding ( 'utf-8' )
filename = r'C:\Python27\bomb.mp3'
clip = mp3play.load(filename)
filename1 = r'C:\Python27\kiss2.mp3'
clip1 = mp3play.load(filename1)
game_window=pyglet.window.Window(1200,700)
#main_batch = pyglet.graphics.Batch()   
lable=pyglet.text.Label('Lets go',font_name='Times New Roman',font_size=36,x=game_window.width/2
    ,y=game_window.height/2,anchor_x='center',anchor_y='center')

nick=pyglet.image.load('n.png')  
hanwei=pyglet.image.load('h.png')
bo=pyglet.image.load('bo.png')
#wang=pyglet.image.load('w.png')
final=pyglet.sprite.Sprite(img=hanwei,x=1050,y=500);
final.scale=0.5
start=pyglet.sprite.Sprite(img=nick,x=-50,y=-250);

keys = key.KeyStateHandler()  #獲取按键狀態 
game_window.push_handlers(keys)  #按鍵

w_lives=[]  
for i in range(15):  
    rand_x=random.randrange(0,1200,1)  
  
    new_sprite=pyglet.sprite.Sprite(img=bo,x=rand_x,y=700)  
    new_sprite.scale=0.8   
    w_lives.append(new_sprite)  
      
 
def check_bounds(self):  
    if self.y<-300:  
        rand_x=random.randrange(-200,200,10)    
        self.x+=rand_x  
        if self.x<0:  
            self.x=0  
        elif self.x>1200:  
            self.x=1200      
        self.y=700  


@game_window.event   #讓窗口知道這個事件
def on_draw():  
    game_window.clear()  
    lable.draw()   
    final.draw()     
    start.draw()
    for live in w_lives:  #掉落的
        live.draw()

@game_window.event  
def on_mouse_press(x,y,button,modif):  
    if button==mouse.LEFT:  
        print u'現在位置'  
  
    elif button==mouse.RIGHT:  
        print u'現在位置'  
    print x  
    print y
def update(dt):
    if keys[key.LEFT]:  
        start.x-=10 
    elif keys[key.RIGHT]:  
        start.x+=10    
    elif keys[key.UP]:  
        start.y+=10  
    elif keys[key.DOWN]:  
        start.y-=10

    if 500<start.x<650 and -350<start.y<-100 :
        start.x=-50
        start.y=-250
        clip.play()
        time.sleep(min(30, clip.seconds()))
        clip.stop()
        print "bomb1"
        
            
    elif 150<start.x<300 and -100<start.y<80 :
        start.x=-50
        start.y=-250
        clip.play()
        time.sleep(min(30, clip.seconds()))
        clip.stop()
        print "bomb2"
            
    elif 150<start.x<300 and 150<start.y<300:
        start.x=-50
        start.y=-250
        clip.play()
        time.sleep(min(30, clip.seconds()))
        clip.stop()
        print "bomb3"
            
    elif 650<start.x<850 and 30<start.y<200:
        start.x=-50
        start.y=-250
        clip.play()
        time.sleep(min(30, clip.seconds()))
        clip.stop()
        print "bomb4"
    elif 400<start.x<500 and 30<start.y<100:
        start.x=-50
        start.y=-250
        clip.play()
        time.sleep(min(30, clip.seconds()))
        clip.stop()
        print "bomb5"
    elif 900<start.x<1200 and -50<start.y<100:
        start.x=-50
        start.y=-250
        clip.play()
        time.sleep(min(30, clip.seconds()))
        clip.stop()
        print "bomb6"
    elif 950<start.x<1500 and 150<start.y<350:
    
        print "WIN"
        clip1.play()
        time.sleep(min(30, clip1.seconds()))
        clip1.stop()
        exit()
    for live in w_lives:
            rand_y=random.randrange(30)  #咚咚往下掉的速度
            live.y-=rand_y  
            check_bounds(live)  #看有沒有出借

    if start.y>300:  
        start.y=300  
    elif start.y<-300:  
        start.y=-300 
      
    if start.x>1000:  
        start.x=1000  
    elif start.x<0:  
        start.x=0     
pyglet.clock.schedule_interval(update, 1/100.0)   

live=3
while live>0:
	r = sr.Recognizer()
	sr.energy_threshold = 4000
	with sr.Microphone() as source:
		audio = r.listen(source)
	try:
		print("You said " + r.recognize_google(audio,language="zh_TW"))
	except sr.UnknownValueError:
		print("Could not understand audio")
	word=r.recognize_google(audio,language="zh_TW")

	if word==u"遊戲開始":
		print u"開始囉"
		pyglet.app.run()
		
	live-=1
print u"遊戲結束"