#CS-301-001
#Yichen Huang
import pandas as pd


data = open("data.txt")
data_dic = dict()
#print("Adding data\n")
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
#print(database)
#print(data_dic)
#print(database)
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
    #print(i,len(queries))
    if(queries[i][len(queries[i])-1]) == ';':
        print("Query " + str(count) + ': ',query)
        query[len(query)-1].remove(';')
        #print('Query: ',query)
        view = database.copy(deep=True)

        if query[0][0] == 'FIND':
            if (len(query[len(query)-1]) == 1)&(query[len(query)-1][0] == 'Z'): #if Z
                if (len(query) == 3)&(len(query[1]) == 1)&(query[1][0] == 'Y'): #if Y
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
                                        if not(d.get(index) == None):
                                            if (d.get(index) == val):
                                                qualified.append(key)
                                    #print(qualified)
                                elif comp == '>':
                                    for key in data_dic:
                                        d = data_dic.get(key)
                                        if not(d.get(index) == None):
                                            if (d.get(index) > val):
                                                qualified.append(key)
                                    #print(qualified)
                                elif comp == '<':
                                    for key in data_dic:
                                        d = data_dic.get(key)
                                        if not(d.get(index) == None):
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
                                        if not(d.get(index) == None):
                                            if(d.get(index) == val):
                                                qualified.append(key)
                                    #print(qualified)
                                elif comp == '>':
                                    for key in data_dic:
                                        d = data_dic.get(key)
                                        if not(d.get(index) == None):
                                            if(d.get(index) > val):
                                                qualified.append(key)
                                    #print(qualified)
                                elif comp == '<':
                                    for key in data_dic:
                                        d = data_dic.get(key)
                                        if not(d.get(index) == None):
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
                if (len(query) == 3)&(len(query[1]) == 1)&(query[1][0] == 'Y'): # if Y
                    f = 0
                    if 'A' in project:
                        if len(project) == 1:
                            f = 1
                        else:
                            f = 2
                            project.remove('A')
                    c = 0
                    for index in range(0,len(view)):
                        k = 0
                        if f == 1:
                            print("A: " + str(index), end = ' ')
                            k = k - 1
                        
                        #print("A: " + str(index), end = ' ')
                        dictionaty = data_dic.get(index)
                        for key in project:
                            if dictionaty.get(key) != None:
                                if (c == 0) & (f == 2):
                                    print("A: " + str(index), end = ' ')
                                    c = c+1
                                print(key + ': ' + str(dictionaty.get(key)),end = ' ')
                            else:
                                k = k + 1
                            if k <= 0:
                                print()
                            k = 0
                        c = 0
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
                                        if not(d.get(index) == None):
                                            if(d.get(index) == val):
                                                qualified.append(key)
                                elif comp == '>':
                                    for key in data_dic:
                                        d = data_dic.get(key)
                                        if not(d.get(index) == None):
                                            if(d.get(index) > val):
                                                qualified.append(key)
                                elif comp == '<':
                                    for key in data_dic:
                                        d = data_dic.get(key)
                                        if not(d.get(index) == None):
                                            if(d.get(index) < val):
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
                                        if not(d.get(index) == None):
                                            if(d.get(index) == val):
                                                qualified.append(key)
                                    #print(qualified)
                                elif comp == '>':
                                    for key in data_dic:
                                        d = data_dic.get(key)
                                        if not(d.get(index) == None):
                                            if(d.get(index) > val):
                                                qualified.append(key)
                                    #print(qualified)
                                elif comp == '<':
                                    for key in data_dic:
                                        d = data_dic.get(key)
                                        if not(d.get(index) == None):
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
                    
                    f = 0
                    if 'A' in project:
                        if len(project) == 1:
                            f = 1
                        else:
                            f = 2
                            project.remove('A')
                    for index in id:
                        c = 0
                        #print("A: " + str(index), end = ' ')
                        if f==1:
                            print("A: " + str(index), end = ' ')
                        dictionaty = data_dic.get(index)
                        k = 0
                        for key in project:
                            if dictionaty.get(key) != None:
                                #print(c,f)
                                if (c == 0) & (f==2):
                                    print("A: " + str(index), end = ' ')
                                    c = c+1
                                print(key + ': ' + str(dictionaty.get(key)),end = ' ')
                            else:
                                k = k + 1
                        if k <= 0:
                            print()
            #print(query)
            print()
        elif query[0][0] == 'SORT':
            flag = 0
            if len(query[1]) != 3:
                flag = 1
            index = query[1][0]
            if (flag == 0)&(query[1][1] != '='):
                flag = 1
            ascend = int(query[1][2])

            if flag == 0:
                   
                if index == 'A':
                    if ascend == 1:
                        for i in range(0,len(view)):
                            print("A: " + str(i), end = ' ')
                            dictionaty = data_dic.get(i)
                            for key in dictionaty:
                                if dictionaty.get(key) != None:
                                    print(key + ': ' + str(dictionaty.get(key)),end = ' ')
                            print()
                    elif ascend == -1:
                        lst = list(view.index)
                        lst.reverse()
                        for i in lst:
                            print("A: " + str(i), end = ' ')
                            dictionaty = data_dic.get(i)
                            for key in dictionaty:
                                if dictionaty.get(key) != None:
                                    print(key + ': ' + str(dictionaty.get(key)),end = ' ')
                            print()
                else:

                    if index in view.columns:
                        #print(index)
                        #print(view)
                        for i in range(0,len(view)):
                            if pd.isnull(view[index][i]):
                                view.drop([i],axis=0,inplace=True)
                        #print(view)
                        if ascend == 1:
                            for i in range(0,len(view)):
                                min_idx = i
                                for j in range(i+1,len(view)):
                                    
                                    if view[index][view.index[min_idx]] > view[index][view.index[j]]:
                                        min_idx = j
                                temp = view[index][view.index[i]].copy()
                                view[index][view.index[i]] = view[index][view.index[min_idx]]
                                view[index][view.index[min_idx]] = temp
                                l = []
                                d = view.index
                                for e in d:
                                    l.append(e)
                                temp = l[i]
                                l[i] = l[min_idx]
                                l[min_idx] = temp
                                view.index = l
                            #print(database)
                            #print(view)
                            #view = view.sort_values(by = index,ascending = True)
                        elif ascend == -1:
                            for i in range(0,len(view)):
                                min_idx = i
                                for j in range(i+1,len(view)):
                                    
                                    if view[index][view.index[min_idx]] < view[index][view.index[j]]:
                                        min_idx = j
                                temp = view[index][view.index[i]].copy()
                                view[index][view.index[i]] = view[index][view.index[min_idx]]
                                view[index][view.index[min_idx]] = temp
                                l = []
                                d = view.index
                                for e in d:
                                    l.append(e)
                                temp = l[i]
                                l[i] = l[min_idx]
                                l[min_idx] = temp
                                view.index = l
                            #view = view.sort_values(by = index,ascending = False)
                        else:
                            flag = 1
                        #print(view)
                    else:
                        print("The field",index, "does not exist!")
                        flag = 1
                    
                    if flag == 0:
                        lst = list(view.index)
                        #print(lst)
                        null_list = []
                        for i in range(0,len(lst)):
                            if pd.isnull(view[index][lst[i]]):
                                null_list.append(lst[i])
                        for value in null_list:
                            lst.remove(value)
                        
                        #print(lst)
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
            #print(query)
            print()
        else:
            print('Error\n')
        query.clear()
        count = count + 1
