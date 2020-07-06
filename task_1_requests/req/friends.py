import requests
import json
import datetime
from collections import OrderedDict

ACCESS_TOKEN = '9de138989de138989de138986f9d93d6d899de19de13898c2e2bb0cf4f436148abfebd9'

def get_user_info(UID, FIELDS = 'bdate'):
    #Для получения id пользователя по username или user_id:
    get_user_id = requests.get('https://api.vk.com/method/users.get?v=5.71&access_token={}&user_ids={}&fields={}'.format(ACCESS_TOKEN, UID, FIELDS))
    return get_user_id.json()['response'][0]['id']

def get_user_friends(UID, FIELDS = 'bdate'):
    #Для получения списка друзей:
    get_user_friends = requests.get('https://api.vk.com/method/friends.get?v=5.71&access_token={}&user_id={}&fields={}'.format(ACCESS_TOKEN, UID, FIELDS))
    return json.loads(get_user_friends.text)['response']['items']

def get_clear_date(jlist):
    new_jlist = []
    for element in jlist:
        if 'bdate' in element:
            if len(element['bdate'].split('.')) == 3:
                new_jlist.append(element)
    return new_jlist

def calc_age(UID):
    age_dict = {}
    date = datetime.date.today()
    friends_list = get_clear_date(get_user_friends(get_user_info(UID)))
    for element in friends_list:
        birth_date = element['bdate'].split('.')[2]
        current_age = int(date.year) - int(birth_date)
        if current_age not in age_dict:
            age_dict[current_age] = 1
        else:
            age_dict[current_age] = age_dict[current_age] + 1
    sorted_res = OrderedDict(sorted(age_dict.items(), key=lambda t: t[0]))
    sorted_res = OrderedDict(sorted(sorted_res.items(), key = lambda t: t[1], reverse = True))
    return list(sorted_res.items())

if __name__ == '__main__':
    res = calc_age('reigning')
    print(res)
