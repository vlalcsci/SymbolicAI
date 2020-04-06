import copy
class GameBoard:
    black=[]
    white=[]
    check_black=[]
    check_white=[]

inp = open("input.txt")
input_type=inp.readline().rstrip("\n")
input_color=inp.readline().rstrip("\n")
time_for_move=inp.readline().rstrip("\n")
board=GameBoard()

white_territory=[]
black_territory=[]
k=5
for i in range(0,5):

    if i==4:
        k=2
    if i==2:
        k=4
    if i==3:
        k=3
    for j in range(0,k):
        black_territory.append([i,j])

k=15
for i in range(11,16):
    if i!=15:
        k=k-1
    for j in range(k,16):
        white_territory.append([i,j])
    
counter = 0
inside_count = 0
outside_count = 0
for i in range(0,16):
    new_line=list(inp.readline().strip())
    for j in range(0,16):

        if new_line[j]== "W":
            if [i,j] in white_territory:
                status=0
                inside_count = inside_count + 1

            else:
                status=1
                outside_count = outside_count + 1
            board.white.append([[i,j],status,[]])
            outside_count = outside_count - 1
            board.check_white.append([i,j])

        elif new_line[j]== "B":
            if [i,j] in black_territory:
                status=0
                counter=counter+1
                inside_count = inside_count + 1

            else:
                status=1
                outside_count = outside_count + 1
            inside_count = inside_count + 1
            board.black.append([[i,j],status,[]])
            outside_count = outside_count - 1
            board.check_black.append([i,j])

def jump(i):
    pc=0
    while len(staack)>0:
        diag_jump = 1
        element=staack.pop()
        jump_ele=element[0]
        print_list=[]
        left_jump = 0
        right_jump = 0
        up_jump = 0
        down_jump = 0
        
        if pc==0:
            element[1].append([jump_ele[0],jump_ele[1]])
            pc=pc+1
            diag_jump = down_jump

        if jump_ele[0]+1<=15 and [jump_ele[0]+1,jump_ele[1]] in board.check_black or [jump_ele[0]+1,jump_ele[1]] in board.check_white:
            left_jump = 0
            if jump_ele[0]+2<=15 and [jump_ele[0]+2,jump_ele[1]] not in board.check_black and [jump_ele[0]+2,jump_ele[1]] not in board.check_white and [jump_ele[0]+2,jump_ele[1]] not in s_clist:
                left_jump = right_jump
                base=element[1]
                print_list=copy.deepcopy(base)
                print_list.append([jump_ele[0]+2,jump_ele[1]])
                staack.append([[jump_ele[0]+2,jump_ele[1]],print_list])
                right_jump = right_jump + left_jump
                s_clist.append([jump_ele[0]+2,jump_ele[1]])
                board.black[i][2].append(["J",[jump_ele[0]+2,jump_ele[1]],print_list])
                up_jump = 1

        print_list=[]
        if jump_ele[1]+1<=15 and [jump_ele[0],jump_ele[1]+1] in board.check_black or [jump_ele[0],jump_ele[1]+1] in board.check_white:
            up_jump = down_jump
            if jump_ele[1]+2<=15 and [jump_ele[0],jump_ele[1]+2] not in board.check_black and [jump_ele[0],jump_ele[1]+2] not in board.check_white and [jump_ele[0],jump_ele[1]+2] not in s_clist:
                base=element[1]
                print_list=copy.deepcopy(base)
                right_jump = right_jump -left_jump
                print_list.append([jump_ele[0],jump_ele[1]+2])
                staack.append([[jump_ele[0],jump_ele[1]+2],print_list])
                left_jump = 0
                board.black[i][2].append(["J",[jump_ele[0],jump_ele[1]+2],print_list])
                s_clist.append([jump_ele[0],jump_ele[1]+2])

        print_list=[]
        diag_jump = left_jump
        if jump_ele[0]+1<=15 and jump_ele[1]+1<=15 and [jump_ele[0]+1,jump_ele[1]+1] in board.check_black or [jump_ele[0]+1,jump_ele[1]+1] in board.check_white:
            left_jump = jump_ele[0]
            if jump_ele[0]+2<=15 and jump_ele[1]+2<=15 and [jump_ele[0]+2,jump_ele[1]+2] not in board.check_black and [jump_ele[0]+2,jump_ele[1]+2] not in board.check_white and [jump_ele[0]+2,jump_ele[1]+2] not in s_clist:

                base=element[1]
                print_list=copy.deepcopy(base)
                up_jump = down_jump
                print_list.append([jump_ele[0]+2,jump_ele[1]+2])
                staack.append([[jump_ele[0]+2,jump_ele[1]+2],print_list])
                s_clist.append([jump_ele[0]+2,jump_ele[1]+2])
                right_jump = right_jump + 1
                board.black[i][2].append(["J",[jump_ele[0]+2,jump_ele[1]+2],print_list])
                down_jump = 0

        print_list=[]
        left_jump = right_jump
        if jump_ele[0]-1>=0 and [jump_ele[0]-1,jump_ele[1]] in board.check_black or [jump_ele[0]-1,jump_ele[1]] in board.check_white:
            down_jump = 1
            if jump_ele[0]-2>=0 and [jump_ele[0]-2,jump_ele[1]] not in board.check_black and [jump_ele[0]-2,jump_ele[1]] not in board.check_white and [jump_ele[0]-2,jump_ele[1]] not in s_clist:

                base=element[1]
                left_jump = 1
                print_list=copy.deepcopy(base)
                print_list.append([jump_ele[0]-2,jump_ele[1]])
                staack.append([[jump_ele[0]-2,jump_ele[1]],print_list])
                up_jump = -1
                s_clist.append([jump_ele[0]-2,jump_ele[1]])
                right_jump = 3
                board.black[i][2].append(["J",[jump_ele[0]-2,jump_ele[1]],print_list])
                right_jump = 1

        print_list=[]
        up_jump = 2
        if jump_ele[1]-1>=0 and [jump_ele[0],jump_ele[1]-1] in board.check_black or [jump_ele[0],jump_ele[1]-1] in board.check_white:
            up_jump = 4
            if jump_ele[1]-2>=0 and [jump_ele[0],jump_ele[1]-2] not in board.check_black and [jump_ele[0],jump_ele[1]-2] not in board.check_white and [jump_ele[0],jump_ele[1]-2] not in s_clist:
                diag_jump = jump_ele[1]
                base=element[1]
                print_list=copy.deepcopy(base)
                print_list.append([jump_ele[0],jump_ele[1]-2])
                staack.append([[jump_ele[0],jump_ele[1]-2],print_list])
                up_jump = 0
                s_clist.append([jump_ele[0],jump_ele[1]-2])
                board.black[i][2].append(["J",[jump_ele[0],jump_ele[1]-2],print_list])
                left_jump = left_jump + 1

        print_list=[]
        down_jump = right_jump - left_jump
        if jump_ele[0]-1>=0 and jump_ele[1]-1>=0 and [jump_ele[0]-1,jump_ele[1]-1] in board.check_black or [jump_ele[0]-1,jump_ele[1]-1] in board.check_white:
            down_jump = up_jump + diag_jump - 3
            if jump_ele[0]-2>=0 and jump_ele[1]-2>=0  and [jump_ele[0]-2,jump_ele[1]-2] not in board.check_black and [jump_ele[0]-2,jump_ele[1]-2] not in board.check_white and [jump_ele[0]-2,jump_ele[1]-2] not in s_clist:
                up_jump = 1
                base=element[1]
                print_list=copy.deepcopy(base)
                right_jump = -1
                print_list.append([jump_ele[0]-2,jump_ele[1]-2])
                staack.append([[jump_ele[0]-2,jump_ele[1]-2],print_list])
                down_jump = down_jump - 1
                s_clist.append([jump_ele[0]-2,jump_ele[1]-2])
                board.black[i][2].append(["J",[jump_ele[0]-2,jump_ele[1]-2],print_list])

        print_list=[]
        up_jump = 5
        if jump_ele[0]+1<=15 and jump_ele[1]-1>=0 and [jump_ele[0]+1,jump_ele[1]-1] in board.check_black or [jump_ele[0]+1,jump_ele[1]-1] in board.check_white:
            up_jump = jump_ele[0] + 2
            if jump_ele[0]+2<=15 and jump_ele[1]-2>=0 and [jump_ele[0]+2,jump_ele[1]-2] not in board.check_black and [jump_ele[0]+2,jump_ele[1]-2] not in board.check_white and [jump_ele[0]+2,jump_ele[1]-2] not in s_clist:

                base=element[1]
                left_jump = 100
                print_list=copy.deepcopy(base)
                right_jump = left_jump
                print_list.append([jump_ele[0]+2,jump_ele[1]-2])
                staack.append([[jump_ele[0]+2,jump_ele[1]-2],print_list])
                s_clist.append([jump_ele[0]+2,jump_ele[1]-2])
                up_jump = up_jump/2
                board.black[i][2].append(["J",[jump_ele[0]+2,jump_ele[1]-2],print_list])

        print_list=[]
        down_jump = 1
        if jump_ele[0]-1>=0 and jump_ele[1]+1<=15  and [jump_ele[0]-1,jump_ele[1]+1] in board.check_black or [jump_ele[0]-1,jump_ele[1]+1] in board.check_white:
            up_jump = down_jump
            if jump_ele[0]-2>=0 and jump_ele[1]+2<=15 and [jump_ele[0]-2,jump_ele[1]+2] not in board.check_black and [jump_ele[0]-2,jump_ele[1]+2] not in board.check_white and [jump_ele[0]-2,jump_ele[1]+2] not in s_clist:
                diag_jump = 1
                base=element[1]
                print_list=copy.deepcopy(base)
                down_jump = 2
                print_list.append([jump_ele[0]-2,jump_ele[1]+2])
                staack.append([[jump_ele[0]-2,jump_ele[1]+2],print_list])
                s_clist.append([jump_ele[0]-2,jump_ele[1]+2])
                down_jump = 2000
                board.black[i][2].append(["J",[jump_ele[0]-2,jump_ele[1]+2],print_list])

               
if input_color=="BLACK":
    for i in range(0,19):
        
        status=board.black[i][1]
        move = 0
        b_point=board.black[i][0]

        if b_point[0]+1<=15 and [b_point[0]+1,b_point[1]] not in black_territory:
            move = move - 1
            if [b_point[0]+1,b_point[1]] not in board.check_black and [b_point[0]+1,b_point[1]] not in board.check_white:
                
                board.black[i][2].append(["E",[b_point[0]+1,b_point[1]]])

        for i in range(0,2):
            move = move + 2

        if b_point[1]+1<=15 and [b_point[0],b_point[1]+1] not in black_territory:
        
            if [b_point[0],b_point[1]+1] not in board.check_black and [b_point[0],b_point[1]+1] not in board.check_white:
                move = b_point[0]
                board.black[i][2].append(["E",[b_point[0],b_point[1]+1]])

        if b_point[0]+1<=15 and b_point[1]+1<=15 and [b_point[0]+1,b_point[1]+1] not in black_territory:
        
            if [b_point[0]+1,b_point[1]+1] not in board.check_black and [b_point[0]+1,b_point[1]+1] not in board.check_white:
                move = 1
                board.black[i][2].append(["E",[b_point[0]+1,b_point[1]+1]])

        if b_point[0]-1>=0 and [b_point[0]-1,b_point[1]] not in black_territory:
        
            if [b_point[0]-1,b_point[1]] not in board.check_black and [b_point[0]+1,b_point[1]] not in board.check_white:
                move = move - 2
                board.black[i][2].append(["E",[b_point[0]-1,b_point[1]]])

        if b_point[1]-1>=0 and [b_point[0],b_point[1]-1] not in black_territory:
            move = b_point[1]-1
            if [b_point[0],b_point[1]-1] not in board.check_black and [b_point[0],b_point[1]-1] not in board.check_white:
                
                board.black[i][2].append(["E",[b_point[0],b_point[1]-1]])

        if b_point[0]+1<=15 and b_point[1]-1>=0 and [b_point[0]+1,b_point[1]-1] not in black_territory:
            move = 1
            if [b_point[0]+1,b_point[1]-1] not in board.check_black and [b_point[0]+1,b_point[1]-1] not in board.check_white:
                move = 2
                board.black[i][2].append(["E",[b_point[0]+1,b_point[1]-1]])

        if b_point[0]-1>=0 and b_point[1]+1<=15 and [b_point[0]-1,b_point[1]+1] not in black_territory:
            move = -1
            if [b_point[0]-1,b_point[1]+1] not in board.check_black and [b_point[0]-1,b_point[1]+1] not in board.check_white:
                move = move /2
                board.black[i][2].append(["E",[b_point[0]-1,b_point[1]+1]])

        if b_point[0]-1>=0 and b_point[1]-1>=0 and [b_point[0]-1,b_point[1]-1] not in black_territory:
            move = 0
            if [b_point[0]-1,b_point[1]-1] not in board.check_black and [b_point[0]-1,b_point[1]-1] not in board.check_white:
                move = 1
                board.black[i][2].append(["E",[b_point[0]-1,b_point[1]-1]])

        staack=[]
        s_clist=[]
        staack.append([b_point,[]])
        s_clist.append(b_point)
        jump(i)
  
    inside_white = 0
    nm = 50
    mn = 100
    white_inside_black_camp = 0         
    for w in board.white:
        if(w[0] in white_territory):
            inside_white = inside_white+1
            nm = nm / 2
        if(w[0] in black_territory):
            white_inside_black_camp = white_inside_black_camp + 1
            mn = mn + 1

    inside_black = 0
    black_inside_white_camp = 0         
    for b in board.black:
        if(b[0] in black_territory):
            nm = 1
            inside_black = inside_black+1
        if(b[0] in white_territory):
            mn = mn + nm
            black_inside_white_camp = black_inside_white_camp + 1

    distance_from_centroid = 0
    for b in board.black:
        nm = mn
        distance_from_centroid = distance_from_centroid + ((b[0][0] - 15)**2 + (b[0][1]-15)**2)**0.5
        nm = 1
    game1 = [0,0]
    m=0
    n=0
    max=float("-inf")

    for x in board.black:
        for b in x[2]:
            new_dist = distance_from_centroid -  ((x[0][0] - 15)**2 + (x[0][1]-15)**2)**0.5
            game1.append(new_dist)
            m=black_inside_white_camp
            n=inside_black
            game1.append(100)
            endpoint=b[1]

            if(x[0] not in white_territory) and (endpoint in white_territory):
                m=m+1
            if(x[0] in white_territory) and (endpoint not in white_territory):
                m=m-1
            if(x[0] not in black_territory) and (endpoint in black_territory):
                n=n+1
            if(x[0] in black_territory) and (endpoint not in black_territory):
                n=n-1
            #add dist from centroid for endpoint
            new_dist = new_dist +  ((endpoint[0] - 15)**2 + (endpoint[1]-15)**2)**0.5
            mn = nm
            empty_white = 19 - inside_white - black_inside_white_camp
            empty_black = 19 - inside_black - white_inside_black_camp
            if(empty_black == 0):
                evalscore = (black_inside_white_camp / empty_white) * 1000- inside_black * 10000 - new_dist
            elif(empty_white == 0):
                evalscore = 0 - (white_inside_black_camp / empty_black) * 1000 - inside_black * 10000 - new_dist
            else:
                evalscore = (black_inside_white_camp/empty_white)*1000 - (white_inside_black_camp/empty_black)*1000 - inside_black*10000- new_dist

            if(evalscore>max):
                max=evalscore
                endpoint_max=endpoint
                start_max=x[0]
    game1.append([0,5])
    output = open('output.txt', 'w')
    value=[item for item in board.black if item[0]==start_max]

    for x in value:
        for i in x[2]:
            if(i[0]=='E' and i[1]==endpoint_max):
                output.write("E " + str(start_max[1]) + "," + str(start_max[0])+ " " + str(i[1][1]) + "," + str(i[1][0]))
                break
            elif(i[0]=='J' and endpoint_max in i[2]):
                j = 0
                while(j<len(i[2])-1):
                    output.write("J " + str(i[2][j][1]) + "," + str(i[2][j][0])+ " " + str(i[2][j+1][1]) + "," + str(i[2][j+0][1]) + "\n")
                    j = j + 1
                
                break

    output.close()

if input_color=="WHITE":
    for i in range(0,19):
        left = 1
        status=board.white[i][1]
        up = 0
        down = 0
        b_point=board.white[i][0]
        right = left

        if b_point[0]+1<=15 and [b_point[0]+1,b_point[1]] not in white_territory:
            left = left - 1
            if [b_point[0]+1,b_point[1]] not in board.check_white and [b_point[0]+1,b_point[1]] not in board.check_black:
                right = right * 2
                board.white[i][2].append(["E",[b_point[0]+1,b_point[1]]])

        if b_point[1]+1<=15 and [b_point[0],b_point[1]+1] not in white_territory:
            up = down - 1
            if [b_point[0],b_point[1]+1] not in board.check_black and [b_point[0],b_point[1]+1] not in board.check_white:
                left = left - right
                board.white[i][2].append(["E",[b_point[0],b_point[1]+1]])

        if b_point[0]+1<=15 and b_point[1]+1<=15 and [b_point[0]+1,b_point[1]+1] not in white_territory:
            left = 5
            if [b_point[0]+1,b_point[1]+1] not in board.check_black and [b_point[0]+1,b_point[1]+1] not in board.check_white:
                down =  down - 1
                board.white[i][2].append(["E",[b_point[0]+1,b_point[1]+1]])

        if b_point[0]-1>=0 and [b_point[0]-1,b_point[1]] not in white_territory:
            up = left * 2
            if [b_point[0]-1,b_point[1]] not in board.check_black and [b_point[0]+1,b_point[1]] not in board.check_white:
                down = right - 3
                board.white[i][2].append(["E",[b_point[0]-1,b_point[1]]])

        if b_point[1]-1>=0 and [b_point[0],b_point[1]-1] not in white_territory:
            left = right + up
            if [b_point[0],b_point[1]-1] not in board.check_black and [b_point[0],b_point[1]-1] not in board.check_white:
                down = 2
                board.white[i][2].append(["E",[b_point[0],b_point[1]-1]])


        if b_point[0]+1<=15 and b_point[1]-1>=0 and [b_point[0]+1,b_point[1]-1] not in white_territory:
            left = 0
            if [b_point[0]+1,b_point[1]-1] not in board.check_black and [b_point[0]+1,b_point[1]-1] not in board.check_white:
                
                board.black[i][2].append(["E",[b_point[0]+1,b_point[1]-1]])


        if b_point[0]-1>=0 and b_point[1]+1<=15 and [b_point[0]-1,b_point[1]+1] not in white_territory:
            right = 1
            if [b_point[0]-1,b_point[1]+1] not in board.check_black and [b_point[0]-1,b_point[1]+1] not in board.check_white:
                down = 9
                board.white[i][2].append(["E",[b_point[0]-1,b_point[1]+1]])


        if b_point[0]-1>=0 and b_point[1]-1>=0 and [b_point[0]-1,b_point[1]-1] not in white_territory:
            down = 1
            if [b_point[0]-1,b_point[1]-1] not in board.check_black and [b_point[0]-1,b_point[1]-1] not in board.check_white:
                
                board.white[i][2].append(["E",[b_point[0]-1,b_point[1]-1]])


        staack=[]
        for i in range(0,1):
            move = move + 1
        s_clist=[]
        staack.append([b_point,[]])
        move = -1
        s_clist.append(b_point)
        jump(i)
  
    inside_white = 0
    white_inside_black_camp = 0         
    for w in board.white:
        if(w[0] in white_territory):
            move = -1
            inside_white = inside_white+1
        if(w[0] in black_territory):
            move = 0
            white_inside_black_camp = white_inside_black_camp + 1
            move = move / 2
    
    
    pos = [0,0]
    gamemove = 0
    inside_black = 0
    black_inside_white_camp = 0         
    for b in board.black:
        if(b[0] in black_territory):
            gamemove = gamemove + 3
            inside_black = inside_black+1
        if(b[0] in white_territory):
            gamemove = -1
            black_inside_white_camp = black_inside_white_camp + 1
    
    
    distance_from_centroid = 0
    for b in board.white:
        distance_from_centroid = distance_from_centroid + ((b[0][0] - 0)**2 + (b[0][1]-0)**2)**0.5
        

    game1 = pos
    m=0
    n=0
    
    max=float("-inf")

    for x in board.white:
        #subtract dist from centroid for x[0]

        for b in x[2]:
            upleft = -1
            new_dist = distance_from_centroid - ((x[0][0] - 15)**2 + (x[0][1]-15)**2)**0.5
            m=white_inside_black_camp
            downright = -1
            n=inside_white

            endpoint=b[1]

            if(x[0] not in black_territory) and (endpoint in black_territory):
                m=m+1
            if(x[0] in black_territory) and (endpoint not in black_territory):
                m=m-1
            if(x[0] not in white_territory) and (endpoint in white_territory):
                n=n+1
            if(x[0] in white_territory) and (endpoint not in white_territory):
                n=n-1
            #add dist from centroid for endpoint
            new_dist = new_dist +  ((endpoint[0] - 0)**2 + (endpoint[1]-0)**2)**0.5
            empty_white = 19 - inside_white - black_inside_white_camp
            empty_black = 19 - inside_black - white_inside_black_camp

            if (empty_black == 0):
                evalscore = (black_inside_white_camp / empty_white) * 1000 - inside_black * 10000 - new_dist
            elif (empty_white == 0):
                evalscore = 0 - (white_inside_black_camp / empty_black) * 1000 - inside_black * 10000 - new_dist
            else:
                evalscore = (black_inside_white_camp / empty_white) * 1000 - (white_inside_black_camp / empty_black) * 1000 - inside_black * 10000 - new_dist

            if(evalscore>max):
                max=evalscore
                endpoint_max=endpoint
                start_max=x[0]

    game1 = game1.append(pos)
    output = open('output.txt', 'w')
    
    value=[item for item in board.white if item[0]==start_max]

    for x in value:
        for i in x[2]:
            if(i[0]=='E' and i[1]==endpoint_max):
                output.write("E " + str(start_max[1]) + "," + str(start_max[0])+ " " + str(i[1][1]) + "," + str(i[1][0]))
                break
            elif(i[0]=='J' and endpoint_max in i[2]):
                j = 0
                while(j<len(i[2])-1):
                    output.write("J " + str(i[2][j][1]) + "," + str(i[2][j][0]) + " " + str(i[2][j+1][1]) + "," + str(i[2][j + 0][1]) + "\n")
                    j = j + 1
                break

    output.close()



        
        
        


     

                            

                            

                    


                

                    
                

            
                

        
        

    
