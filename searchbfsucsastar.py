# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 21:23:16 2019

@author: visha
"""

import sys
import collections
from collections import deque
import queue

################################################input##################################################
inputFile = open('input_t.txt')
algorithm=inputFile.readline().strip()
matrix=inputFile.readline().strip()
matrix_list = matrix.split()
matrix_width=int(matrix_list[0])
matrix_height=int(matrix_list[1])   

landingpoint=inputFile.readline().strip()
landingpoint_list = landingpoint.split()
landing_x=int(landingpoint_list[1])
landing_y=int(landingpoint_list[0])

zthresh=inputFile.readline().strip()
targetpoints=inputFile.readline().strip()
targetpoints=int(targetpoints)
targetlist=[]
for x in range(0,targetpoints):
    line=inputFile.readline().strip()
    new_line=line.split()
    targetlist.append(new_line)

slopematrix=[]
for i in range(0,matrix_height): 
    line=inputFile.readline().strip()
    new_line=line.split()
    slopematrix.append(new_line)


print("Algorithm:", algorithm)
print("Matrix:",matrix)
print("Matrix Width:",matrix_width)
print("Matrix Height:",matrix_height)
print("Landing Point:",landingpoint)
print("Landing_X:",landing_x)
print("Landing_Y:",landing_y)
print("Z thresh:",zthresh)
print("Target Points:",targetpoints)
print("Target List:")
print(targetlist)


print("Slope Matrix:")
print(slopematrix)


def displayresult_bfs(x,y,parentcounter,targetcounter):
        #print(y,",",x)
        output.appendleft((y,x,targetcounter))
        displayresultrec_bfs(parentcounter)
        
def displayresultrec_bfs(parentcounter):
        i=0
        #print(counter)
        while(i<=counter):
            #print(result[i][2])
            #print(parentcounter)
            if(result[i][2]==int(parentcounter)):
                #print("Match")
                #print(result[i][1],",",result[i][0])
                output.appendleft((result[i][1],result[i][0],targetcounter))
                displayresultrec_bfs(result[i][3])
            i=i+1

def displayresult_ucs(x,y,parentcounter,targetcounter):
        #print(y,",",x)
        output.appendleft((y,x,targetcounter))
        displayresultrec_ucs(parentcounter)
        
def displayresultrec_ucs(parentcounter):
        i=0
        #print("Counter:",counter)
        while(i<=counter-1):
            #print(result[i][2])
            #print(parentcounter)
            if(result[i][2]==int(parentcounter)):
                #print("Match")
                #print(result[i][1],",",result[i][0])
                output.appendleft((result[i][1],result[i][0],targetcounter))
                displayresultrec_ucs(result[i][3])
            i=i+1
def displayresult_astar(x,y,parentcounter,targetcounter):
        #print("Output")
        #print(y,",",x)
        output.appendleft((y,x,targetcounter))
        displayresultrec_astar(parentcounter)
        
def displayresultrec_astar(parentcounter):
        i=0
        #print(counter)
        while(i<=counter):
            #print(result[i][2])
            #print("ParentCounter",parentcounter)
            if(result[i][2]==int(parentcounter)):
                #print("Match")
                #print(result[i][1],",",result[i][0])
                output.appendleft((result[i][1],result[i][0],targetcounter))
                displayresultrec_astar(result[i][3])
            i=i+1


def writeoutput(targetpoints, output):
    outputfile = open('output.txt', 'w')
    outputfile.write("")
    i=1
    
    while(i<=targetpoints):
        #print(i)
        flag=0
        for x in output:
            #print(output[x])
            if(x[2]==i):
                flag=1
                #print((x[0],x[1]))
                outputfile.write(str(x[0])+","+str(x[1])+" ")
        if(flag==0):
            outputfile.write("FAIL")
        outputfile.write("\n")
        i=i+1
    outputfile.close()

#######################################################BFS################################################
if(algorithm=='BFS'):            
    
    valinf=float('inf')
    landingzvalue=slopematrix[landing_x][landing_y]
    #print("Landing Point Z Value:")
    #print(slopematrix[landing_y][landing_x])
    slopematrix[landing_x][landing_y]=valinf
    
    qval=deque()
    qval.append((landing_x,landing_y,landingzvalue, -1))
    #print("Queue Size:")
    #print(qval.qsize())
    
    zthresh=int(zthresh)
    landingzvalue=int(landingzvalue)
    
    
    result=deque()
    counter=0
    output=deque()
    
    targetct=0
    for g in targetlist:
            targetct=targetct+1
            a=int(g[1])
            b=int(g[0])
            if(a==landing_x and b==landing_y):
                output.appendleft((landing_y,landing_x,targetct))
    
    
    
    targetflag=0
    targetfound=0
    while(qval):
        neighbors=[]
        
        landing_x=qval[0][0]
        landing_y=qval[0][1]
        landingzvalue=int(qval[0][2])
        landing_parentcounter=qval[0][3]
        #print("Landing Point Z Value:")
        #print(landingzvalue)
        
        north=(landing_x-1,landing_y)
        south=(landing_x+1,landing_y)
        east=(landing_x,landing_y+1)
        west=(landing_x,landing_y-1)
        northeast=(landing_x+1,landing_y-1)
        northwest=(landing_x-1,landing_y-1)
        southeast=(landing_x+1,landing_y+1)
        southwest=(landing_x-1,landing_y+1)
        
        if(landing_x-1>=0 and landing_x-1<matrix_height) and (landing_y>=0 and landing_y<matrix_width):
            neighbors.append(north)
        if(landing_x+1>=0 and landing_x+1<matrix_height) and (landing_y>=0 and landing_y<matrix_width):
            neighbors.append(south)
        if(landing_x>=0 and landing_x<matrix_height) and (landing_y+1>=0 and landing_y+1<matrix_width):
            neighbors.append(east)
        if(landing_x>=0 and landing_x<matrix_height) and (landing_y-1>=0 and landing_y-1<matrix_width):
            neighbors.append(west)
        if(landing_x+1>=0 and landing_x+1<matrix_height) and (landing_y-1>=0 and landing_y-1<matrix_width):
            neighbors.append(northeast)
        if(landing_x-1>=0 and landing_x-1<matrix_height) and (landing_y-1>=0 and landing_y-1<matrix_width):
            neighbors.append(northwest)
        if(landing_x+1>=0 and landing_x+1<matrix_height) and (landing_y+1>=0 and landing_y+1<matrix_width):
            neighbors.append(southeast)
        if(landing_x-1>=0 and landing_x-1<matrix_height) and (landing_y+1>=0 and landing_y+1<matrix_width):
            neighbors.append(southwest)
        
        
        result.append((landing_x,landing_y, counter,landing_parentcounter))
        #print("Result:")
        #print(result)
        #print("Neighbors:")
        #print(neighbors)
        
        
        
        for x in neighbors:
            neighbor_zvalue=slopematrix[x[0]][x[1]]
            neighbor_zvalue=float(neighbor_zvalue)
            if(abs(landingzvalue-neighbor_zvalue)<=zthresh and (float(neighbor_zvalue)!=valinf)):
                targetcounter=0
                for g in targetlist:
                    targetcounter=targetcounter+1
                    a=int(g[1])
                    b=int(g[0])
                    if(x[0]==a and x[1]==b):
                        #print("Target Found")
                        targetfound=targetfound+1
                        displayresult_bfs(x[0],x[1],counter,targetcounter)
                        #print(output)
                    if(targetfound==targetpoints):
                        targetflag=1
                        break
                #print(neighbor_zvalue)
                
                qval.append((x[0],x[1],neighbor_zvalue,counter))
                slopematrix[x[0]][x[1]]=valinf
                
                
        
       
        if(targetflag==1):
            break
        
        qval.popleft()
        counter=counter+1
        
        #print("Queue Elements:")
        #for x in qval:
            #print(x)
    ################################################Output#################################################
    writeoutput(targetpoints, output)
    
     

###############################################UCS####################################################
if(algorithm=='UCS'):
    #print("Landing Point Z Value:")
    #print(slopematrix[landing_y][landing_x])
    
    landingzvalue=slopematrix[landing_x][landing_y]
    #slopematrix[landing_y][landing_x]=-1
    
    qval=deque()
    qval.append((landing_x,landing_y,int(landingzvalue), -1,0))
    #open_set={}
    #open_set.add(tuple(landing_x,landing_y))
    #print("Open Set")
    #print(open_set)
    
    numelem=1
    
    qval_closed=deque()
    #print("Queue Size:")
    #print(qval.qsize())
    
    zthresh=int(zthresh)
    landingzvalue=int(landingzvalue)
    
    
    result=deque()
    counter=0
    output=deque()
            
    while(qval):
        neighbors=[]
        
        landing_x=qval[0][0]
        landing_y=qval[0][1]
        landingzvalue=int(qval[0][2])
        landing_parentcounter=qval[0][3]
        landing_distance=qval[0][4]
        #print("Landing Point Z Value:")
        #print(landingzvalue)
        
        st=10
        diag=14
        
        north=(landing_x-1,landing_y,st)
        south=(landing_x+1,landing_y,st)
        east=(landing_x,landing_y+1,st)
        west=(landing_x,landing_y-1,st)
        northeast=(landing_x+1,landing_y-1,diag)
        northwest=(landing_x-1,landing_y-1,diag)
        southeast=(landing_x+1,landing_y+1,diag)
        southwest=(landing_x-1,landing_y+1,diag)
        
        if(landing_x-1>=0 and landing_x-1<matrix_height) and (landing_y>=0 and landing_y<matrix_width):
            neighbors.append(north)
        if(landing_x+1>=0 and landing_x+1<matrix_height) and (landing_y>=0 and landing_y<matrix_width):
            neighbors.append(south)
        if(landing_x>=0 and landing_x<matrix_height) and (landing_y+1>=0 and landing_y+1<matrix_width):
            neighbors.append(east)
        if(landing_x>=0 and landing_x<matrix_height) and (landing_y-1>=0 and landing_y-1<matrix_width):
            neighbors.append(west)
        if(landing_x+1>=0 and landing_x+1<matrix_height) and (landing_y-1>=0 and landing_y-1<matrix_width):
            neighbors.append(northeast)
        if(landing_x-1>=0 and landing_x-1<matrix_height) and (landing_y-1>=0 and landing_y-1<matrix_width):
            neighbors.append(northwest)
        if(landing_x+1>=0 and landing_x+1<matrix_height) and (landing_y+1>=0 and landing_y+1<matrix_width):
            neighbors.append(southeast)
        if(landing_x-1>=0 and landing_x-1<matrix_height) and (landing_y+1>=0 and landing_y+1<matrix_width):
            neighbors.append(southwest)
        
        
        result.append((landing_x,landing_y, counter,landing_parentcounter))
        #print("Result:")
        #print(result)
        #print("Neighbors:")
        #print(neighbors)
        
        #current_set={}
        
        for x in neighbors:
            #current_set.add(x[0],x[1])
           
            neighbor_zvalue=slopematrix[x[0]][x[1]]
            neighbor_zvalue=int(neighbor_zvalue)
            if(abs(landingzvalue-neighbor_zvalue)<=zthresh):
                #print("Current Neighbor is:")
                #print(x)
                distance=landing_distance+x[2]
                #print("New Distance")
                #print(distance)
                #targetcounter=0
                #for g in targetlist:
                #    targetcounter=targetcounter+1
                #    a=int(g[1])
                #    b=int(g[0])
                #    if(x[0]==a and x[1]==b and distance<mindist):
                #        print("Target Found")
                #        displayresult(x[0],x[1],counter,targetcounter)
                        #print(output)
                #print(neighbor_zvalue)
                pos=qval.__len__()-1
                flag_insert=0
                while(distance<qval[pos][4]):
                    #print("Change")
                    pos=pos-1
                    flag_insert=1
                    
                
                
                #print("position")
                #print(pos)
                
                if(flag_insert==0):
                    open_xy=([item for item in qval if (item[0] == x[0] and item[1]==x[1])])
                    #print("Open XY")
                    #print(open_xy)
                    #print(open_xy[0])
                    closed_xy=[item for item in qval_closed if (item[0] == x[0] and item[1]==x[1])]
                    #print("Closed XY")
                    #print(closed_xy)
                    if((not open_xy) and (not closed_xy)):
                        qval.append((x[0],x[1],neighbor_zvalue,counter,distance))
                        #print("Case1")
                    elif(open_xy):
                        open_xy=[item for item in qval if (item[0] == x[0] and item[1]==x[1])]
                        #print("Old distance")
                        #print(open_xy[0][4])
                        if(distance<open_xy[0][4]):
                            #print("Case2")
                            qval.append((x[0],x[1],neighbor_zvalue,counter,distance))
                            qval.remove(open_xy[0])
                    elif(closed_xy):
                        closed_xy=[item for item in qval_closed if (item[0] == x[0] and item[1]==x[1])]
                        if(distance<closed_xy[0][4]):
                            #print("Case3")
                            qval.append((x[0],x[1],neighbor_zvalue,counter,distance))
                            qval_closed.remove(closed_xy[0])
                            #parent needs to be updated
                            resultval=[item for item in result if (item[0] == x[0] and item[1]==x[1])]
                            resultval_index=result.index(resultval[0])
                            result[resultval_index][4]=counter
                            
                else:
                    open_xy=([item for item in qval if (item[0] == x[0] and item[1]==x[1])])
                    #print("Open XY")
                    #print(open_xy)
                    #print(open_xy[0])
                    closed_xy=[item for item in qval_closed if (item[0] == x[0] and item[1]==x[1])]
                    #print("Closed XY")
                    #print(closed_xy)
                    if((not open_xy) and (not closed_xy)):
                        #qval.append((x[0],x[1],neighbor_zvalue,counter,distance))
                        qval.insert(pos+1,(x[0],x[1],neighbor_zvalue,counter,distance))
                        #print("Case1")
                    elif(open_xy):
                        open_xy=[item for item in qval if (item[0] == x[0] and item[1]==x[1])]
                        #print("Old distance")
                        #print(open_xy[0][4])
                        if(distance<open_xy[0][4]):
                            #print("Case2")
                            #qval.append((x[0],x[1],neighbor_zvalue,counter,distance))
                            qval.insert(pos+1,(x[0],x[1],neighbor_zvalue,counter,distance))
                            qval.remove(open_xy[0])
                    elif(closed_xy):
                        closed_xy=[item for item in qval_closed if (item[0] == x[0] and item[1]==x[1])]
                        if(distance<closed_xy[0][4]):
                            #print("Case3")
                            
                            #qval.append((x[0],x[1],neighbor_zvalue,counter,distance))
                            qval.insert(pos+1,(x[0],x[1],neighbor_zvalue,counter,distance))
                            qval_closed.remove(closed_xy[0])
                            #parent update logic
                            resultval=[item for item in result if (item[0] == x[0] and item[1]==x[1])]
                            resultval_index=result.index(resultval[0])
                            result[resultval_index][4]=counter
                   # same logic as above
                
                
         
                #slopematrix[x[0]][x[1]]=-1
        
       
        qval_closed.append(qval.popleft())
        #qval.popleft()
        counter=counter+1
        
    
        
        #print("Open Queue Elements:")
        #for x in qval:
         #   print(x)
        
            
        #print("Closed Queue Elements:")
        #for x in qval_closed:
        #    print(x)
    
    
    
    for x in result:
        targetcounter=0
        for g in targetlist:
            targetcounter=targetcounter+1
            a=int(g[1])
            b=int(g[0])
            if(x[0]==a and x[1]==b):
                #print("Target Found")
                displayresult_ucs(x[0],x[1],x[3],targetcounter)
                
    ################################################Output#################################################
    writeoutput(targetpoints, output)
    
    

################################################A*###################################################
if(algorithm=='A*'):
    initial_x=landing_x
    initial_y=landing_y
    
    
    output=deque()
    
    
    
    targetcounter=0
    for g in targetlist:
        targetcounter=targetcounter+1
        targetflag=0
        a=int(g[1])
        b=int(g[0])
        
        
        #print("Target"+g[1]+" "+g[0])
        
        #print("Landing Point Z Value:")
        #print(slopematrix[initial_x][initial_y])
        
        intial_zvalue=slopematrix[initial_x][initial_y]
        #slopematrix[landing_y][landing_x]=-1
        
        initial_heuristic_dist=((initial_x-a)**2+(initial_y-b)**2)**(0.5)#estimate
        
        qval=deque()
        qval.append((initial_x,initial_y,int(intial_zvalue), -1,0,initial_heuristic_dist))
        
        qval_closed=deque()
        #print("Queue Size:")
        #print(qval.qsize())
        
        zthresh=int(zthresh)
        landingzvalue=int(intial_zvalue)
        result=deque()
        counter=0
        while(qval):
            if(a==initial_x and b==initial_y):
                output.appendleft((initial_y,initial_x,targetcounter))
                break;
            neighbors=[]
            
            landing_x=qval[0][0]
            landing_y=qval[0][1]
            landingzvalue=int(qval[0][2])
            landing_parentcounter=qval[0][3]
            landing_distance=qval[0][4]
            #print("Landing Point Z Value:")
            #print(landingzvalue)
            
            st=10
            diag=14
            
            north=(landing_x-1,landing_y,st)
            south=(landing_x+1,landing_y,st)
            east=(landing_x,landing_y+1,st)
            west=(landing_x,landing_y-1,st)
            northeast=(landing_x+1,landing_y-1,diag)
            northwest=(landing_x-1,landing_y-1,diag)
            southeast=(landing_x+1,landing_y+1,diag)
            southwest=(landing_x-1,landing_y+1,diag)
            
            if(landing_x-1>=0 and landing_x-1<matrix_height) and (landing_y>=0 and landing_y<matrix_width):
                neighbors.append(north)
            if(landing_x+1>=0 and landing_x+1<matrix_height) and (landing_y>=0 and landing_y<matrix_width):
                neighbors.append(south)
            if(landing_x>=0 and landing_x<matrix_height) and (landing_y+1>=0 and landing_y+1<matrix_width):
                neighbors.append(east)
            if(landing_x>=0 and landing_x<matrix_height) and (landing_y-1>=0 and landing_y-1<matrix_width):
                neighbors.append(west)
            if(landing_x+1>=0 and landing_x+1<matrix_height) and (landing_y-1>=0 and landing_y-1<matrix_width):
                neighbors.append(northeast)
            if(landing_x-1>=0 and landing_x-1<matrix_height) and (landing_y-1>=0 and landing_y-1<matrix_width):
                neighbors.append(northwest)
            if(landing_x+1>=0 and landing_x+1<matrix_height) and (landing_y+1>=0 and landing_y+1<matrix_width):
                neighbors.append(southeast)
            if(landing_x-1>=0 and landing_x-1<matrix_height) and (landing_y+1>=0 and landing_y+1<matrix_width):
                neighbors.append(southwest)
            
            
            result.append((landing_x,landing_y, counter,landing_parentcounter))
            #print("Result:")
            #print(result)
            #print("Neighbors:")
            #print(neighbors)
            
            #current_set={}
            
            for x in neighbors:
                #current_set.add(x[0],x[1])
               
                neighbor_zvalue=slopematrix[x[0]][x[1]]
                neighbor_zvalue=int(neighbor_zvalue)
                if(abs(landingzvalue-neighbor_zvalue)<=zthresh):
                    #print("Current Neighbor is:")
                    #print(x)
                    distance=landing_distance+x[2]+abs(landingzvalue-neighbor_zvalue)#actual dist
                    heuristic_dist=((x[0]-a)**2+(x[1]-b)**2)**(0.5)#estimate abs(x[0]-a)+abs(x[1]-b)
                    total_dist=distance+heuristic_dist
                    
                    if(x[0]==a and x[1]==b):
                            targetflag=1
                            #print("Target Found"+str(x[0])+" "+str(x[1]))
                            print("Total Dist",total_dist)
                            displayresult_astar(x[0],x[1],counter,targetcounter)
                            break;
                    #targetcounter=0
                    #for g in targetlist:
                    #    targetcounter=targetcounter+1
                    #    a=int(g[1])
                    #    b=int(g[0])
                    #    if(x[0]==a and x[1]==b and distance<mindist):
                    #        print("Target Found")
                    #        displayresult(x[0],x[1],counter,targetcounter)
                            #print(output)
                    #print(neighbor_zvalue)
                    pos=qval.__len__()-1
                    #print("Position ",pos)
                    flag_insert=0
                    #print("New Distance")
                    #print(total_dist)
                    #print("Old Distance")
                    #print(qval[pos-1][5])
                    while(total_dist<qval[pos][5]):
                        #print("Change")
                        pos=pos-1
                        flag_insert=1
                    
       
                      
             
                   # print("Insert/Append Position",pos)
                    
                    
                    if(flag_insert==0):
                        #print("Flag 0")
                        open_xy=([item for item in qval if (item[0] == x[0] and item[1]==x[1])])
                        #print("Open XY")
                        #print(open_xy)
                        #print(open_xy[0])
                        closed_xy=[item for item in qval_closed if (item[0] == x[0] and item[1]==x[1])]
                        #print("Closed XY")
                        #print(closed_xy)
                        if((not open_xy) and (not closed_xy)):
                            qval.append((x[0],x[1],neighbor_zvalue,counter,distance,total_dist))
                            #print("Case1")
                        elif(open_xy):
                            open_xy=[item for item in qval if (item[0] == x[0] and item[1]==x[1])]
                            #print("Old distance")
                            #print(open_xy[0][4])
                            if(total_dist<open_xy[0][5]):
                                #print("Case2")
                                qval.append((x[0],x[1],neighbor_zvalue,counter,distance,total_dist))
                                qval.remove(open_xy[0])
                                
                        elif(closed_xy):
                            closed_xy=[item for item in qval_closed if (item[0] == x[0] and item[1]==x[1])]
                            if(total_dist<closed_xy[0][5]):
                                #print("Case3")
                                qval.append((x[0],x[1],neighbor_zvalue,counter,distance,total_dist))
                                qval_closed.remove(closed_xy[0])
                                
                                #parent needs to be updated
                                resultval=[item for item in result if (item[0] == x[0] and item[1]==x[1])]
                                resultval_index=result.index(resultval[0])
                                result[resultval_index][4]=counter
                                
                    else:
                        #print("Flag 1")
                        open_xy=([item for item in qval if (item[0] == x[0] and item[1]==x[1])])
                        #print("Open XY")
                        #print(open_xy)
                        #print(open_xy[0])
                        closed_xy=[item for item in qval_closed if (item[0] == x[0] and item[1]==x[1])]
                        #print("Closed XY")
                        #print(closed_xy)
                        if((not open_xy) and (not closed_xy)):
                            #qval.append((x[0],x[1],neighbor_zvalue,counter,distance))
                            qval.insert(pos+1,(x[0],x[1],neighbor_zvalue,counter,distance,total_dist))
                            #print("Case1_insert")
                        elif(open_xy):
                            open_xy=[item for item in qval if (item[0] == x[0] and item[1]==x[1])]
                            #print("Old distance")
                            #print(open_xy[0][4])
                            if(total_dist<open_xy[0][5]):
                                #print("Case2_insert")
                                qval.insert(pos+1,(x[0],x[1],neighbor_zvalue,counter,distance,total_dist))
                                qval.remove(open_xy[0])
                                #qval.append((x[0],x[1],neighbor_zvalue,counter,distance))
                                
                        elif(closed_xy):
                            closed_xy=[item for item in qval_closed if (item[0] == x[0] and item[1]==x[1])]
                            if(total_dist<closed_xy[0][5]):
                                #print("Case3_insert")
                                qval.insert(pos+1,(x[0],x[1],neighbor_zvalue,counter,distance,total_dist))
                                qval_closed.remove(closed_xy[0])
                                #qval.append((x[0],x[1],neighbor_zvalue,counter,distance))
                                
                                #parent update logic
                                resultval=[item for item in result if (item[0] == x[0] and item[1]==x[1])]
                                resultval_index=result.index(resultval[0])
                                result[resultval_index][4]=counter
                    
                    
             
                    #slopematrix[x[0]][x[1]]=-1
            
            if(targetflag==1):
               break;
               qval.clear()
               qval_closed.clear()
               result.clear()
            qval_closed.append(qval.popleft())
            #qval.popleft()
            counter=counter+1
            
            #print("Open Queue Elements:")
            #for x in qval:
                #print(x)
                        
                            
            #print("Closed Queue Elements:")
            #for x in qval_closed:
                #print(x)
    
    ################################################Output#################################################
    writeoutput(targetpoints, output)

        

    


