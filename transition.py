import copy
class layout:
    black_detail=[]
    white_detail=[]
    black_pieces_list=[]
    white_pieces_list=[]

   

filetoread = open("input2.txt")
gametype=filetoread.readline().strip()
gamecolor=filetoread.readline().strip()

time_rem=filetoread.readline().strip()
game_layout=layout()

whitecamp_coord=[]
blackcamp_coord=[]
r=5
for i in range(0,5):

    if i==2:
        r=4

    if i==3:
        r=3

    if i==4:
        r=2
        

    for j in range(0,r):
        blackcamp_coord.append([i,j])

r=15
for i in range(11,16):

    if i!=15:
        r=r-1

    for j in range(r,16):

        whitecamp_coord.append([i,j])
    

    
        

    
loop=0;
for i in range(0,16):

    fileline=filetoread.readline().strip()
    lineread=list(fileline)
    #print(lineread)
    for j in range(0,16):

        if lineread[j]== "W":

            if [i,j] in whitecamp_coord:
                iscamp=0
                

            else:
                iscamp=1
            game_layout.white_detail.append([[i,j],iscamp,[]])
            game_layout.white_pieces_list.append([i,j])

        elif lineread[j]== "B":

            if [i,j] in blackcamp_coord:
                iscamp=0
                loop=loop+1;

            else:
                iscamp=1

            game_layout.black_detail.append([[i,j],iscamp,[]])
            game_layout.black_pieces_list.append([i,j])



def jump_black(i):
    loopinc_pt=0    
    while len(stack_storeelem)>0:

        val_elem=stack_storeelem.pop()
        varj=val_elem[0]
        list_of_elem=[]
        
        if loopinc_pt==0:
            val_elem[1].append([varj[0],varj[1]])
            loopinc_pt=loopinc_pt+1
            
            
         
        
        if varj[0]+1<=15 and [varj[0]+1,varj[1]] in game_layout.black_pieces_list or [varj[0]+1,varj[1]] in game_layout.white_pieces_list:
            
            if varj[0]+2<=15 and [varj[0]+2,varj[1]] not in game_layout.black_pieces_list and [varj[0]+2,varj[1]] not in game_layout.white_pieces_list and [varj[0]+2,varj[1]] not in stack_prioritycheck:
                

                parent_elem=val_elem[1]
                list_of_elem=copy.deepcopy(parent_elem)
                list_of_elem.append([varj[0]+2,varj[1]])
                stack_storeelem.append([[varj[0]+2,varj[1]],list_of_elem])
                stack_prioritycheck.append([varj[0]+2,varj[1]])
                game_layout.black_detail[i][2].append(["J",[varj[0]+2,varj[1]],list_of_elem])



        list_of_elem=[]
        if varj[1]+1<=15 and [varj[0],varj[1]+1] in game_layout.black_pieces_list or [varj[0],varj[1]+1] in game_layout.white_pieces_list:
            
            if varj[1]+2<=15 and [varj[0],varj[1]+2] not in game_layout.black_pieces_list and [varj[0],varj[1]+2] not in game_layout.white_pieces_list and [varj[0],varj[1]+2] not in stack_prioritycheck:
                
               
                parent_elem=val_elem[1]
                list_of_elem=copy.deepcopy(parent_elem)
                list_of_elem.append([varj[0],varj[1]+2])
                stack_storeelem.append([[varj[0],varj[1]+2],list_of_elem])
                stack_prioritycheck.append([varj[0],varj[1]+2])
                
                game_layout.black_detail[i][2].append(["J",[varj[0],varj[1]+2],list_of_elem])
               
                    

                               
                

        list_of_elem=[]        
        if varj[0]+1<=15 and varj[1]+1<=15 and [varj[0]+1,varj[1]+1] in game_layout.black_pieces_list or [varj[0]+1,varj[1]+1] in game_layout.white_pieces_list:
            
            if varj[0]+2<=15 and varj[1]+2<=15 and [varj[0]+2,varj[1]+2] not in game_layout.black_pieces_list and [varj[0]+2,varj[1]+2] not in game_layout.white_pieces_list and [varj[0]+2,varj[1]+2] not in stack_prioritycheck:
                
                

                parent_elem=val_elem[1]
                list_of_elem=copy.deepcopy(parent_elem)
                list_of_elem.append([varj[0]+2,varj[1]+2])
                stack_storeelem.append([[varj[0]+2,varj[1]+2],list_of_elem])
                stack_prioritycheck.append([varj[0]+2,varj[1]+2])
                game_layout.black_detail[i][2].append(["J",[varj[0]+2,varj[1]+2],list_of_elem])



        list_of_elem=[]
        if varj[0]-1>=0 and [varj[0]-1,varj[1]] in game_layout.black_pieces_list or [varj[0]-1,varj[1]] in game_layout.white_pieces_list:
            
            if varj[0]-2>=0 and [varj[0]-2,varj[1]] not in game_layout.black_pieces_list and [varj[0]-2,varj[1]] not in game_layout.white_pieces_list and [varj[0]-2,varj[1]] not in stack_prioritycheck:
                

                parent_elem=val_elem[1]
                list_of_elem=copy.deepcopy(parent_elem)
                list_of_elem.append([varj[0]-2,varj[1]])
                stack_storeelem.append([[varj[0]-2,varj[1]],list_of_elem])
                stack_prioritycheck.append([varj[0]-2,varj[1]])
                game_layout.black_detail[i][2].append(["J",[varj[0]-2,varj[1]],list_of_elem])

               

        list_of_elem=[]
        if varj[1]-1>=0 and [varj[0],varj[1]-1] in game_layout.black_pieces_list or [varj[0],varj[1]-1] in game_layout.white_pieces_list:
            
            if varj[1]-2>=0 and [varj[0],varj[1]-2] not in game_layout.black_pieces_list and [varj[0],varj[1]-2] not in game_layout.white_pieces_list and [varj[0],varj[1]-2] not in stack_prioritycheck:
                
                

                parent_elem=val_elem[1]
                list_of_elem=copy.deepcopy(parent_elem)
                list_of_elem.append([varj[0],varj[1]-2])
                stack_storeelem.append([[varj[0],varj[1]-2],list_of_elem])
                stack_prioritycheck.append([varj[0],varj[1]-2])
                game_layout.black_detail[i][2].append(["J",[varj[0],varj[1]-2],list_of_elem])

               
# from here add cases


        list_of_elem=[]
        if varj[0]-1>=0 and varj[1]-1>=0 and [varj[0]-1,varj[1]-1] in game_layout.black_pieces_list or [varj[0]-1,varj[1]-1] in game_layout.white_pieces_list:
            
            if varj[0]-2>=0 and varj[1]-2>=0  and [varj[0]-2,varj[1]-2] not in game_layout.black_pieces_list and [varj[0]-2,varj[1]-2] not in game_layout.white_pieces_list and [varj[0]-2,varj[1]-2] not in stack_prioritycheck:
                
                

                parent_elem=val_elem[1]
                list_of_elem=copy.deepcopy(parent_elem)
                list_of_elem.append([varj[0]-2,varj[1]-2])
                stack_storeelem.append([[varj[0]-2,varj[1]-2],list_of_elem])
                stack_prioritycheck.append([varj[0]-2,varj[1]-2])
                game_layout.black_detail[i][2].append(["J",[varj[0]-2,varj[1]-2],list_of_elem])

                

        list_of_elem=[]
        if varj[0]+1<=15 and varj[1]-1>=0 and [varj[0]+1,varj[1]-1] in game_layout.black_pieces_list or [varj[0]+1,varj[1]-1] in game_layout.white_pieces_list:
            
            if varj[0]+2<=15 and varj[1]-2>=0 and [varj[0]+2,varj[1]-2] not in game_layout.black_pieces_list and [varj[0]+2,varj[1]-2] not in game_layout.white_pieces_list and [varj[0]+2,varj[1]-2] not in stack_prioritycheck:
                
                

                parent_elem=val_elem[1]
                list_of_elem=copy.deepcopy(parent_elem)
                list_of_elem.append([varj[0]+2,varj[1]-2])
                stack_storeelem.append([[varj[0]+2,varj[1]-2],list_of_elem])
                stack_prioritycheck.append([varj[0]+2,varj[1]-2])
                game_layout.black_detail[i][2].append(["J",[varj[0]+2,varj[1]-2],list_of_elem])

               



        list_of_elem=[]
        if varj[0]-1>=0 and varj[1]+1<=15  and [varj[0]-1,varj[1]+1] in game_layout.black_pieces_list or [varj[0]-1,varj[1]+1] in game_layout.white_pieces_list:
            
            if varj[0]-2>=0 and varj[1]+2<=15 and [varj[0]-2,varj[1]+2] not in game_layout.black_pieces_list and [varj[0]-2,varj[1]+2] not in game_layout.white_pieces_list and [varj[0]-2,varj[1]+2] not in stack_prioritycheck:
                
                

                parent_elem=val_elem[1]
                list_of_elem=copy.deepcopy(parent_elem)
                list_of_elem.append([varj[0]-2,varj[1]+2])
                stack_storeelem.append([[varj[0]-2,varj[1]+2],list_of_elem])
                stack_prioritycheck.append([varj[0]-2,varj[1]+2])
                game_layout.black_detail[i][2].append(["J",[varj[0]-2,varj[1]+2],list_of_elem])

               
        

            

##def Jumping_Pawn_Moves(position,overall_path):
##        movements=list()
##        range1=list(range(-1, 2))
##        range2=list(range(-1, 2))
##        for r1 in range1:
##            for r2 in range2:
##              if(r1!=0 and r2!=0):
##                position_1 = position[0]+2*r1
##                position_2 = position[1]+2*r2
##                if((position_1 >0 or position_1 < 15 or position_2 > 0 or position_2 < 15) and (board[position_1][position_2] != 'B' or board[position_1][position_2] != 'W')):
##                        previous_1= position[0]+r1
##                        previous_2 = position[1]+r2
##                        if(previous_1 >0 or previous_1 < 15 or previous_2 > 0 or previous_2 < 15):
##                          if(board[previous_1][previous_2] == 'B' or board[previous_1][previous_2] == 'W'):
##                            l=[position_1,position_2]
##                            if (not(l in overall_path)):
##                                overall_path.append([position[0],position[1]])
##                                overall_path.append([previous_1,previous_2])
##                                jumps = Jumping_Pawn_Moves([previous_1,previous_2],overall_path)[0]
##                                for a in jumps:
##                                    movements.append(a)
##                                movements.append([previous_1,previous_2])
##        return (movements,overall_path)

def jump_white(i):
    loopinc_pt=0    
    while len(stack_storeelem)>0:

        val_elem=stack_storeelem.pop()
        varj=val_elem[0]
        list_of_elem=[]
        
        if loopinc_pt==0:
            val_elem[1].append([varj[0],varj[1]])
            loopinc_pt=loopinc_pt+1
            
            
         
        
        if varj[0]+1<=15 and [varj[0]+1,varj[1]] in game_layout.black_pieces_list or [varj[0]+1,varj[1]] in game_layout.white_pieces_list:
            
            if varj[0]+2<=15 and [varj[0]+2,varj[1]] not in game_layout.black_pieces_list and [varj[0]+2,varj[1]] not in game_layout.white_pieces_list and [varj[0]+2,varj[1]] not in stack_prioritycheck:
                

                parent_elem=val_elem[1]
                list_of_elem=copy.deepcopy(parent_elem)
                list_of_elem.append([varj[0]+2,varj[1]])
                stack_storeelem.append([[varj[0]+2,varj[1]],list_of_elem])
                stack_prioritycheck.append([varj[0]+2,varj[1]])
                game_layout.white_detail[i][2].append(["J",[varj[0]+2,varj[1]],list_of_elem])



        list_of_elem=[]
        if varj[1]+1<=15 and [varj[0],varj[1]+1] in game_layout.black_pieces_list or [varj[0],varj[1]+1] in game_layout.white_pieces_list:
            
            if varj[1]+2<=15 and [varj[0],varj[1]+2] not in game_layout.black_pieces_list and [varj[0],varj[1]+2] not in game_layout.white_pieces_list and [varj[0],varj[1]+2] not in stack_prioritycheck:
                
                
               
                parent_elem=val_elem[1]
                list_of_elem=copy.deepcopy(parent_elem)
                list_of_elem.append([varj[0],varj[1]+2])
                stack_storeelem.append([[varj[0],varj[1]+2],list_of_elem])
                stack_prioritycheck.append([varj[0],varj[1]+2])
                
                game_layout.white_detail[i][2].append(["J",[varj[0],varj[1]+2],list_of_elem])
                
                    

                               
                

        list_of_elem=[]        
        if varj[0]+1<=15 and varj[1]+1<=15 and [varj[0]+1,varj[1]+1] in game_layout.black_pieces_list or [varj[0]+1,varj[1]+1] in game_layout.white_pieces_list:
            
            if varj[0]+2<=15 and varj[1]+2<=15 and [varj[0]+2,varj[1]+2] not in game_layout.black_pieces_list and [varj[0]+2,varj[1]+2] not in game_layout.white_pieces_list and [varj[0]+2,varj[1]+2] not in stack_prioritycheck:
                
                

                parent_elem=val_elem[1]
                list_of_elem=copy.deepcopy(parent_elem)
                list_of_elem.append([varj[0]+2,varj[1]+2])
                stack_storeelem.append([[varj[0]+2,varj[1]+2],list_of_elem])
                stack_prioritycheck.append([varj[0]+2,varj[1]+2])
                game_layout.white_detail[i][2].append(["J",[varj[0]+2,varj[1]+2],list_of_elem])



        list_of_elem=[]
        if varj[0]-1>=0 and [varj[0]-1,varj[1]] in game_layout.black_pieces_list or [varj[0]-1,varj[1]] in game_layout.white_pieces_list:
            
            if varj[0]-2>=0 and [varj[0]-2,varj[1]] not in game_layout.black_pieces_list and [varj[0]-2,varj[1]] not in game_layout.white_pieces_list and [varj[0]-2,varj[1]] not in stack_prioritycheck:
                

                parent_elem=val_elem[1]
                list_of_elem=copy.deepcopy(parent_elem)
                list_of_elem.append([varj[0]-2,varj[1]])
                stack_storeelem.append([[varj[0]-2,varj[1]],list_of_elem])
                stack_prioritycheck.append([varj[0]-2,varj[1]])
                game_layout.white_detail[i][2].append(["J",[varj[0]-2,varj[1]],list_of_elem])

               

        list_of_elem=[]
        if varj[1]-1>=0 and [varj[0],varj[1]-1] in game_layout.black_pieces_list or [varj[0],varj[1]-1] in game_layout.white_pieces_list:
            
            if varj[1]-2>=0 and [varj[0],varj[1]-2] not in game_layout.black_pieces_list and [varj[0],varj[1]-2] not in game_layout.white_pieces_list and [varj[0],varj[1]-2] not in stack_prioritycheck:
                
                

                parent_elem=val_elem[1]
                list_of_elem=copy.deepcopy(parent_elem)
                list_of_elem.append([varj[0],varj[1]-2])
                stack_storeelem.append([[varj[0],varj[1]-2],list_of_elem])
                stack_prioritycheck.append([varj[0],varj[1]-2])
                game_layout.white_detail[i][2].append(["J",[varj[0],varj[1]-2],list_of_elem])

               
# from here add cases


        list_of_elem=[]
        if varj[0]-1>=0 and varj[1]-1>=0 and [varj[0]-1,varj[1]-1] in game_layout.black_pieces_list or [varj[0]-1,varj[1]-1] in game_layout.white_pieces_list:
            
            if varj[0]-2>=0 and varj[1]-2>=0  and [varj[0]-2,varj[1]-2] not in game_layout.black_pieces_list and [varj[0]-2,varj[1]-2] not in game_layout.white_pieces_list and [varj[0]-2,varj[1]-2] not in stack_prioritycheck:
                
                

                parent_elem=val_elem[1]
                list_of_elem=copy.deepcopy(parent_elem)
                list_of_elem.append([varj[0]-2,varj[1]-2])
                stack_storeelem.append([[varj[0]-2,varj[1]-2],list_of_elem])
                stack_prioritycheck.append([varj[0]-2,varj[1]-2])
                game_layout.white_detail[i][2].append(["J",[varj[0]-2,varj[1]-2],list_of_elem])

                

        list_of_elem=[]
        if varj[0]+1<=15 and varj[1]-1>=0 and [varj[0]+1,varj[1]-1] in game_layout.black_pieces_list or [varj[0]+1,varj[1]-1] in game_layout.white_pieces_list:
            
            if varj[0]+2<=15 and varj[1]-2>=0 and [varj[0]+2,varj[1]-2] not in game_layout.black_pieces_list and [varj[0]+2,varj[1]-2] not in game_layout.white_pieces_list and [varj[0]+2,varj[1]-2] not in stack_prioritycheck:
                
                

                parent_elem=val_elem[1]
                list_of_elem=copy.deepcopy(parent_elem)
                list_of_elem.append([varj[0]+2,varj[1]-2])
                stack_storeelem.append([[varj[0]+2,varj[1]-2],list_of_elem])
                stack_prioritycheck.append([varj[0]+2,varj[1]-2])
                game_layout.white_detail[i][2].append(["J",[varj[0]+2,varj[1]-2],list_of_elem])

               



        list_of_elem=[]
        if varj[0]-1>=0 and varj[1]+1<=15  and [varj[0]-1,varj[1]+1] in game_layout.black_pieces_list or [varj[0]-1,varj[1]+1] in game_layout.white_pieces_list:
            
            if varj[0]-2>=0 and varj[1]+2<=15 and [varj[0]-2,varj[1]+2] not in game_layout.black_pieces_list and [varj[0]-2,varj[1]+2] not in game_layout.white_pieces_list and [varj[0]-2,varj[1]+2] not in stack_prioritycheck:
                
                

                parent_elem=val_elem[1]
                list_of_elem=copy.deepcopy(parent_elem)
                list_of_elem.append([varj[0]-2,varj[1]+2])
                stack_storeelem.append([[varj[0]-2,varj[1]+2],list_of_elem])
                stack_prioritycheck.append([varj[0]-2,varj[1]+2])
                game_layout.white_detail[i][2].append(["J",[varj[0]-2,varj[1]+2],list_of_elem])







                
eval_scoreval_max=float("-inf")

eval_scoreval_list=[]
if gamecolor=="BLACK":

    
    for i in range(0,19):
        
        iscamp=game_layout.black_detail[i][1]
        b_point=game_layout.black_detail[i][0]

        if b_point[0]+1<=15 :
        
            if [b_point[0]+1,b_point[1]] not in game_layout.black_pieces_list and [b_point[0]+1,b_point[1]] not in game_layout.white_pieces_list:
                
                game_layout.black_detail[i][2].append(["E",[b_point[0]+1,b_point[1]]])


        if b_point[1]+1<=15 :
        
            if [b_point[0],b_point[1]+1] not in game_layout.black_pieces_list and [b_point[0],b_point[1]+1] not in game_layout.white_pieces_list:
                
                game_layout.black_detail[i][2].append(["E",[b_point[0],b_point[1]+1]])


        if b_point[0]+1<=15 and b_point[1]+1<=15:
        
            if [b_point[0]+1,b_point[1]+1] not in game_layout.black_pieces_list and [b_point[0]+1,b_point[1]+1] not in game_layout.white_pieces_list:
                
                game_layout.black_detail[i][2].append(["E",[b_point[0]+1,b_point[1]+1]])


        if b_point[0]-1>=0:
        
            if [b_point[0]-1,b_point[1]] not in game_layout.black_pieces_list and [b_point[0]+1,b_point[1]] not in game_layout.white_pieces_list:
                
                game_layout.black_detail[i][2].append(["E",[b_point[0]-1,b_point[1]]])


        if b_point[1]-1>=0:
        
            if [b_point[0],b_point[1]-1] not in game_layout.black_pieces_list and [b_point[0],b_point[1]-1] not in game_layout.white_pieces_list:
                
                game_layout.black_detail[i][2].append(["E",[b_point[0],b_point[1]-1]])


        if b_point[0]+1<=15 and b_point[1]-1>=0:
        
            if [b_point[0]+1,b_point[1]-1] not in game_layout.black_pieces_list and [b_point[0]+1,b_point[1]-1] not in game_layout.white_pieces_list:
                
                game_layout.black_detail[i][2].append(["E",[b_point[0]+1,b_point[1]-1]])


        if b_point[0]-1>=0 and b_point[1]+1<=15:
        
            if [b_point[0]-1,b_point[1]+1] not in game_layout.black_pieces_list and [b_point[0]-1,b_point[1]+1] not in game_layout.white_pieces_list:
                
                game_layout.black_detail[i][2].append(["E",[b_point[0]-1,b_point[1]+1]])


        if b_point[0]-1>=0 and b_point[1]-1>=0:
        
            if [b_point[0]-1,b_point[1]-1] not in game_layout.black_pieces_list and [b_point[0]-1,b_point[1]-1] not in game_layout.white_pieces_list:
                
                game_layout.black_detail[i][2].append(["E",[b_point[0]-1,b_point[1]-1]])


        stack_storeelem=[]
        stack_prioritycheck=[]   
        stack_storeelem.append([b_point,[]])
        stack_prioritycheck.append(b_point)
        jump_black(i)



    black_in_wcamp=0
    for i in range(0,19):
        if game_layout.black_pieces_list[i] in whitecamp_coord:
            black_in_wcamp=black_in_wcamp+1
    white_in_wcamp=0
    for i in range(0,19):
        if whitecamp_coord[i] not in game_layout.black_pieces_list and whitecamp_coord[i] not in game_layout.white_pieces_list:
            white_in_wcamp=white_in_wcamp+1
            
    white_in_bcamp=0
    for i in range(0,19):
        if game_layout.white_pieces_list[i] in blackcamp_coord:
            white_in_bcamp=white_in_bcamp+1
    black_in_bcamp=0
    for i in range(0,19):
        if blackcamp_coord[i] not in game_layout.black_pieces_list and blackcamp_coord[i] not in game_layout.white_pieces_list:
            black_in_bcamp=black_in_bcamp+1
    black_in_bcamp_base=0
    for i in range(0,19):
        if game_layout.black_pieces_list[i] in blackcamp_coord:
            black_in_bcamp_base=black_in_bcamp_base+1
            
    avgpos=0
   
    for i in range(0,19):
        
        for pieces in game_layout.black_detail[i][2]:

            #print(pieces)

            black_in_empty_white=black_in_wcamp
            white_emptybase=white_in_wcamp
            white_in_empty_black=white_in_bcamp
            black_emptybase=black_in_bcamp
            blackpieces_base=black_in_bcamp_base
            avgpos=0
            
            #print("This is pieces", pieces)

            if game_layout.black_detail[i][1]==0:

                if pieces[1] in whitecamp_coord:
                    white_emptybase=white_emptybase-1
                    black_in_empty_white=black_in_empty_white+1
                    blackpieces_base=blackpieces_base-1
                    black_emptybase=black_emptybase+1

                elif pieces[1] not in whitecamp_coord and pieces[1] not in blackcamp_coord:
                    blackpieces_base=blackpieces_base-1
                    black_emptybase=black_emptybase+1
                    


            elif game_layout.black_detail[i][1]==1:

                if game_layout.black_detail[i][0] not in whitecamp_coord:

                    if pieces[1] in whitecamp_coord:

                        white_emptybase=white_emptybase-1
                        black_in_empty_white=black_in_empty_white+1

                    elif pieces[1] in blackcamp_coord:

                        blackpieces_base=blackpieces_base+1
                        black_emptybase=black_emptybase-1
                        

                        

                elif game_layout.black_detail[i][0] in whitecamp_coord:

                    if pieces[1] not in whitecamp_coord and pieces[1] not in blackcamp_coord :

                        white_emptybase=white_emptybase+1
                        black_in_empty_white=black_in_empty_white-1

                    elif pieces[1] in blackcamp_coord:

                        white_emptybase=white_emptybase+1
                        black_in_empty_white=black_in_empty_white-1
                        blackpieces_base=blackpieces_base+1
                        black_emptybase=black_emptybase-1

            #print("black_in_empty_white ",black_in_empty_white)
            #print("white_emptybase",white_emptybase)
            #print("white_in_empty_black",white_in_empty_black)
            #print("black_emptybase",black_emptybase)
            #print("blackpieces_base",blackpieces_base)
            #print("avgpos",avgpos)
                
            for j in  game_layout.black_pieces_list:

                avgpos=avgpos+((j[0]-15)**2 + (j[1]-15)**2)**0.5
            pott=game_layout.black_detail[i][0]
            avgpos=avgpos-((pott[0]-15)**2 + (pott[1]-15)**2)**0.5
            avgpos=avgpos+((pieces[1][0]-15)**2 + (pieces[1][1]-15)**2)**0.5


            if white_emptybase==0:
                eval_scoreval=(-1000*(white_in_empty_black/black_emptybase))- blackpieces_base*10000-avgpos
                #print(eval_scoreval)
                

            elif black_emptybase==0:
                eval_scoreval=(black_in_empty_white/white_emptybase)*1000 - blackpieces_base*10000-avgpos
                #print(eval_scoreval)

            elif white_emptybase==0 and black_emptybase==0:
                eval_scoreval= (blackpieces_base*(-10000))-avgpos
                #print(eval_scoreval)

            else:
                eval_scoreval=(black_in_empty_white/white_emptybase)*1000 + (-1000*(white_in_empty_black/black_emptybase)) - blackpieces_base*10000-avgpos
                #print(eval_scoreval)
            #print("The eval_scoreval_max value is",eval_scoreval_max)
            if eval_scoreval>=eval_scoreval_max:
                eval_scoreval_max=eval_scoreval
                print("We entered the if loop")
                #print("The  max_value inside loop is",eval_scoreval_max)
                if pieces[0]=="E":
                    eval_scoreval_list=[]
                    eval_scoreval_list.append("E")
                    pint=game_layout.black_detail[i][0]
                    
                    #print("pint is ",pint)
                    
                    eval_scoreval_list.append(pint)
                    #print("pieces[1] is",pieces[1])
                    eval_scoreval_list.append(pieces[1])
                    #print("eval_scoreval_list",eval_scoreval_list)
                    print("The eval_scoreval_list inside E loop is ",eval_scoreval_list)
                    

                elif pieces[0]=="J":

                    eval_scoreval_list=[]
                    #print("the value of pieces[2] ",pieces[2])
                    eval_scoreval_list=pieces[2]
                    eval_scoreval_list.insert(0,"J")
                    #print("The eval_scoreval_list inside J loop is ",eval_scoreval_list)
                    print("The eval_scoreval_list inside J loop is ",eval_scoreval_list)


    print(eval_scoreval_max)
    print(eval_scoreval_list)
    outputfile = open('output.txt', 'w')
    outputfile.write("")
    if eval_scoreval_list[0]=="E":

        outputfile.write("E "+str(eval_scoreval_list[1][1])+","+str(eval_scoreval_list[1][0])+" "+str(eval_scoreval_list[2][1])+","+str(eval_scoreval_list[2][0]))
       
            
    elif eval_scoreval_list[0]=="J":

        for p in range(0,len(eval_scoreval_list)-2):

            outputfile.write("J "+str(eval_scoreval_list[p+1][1])+","+str(eval_scoreval_list[p+1][0])+" "+str(eval_scoreval_list[p+2][1])+","+str(eval_scoreval_list[p+2][0]))
            outputfile.write("\n")

        
            


    outputfile.close()
                
                





if gamecolor=="WHITE":

    
    for i in range(0,19):
        
        iscamp=game_layout.white_detail[i][1]
        w_point=game_layout.white_detail[i][0]

        if w_point[0]+1<=15 :
        
            if [w_point[0]+1,w_point[1]] not in game_layout.black_pieces_list and [w_point[0]+1,w_point[1]] not in game_layout.white_pieces_list:
                
                game_layout.black_detail[i][2].append(["E",[w_point[0]+1,w_point[1]]])


        if w_point[1]+1<=15 :
        
            if [w_point[0],w_point[1]+1] not in game_layout.black_pieces_list and [w_point[0],w_point[1]+1] not in game_layout.white_pieces_list:
                
                game_layout.black_detail[i][2].append(["E",[w_point[0],w_point[1]+1]])


        if w_point[0]+1<=15 and w_point[1]+1<=15:
        
            if [w_point[0]+1,w_point[1]+1] not in game_layout.black_pieces_list and [w_point[0]+1,w_point[1]+1] not in game_layout.white_pieces_list:
                
                game_layout.black_detail[i][2].append(["E",[w_point[0]+1,w_point[1]+1]])


        if w_point[0]-1>=0:
        
            if [w_point[0]-1,w_point[1]] not in game_layout.black_pieces_list and [w_point[0]+1,w_point[1]] not in game_layout.white_pieces_list:
                
                game_layout.black_detail[i][2].append(["E",[w_point[0]-1,w_point[1]]])


        if w_point[1]-1>=0:
        
            if [w_point[0],w_point[1]-1] not in game_layout.black_pieces_list and [w_point[0],w_point[1]-1] not in game_layout.white_pieces_list:
                
                game_layout.black_detail[i][2].append(["E",[w_point[0],w_point[1]-1]])


        if w_point[0]+1<=15 and w_point[1]-1>=0:
        
            if [w_point[0]+1,w_point[1]-1] not in game_layout.black_pieces_list and [w_point[0]+1,w_point[1]-1] not in game_layout.white_pieces_list:
                
                game_layout.black_detail[i][2].append(["E",[w_point[0]+1,w_point[1]-1]])


        if w_point[0]-1>=0 and w_point[1]+1<=15:
        
            if [w_point[0]-1,w_point[1]+1] not in game_layout.black_pieces_list and [w_point[0]-1,w_point[1]+1] not in game_layout.white_pieces_list:
                
                game_layout.black_detail[i][2].append(["E",[w_point[0]-1,w_point[1]+1]])


        if w_point[0]-1>=0 and w_point[1]-1>=0:
        
            if [w_point[0]-1,w_point[1]-1] not in game_layout.black_pieces_list and [w_point[0]-1,w_point[1]-1] not in game_layout.white_pieces_list:
                
                game_layout.black_detail[i][2].append(["E",[w_point[0]-1,w_point[1]-1]])


        stack_storeelem=[]
        stack_prioritycheck=[]   
        stack_storeelem.append([w_point,[]])
        stack_prioritycheck.append(w_point)
        jump_white(i)



    black_in_wcamp=0
    for i in range(0,19):
        if game_layout.black_pieces_list[i] in whitecamp_coord:
            black_in_wcamp=black_in_wcamp+1
    white_in_wcamp=0
    for i in range(0,19):
        if whitecamp_coord[i] not in game_layout.black_pieces_list and whitecamp_coord[i] not in game_layout.white_pieces_list:
            white_in_wcamp=white_in_wcamp+1
            
    white_in_bcamp=0
    for i in range(0,19):
        if game_layout.white_pieces_list[i] in blackcamp_coord:
            white_in_bcamp=white_in_bcamp+1
    black_in_bcamp=0
    for i in range(0,19):
        if blackcamp_coord[i] not in game_layout.black_pieces_list and blackcamp_coord[i] not in game_layout.white_pieces_list:
            black_in_bcamp=black_in_bcamp+1
    number_white_original_o=0
    for i in range(0,19):
        if game_layout.white_pieces_list[i] in whitecamp_coord:
            number_white_original_o=number_white_original_o+1
            
    avgpos=0
   
    for i in range(0,19):
        
        for pieces in game_layout.white_detail[i][2]:

            #print(pieces)

            black_in_empty_white=black_in_wcamp
            white_emptybase=white_in_wcamp
            white_in_empty_black=white_in_bcamp
            black_emptybase=black_in_bcamp
            number_white_original=number_white_original_o
            avgpos=0
            
            #print("This is pieces", pieces)

            if game_layout.white_detail[i][1]==0:

                if pieces[1] in blackcamp_coord:
                    white_emptybase=white_emptybase+1
                    white_in_empty_black=white_in_empty_black+1
                    number_white_original=number_white_original-1
                    black_emptybase=black_emptybase-1

                elif pieces[1] not in whitecamp_coord and pieces[1] not in blackcamp_coord:
                    number_white_original=number_white_original-1
                    white_emptybase=white_emptybase+1
                    


            elif game_layout.white_detail[i][1]==1:

                if game_layout.white_detail[i][0] not in blackcamp_coord:

                    if pieces[1] in blackcamp_coord:

                        black_emptybase=black_emptybase-1
                        white_in_empty_black=white_in_empty_black+1

                    elif pieces[1] in whitecamp_coord:

                        number_white_original=number_white_original+1
                        white_emptybase=white_emptybase-1
                        

                        

                elif game_layout.white_detail[i][0] in blackcamp_coord:

                    if pieces[1] not in whitecamp_coord and pieces[1] not in blackcamp_coord :

                        black_emptybase=black_emptybase+1
                        white_in_empty_black=white_in_empty_black-1

                    elif pieces[1] in whitecamp_coord:

                        black_emptybase=black_emptybase+1
                        white_in_empty_black=white_in_empty_black-1
                        number_white_original=number_white_original+1
                        white_emptybase=white_emptybase-1

            #print("black_in_empty_white ",black_in_empty_white)
            #print("white_emptybase",white_emptybase)
            #print("white_in_empty_black",white_in_empty_black)
            #print("black_emptybase",black_emptybase)
            #print("blackpieces_base",blackpieces_base)
            #print("avgpos",avgpos)
                
            for j in  game_layout.white_pieces_list:

                avgpos=avgpos+((j[0]-0)**2 + (j[1]-0)**2)**0.5
            pott=game_layout.white_detail[i][0]
            avgpos=avgpos-((pott[0]-0)**2 + (pott[1]-0)**2)**0.5
            avgpos=avgpos+((pieces[1][0]-0)**2 + (pieces[1][1]-0)**2)**0.5


            if black_emptybase==0:
                eval_scoreval=(-1000*(black_in_empty_white/white_emptybase))- number_white_original*10000-avgpos
                #print(eval_scoreval)
                

            elif white_emptybase==0:
                eval_scoreval=(white_in_empty_black/black_emptybase)*1000 - number_white_original*10000-avgpos
                #print(eval_scoreval)

            elif white_emptybase==0 and black_emptybase==0:
                eval_scoreval= (number_white_original*(-10000))-avgpos
                #print(eval_scoreval)

            else:
                eval_scoreval=(white_in_empty_black/black_emptybase)*1000 + (-1000*(black_in_empty_white/white_emptybase)) - number_white_original*10000-avgpos
                #print(eval_scoreval)
            #print("The eval_scoreval_max value is",eval_scoreval_max)
            if eval_scoreval>=eval_scoreval_max:
                eval_scoreval_max=eval_scoreval
                
                #print("The  max_value inside loop is",eval_scoreval_max)
                if pieces[0]=="E":
                    eval_scoreval_list=[]
                    eval_scoreval_list.append("E")
                    pint=game_layout.black_detail[i][0]
                    
                    #print("pint is ",pint)
                    
                    eval_scoreval_list.append(pint)
                    #print("pieces[1] is",pieces[1])
                    eval_scoreval_list.append(pieces[1])
                    print("eval_scoreval_list",eval_scoreval_list)
                    #print("The eval_scoreval_list inside E loop is ",eval_scoreval_list)
                    

                elif pieces[0]=="J":

                    eval_scoreval_list=[]
                    #print("the value of pieces[2] ",pieces[2])
                    eval_scoreval_list=pieces[2]
                    eval_scoreval_list.insert(0,"J")
                    #print("The eval_scoreval_list inside J loop is ",eval_scoreval_list)                        

                        


    outputfile = open('output.txt', 'w')
    outputfile.write("")
    if eval_scoreval_list[0]=="E":

        outputfile.write("E "+str(eval_scoreval_list[1][1])+","+str(eval_scoreval_list[1][0])+" "+str(eval_scoreval_list[2][1])+","+str(eval_scoreval_list[2][0]))
        
            
    elif eval_scoreval_list[0]=="J":

        for p in range(0,len(eval_scoreval_list)-2):

            outputfile.write("J "+str(eval_scoreval_list[p+1][1])+","+str(eval_scoreval_list[p+1][0])+" "+str(eval_scoreval_list[p+2][1])+","+str(eval_scoreval_list[p+2][0]))
            outputfile.write("\n")

        
            


    outputfile.close()
                        

                        

                

                    

                
                    
                    
                
                
                

            
                
            

            
           
#print()
#print()
#print(game_layout.black_detail)





                            

                            

                    


                

                    
                

            
                

        
        

    
