# -*- coding: utf-8 -*-
import sys
import os
import pathlib
import blessed

import re
import time
import numpy 
import datetime
term = blessed.Terminal()
term.hidden_cursor()
tile=(' ','.','$','*','@','+','6','7','#','9','A','B','C','D','E','F','!')
"""
移動関数
0:床 半角空白
1:置き場 .
2:荷物 $
3:置かれた荷物 *
4:床の人 @
5:置き場の人 +
8:壁 #
"""
XMAX=32
YMAX=24
px=0
py=0
name=''
floor=numpy.zeros([XMAX,YMAX],dtype=int)

def chipprint(x,y):
    print(term.move_xy(x*2,y)+tile[floor[x,y]])

def fullprint():
    for x in range(XMAX):
        for y in range(YMAX):
            chipprint(x,y)
def changestartpos():
    for x in range(XMAX):
        for y in range(YMAX):
            if floor[x,y]&4!=0:
                if x!=px or y!=py:
                    floor[x,y]-= floor[x,y]&4
                    chipprint(x,y)
def putchip(key):
    if key==1: # 床か壁
        if floor[px,py]>=8:
            floor[px,py]-=8
        else:
            floor[px,py]+=8
    elif key==2: #置き場
        if int(floor[px,py])&1!=0:
            floor[px,py]-= floor[px,py]&1
        else:
            floor[px,py]|=1
    elif key==3:# 荷物
        if floor[px,py]&2!=0:
            floor[px,py]-= floor[px,py]&2
        else:
            floor[px,py]|=2
    elif key==0:# 人
        changestartpos()
        if floor[px,py]&4!=0:
            floor[px,py]-= floor[px,py]&4
        else:
             floor[px,py]|=4
    if floor[px,py]>=8:
        floor[px,py]=8
    chipprint(px,py)

def walk(x,y):
    global px
    global py
    print(term.move_xy(px*2+1,py)+' ')
    if x<0:
        if px+x>=0:
            px+=x    
    if x>=0:
        if px+x<XMAX:
            px+=x  
    if y<0:
        if py+y>=0:
            py+=y
    if y>=0:
        if py+y<YMAX:
            py+=y
    print(term.move_xy(px*2+1,py)+'<')

def getch():
    with term.cbreak():
        val = ''
        while val=='':
            val = term.inkey(timeout=0.1)
        
    return val
def save(names):
    xmax=getxmax()
    ymax=getymax()
    newfile =names  if names!='' else str(datetime.datetime.now())
    newfile=re.sub('\:|\.','',newfile)
    newfile=re.sub(' ','_',newfile)
    print('ファイル名：'+newfile+'.datlevel')
    s=str(xmax).zfill(2)+str(ymax).zfill(2)+'|'
    for y in range(ymax):
        s+='\n'
        for x in range(xmax):
            s+=str(floor[x,y])
    s+='|'
    f=open(newfile+'.datlevel','w',encoding='utf=8')
    f.write(s)
    f.close()

def getxmax():
	rm=0
	x=XMAX-1
	while x>=0:
		for y in range(YMAX):
			if floor[x,y]>0:
				rm=x
				break
		if rm>0:
			break
		x-=1
	return rm+1
def getymax():
	cm=0
	y=YMAX-1
	while y>=0:
		for x in range(XMAX):
			if floor[x,y]>0:
				cm=y
				break
		if cm>0:
			break
		y-=1
	return cm+1

def joined(p):
    if os.path.exists(p)==False:
        return
    merged=pathlib.Path(p)
    os.chdir(p)
    print(p)
    
    files=list(merged.glob('*.datlevel'))

    result=''
    filename=''

    for i in range(len(files)):
        filename=os.path.basename(str(files[i]))
        with open(filename,'r',encoding='utf-8') as fp:
            result+=fp.read()+'\n'
    with open('stage.cr','w',encoding='utf-8') as fp:
        fp.write(result)
    sys.exit()

def main():
    global name
    global floor
    jpath=os.getcwd()
    while input('ファイルの結合作業を行いますか？yを押すと結合を行います')=='y':
        jpath==input('ディレクトリを指定してください 現在>'+jpath)
        joined(jpath)

    name=input('読み取るファイルを指定してください(拡張子不要　enter・エラーで新規)')
    try:
        f=open(name+'.datlevel','r',encoding='utf-8')
        words = f.read()
        f.close()
        words=re.sub('[^0123456789\|]','',words)
        words=words.split('|')
        xy=words[0]
        xmax=int(xy[0:2])
        ymax=int(xy[2:4])
        tiles=words[1]
        for x in range(xmax):
            for y in range(ymax):
                floor[x,y]=tiles[x+y*xmax]
    except:
        pass
    
    print(term.enter_fullscreen+term.clear_eol)
    fullprint()
    print(term.move_xy(1,0)+'<')
    print(term.move_xy(36,7)+'CARRIER-EDITOR (c)2021-')
    print(term.move_xy(36,8)+'by grurqApps')
    print(term.move_xy(36,10)+'操作')
    print(term.move_xy(36,11)+'↑→↓←:移動')
    print(term.move_xy(36,12)+'1:壁')
    print(term.move_xy(36,13)+'2:置き場')
    print(term.move_xy(36,14)+'3:荷物')
    print(term.move_xy(36,16)+'ESC:終了')

    while 1:
        keypress=getch()
        if keypress.name=='KEY_ESCAPE':
            print(term.exit_fullscreen+term.move_xy(0,0)+term.clear())
            print(term.move_xy(0,0)+'保存してこのアプリを終了します')
            save(name)
            getch()
            return 0
        elif keypress.name=='KEY_UP':
            walk(0,-1)
        elif keypress.name=='KEY_RIGHT':
            walk(1,0)
        elif keypress.name=='KEY_DOWN':
            walk(0,1)
        elif keypress.name=='KEY_LEFT':
            walk(-1,0)
        elif keypress.is_sequence==False:
            if keypress=='1':
                putchip(1)
            elif keypress=='2':
                putchip(2)
            elif keypress=='3':
                putchip(3)
            elif keypress=='0':
                putchip(0)
    input('test')
    return 0

if __name__ == '__main__':
    main()
"""

# 日誌
2021-04-09
例外が発生しました: FileNotFoundError
[Errno 2] No such file or directory: ']'

2021-04-08
pathlibを使ってみたがうまく行ってない。
D&Dは認識しているのでファイル操作の問題。
2021-04-06
結合モードはドラッグアンドドロップにする。
ファイル呼び出しを修復。
"""