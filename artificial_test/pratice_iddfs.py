#
import copy
def input_chess():
    chess=[1 ,1, 1, 1, 3, 2, 3, 2, 3, 1, 3, 2, 2, 3, 1, 2, 2, 2, 3, 1, 2, 1, 3, 3,
1, 1, 1, 1, 1, 1 ,1, 1, 2, 2 ,2 ,2 ,2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3]
    return chess
class chess_mode:
    def __init__(self,chess):
        self.af=[chess[0],chess[2],chess[6],chess[11],chess[15],chess[20],chess[22]]
        self.be=[chess[1],chess[3],chess[8],chess[12],chess[17],chess[21],chess[23]]
        self.hc= [chess[4],chess[5],chess[6],chess[7],chess[8],chess[9],chess[10]]
        self.gd=[chess[13],chess[14],chess[15],chess[16],chess[17],chess[18],chess[19]]
        print(len(self.be))
        print(type(self.be))
    def a_move(self):
        temp=self.af.pop(0)
        self.af.append(temp)
        self.hc[2]=self.af[2]
        self.gd[2]=self.af[4]
    def b_move(self):
        temp=self.be.pop(0)
        self.af.append(temp)
        self.hc[4]=self.be[2]
        self.gd[4]=self.be[4]
        print(self.be[4])
    def h_move(self):
        temp=self.hc.pop(0)
        self.hc.append(temp)
        self.af[2]=self.hc[2]
        self.be[2]=self.hc[4]
    def g_move(self):
        temp=self.gd.pop(0)
        self.gd.append(temp)
        self.af[4]=self.gd[2]
        self.be[4]=self.gd[4]
    def f_move(self):
        temp=self.af.pop(-1)
        self.af.insert(0,temp)
        self.hc[2]=self.af[2]
        self.gd[2]=self.af[4]
    def e_move(self):
        temp=self.be.pop(-1)
        self.be.insert(0,temp)
        self.hc[4]=self.be[2]
        self.gd[4]=self.be[4]
    def c_move(self):
        temp=self.hc.pop(-1)
        self.hc.insert(0,temp)
        self.af[2]=self.hc[2]
        self.be[2]=self.hc[4]
    def d_move(self):
        temp=self.gd.pop(-1)
        self.gd.insert(0,temp)
        self.af[4]=self.gd[2]
        self.be[4]=self.gd[4]
    def check(self):
        if self.af[3]==self.be[4]==self.hc[2]==self.hc[3]==self.hc[4]==self.gd[2]==self.gd[3]==self.gd[4] :
            return True
        else:
            return False 
ch_1=input_chess()
step=[]
print('hhhhhhhhhhhhhhhhhhhhhhhhh')
ch=chess_mode(ch_1)
print(ch.be)
long=0
def dfs(dep,maxdep,map):
    if maxdep<=0:
        return False
    if  map.check()==True:
        long=dep
        print('sssssssssssssssssss')
        return True
    for i in range(8):
        step.append('move'+str(i)+'\n')
        print(step)
        print(i)
        if i==0:
            map.a_move()
        if i==1:
            map.b_move()
        if i==2:
            map.c_move()
        if i==3:
            map.d_move()
        if i==4:
            map.e_move()
        if i==5:
            map.f_move()
        if i==6:
            map.g_move()
        if i==7:
            map.h_move()
        if dfs(dep+1,maxdep-1,map)==True:
            return True
        else:
            if i==0:
                map.f_move()
            if i==1:
                map.e_move()
            if i==2:
                map.h_move()
            if i==3:
                map.g_move()
            if i==4:
                map.b_move()
            if i==5:
                map.a_move()
            if i==6:
                map.d_move()
            if i==7:
                map.c_move()
            step.pop()
def IDDFS(ch):
    i=1
    while 1:
        print('xxxxxxxxxxxxxxxxxxxx'+f'{i}')
        isok=dfs(0,i,ch)
        if isok==True:
            return True
        else:
            i+=1
    return True


if IDDFS(ch)==True:
    print(step)
    print(long)