import vk
import time

token = "2b5ae81ac576e88bb62d43335dd2523fd84df8463361066cd4249d64ea4d474a18a1d20a52e2e90400af8"
session = vk.Session(access_token=token)
vk_api = vk.API(session, v='5.89')


#метод считает количество общих элементов в двух листах
def count_common_elements(list_of_groups1: list, list_of_groups2: list):
    set1 = set(list_of_groups1)
    set2 = set(list_of_groups2)
    set1.intersection_update(set2)
    return len(set1)


# Считаем коэффициент Тонимото.
# k = (c/(a+b-c))
# a — количество элементов в первом множестве
# b — количество элементов во втором множестве
# c — количество общих элементов в двух множествах
def tanimoto(id_1: int, id_2: int):
    first_user_groups = vk_api.groups.get(user_id=id_1).get('items')
    second_user_groups = vk_api.groups.get(user_id=id_2).get('items')
    a = len(first_user_groups)
    b = len(second_user_groups)
    c = count_common_elements(first_user_groups, second_user_groups)
    k = (c / (a + b - c))
    return k


def list_of_top_matching_friends():  # метод для пользователя, чей токен сейчас используется
    userget = vk_api.users.get()
    id1 = userget[0]['id']
    friends = vk_api.friends.get().get('items')
    print(friends)
    result = list()
    for i in range(len(friends)):
        time.sleep(1)  # задержка, чтобы избежать "Too many request"
        if tanimoto(id1, friends[i]) > 0.1:
            list.append(friends[i])
            print(friends[i])
    return result


def list_of_top_matching_friends(id1):  # метод для любого пользователя
    friends = vk_api.friends.get(id1).get('items')
    print(friends)
    result = list()
    for i in range(len(friends)):
        time.sleep(1)  # задержка, чтобы избежать "Too many request"
        if tanimoto(id1, friends[i]) > 0.1:
            list.append(friends[i])
            print(friends[i])
    return result
