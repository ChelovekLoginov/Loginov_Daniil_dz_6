import sys

result_dict = {}
with open('users.csv', 'r', encoding='utf-8') as f1, \
        open('hobby.csv', 'r', encoding='utf-8') as f2:
    user = (el for el in f1.read().splitlines())
    hobbys = (el for el in f2.read().splitlines())
    for hobbys, user in zip(hobbys, user):
        result_dict[user.strip()] = hobbys.strip()
    for el in hobbys:
        sys.exit(1)
    for user in user:
        result_dict[user.strip()] = None
print(result_dict)
#with open('result.json')