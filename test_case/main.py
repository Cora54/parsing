import json, time

def ParseTime(tm):
    a, b = tm.split(',')
    resultA = time.mktime(time.strptime('2000 ' + a, '%Y %H:%M:%S'))
    resultB = int(b)
    return resultA + resultB / 1000000

def OpenCom():
    with open('competitors2.json', 'r', encoding='utf8') as file: #'Инга'??????
        f = file.read()
        name_list = json.loads(f)
        return name_list


def OpenResults():
    s = {}
    with open('results_RUN.txt', 'r', encoding='utf8') as file:
        for i in file:
            id, sf, tm =  i.split()
            if sf == 'start':
                t1 = tm
            elif sf == 'finish':
                t2 = tm
                result1 = ParseTime(t1)
                result2 = ParseTime(t2)
                result = result2 - result1
                s[id] = result               
    return(s)
    
def MakeResult():
    s = []
    name = OpenCom()
    tm = OpenResults()
    for id in name:
        try:
            s.append([name[id], tm[id], id])
        except KeyError:
            pass
    s = sorted(s, key=lambda x: x[1], reverse=False)
    return(s)

def Format():
    s = MakeResult()
    i = 1
    for [name, tm, id] in s:
        print(f"""{i} {
            id
        }\t{
            name['Surname']
        }\t{
            name['Name']
        }\t{
            '%02d' % int(tm / 60)
        }:{
            ('%05.2f' % (tm % 60)).replace('.', ',')
        }""")
        i = i + 1

Format()
