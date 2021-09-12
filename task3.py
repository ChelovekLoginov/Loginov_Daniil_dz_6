import json
import sys

result_dict = {}
with open('users.csv', 'r', encoding='utf-8') as f1, \
        open('hobby.csv', 'r', encoding='utf-8') as f2:
    user = (el for el in f1.read().splitlines())
    hobby = (el for el in f2.read().splitlines())
    for hobby, users in zip(hobby, user):
        result_dict[users.strip()] = hobby.strip()
    for el in hobby:
        sys.exit(1)
    for users in user:
        result_dict[user.strip()] = None
print(result_dict)
with open('result.json', 'w', encoding='utf-8') as result:
    json.dump(result_dict, result, unsure_ascii=False)
