#!/usr/bin/env python3
"""Generate original pixel-art sprites for Shinobi Bros (Naruto-concept, Mario-style).
All art is drawn here from scratch - no copyrighted assets."""
from PIL import Image
import os

os.makedirs('sprites', exist_ok=True)

def newimg(w, h):
    return Image.new('RGBA', (w, h), (0, 0, 0, 0))

def px(im, x, y, c):
    if 0 <= x < im.width and 0 <= y < im.height:
        im.putpixel((x, y), c)

def rect(im, x, y, w, h, c):
    for yy in range(y, y+h):
        for xx in range(x, x+w):
            px(im, xx, yy, c)

# ---------------- palette ----------------
SKIN   = (244, 196, 140, 255)
SKIN_D = (214, 160, 105, 255)
HAIR   = (255, 210, 63, 255)
HAIR_D = (224, 170, 30, 255)
ORANGE = (255, 122, 26, 255)
ORANGE_D=(214, 92, 10, 255)
BLUE   = (43, 80, 200, 255)
BLUE_D = (28, 52, 140, 255)
BAND   = (58, 63, 74, 255)
METAL  = (192, 200, 216, 255)
METAL_D=(140, 148, 165, 255)
BLACK  = (20, 22, 30, 255)
WHITE  = (255, 255, 255, 255)
SAGE_R = (235, 60, 45, 255)
AURA   = (255, 170, 40, 255)

T = (0,0,0,0)

# =========================================================
# TILES  16x16 grid, 16 cols x 4 rows  (256x64)
# =========================================================
tiles = newimg(256, 64)
TW = 16

def tile_base(idx, c):
    x0 = (idx % 16) * TW; y0 = (idx // 16) * TW
    rect(tiles, x0, y0, TW, TW, c)
    return x0, y0

# 1 ground_top (grass over dirt)
x0,y0 = tile_base(1, (146, 90, 44, 255))
rect(tiles,x0,y0,16,4,(86,176,84,255))
rect(tiles,x0,y0+4,16,1,(66,146,66,255))
for i in range(0,16,2):
    px(tiles,x0+i,y0+3,(66,146,66,255))
# dirt speckles
import random; random.seed(7)
for _ in range(18):
    px(tiles,x0+random.randint(0,15),y0+5+random.randint(0,10),(120,72,34,255))

# 2 ground fill
x0,y0 = tile_base(2, (146, 90, 44, 255))
for _ in range(22):
    px(tiles,x0+random.randint(0,15),y0+random.randint(0,15),(120,72,34,255))
for _ in range(6):
    px(tiles,x0+random.randint(0,15),y0+random.randint(0,15),(170,112,60,255))

# 3 brick
x0,y0 = tile_base(3, (196, 96, 44, 255))
rect(tiles,x0,y0,16,1,(140,60,26,255)); rect(tiles,x0,y0+8,16,1,(140,60,26,255))
rect(tiles,x0+7,y0+1,1,7,(140,60,26,255)); rect(tiles,x0+3,y0+9,1,7,(140,60,26,255)); rect(tiles,x0+11,y0+9,1,7,(140,60,26,255))
rect(tiles,x0,y0+15,16,1,(120,50,20,255))
for xx in range(16): px(tiles,x0+xx,y0+1,(220,120,60,255))

# 4,5,6 question block frames (chakra '?')
def qblock(idx, bright):
    x0,y0 = tile_base(idx, (255,196,60,255))
    frame=[(x0,y0),(x0+15,y0),(x0,y0+15),(x0+15,y0+15)]
    rect(tiles,x0,y0,16,1,(190,120,20,255)); rect(tiles,x0,y0+15,16,1,(190,120,20,255))
    rect(tiles,x0,y0,1,16,(190,120,20,255)); rect(tiles,x0+15,y0,1,16,(190,120,20,255))
    for fx,fy in frame: px(tiles,fx,fy,(90,55,10,255))
    qc = (255,255,255,255) if bright else (235,220,170,255)
    rect(tiles,x0+5,y0+3,6,2,qc); rect(tiles,x0+10,y0+5,2,3,qc)
    rect(tiles,x0+7,y0+8,3,2,qc); rect(tiles,x0+7,y0+12,3,3,qc)
    px(tiles,x0+4,y0+4,qc)
qblock(4, True); qblock(5, False); qblock(6, True)

# 7 used block
x0,y0 = tile_base(7, (160,110,50,255))
rect(tiles,x0,y0,16,1,(120,80,35,255)); rect(tiles,x0,y0+15,16,1,(120,80,35,255))
rect(tiles,x0,y0,1,16,(120,80,35,255)); rect(tiles,x0+15,y0,1,16,(120,80,35,255))
for fx,fy in [(x0,y0),(x0+15,y0),(x0,y0+15),(x0+15,y0+15)]: px(tiles,fx,fy,(90,60,25,255))

# 8 solid block (stone)
x0,y0 = tile_base(8, (176,160,140,255))
rect(tiles,x0,y0,16,2,(210,196,176,255))
rect(tiles,x0,y0+14,16,2,(140,124,104,255))
rect(tiles,x0,y0,2,16,(210,196,176,255)); rect(tiles,x0+14,y0,2,16,(140,124,104,255))

# 9-12 pipe: tl, tr, l, r  (bamboo-green ninja pipe)
PG=(64,190,84,255); PGD=(34,120,50,255); PGL=(140,235,150,255)
x0,y0 = tile_base(9, PG);  # top-left
rect(tiles,x0,y0,16,3,PGL); rect(tiles,x0,y0+15,16,1,PGD); rect(tiles,x0,y0,1,16,PGD)
rect(tiles,x0+13,y0+3,3,12,PGD)
x0,y0 = tile_base(10, PG); # top-right
rect(tiles,x0,y0,16,3,PGL); rect(tiles,x0,y0+15,16,1,PGD); rect(tiles,x0+15,y0,1,16,PGD)
rect(tiles,x0+2,y0+3,3,12,PGD)
x0,y0 = tile_base(11, PG); # body-left
rect(tiles,x0,y0,1,16,PGD); rect(tiles,x0+13,y0,3,16,PGD); rect(tiles,x0+1,y0,3,16,PGL)
x0,y0 = tile_base(12, PG); # body-right
rect(tiles,x0+15,y0,1,16,PGD); rect(tiles,x0+2,y0,3,16,PGD)

# 13 stairs block (rock)
x0,y0 = tile_base(13, (150,140,160,255))
rect(tiles,x0,y0,16,1,(110,100,125,255)); rect(tiles,x0,y0+15,16,1,(110,100,125,255))
rect(tiles,x0,y0,1,16,(110,100,125,255)); rect(tiles,x0+15,y0,1,16,(110,100,125,255))
px(tiles,x0+7,y0+7,(110,100,125,255)); px(tiles,x0+8,y0+8,(110,100,125,255))
rect(tiles,x0+1,y0+1,14,1,(185,176,200,255))

# 14-15 cloud left/right, 19 mid  (soft white)
CW=(250,250,255,255); CWS=(214,224,240,255)
x0,y0 = tile_base(14, T)
rect(tiles,x0+4,y0+6,12,6,CW); rect(tiles,x0+6,y0+4,8,2,CW)
rect(tiles,x0+4,y0+12,12,2,CWS)
x0,y0 = tile_base(15, T)
rect(tiles,x0,y0+6,12,6,CW); rect(tiles,x0+2,y0+4,8,2,CW)
rect(tiles,x0,y0+12,12,2,CWS)
x0,y0 = tile_base(19, T)
rect(tiles,x0,y0+6,16,6,CW); rect(tiles,x0,y0+12,16,2,CWS)

# 16 grass deco (tuft on transparent, drawn over ground)
x0,y0 = tile_base(16, T)
for i,h in [(3,5),(6,7),(9,6),(12,4)]:
    rect(tiles,x0+i,y0+13-h,2,h,(86,176,84,255))
    px(tiles,x0+i,y0+13-h-1,(120,210,120,255))

# 17 flag pole
x0,y0 = tile_base(17, T)
rect(tiles,x0+7,y0,2,16,(200,205,215,255))
rect(tiles,x0+8,y0,1,16,(150,155,168,255))
# 18 flag (orange Konoha-leaf style pennant, original swirl)
x0,y0 = tile_base(18, T)
rect(tiles,x0+8,y0+2,2,14,(200,205,215,255))
for i in range(9):
    rect(tiles,x0+9,y0+2+i,8-i//2,1,(255,122,26,255))
px(tiles,x0+11,y0+4,WHITE); px(tiles,x0+12,y0+5,WHITE)
# 20 pole top ball
x0,y0 = tile_base(20, T)
rect(tiles,x0+5,y0+5,6,6,(255,210,63,255))
rect(tiles,x0+6,y0+4,4,8,(255,210,63,255)); rect(tiles,x0+4,y0+6,8,4,(255,210,63,255))
px(tiles,x0+6,y0+6,(255,240,180,255))

# 21 night star deco
x0,y0 = tile_base(21, T)
px(tiles,x0+4,y0+4,WHITE); px(tiles,x0+11,y0+8,(255,255,200,255)); px(tiles,x0+7,y0+12,WHITE)

tiles.save('sprites/tiles.png')

# =========================================================
# HERO  frames 16x24, 11 per row; row0 normal, row1 sage
# cols: 0 idle1,1 idle2, 2-5 run1-4, 6 jump, 7 fall, 8 throw1, 9 throw2, 10 dead
# =========================================================
FW, FH = 16, 24
hero = newimg(FW*11, FH*2)

def draw_ninja(ox, oy, pose, sage=False):
    hair = HAIR if not sage else (255,190,70,255)
    jacket = ORANGE if not sage else SAGE_R
    jdark = ORANGE_D if not sage else (180,40,30,255)
    def P(x,y,c): px(hero, ox+x, oy+y, c)
    def R(x,y,w,h,c): rect(hero, ox+x, oy+y, w, h, c)
    # aura for sage
    if sage:
        for x,y in [(3,1),(12,2),(2,8),(13,9),(3,16),(12,17),(1,12),(14,5)]:
            P(x,y,AURA)
    # hair spikes
    R(4,0,8,3,hair)
    for sx,sy in [(3,1),(5,-0),(7,0),(9,0),(11,1),(12,2),(2,3)]:
        P(sx,sy+1,hair)
    R(3,3,10,2,hair)
    R(2,4,2,3,hair); R(12,4,2,3,hair)
    # headband
    R(3,5,10,2,BAND); R(4,5,8,1,METAL)
    P(7,5,METAL_D); P(8,5,METAL_D)  # plate swirl notch
    # face
    R(4,7,8,4,SKIN)
    # eyes
    ec = (55,110,220,255)
    P(6,8,ec); P(9,8,ec)
    P(6,9,BLACK); P(9,9,BLACK)
    # whisker marks
    P(4,9,SKIN_D); P(4,10,SKIN_D); P(11,9,SKIN_D); P(11,10,SKIN_D)
    # mouth
    if pose=='dead':
        P(6,8,BLACK); P(9,8,BLACK)
    # body (jacket)
    R(4,11,8,5,jacket)
    R(4,11,8,1,jdark)         # collar
    R(7,11,2,5,jdark)         # zipper
    P(5,13,WHITE);            # swirl patch
    # arms per pose
    if pose in ('idle1','idle2'):
        R(2,11,2,5,jacket); R(12,11,2,5,jacket)
        R(2,15,2,2,SKIN); R(12,15,2,2,SKIN)
    elif pose in ('run1','run3'):
        R(1,11,2,4,jacket); R(13,12,2,4,jacket)
        R(1,15,2,2,SKIN); R(13,16,2,2,SKIN)
    elif pose in ('run2','run4'):
        R(2,11,2,5,jacket); R(12,11,2,5,jacket)
        R(3,15,2,2,SKIN); R(11,15,2,2,SKIN)
    elif pose=='jump' or pose=='fall':
        R(1,9,2,4,jacket); R(13,9,2,4,jacket)
        R(1,8,2,2,SKIN); R(13,8,2,2,SKIN)
    elif pose=='throw1':
        R(2,11,2,4,jacket); R(11,10,4,2,jacket)
        R(14,9,2,2,SKIN)
    elif pose=='throw2':
        R(2,11,2,4,jacket); R(11,12,4,2,jacket)
        R(14,12,2,2,SKIN)
    else:
        R(2,11,2,5,jacket); R(12,11,2,5,jacket)
    # legs per pose
    pants = BLUE
    if pose in ('idle1','idle2'):
        R(4,16,3,5,pants); R(9,16,3,5,pants)
        R(3,21,4,2,BLUE_D); R(9,21,4,2,BLUE_D)   # sandals/ankle
        R(3,23,4,1,BLACK); R(9,23,4,1,BLACK)
    elif pose=='run1':
        R(3,16,3,4,pants); R(10,16,3,3,pants)
        R(2,20,4,2,pants); R(10,19,4,2,pants)
        R(2,22,4,1,BLACK); R(11,21,3,1,BLACK)
    elif pose=='run2':
        R(5,16,6,3,pants)
        R(4,19,3,3,pants); R(9,19,3,3,pants)
        R(4,22,3,1,BLACK); R(9,22,3,1,BLACK)
    elif pose=='run3':
        R(4,16,3,3,pants); R(9,16,3,4,pants)
        R(2,19,4,2,pants); R(10,20,4,2,pants)
        R(2,21,3,1,BLACK); R(10,22,4,1,BLACK)
    elif pose=='run4':
        R(5,16,6,3,pants)
        R(4,19,3,3,pants); R(9,19,3,3,pants)
        R(4,22,3,1,BLACK); R(9,22,3,1,BLACK)
    elif pose=='jump':
        R(3,16,3,4,pants); R(10,16,3,3,pants)
        R(3,20,3,2,BLACK); R(10,19,3,2,BLACK)
    elif pose=='fall':
        R(4,16,3,4,pants); R(9,16,3,4,pants)
        R(4,20,3,2,BLACK); R(9,20,3,2,BLACK)
    elif pose=='dead':
        R(4,16,8,3,pants); R(4,19,8,2,BLACK)
    else:
        R(4,16,3,5,pants); R(9,16,3,5,pants)
        R(3,21,4,2,BLUE_D); R(9,21,4,2,BLUE_D)
    # idle2 blink
    if pose=='idle2':
        R(4,7,8,4,SKIN)
        R(5,8,2,1,BLACK); R(9,8,2,1,BLACK)
        P(4,9,SKIN_D); P(11,9,SKIN_D)

poses = ['idle1','idle2','run1','run2','run3','run4','jump','fall','throw1','throw2','dead']
for i,p in enumerate(poses):
    draw_ninja(i*FW, 0, p, sage=False)
    draw_ninja(i*FW, FH, p, sage=True)
hero.save('sprites/hero.png')

# =========================================================
# ENEMIES 16x16: row0 rogue ninja (walk1, walk2, squashed), row1 spiky (2 frames)
# =========================================================
en = newimg(48, 32)
def walker(ox, step):
    def P(x,y,c): px(en, ox+x, y, c)
    def R(x,y,w,h,c): rect(en, ox+x, y, w, h, c)
    cloak=(70,72,88,255); hood=(52,54,68,255); cloud=(200,60,60,255)
    R(3,3,10,9,cloak)                    # body cloak
    R(4,1,8,4,hood)                      # hood
    R(5,3,6,2,SKIN)                      # face slit
    P(6,4,(220,50,50,255)); P(9,4,(220,50,50,255))  # red eyes
    P(5,8,cloud); P(10,7,cloud)          # red clouds (Akatsuki-ish, original)
    if step==0:
        R(4,12,3,3,hood); R(9,12,3,3,hood)
    else:
        R(3,12,3,3,hood); R(10,12,3,3,hood)
walker(0,0); walker(16,1)
def squashed(ox):
    def R(x,y,w,h,c): rect(en, ox+x, y, w, h, c)
    R(2,11,12,4,(70,72,88,255)); R(4,9,8,2,(52,54,68,255))
    R(5,12,2,1,(220,50,50,255)); R(9,12,2,1,(220,50,50,255))
squashed(32)
def spiky(ox, step):
    def P(x,y,c): px(en, ox+x, 16+y, c)
    def R(x,y,w,h,c): rect(en, ox+x, 16+y, w, h, c)
    shell=(40,90,60,255); spike=(230,235,240,255)
    R(3,5,10,8,shell)
    for sx in [4,7,10,12]:
        P(sx,3,spike); P(sx,4,spike)
    R(4,9,2,2,(20,22,30,255)); R(10,9,2,2,(20,22,30,255))
    if step==0: R(4,13,3,2,(30,60,40,255)); R(9,13,3,2,(30,60,40,255))
    else: R(3,13,3,2,(30,60,40,255)); R(10,13,3,2,(30,60,40,255))
spiky(0,0); spiky(16,1)
en.save('sprites/enemies.png')

# =========================================================
# ITEMS 16x16: row0 coin x4, row1 scroll, ramen, rasengan x4 (12px drawn in 16)
# =========================================================
it = newimg(64, 48)
def coin(ox, w):
    def R(x,y,ww,h,c): rect(it, ox+x, y, ww, h, c)
    cx=8
    R(cx-w//2,3,w,10,(255,205,55,255))
    R(cx-w//2+1,4,max(1,w-2),8,(255,235,150,255))
    R(cx-w//2,5,1,6,(190,140,30,255)); R(cx+w//2-1,5,1,6,(190,140,30,255))
coin(0,10); coin(16,6); coin(32,3); coin(48,6)
def scroll(ox,oy):
    def R(x,y,w,h,c): rect(it, ox+x, oy+y, w, h, c)
    R(3,4,10,9,(240,230,200,255)); R(3,4,10,2,(200,120,50,255)); R(3,11,10,2,(200,120,50,255))
    R(5,7,6,1,(150,80,60,255)); R(5,9,4,1,(150,80,60,255))
    R(2,3,2,11,(160,80,40,255)); R(12,3,2,11,(160,80,40,255))
scroll(0,16)
def ramen(ox,oy):
    def R(x,y,w,h,c): rect(it, ox+x, oy+y, w, h, c)
    R(3,6,10,6,(235,90,90,255)); R(2,7,12,3,(255,255,255,255))
    R(4,3,8,3,(255,225,150,255)); R(6,2,1,2,(255,225,150,255)); R(9,2,1,2,(255,225,150,255))
    R(11,1,1,6,(190,140,90,255))
ramen(16,16)
def rasengan(ox,oy,rot):
    cx,cy=ox+8,oy+8
    for dy in range(-5,6):
        for dx in range(-5,6):
            d=(dx*dx+dy*dy)**0.5
            if d<=4.6:
                if d<2: c=(240,255,255,255)
                elif d<3.5: c=(140,220,255,255)
                else: c=(70,160,255,255)
                px(it,cx+dx,cy+dy,c)
    import math
    for k in range(6):
        a=rot+k*1.05; r=4.5
        px(it,int(cx+math.cos(a)*r),int(cy+math.sin(a)*r),(255,255,255,255))
rasengan(32,16,0); rasengan(48,16,1.5)
it.save('sprites/items.png')
print("sprites generated:", os.listdir('sprites'))
