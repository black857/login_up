import pickle as p
import os

os.chdir(r'E:/python/learnpython/login_up')
a = {
'2148537445':['2148537445','huitong','xxx','2447687327@qq.com','1593572486','nijiaosha','cxk']
}
f = open('User','wb')
p.dump(a,f)

# b = p.load(f)
# print(b)
f.close()