import pandas as pd
import numpy as np


data = open("data.txt")
data_dic = dict()
print("Adding data\n")
lines = data.readlines()
for i in range(0,len(lines)):
    value = []
    key = []
    collection = {}
    lst = lines[i].split()
    for j in range(0,len(lst)):
        if j%2 == 0:
            lst[j] = lst[j][0]
            value.append(lst[j])
        else:
            lst[j] = int(lst[j])
            key.append(lst[j])
    #print(value)
    #print(key)
    for k in range(0,len(value)):
        collection[value[k]] = key[k]
    data_dic[i] = collection
database = pd.DataFrame(data_dic).T

print(data_dic)
print(database)
data.close()

queries = open("final.txt")
queries = queries.readlines()
for i in range(0,len(queries)):
    queries[i] = queries[i].split()
#print(queries)
query = []
count = 1
for i in range(0,len(queries)):
    query.append(queries[i][:])
    if(queries[i][len(queries[i])-1]) == ';':
        print("Query " + str(count))
        query[len(query)-1].remove(';')
        #print(query)
        view = database.copy(deep=True)

        if query[0][0] == 'FIND':
            if(query[len(query)-1][0] == 'Z'): #if Z
                if(query[1][0] == 'Y'): #if Y
                    for index in range(0,len(view)):
                        print("A: " + str(index), end = ' ')
                        dictionaty = data_dic.get(index)
                        for key in dictionaty:
                            if dictionaty.get(key) != None:
                                print(key + ': ' + str(dictionaty.get(key)),end = ' ')
                        print()
                        
                else: #not Y
                    id = []
                    for sub in range(1,len(query)-1):
                        if len(query[sub]) != 3:
                            break
                        if sub == 1:
                            qualified = []
                            index = query[sub][0]
                            comp = query[sub][1]
                            val = int(query[sub][2])
                           
                            if index in view.columns:
                                if comp == '=':
                                    for key in data_dic:
                                        d = data_dic.get(key)
                                        if(d.get(index) == val):
                                            qualified.append(key)
                                    #print(qualified)
                                elif comp == '>':
                                    for key in data_dic:
                                        d = data_dic.get(key)
                                        if(d.get(index) > val):
                                            qualified.append(key)
                                    #print(qualified)
                                elif comp == '<':
                                    for key in data_dic:
                                        d = data_dic.get(key)
                                        if(d.get(index) < val):
                                            qualified.append(key)
                                    #print(qualified)
                                else:
                                    id.clear()
                                    break
                            else:
                                id.clear()
                                break
                            id = list(set(id) | set(qualified))
                        else:
                            qualified = []
                            index = query[sub][0]
                            comp = query[sub][1]
                            val = int(query[sub][2])

                            if index in view.columns:
                                if comp == '=':
                                    for key in data_dic:
                                        d = data_dic.get(key)
                                        if(d.get(index) == val):
                                            qualified.append(key)
                                    #print(qualified)
                                elif comp == '>':
                                    for key in data_dic:
                                        d = data_dic.get(key)
                                        if(d.get(index) > val):
                                            qualified.append(key)
                                    #print(qualified)
                                elif comp == '<':
                                    for key in data_dic:
                                        d = data_dic.get(key)
                                        if(d.get(index) < val):
                                            qualified.append(key)
                                    #print(qualified)
                                else:
                                    id.clear()
                                    break
                            else:
                                id.clear()
                                break
                            id = list(set(id) & set(qualified))
                    #print(id)
                    for index in id:
                        print("A: " + str(index), end = ' ')
                        dictionaty = data_dic.get(index)
                        for key in dictionaty:
                            if dictionaty.get(key) != None:
                                print(key + ': ' + str(dictionaty.get(key)),end = ' ')
                        print()
            else: #not Z
                project = query[len(query)-1]
                if(query[1][0] == 'Y'): # if Y
                    if 'A' in project:
                        project.remove('A')
                    for index in range(0,len(view)):
                        k = 0
                        #print("A: " + str(index), end = ' ')
                        dictionaty = data_dic.get(index)
                        for key in project:
                            if dictionaty.get(key) != None:
                                if k == 0:
                                    print("A: " + str(index), end = ' ')
                                    k = k+1
                                print(key + ': ' + str(dictionaty.get(key)),end = ' ')
                        print()
                else:   #not Y
                    id = []
                    for sub in range(1,len(query)-1):
                        if len(query[sub]) != 3:
                            break
                        if sub == 1:
                            qualified = []
                            index = query[sub][0]
                            comp = query[sub][1]
                            val = int(query[sub][2])

                            if index in view.columns:
                                if comp == '=':
                                    for key in data_dic:
                                        d = data_dic.get(key)
                                        if d.get(index) == val:
                                            qualified.append(key)
                                elif comp == '>':
                                    for key in data_dic:
                                        d = data_dic.get(key)
                                        if d.get(index) > val:
                                            qualified.append(key)
                                elif comp == '<':
                                    for key in data_dic:
                                        d = data_dic.get(key)
                                        if d.get(index) < val:
                                            qualified.append(key)
                                else:
                                    id.clear()
                                    break
                            else:
                                id.clear()
                                break
                            id = list(set(id) | set(qualified))
                        else:
                            qualified = []
                            index = query[sub][0]
                            comp = query[sub][1]
                            val = int(query[sub][2])

                            if index in view.columns:
                                if comp == '=':
                                    for key in data_dic:
                                        d = data_dic.get(key)
                                        if(d.get(index) == val):
                                            qualified.append(key)
                                    #print(qualified)
                                elif comp == '>':
                                    for key in data_dic:
                                        d = data_dic.get(key)
                                        if(d.get(index) > val):
                                            qualified.append(key)
                                    #print(qualified)
                                elif comp == '<':
                                    for key in data_dic:
                                        d = data_dic.get(key)
                                        if(d.get(index) < val):
                                            qualified.append(key)
                                    #print(qualified)
                                else:
                                    id.clear()
                                    break
                            else:
                                id.clear()
                                break
                            id = list(set(id) & set(qualified))
                    #print(id)
                    for index in id:
                        #print("A: " + str(index), end = ' ')
                        dictionaty = data_dic.get(index)
                        for key in project:
                            if dictionaty.get(key) != None:
                                print(key + ': ' + str(dictionaty.get(key)),end = ' ')
                        print()
            #print(query)
        elif query[0][0] == 'SORT':
            if len(query[1]) != 3:
                break
            index = query[1][0]
            if query[1][1] != '=':
                break
            ascend = int(query[1][2])
            
            if index == 'A':
                if ascend == 1:
                    for index in range(0,len(view)):
                        print("A: " + str(index), end = ' ')
                        dictionaty = data_dic.get(index)
                        for key in dictionaty:
                            if dictionaty.get(key) != None:
                                print(key + ': ' + str(dictionaty.get(key)),end = ' ')
                        print()
                elif ascend == -1:
                    lst = list(view.index)
                    lst.reverse()
                    for index in lst:
                        print("A: " + str(index), end = ' ')
                        dictionaty = data_dic.get(index)
                        for key in dictionaty:
                            if dictionaty.get(key) != None:
                                print(key + ': ' + str(dictionaty.get(key)),end = ' ')
                        print()
            else:
                if index in view.columns:
                    if ascend == 1:
                        view = view.sort_values(by = index,ascending = True)
                    elif ascend == -1:
                        view = view.sort_values(by = index,ascending = False)
                    else:
                        break
                    print(view)
                else:
                    break
                lst = list(view.index)
                null_list = []
                for i in range(0,len(lst)):
                    if pd.isnull(view[index][lst[i]]):
                        null_list.append(lst[i])
                lst = list(set(lst) - set(null_list))

                for i in lst:
                    print("A: " + str(i), end = ' ')
                    dictionaty = data_dic.get(i)
                    for k in dictionaty:
                        if dictionaty.get(k) != None:
                            print(k + ': ' + str(dictionaty.get(k)),end = ' ')
                    print()
                #print(lst)
            #view = view.sort_values(by = 'C',ascending = False)
            #print(view)
            print(query)
        else:
            print('Error')
        query.clear()
        count = count + 1
    