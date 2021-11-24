import urllib.request
import json
import os

url = 'https://pvp.qq.com/web201605/js/herolist.json'
json_text = urllib.request.urlopen(url).read()
json_hero_list = json.loads(json_text)

def get_hero_list(type=0):
    '''
    type 类型:
        10 -> 周免英雄
        11 -> 新手推荐

        0  -> 全部英雄
        1  -> 战士
        2  -> 法师
        3  -> 坦克
        4  -> 刺客
        5  -> 射手
        6  -> 辅助
    '''
    
    hero_list = []
    for hero in json_hero_list:
        if not type:
            hero_list.append((hero['title'],hero['cname']))
        else:
            if 'pay_type' in hero:
                pay_type_list = str(hero['pay_type']).split(',')
                if hero['hero_type'] == type or ('hero_type2' in hero and hero['hero_type2'] == type) or int(pay_type_list[0]) == type or (len(pay_type_list) > 1 and int(pay_type_list[1]) == type):
                    hero_list.append((hero['title'],hero['cname']))
            else:
                if hero['hero_type'] == type or ('hero_type2' in hero and hero['hero_type2'] == type):
                    hero_list.append((hero['title'],hero['cname']))
            
    return hero_list

print(    '''
    type 类型:
        10 -> 周免英雄
        11 -> 新手推荐

        0  -> 全部英雄
        1  -> 战士
        2  -> 法师
        3  -> 坦克
        4  -> 刺客
        5  -> 射手
        6  -> 辅助
    ''')

while True:
    n = input("type:")
    if n == 'exit':
        break

    try:
        n = int(n)
    except ValueError :
        print('<',n,'>','不是一个数字..')
        continue

    data_list = get_hero_list(n)
    for each in data_list:
        print(each[0],each[1])
    print('共找到了%d个英雄' % len(data_list),end='\n\n')
