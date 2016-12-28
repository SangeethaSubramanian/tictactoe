import random


"""
populate outlist with character using values in in_list as index
"""

def populate_list(out_list, in_list, character):
    for i in range(0,len(in_list)):
        out_list[in_list[i]] = character


"""
print a tic-tac-toe frame
"""  
def print_list(inlist):
    print(inlist[0],inlist[1],inlist[2])  
    print(inlist[3],inlist[4],inlist[5])   
    print(inlist[6],inlist[7],inlist[8])  


"""
occupy a position pos in list l, freeing the position in flist
"""
def occupy_list(l, flist, pos):
    l.append(pos)
    flist.remove(pos)

   
"""
check if list has a winning combination
"""
def winner(list):
    comb = [{0,1,2},{3,4,5},{6,7,8},{0,3,6},{1,4,7},{2,5,8},{0,4,8},{2,4,6}]
    for item in comb:
        if(item.issubset(set(list))):                  
                  return True
    return False
                      
"""
Find a position that can complete a triple
"""
triples  = [(0,1,2),(1,2,0),(2,0,1),(3,4,5),(4,5,3),(5,3,4),(6,7,8),(7,8,6),(8,6,7),(0,3,6),(3,6,0),(6,0,3),(1,4,7),(4,7,1),(7,1,4),(2,5,8),(5,8,2),(8,2,5),(0,4,8),(4,8,0),(8,0,4),(2,4,6),(4,6,2),(6,2,4)]
def find_third(l, flist):
    for i in triples:
         if({i[0],i[1]}.issubset(l)):
            if i[2] in flist:        
              return i[2]
    return None
    
"""
Find a position that can complete a double,  providing an opportunity to complete
a triple in the next play
"""
def find_second(clist, flist):
    for i in triples:
        if ({i[0]}.issubset(clist)):
            if ({i[1],i[2]}.issubset(flist)):                   
                pos = random.choice([i[1],i[2]])
                return pos
    return None
    
"""
Main loop
"""
def main_loop():
    clist =[]
    flist = [i for i in range(9)]
    ulist = []
    plist = ['-' for i in range(9)]
    
    print ("Welcome to the game tic tac toe")
    for i in range (9):          
        if (i%2 == 0):              
            a = find_third(clist, flist) 
            if (a == None ):
                a = find_third(ulist, flist)
                if(a == None):    
                    a= find_second(clist, flist)
                    if(a == None):                                                                          
                        a = random.choice(flist)       
            print("[Play",i,"] Computer occupied position",a)
            occupy_list(clist,flist,a)                 
            populate_list(plist,clist,'o')
            print_list(plist)
            if i >= 4:
                if(winner(clist)):           
                    print ("Computer won")
                    return
        else:
            position = input("Your position is:")
            p1 = int(position)
            if p1 < 0:
                print ("Invalid choice: It should be a number between 0 and 8")
            elif p1>8:
                print ("Invalid choice: It should be a number between 0 and 8")
            elif p1 not in (flist):
                print ("Invalid choice: choose the unoccupied position")
            else:               
                print("[Play",i,"]Your position is",p1)
                occupy_list(ulist,flist,p1)
                populate_list(plist,ulist,'X')
                print_list(plist)
                if i > 4:
                   if(winner(ulist)):           
                       print ("You won")
                       return
    print ("No winner")
              
if __name__ == '__main__':
    main_loop()
