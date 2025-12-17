import tkiteasy as tk
lk=[[["R1"],[1],[1],[1],[1], [],[],[],[],[], [2],[2],[2],[2],["R2"],]
    [[1],[1],[1],[1],[1], [],[],[],[],[], [2],[2],[2],[2],[2],],
    [[1],[1],[1],[1],[1], [],[],[],[],[], [2],[2],[2],[2],[2],],
    [[1],[1],[1],[1],[1], [],[],[],[],[], [2],[2],[2],[2],[2],],
    [[1],[1],[1],[1],[1], [],[],[],[],[], [2],[2],[2],[2],[2],],
    [[ ],[ ],[ ],[ ],[ ], [],[],[],[],[], [ ],[ ],[ ],[ ],[ ],],
    [[ ],[ ],[ ],[ ],[ ], [],[],[],[],[], [ ],[ ],[ ],[ ],[ ],],
    [[ ],[ ],[ ],[ ],[ ], [],[],[],[],[], [ ],[ ],[ ],[ ],[ ],],
    [[ ],[ ],[ ],[ ],[ ], [],[],[],[],[], [ ],[ ],[ ],[ ],[ ],],
    [[ ],[ ],[ ],[ ],[ ], [],[],[],[],[], [ ],[ ],[ ],[ ],[ ],],
    [[3],[3],[3],[3],[3], [],[],[],[],[], [4],[4],[4],[4],[4],],
    [[3],[3],[3],[3],[3], [],[],[],[],[], [4],[4],[4],[4],[4],],
    [[3],[3],[3],[3],[3], [],[],[],[],[], [4],[4],[4],[4],[4],],
    [[3],[3],[3],[3],[3], [],[],[],[],[], [4],[4],[4],[4],[4],],
    [["R3"],[3],[3],[3],[3], [],[],[],[],[], [4],[4],[4],[4],["R4"],]]

class Ruche:
    def __init__(self,posx:int,posy:int,nbplay:int,qte_nec:int):
        self.posx=posx
        self.posy=posy
        self.nbplay=nbplay
        self.qte_nec=qte_nec
    
    def ponte_abeille(self,type:int,cout:int):
        r=abeille(self.x ,self.y,type,self.nbplay)
        self.qte_nec-=cout
        return r, self.qte_nec
    



class Fleur:
    def __init__(self,fx:int,fy:int,qte_nec:int):
        self.fx=fx
        self.fy=fy
        self.qte_nec=qte_nec

    def retire_nec(self,pren:int):
        self.qte_nec-=pren
        return self.qte_nec

 
class abeille:
    def __init__(self,x:int,y:int,type:int,nbplay:int):
        self.type=type
        self.x=x
        self.y=y
        self.nbplay=nbplay
    
    def deplacement(self,nx:int,ny:int):
        if self.renvoie_type==1 or self.renvoie_type==3:
            if nx==self.x and ny==self.y+1 or nx==self.x-1 and ny==self.y or nx==self.x+1 and ny==self.y or nx==self.x and ny==self.y-1 :  """On verif que les cases autour de l'abeille sont valides pour les deplacements en croix"""
                self.x=nx
                self.y=ny
        elif self.renvoie_type==2:
            if nx==self.x and ny==self.y+1 or nx==self.x-1 and ny==self.y or nx==self.x+1 and ny==self.y or nx==self.x and ny==self.y-1 or nx==self.x+1 and ny==self.y+1 or nx==self.x-1 and ny==self.y+1 or nx==self.x+1 and ny==self.y-1 or nx==self.x-1 and ny==self.y-1 : """On verif que les cases autour de l'abeille sont valides pour les deplacements en diag"""
                self.x=nx
                self.y=ny 