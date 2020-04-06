
class Grid:
    black=[]
    white=[]
    black_pts=[]
    white_pts=[]

   
#path=path='C:\\Users\\yash\\Desktop\\PYTHON_PROGRAMS\\hw2_input.txt'
inputFile = open("input.txt")
input_type=inputFile.readline().strip()
input_color=inputFile.readline().strip()
print("Input color is ",input_color)
print(type(input_color))
#this will be a string
move_time=inputFile.readline().strip()
grid_struct=Grid()

check_list_w=[]
check_list_b=[]
r=5
for i in range(0,5):

    if i==2:
        r=4

    if i==3:
        r=3

    if i==4:
        r=2
        

    for j in range(0,r):
        check_list_b.append([i,j])

r=15
for i in range(11,16):

    if i!=15:
        r=r-1

    for j in range(r,16):

        check_list_w.append([i,j])
    

    
        

    
counter=0;
for i in range(0,16):

    line=inputFile.readline().strip()
    new_line=list(line)
    #print(new_line)
    for j in range(0,16):

        if new_line[j]== "W":

            if [i,j] in check_list_w:
                status=0
                

            else:
                status=1
            grid_struct.white.append([[i,j],status,[]])
            grid_struct.white_pts.append([i,j])

        elif new_line[j]== "B":

            if [i,j] in check_list_b:
                status=0
                counter=counter+1;

            else:
                status=1

            grid_struct.black.append([[i,j],status,[]])
            grid_struct.black_pts.append([i,j])

            
print(grid_struct.black)

list_pt1=[] #The resultant states, when we move 1st point in one of the feasable directions


def jump(i):
    point_counter=0    
    while len(staack)>0:

        element=staack.pop()
        j_point=element[0]
        pri_list=[]
        
        if point_counter==0:
            element[1].append([j_point[0],j_point[1]])
            point_counter=point_counter+1
            
            
            
        
        if j_point[0]+1<=15 and [j_point[0]+1,j_point[1]] in grid_struct.black_pts or [j_point[0]+1,j_point[1]] in grid_struct.white_pts:
            
            if j_point[0]+2<=15 and [j_point[0]+2,j_point[1]] not in grid_struct.black_pts and [j_point[0]+2,j_point[1]] not in grid_struct.white_pts and [j_point[0]+2,j_point[1]] not in stack_checklist:

                if [j_point[0]+2,j_point[1]] not in check_list_b:

                    pri_list=element[1]
                    pri_list.append([j_point[0]+2,j_point[1]])
                    staack.append([[j_point[0]+2,j_point[1]],pri_list])
                    stack_checklist.append([j_point[0]+2,j_point[1]])
                    grid_struct.black[i][2].append(["J",[j_point[0]+2,j_point[1]],pri_list])

                else:

                    pri_list=element[1]
                    pri_list.append([j_point[0]+2,j_point[1]])

                    varrr=2
                    while [j_point[0]+varrr,j_point[1]] in check_list_b:

                        varrr=varrr+1
                        if j_point[0]+varrr<=15 and [j_point[0]+varrr,j_point[1]] in grid_struct.black_pts or [j_point[0]+varrr,j_point[1]] in grid_struct.white_pts:
                            varrr=varrr+1
                            if j_point[0]+varrr<=15 and [j_point[0]+varrr,j_point[1]] not in grid_struct.black_pts and [j_point[0]+varrr,j_point[1]] not in grid_struct.white_pts and [j_point[0]+varrr,j_point[1]] not in stack_checklist:

                                
                                pri_list.append([j_point[0]+varrr,j_point[1]])
                                if [j_point[0]+varrr,j_point[1]] not in check_list_b:

                                    staack.append([[j_point[0]+varrr,j_point[1]],pri_list])
                                    stack_checklist.append([j_point[0]+varrr,j_point[1]])
                                    grid_struct.black[i][2].append(["J",[j_point[0]+varrr,j_point[1]],pri_list])
                                    break

                            else:

                                break

                        else:

                            break




        if j_point[1]+1<=15 and [j_point[0],j_point[1]+1] in grid_struct.black_pts or [j_point[0],j_point[1]+1] in grid_struct.white_pts:
            
            if j_point[1]+2<=15 and [j_point[0],j_point[1]+2] not in grid_struct.black_pts and [j_point[0],j_point[1]+2] not in grid_struct.white_pts and [j_point[0],j_point[1]+2] not in stack_checklist:

                if [j_point[0],j_point[1]+2] not in check_list_b:

                    pri_list=element[1]
                    pri_list.append([j_point[0],j_point[1]+2])
                    staack.append([[j_point[0],j_point[1]+2],pri_list])
                    stack_checklist.append([j_point[0],j_point[1]+2])
                    grid_struct.black[i][2].append(["J",[j_point[0],j_point[1]+2],pri_list])

                else:

                    pri_list=element[1]
                    pri_list.append([j_point[0],j_point[1]+2])

                    varrr=2
                    while [j_point[0],j_point[1]+varrr] in check_list_b:

                        varrr=varrr+1
                        if j_point[1]+varrr<=15 and [j_point[0],j_point[1]+varrr] in grid_struct.black_pts or [j_point[0],j_point[1]+varrr] in grid_struct.white_pts:
                            varrr=varrr+1
                            if j_point[1]+varrr<=15 and [j_point[0],j_point[1]+varrr] not in grid_struct.black_pts and [j_point[0],j_point[1]+varrr] not in grid_struct.white_pts and [j_point[0],j_point[1]+varrr] not in stack_checklist:

                                
                                pri_list.append([j_point[0],j_point[1]+varrr])
                                if [j_point[0],j_point[1]+varrr] not in check_list_b:

                                    staack.append([[j_point[0],j_point[1]+varrr],pri_list])
                                    stack_checklist.append([j_point[0],j_point[1]+varrr])
                                    grid_struct.black[i][2].append(["J",[j_point[0],j_point[1]+varrr],pri_list])
                                    break

                            else:

                                break

                        else:

                            break                                    
                

                
        if j_point[0]+1<=15 and j_point[1]+1<=15 and [j_point[0]+1,j_point[1]+1] in grid_struct.black_pts or [j_point[0]+1,j_point[1]+1] in grid_struct.white_pts:
            
            if j_point[0]+2<=15 and j_point[1]+2<=15 and [j_point[0]+2,j_point[1]+2] not in grid_struct.black_pts and [j_point[0]+2,j_point[1]+2] not in grid_struct.white_pts and [j_point[0]+2,j_point[1]+2] not in stack_checklist:

                if [j_point[0]+2,j_point[1]] not in check_list_b:

                    pri_list=element[1]
                    pri_list.append([j_point[0]+2,j_point[1]+2])
                    staack.append([[j_point[0]+2,j_point[1]+2],pri_list])
                    stack_checklist.append([j_point[0]+2,j_point[1]+2])
                    grid_struct.black[i][2].append(["J",[j_point[0]+2,j_point[1]+2],pri_list])

                else:

                    pri_list=element[1]
                    pri_list.append([j_point[0]+2,j_point[1]+2])

                    varrr=2
                    while [j_point[0]+varrr,j_point[1]+varrr] in check_list_b:

                        varrr=varrr+1
                        if j_point[0]+varrr<=15 and j_point[1]+varrr<=15 and [j_point[0]+varrr,j_point[1]+varrr] in grid_struct.black_pts or [j_point[0]+varrr,j_point[1]+varrr] in grid_struct.white_pts:
                            varrr=varrr+1
                            if j_point[0]+varrr<=15 and j_point[1]+varrr<=15 and [j_point[0]+varrr,j_point[1]+varrr] not in grid_struct.black_pts and [j_point[0]+varrr,j_point[1]+varrr] not in grid_struct.white_pts and [j_point[0]+varrr,j_point[1]+varrr] not in stack_checklist:

                                
                                pri_list.append([j_point[0]+varrr,j_point[1]+varrr])
                                if [j_point[0]+varrr,j_point[1]+varrr] not in check_list_b:

                                    staack.append([[j_point[0]+varrr,j_point[1]+varrr],pri_list])
                                    stack_checklist.append([j_point[0]+varrr,j_point[1]+varrr])
                                    grid_struct.black[i][2].append(["J",[j_point[0]+varrr,j_point[1]+varrr],pri_list])
                                    break

                            else:

                                break

                        else:

                            break


        if j_point[0]-1>=0 and [j_point[0]-1,j_point[1]] in grid_struct.black_pts or [j_point[0]-1,j_point[1]] in grid_struct.white_pts:
            
            if j_point[0]-2>=0 and [j_point[0]-2,j_point[1]] not in grid_struct.black_pts and [j_point[0]-2,j_point[1]] not in grid_struct.white_pts and [j_point[0]-2,j_point[1]] not in stack_checklist:

                if [j_point[0]-2,j_point[1]] not in check_list_b:

                    pri_list=element[1]
                    pri_list.append([j_point[0]-2,j_point[1]])
                    staack.append([[j_point[0]-2,j_point[1]],pri_list])
                    stack_checklist.append([j_point[0]-2,j_point[1]])
                    grid_struct.black[i][2].append(["J",[j_point[0]-2,j_point[1]],pri_list])

                else:

                    pri_list=element[1]
                    pri_list.append([j_point[0]-2,j_point[1]])

                    varrr=2
                    while [j_point[0]-varrr,j_point[1]] in check_list_b:

                        varrr=varrr+1
                        if j_point[0]-varrr>=0 and [j_point[0]-varrr,j_point[1]] in grid_struct.black_pts or [j_point[0]-varrr,j_point[1]] in grid_struct.white_pts:
                            varrr=varrr+1
                            if j_point[0]-varrr>=0 and [j_point[0]-varrr,j_point[1]] not in grid_struct.black_pts and [j_point[0]-varrr,j_point[1]] not in grid_struct.white_pts and [j_point[0]-varrr,j_point[1]] not in stack_checklist:

                                
                                pri_list.append([j_point[0]-varrr,j_point[1]])
                                if [j_point[0]-varrr,j_point[1]] not in check_list_b:

                                    staack.append([[j_point[0]-varrr,j_point[1]],pri_list])
                                    stack_checklist.append([j_point[0]-varrr,j_point[1]])
                                    grid_struct.black[i][2].append(["J",[j_point[0]-varrr,j_point[1]],pri_list])
                                    break

                            else:

                                break

                        else:

                            break


        if j_point[1]-1>=0 and [j_point[0],j_point[1]-1] in grid_struct.black_pts or [j_point[0],j_point[1]-1] in grid_struct.white_pts:
            
            if j_point[1]-2>=0 and [j_point[0],j_point[1]-2] not in grid_struct.black_pts and [j_point[0],j_point[1]-2] not in grid_struct.white_pts and [j_point[0],j_point[1]-2] not in stack_checklist:

                if [j_point[0],j_point[1]-2] not in check_list_b:

                    pri_list=element[1]
                    pri_list.append([j_point[0],j_point[1]-2])
                    staack.append([[j_point[0],j_point[1]-2],pri_list])
                    stack_checklist.append([j_point[0],j_point[1]-2])
                    grid_struct.black[i][2].append(["J",[j_point[0],j_point[1]-2],pri_list])

                else:

                    pri_list=element[1]
                    pri_list.append([j_point[0],j_point[1]-2])

                    varrr=2
                    while [j_point[0],j_point[1]-varrr] in check_list_b:

                        varrr=varrr+1
                        if j_point[1]-varrr>=0 and [j_point[0],j_point[1]-varrr] in grid_struct.black_pts or [j_point[0],j_point[1]-varrr] in grid_struct.white_pts:
                            varrr=varrr+1
                            if j_point[1]-varrr>=0 and [j_point[0],j_point[1]-varrr] not in grid_struct.black_pts and [j_point[0],j_point[1]-varrr] not in grid_struct.white_pts and [j_point[0],j_point[1]-varrr] not in stack_checklist:

                                
                                pri_list.append([j_point[0],j_point[1]-varrr])
                                if [j_point[0],j_point[1]-varrr] not in check_list_b:

                                    staack.append([[j_point[0],j_point[1]-varrr],pri_list])
                                    stack_checklist.append([j_point[0],j_point[1]-varrr])
                                    grid_struct.black[i][2].append(["J",[j_point[0],j_point[1]-varrr],pri_list])
                                    break

                            else:

                                break

                        else:

                            break
# from here add cases

        if j_point[0]+1<=15 and [j_point[0]+1,j_point[1]] in grid_struct.black_pts or [j_point[0]+1,j_point[1]] in grid_struct.white_pts:
            
            if j_point[0]+2<=15 and [j_point[0]+2,j_point[1]] not in grid_struct.black_pts and [b_point[0]+2,b_point[1]] not in grid_struct.white_pts and [j_point[0]+2,j_point[1]] not in stack_checklist:

                if [j_point[0]+2,j_point[1]] not in check_list_b:

                    pri_list=element[1]
                    pri_list.append([j_point[0]+2,j_point[1]])
                    staack.append([[j_point[0]+2,j_point[1]],pri_list])
                    stack_checklist.append([j_point[0]+2,j_point[1]])
                    grid_struct.black[i][2].append(["J",[j_point[0]+2,j_point[1]],pri_list])

                else:

                    pri_list=element[1]
                    pri_list.append([j_point[0]+2,j_point[1]])

                    varrr=2
                    while [j_point[0]+varrr,j_point[1]] in check_list_b:

                        varrr=varrr+1
                        if j_point[0]+varrr<=15 and [j_point[0]+varrr,j_point[1]] in grid_struct.black_pts or [j_point[0]+varrr,j_point[1]] in grid_struct.white_pts:
                            varrr=varrr+1
                            if j_point[0]+varrr<=15 and [j_point[0]+varrr,j_point[1]] not in grid_struct.black_pts and [b_point[0]+varrr,b_point[1]] not in grid_struct.white_pts and [j_point[0]+varrr,j_point[1]] not in stack_checklist:

                                
                                pri_list.append([j_point[0]+varrr,j_point[1]])
                                if [j_point[0]+varrr,j_point[1]] not in check_list_b:

                                    staack.append([[j_point[0]+varrr,j_point[1]],pri_list])
                                    stack_checklist.append([j_point[0]+varrr,j_point[1]])
                                    grid_struct.black[i][2].append(["J",[j_point[0]+varrr,j_point[1]],pri_list])
                                    break

                            else:

                                break

                        else:

                            break


        if j_point[0]+1<=15 and [j_point[0]+1,j_point[1]] in grid_struct.black_pts or [j_point[0]+1,j_point[1]] in grid_struct.white_pts:
            
            if j_point[0]+2<=15 and [j_point[0]+2,j_point[1]] not in grid_struct.black_pts and [b_point[0]+2,b_point[1]] not in grid_struct.white_pts and [j_point[0]+2,j_point[1]] not in stack_checklist:

                if [j_point[0]+2,j_point[1]] not in check_list_b:

                    pri_list=element[1]
                    pri_list.append([j_point[0]+2,j_point[1]])
                    staack.append([[j_point[0]+2,j_point[1]],pri_list])
                    stack_checklist.append([j_point[0]+2,j_point[1]])
                    grid_struct.black[i][2].append(["J",[j_point[0]+2,j_point[1]],pri_list])

                else:

                    pri_list=element[1]
                    pri_list.append([j_point[0]+2,j_point[1]])

                    varrr=2
                    while [j_point[0]+varrr,j_point[1]] in check_list_b:

                        varrr=varrr+1
                        if j_point[0]+varrr<=15 and [j_point[0]+varrr,j_point[1]] in grid_struct.black_pts or [j_point[0]+varrr,j_point[1]] in grid_struct.white_pts:
                            varrr=varrr+1
                            if j_point[0]+varrr<=15 and [j_point[0]+varrr,j_point[1]] not in grid_struct.black_pts and [b_point[0]+varrr,b_point[1]] not in grid_struct.white_pts and [j_point[0]+varrr,j_point[1]] not in stack_checklist:

                                
                                pri_list.append([j_point[0]+varrr,j_point[1]])
                                if [j_point[0]+varrr,j_point[1]] not in check_list_b:

                                    staack.append([[j_point[0]+varrr,j_point[1]],pri_list])
                                    stack_checklist.append([j_point[0]+varrr,j_point[1]])
                                    grid_struct.black[i][2].append(["J",[j_point[0]+varrr,j_point[1]],pri_list])
                                    break

                            else:

                                break

                        else:

                            break


        if j_point[0]+1<=15 and [j_point[0]+1,j_point[1]] in grid_struct.black_pts or [j_point[0]+1,j_point[1]] in grid_struct.white_pts:
            
            if j_point[0]+2<=15 and [j_point[0]+2,j_point[1]] not in grid_struct.black_pts and [b_point[0]+2,b_point[1]] not in grid_struct.white_pts and [j_point[0]+2,j_point[1]] not in stack_checklist:

                if [j_point[0]+2,j_point[1]] not in check_list_b:

                    pri_list=element[1]
                    pri_list.append([j_point[0]+2,j_point[1]])
                    staack.append([[j_point[0]+2,j_point[1]],pri_list])
                    stack_checklist.append([j_point[0]+2,j_point[1]])
                    grid_struct.black[i][2].append(["J",[j_point[0]+2,j_point[1]],pri_list])

                else:

                    pri_list=element[1]
                    pri_list.append([j_point[0]+2,j_point[1]])

                    varrr=2
                    while [j_point[0]+varrr,j_point[1]] in check_list_b:

                        varrr=varrr+1
                        if j_point[0]+varrr<=15 and [j_point[0]+varrr,j_point[1]] in grid_struct.black_pts or [j_point[0]+varrr,j_point[1]] in grid_struct.white_pts:
                            varrr=varrr+1
                            if j_point[0]+varrr<=15 and [j_point[0]+varrr,j_point[1]] not in grid_struct.black_pts and [b_point[0]+varrr,b_point[1]] not in grid_struct.white_pts and [j_point[0]+varrr,j_point[1]] not in stack_checklist:

                                
                                pri_list.append([j_point[0]+varrr,j_point[1]])
                                if [j_point[0]+varrr,j_point[1]] not in check_list_b:

                                    staack.append([[j_point[0]+varrr,j_point[1]],pri_list])
                                    stack_checklist.append([j_point[0]+varrr,j_point[1]])
                                    grid_struct.black[i][2].append(["J",[j_point[0]+varrr,j_point[1]],pri_list])
                                    break

                            else:

                                break

                        else:

                            break



        

            

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

if input_color=="BLACK":

    
    for i in range(0,19):
        
        status=grid_struct.black[i][1]
        b_point=grid_struct.black[i][0]

        if b_point[0]+1<=15 and [b_point[0]+1,b_point[1]] not in check_list_b:
        
            if [b_point[0]+1,b_point[1]] not in grid_struct.black_pts and [b_point[0]+1,b_point[1]] not in grid_struct.white_pts:
                
                grid_struct.black[i][2].append(["E",[b_point[0]+1,b_point[1]]])


        if b_point[1]+1<=15 and [b_point[0],b_point[1]+1] not in check_list_b:
        
            if [b_point[0],b_point[1]+1] not in grid_struct.black_pts and [b_point[0],b_point[1]+1] not in grid_struct.white_pts:
                
                grid_struct.black[i][2].append(["E",[b_point[0],b_point[1]+1]])


        if b_point[0]+1<=15 and b_point[1]+1<=15 and [b_point[0]+1,b_point[1]+1] not in check_list_b:
        
            if [b_point[0]+1,b_point[1]+1] not in grid_struct.black_pts and [b_point[0]+1,b_point[1]+1] not in grid_struct.white_pts:
                
                grid_struct.black[i][2].append(["E",[b_point[0]+1,b_point[1]+1]])


        if b_point[0]-1>=0 and [b_point[0]-1,b_point[1]] not in check_list_b:
        
            if [b_point[0]-1,b_point[1]] not in grid_struct.black_pts and [b_point[0]+1,b_point[1]] not in grid_struct.white_pts:
                
                grid_struct.black[i][2].append(["E",[b_point[0]-1,b_point[1]]])


        if b_point[1]-1>=0 and [b_point[0],b_point[1]-1] not in check_list_b:
        
            if [b_point[0],b_point[1]-1] not in grid_struct.black_pts and [b_point[0],b_point[1]-1] not in grid_struct.white_pts:
                
                grid_struct.black[i][2].append(["E",[b_point[0],b_point[1]-1]])


        if b_point[0]+1<=15 and b_point[1]-1>=0 and [b_point[0]+1,b_point[1]-1] not in check_list_b:
        
            if [b_point[0]+1,b_point[1]-1] not in grid_struct.black_pts and [b_point[0]+1,b_point[1]-1] not in grid_struct.white_pts:
                
                grid_struct.black[i][2].append(["E",[b_point[0]+1,b_point[1]-1]])


        if b_point[0]-1>=0 and b_point[1]+1<=15 and [b_point[0]-1,b_point[1]+1] not in check_list_b:
        
            if [b_point[0]-1,b_point[1]+1] not in grid_struct.black_pts and [b_point[0]-1,b_point[1]+1] not in grid_struct.white_pts:
                
                grid_struct.black[i][2].append(["E",[b_point[0]-1,b_point[1]+1]])


        if b_point[0]-1>=0 and b_point[1]-1>=0 and [b_point[0]-1,b_point[1]-1] not in check_list_b:
        
            if [b_point[0]-1,b_point[1]-1] not in grid_struct.black_pts and [b_point[0]-1,b_point[1]-1] not in grid_struct.white_pts:
                
                grid_struct.black[i][2].append(["E",[b_point[0]-1,b_point[1]-1]])


        staack=[]
        stack_checklist=[]   
        staack.append([b_point,[]])
        stack_checklist.append(b_point)
        jump(i)
        print(grid_struct.black)
        
    
    for x in grid_struct:
        for b in x[2]:
            endpoint=b[1]
            print(endpoint)
                        
        
                    
        

        
        
        


                            

                            

                    


                

                    
                

            
                

        
        

    
