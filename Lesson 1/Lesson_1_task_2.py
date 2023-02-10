# 2. Изучить список открытых API (https://www.programmableweb.com/category/all/apis). Найти среди них любое, требующее
# авторизацию (любого типа). Выполнить запросы к нему, пройдя авторизацию. Ответ сервера записать в файл.
# Если нет желания заморачиваться с поиском, возьмите API вконтакте (https://vk.com/dev/first_guide). Сделайте запрос,
# чтобы получить список всех сообществ на которые вы подписаны.

import vk_api
import json


session = vk_api.VkApi(token='vk1.a.CsRzpdEv8GFxTbGwwVzjTM86mwmwy5UMG5yUpm75V49sjWDYrN9njYOdtmsD-fb_F6BXP4Y3TVyn1o6eT-kePEK2NKAZ4JHMvpTmstMRHw_ixYsVXxH5o0-MmXjJzllysj3LWJN0xq2GN2632AaIkBHey6PWpJMHUEaoEcb8EM9pD6CffbZXMg_dKcEBW9CivvxCC2t_dIivUmAzxvq1Vw')


def get_friends_status(user_id):
    info = []
    friends = session.method('friends.get', {'user_id': user_id})
    for friend in friends["items"]:
        user = session.method("users.get", {"user_ids": friend})
        info.append(user[0]['first_name'] + ' ' + user[0]['last_name'])
        print(f"{user[0]['first_name']} {user[0]['last_name']}")
        filename = 'info.json'
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(info, f)
    print(info)


get_friends_status(4352738)



