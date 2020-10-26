import time
global times, tot
tot = 0
times = 1

class Cell:
    def __init__(self, pos):
        self.pos = pos
        self.rad = 10
        self.alanine = 0
        self.state = 0
        self.still = True
        
    def draws(self):
        global times, tot
        self.alanize()
        if times == 1:
            if dist(mouseX, mouseY, self.pos[1]*self.rad*4+self.alanine, self.pos[0]*self.rad*4+100) <= self.rad*2:
                fill(255,100,0)
                if mousePressed:
                    if self.still:
                        if self.state == 0:
                            tot += 1
                            self.state = 1
                        else:
                            tot -= 1
                            self.state = 0
                        self.still = False
                elif self.still == False:
                    self.still = True
            else: fill(255)
        if self.state == 1:
            fill(255,0,0)
        elif times != 1: fill(255)
        stroke(0)
        self.polygon(self.pos[1]*self.rad*4+self.alanine, self.pos[0]*self.rad*4+100,self.rad)
        
    def polygon(self, x, y, rad):
        angle = PI/3
        beginShape()
        a=0
        while a < PI*2:
            sx = x + cos(a+PI/6)*25
            sy = y + sin(a+PI/6)*25
            vertex(sx, sy)
            a += angle
        endShape(CLOSE)
        
    def alanize(self):
        self.alanine = width/2-self.rad*2*(9-abs(self.pos[0]-4))+self.rad*2

'''
0     0 1 2 3 4
1    0 1 2 3 4 5
2   0 1 2 3 4 5 6
3  0 1 2 3 4 5 6 7
4 0 1 2 3 4 5 6 7 8
5  0 1 2 3 4 5 6 7
6   0 1 2 3 4 5 6
7    0 1 2 3 4 5
8     0 1 2 3 4
'''

def counting(g, p):
    c = 0
    if p[0] < 4:
        if p[0] > 0 and p[1] > 0:
            if g[p[0]-1][p[1]-1] == 1: c += 1
        if p[0] > 0 and p[1] < len(g[p[0]])-1:
            if g[p[0]-1][p[1]] == 1: c += 1
        if g[p[0]+1][p[1]] == 1: c += 1
        if g[p[0]+1][p[1]+1] == 1: c += 1
    if p[0] == 4:
        if p[1] > 0:
            if g[p[0]-1][p[1]-1] == 1: c += 1
        if p[1] < len(g[p[0]])-1:
            if g[p[0]-1][p[1]] == 1: c += 1
        if p[1] > 0:
            if g[p[0]+1][p[1]-1] == 1: c += 1
        if p[1] < len(g[p[0]])-1:
            if g[p[0]+1][p[1]] == 1: c += 1
    if p[0] > 4:
        if g[p[0]-1][p[1]] == 1: c += 1
        if g[p[0]-1][p[1]+1] == 1: c += 1
        if p[0] < 8 and p[1] > 0:
            if g[p[0]+1][p[1]-1] == 1: c += 1
        if p[0] < 8 and p[1] < len(g[p[0]])-1:
            if g[p[0]+1][p[1]] == 1: c += 1
    if p[1] > 0:
        if g[p[0]][p[1]-1] == 1: c += 1
    if p[1] < len(g[p[0]])-1:
        if g[p[0]][p[1]+1] == 1: c += 1
    return c
def setup():
    global cells, testing
    testing = 0
    size(600,600)
    background(240,255,240)
    cells = []
    for row in range(9):
        amt = 9-abs(row-4)
        for col in range(amt):
            cells.append(Cell([row,col]))
    
def draw():
    global cells, testing, times, done
    done = False
    for cell in cells:
        cell.draws()
    if times == 0:
        done = True
        grid = []
        for cell in cells:
            if cell.pos[1]==0:
                grid.append([])
            grid[-1].append(cell.state)
        for cell in range(len(cells)):
            bell = cells[cell]
            prevstate = bell.state
            count = counting(grid, bell.pos)
            if count >= 3:
                bell.state = 1
                if prevstate == 0: done = False
        time.sleep(0.5)
        if done: times = 2
    rectMode(CORNERS)
    fill(240,255,240)
    stroke(240,255,240)
    rect(0,452,width,height)
    textAlign(CENTER)
    fill(0)
    textSize(32)
    text("Total bees: " + str(tot), width/2, 475)
    if times == 1:
        fill(255,240,240)
        stroke(0)
        rect(220,500,380,540)
        fill(0)
        text("START", 300, 530)
        if mousePressed and mouseX >= 220 and mouseX <= 380 and mouseY >= 500 and mouseY <= 540:
            times = 0
