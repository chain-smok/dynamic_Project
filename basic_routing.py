import json

with open('member.json') as f:
  info = json.load(f)

print('school:',info['school'])
print('\nteacher:',info['teacher'])
print('\nProjectname:',info['Projectname'])
print('\n組員資料')
print('_____________________________________________')
for members in info['member']:
    print("名字:%s 學號:%s 性別:%s"%(members['name'],members['number'],members['gender']))
