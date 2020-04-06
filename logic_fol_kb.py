# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 20:48:27 2019

@author: visha
"""

import copy
def removeImplication(p):
    newList = []
    index_of_imply = p.index('=>')
    firstHalf = p[0:index_of_imply]
    if('&' in firstHalf or '|' in firstHalf):
        firstElement = notInside(firstHalf)
        for e in firstElement:
            newList.append(e)
    else:
        firstElement = '~' + p[0]
        newList.append(firstElement)
        for element in p[1:index_of_imply]:
            newList.append(element)

    newList.append('|')

    for element in p[index_of_imply+1:]:
        newList.append(element)

    return newList

def notInside(s):
    newList = []
    for l in s:
        if l[0] == '~':
            newList.append(l[1:])
        elif l == '&':
            newList.append('|')
        elif l == '|':
            newList.append('&')
        else:
            newList.append('~' + l)
    return newList

def unification(kbvallist, n,unif_list):
    
    flag = False
    for k in kbvallist:
        temp_list = [k[0]]
        for i in range(len(n)):
            # temp_list.append(k[i])
            if k[i+1] == n[i] or (not (str.isupper(k[i+1][0]) and str.isupper(n[i][0]))):
                print("KBVAL ELEMENT", k[i+1])
                print("NEGATED ELEMENT", n[i])
                flag = True
                temp_list.append([k[i+1],n[i]])
                # print(temp_list)
            else:
                flag = False
                break
        if flag == True:
            unif_list.append(temp_list)
            print("Current Unif list",unif_list)
            #print("\n\n\n")
            # print(i)



    print("unif unif_list = ",unif_list)
    return unif_list


def updatelists(unified_val,mydictcopy,key_check,negpredlist,new_key_list,opval,kbvallist):
                print("negpredlist=",negpredlist)
                lenu=len(unified_val)
                print("Unified val len:", lenu)
                counter=0

                print("opval=",opval)
                if(len(negpredlist)==0):
                    return opval
                opval=False
                for x in unified_val:
                    print("##############Now for branch x:",x)
                    print("counter:", counter)
                    print(x[0]) #ruleno
                    for y in range(1,len(x)):#over rest
                        if(not (str.isupper(x[y][0][0]) and str.isupper(x[y][1][0]))):
                            print("Substitute=",x[y][0],"    ",x[y][1]) #reverse
                            print("mydictcopy=",mydictcopy)
                            for z in mydictcopy.keys():
                                print("z=",z)
                                for l in mydictcopy[z]:
                                    if(l[0]==x[0]):
                                        print("Key =",z)
                                        print("Value= ",l)
                                        for k in range(1,len(l)):
                                            print("Value to be replaced:",l[k])
                                            print("Unif list val:",x[y][0])
                                            print("Unif list val update:",x[y][1])
                                            if(l[k]==x[y][0]):
                                                l[k]=x[y][1] #replacement
                                                print(l[1:])
                                                print("z=",z)
                                                print("key_check=",key_check)
                                                print("negpredlist=",negpredlist)
                                                if(z == key_check and l[1:]==negpredlist[0]):
                                                    print("YIY")
                                                    
                                                    negpredlist.pop(0)
                                                    new_key_list.pop(0)
                                                    if(len(negpredlist)==0):
                                                        opval=True
                                                        return opval
                                                else:
                                                    negpredlist.append(l[1:])
                                                    new_key_list.append(z)
                           
                            newk=None
                            if new_key_list[0][0] == '~':
                                newk = new_key_list[0][1:]
                                 
                            else:
                                newk = '~' + new_key_list[0]
                            kbvallist=mydictcopy[newk]
                            key_check = newk
                            print("Updated Dict:",mydictcopy)
                            print("\n\n\n")
                            print("Updated Negated List", negpredlist)
                            print("Updated KEY LIST", new_key_list)
                            print("Updated Key", newk)
                            print("Key Check",key_check)
                            #kbvallist = mydictcopy[newk]
                            #print(notInside(new_key_list[0]))
                            print("Updated KB Val List", mydictcopy[newk])
                            unif_list = []
                            unified_val = unification(kbvallist,negpredlist[0],unif_list)
                            print("Unified Val", unified_val)
                            flagrec= updatelists(unified_val,mydictcopy,key_check,negpredlist,new_key_list,opval,kbvallist)
                            if(flagrec==True):
                                return flagrec
                            else:
                                break
                        elif (x[y][0]==x[y][1]):
                            print("FOR CONSTANTS")
                            print(x[y][0])
                            print(x[y][1])
                            
                            
                           
                            negpredlist.pop(0)
                            new_key_list.pop(0)
                            
                            if(len(negpredlist)==0):
                                opval=True
                                return opval
                            
                            newk=None
                            if new_key_list[0][0] == '~':
                                newk = new_key_list[0][1:]
                                 
                            else:
                                newk = '~' + new_key_list[0]
                            kbvallist=mydictcopy[newk]
                            key_check = newk
                            print("Updated Dict:",mydictcopy)
                            print("\n\n\n")
                            print("Updated Negated List", negpredlist)
                            print("Updated KEY LIST", new_key_list)
                            print("Updated Key", newk)
                            print("Key Check",key_check)
                            #kbvallist = mydictcopy[newk]
                            #print(notInside(new_key_list[0]))
                            print("Updated KB Val List", mydictcopy[newk])
                            unif_list = []
                            
                            unified_val = unification(kbvallist,negpredlist[0],unif_list)
                            print("Unified Val", unified_val)
                            flagrec= updatelists(unified_val,mydictcopy,key_check,negpredlist,new_key_list,opval,kbvallist)
                            if(flagrec==True):
                                return flagrec
                            else:
                                break
                            #return updatelists(unified_val,mydictcopy,key_check,negpredlist,new_key_list,opval,kbvallist)
                        else:
                            print("Len Unified Else:", lenu)
                            print("Counter Else:", counter)
                            break
                            #if(counter==lenu):
                             #   opval=False
                             #   continue
                            #return opval

                    if(flagrec==True):
                        print("Returning True")
                        return flagrec
                    else:
                        # print("Reinitilizing")
                        # negpredlist=[]
                        # new_key_list=[]
                        # kbvallist=[]
                        continue   
                    counter=counter+1
                return opval


def resolution(pred, mydictcopy):
    opval = True
    flagval= False
    key_check = None
    negpredlist = []
    kbvallist = []
    new_key_list= []
    for p in pred:
        if p[0] != '&' and p[0] != '|':
            if p[0] == '~':
                ind = p.index('(')
                key_check = p[1:ind]
                if key_check in mydictcopy:
                    print(p, " " , mydictcopy[key_check])
                # kbvallist = mydictcopy[key_check]
            else:
                ind = p.index('(')
                key_check = '~' + p[0:ind]
                if key_check in mydictcopy:
                    print(p, " " , mydictcopy[key_check])
            print("Keycheck",key_check,"\n")
            
            kbvallist = mydictcopy[key_check]
            negpredlist.append(p[ind+1:][:-1].split(','))
            new_key_list.append(key_check)
            
            print('New Key list', new_key_list)
            print('Negated predicate list', negpredlist)
            print('KB val list', kbvallist)
           
            unif_list = []
            unified_val = unification(kbvallist,negpredlist[0],unif_list)
            i=0
            
            opval=updatelists(unified_val,mydictcopy,key_check,negpredlist,new_key_list,opval,kbvallist)
            
            '''
            while(i<10):
                print("i=",i)
                
                print("Unified Val", unified_val)
                negpredlist,new_key_list,opval,kbvallist=updatelists(unified_val,mydictcopy,key_check,negpredlist,new_key_list,opval,kbvallist)
                #unif_list = []
                #unified_val = unification(kbvallist,negpredlist[0],unif_list)
                if(opval==True):
                    return opval
               
                
                print("\n\n\n")
                i=i+1
                
                         '''       
                                   
                            
                            
          

    return opval





inputFile = open("input3.txt")
kb = []
predicates = []
predicate_size=int(inputFile.readline().rstrip("\n"))
for i in range(predicate_size):
    predicates.append(inputFile.readline().rstrip("\n").split(" "))
kb_size = int(inputFile.readline().rstrip("\n"))
for i in range(kb_size):
    kb.append(inputFile.readline().rstrip("\n").split(" "))

# print(kb)
# print(predicates)
kbCNF = []
negatedpredicates = []
for k in kb:
    if '=>' in k:
        kbCNF.append(removeImplication(k))
    else:
        kbCNF.append(k)

for p in predicates:
    if '=>' in p:
        s = removeImplication(p)
        negatedpredicates.append(notInside(s))
    else:
        negatedpredicates.append(notInside(p))


print("after negation", negatedpredicates)
print("kbcnf", kbCNF)
kb_dict = {}
for i,k in enumerate(kbCNF):
    for element in k:
        if element[0] != '&' and element[0] != '|':
            splitarray = element.split("(")
            currkey = splitarray[0]
            currval = splitarray[1][:-1]
            if currkey not in kb_dict:
                kb_dict[currkey] = []

            valuelist = [i]
            predargs = currval.split(",")
            for value in predargs:
                valuelist.append(value)
            kb_dict[currkey].append(valuelist)

print("KBDICT",kb_dict)

for p in negatedpredicates:
    kb_dict_copy=copy.deepcopy(kb_dict)
    outputval = resolution(p, kb_dict_copy)
    print("OUTPUT!!!!!!!!!!!!")
    print(outputval)
    #write outputval in output file







