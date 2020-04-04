import easygui as gui   #GUI
import pickle           #写（读取）用户信息
import random           #随机验证码
import os               #用来写系统路径分割符和......

#以只读二进制模式打开用户信息文件并读取
os.chdir('E:\\python\\learnpython\\login_up')
f = open('User','rb')
user = pickle.load(f)
f.close()

errortime = 0                   #记录输入密码时错误次数。
find_score = 0                  #记录找回密码时的分数
error_information = []          #记录用户找回密码时填错的选项
b = False                       #记录注册时账号是否存在
listcodes = os.listdir(r'E:/python/learnpython/login_up/code')  #记录验证码的列表


#登录
def log_in():
    global errortime
    while True:
        field = gui.multpasswordbox(msg = '请输入账号密码',title = '\t登录\t',fields = ['*账号','*密码'])

        #判断用户是否退出程序
        if field == None:
            return False
		
        #判断账号是否为纯数字
        if not field[0].isdigit():
            gui.msgbox('账号只可以包含数字')
            continue
        
        #判断账号密码是否为空
        if '' in field:
            gui.msgbox(msg = '请输入账号和密码！')
            continue
	
        #判断账号是否存在
        if field[0] not in user:
            gui.msgbox('改账号不存在')
            continue
		
		#判断密码是否正确
        if not(field[1] == user[field[0]] [4]):
            find_choice = gui.buttonbox(msg = '密码输入错误！\n要找回密码吗？',title = '\tError\t',choices = ['重新尝试','找回密码'])
            if find_choice == '找回密码':
                if findpassword():
                    return True
                else:
                    continue
            else:
                continue

        return True    #莫得问题就跳出循环吧。
	
#找回密码
def findpassword():
    global find_score
    while 1:

        find_information = gui.multenterbox(msg = '请输入信息',title = '\t找回密码\t',fields = ['账号','用户名','真实姓名','邮箱'])
			
		# 判断是否取消
        if find_information == None:
            return False
		
        find_answer = gui.enterbox(msg = user[5],title = '找回密码')
        if find_answer == user[6]:
            find_score += 2.5
            break
			
		# 检查账号是否存在
        for i in user:
            if i[0] == find_information[0]:
                break
        else:
            gui.msgbox(msg = '账号不存在',title = 'Error')
            continue
				
		# 检查信息是否正确
        if not user[0] == find_information[0]:
            error_information.append('账号')
        else:
            find_score += 1
        if not user[1] == find_information[1]:
            error_information.append('用户名')
        else:
            find_score += 1
        if not user[2] == find_information[2]:
            error_information.append('真实姓名')
        else:
            find_score += 1
        if not user[3] == find_information[3]:
            error_information.append('邮箱')
        else:
            find_score += 1
		
		# 判断找回是否成功
        if find_score >= 6:
            gui.msgbox(msg = '找回成功！',title = '成功！')
            gui.msgbox(msg = user[find_information[0]],title = '成功！')
            return True
        else:
            gui.msgbox(msg = '找回失败...\n以下选项填写错误：\n%s' % error_information,title = '失败')
            continue

# 注册 
def  log_up():
    while 1:
        # 收集用户信息
        field = gui.multenterbox(msg = '请输入信息',title = '注册',fields = ['账号','用名户','真实姓名','邮箱','密码','找回密码时的问题','问题的答案'])
        # 判断用户是否取消
        if field == None:
            return False
        # 确认用户是否存在
        for each_user in user.values():
            if field[0] != each_user[0]:
                b = True
                break
            if each_user[1] != field[1]:
                b = True
                break
        
        if not b:
            gui.msgbox('账号(或用户名已存在)')
            continue
        
        while 1:
            # 随机验证码
            code = random.choice(listcodes)
            # 输入验证码
            index_code = gui.enterbox(msg = '输入验证码',title = '注册',image = 'code%s%s' % (os.sep,code))
            
            # 检查验证码是否为空
            if index_code == None:
                return False
            
            # 检查验证码
            if index_code == code[:4]:
                
                # 记录信息
                user[field[0]] = field
                f = open('User','wb')
                f.write(user)
                f.close()
                return True
            
            else:
                gui.msgbox(msg = '输入错误...')
                continue



while 1:
    choice = gui.choicebox(msg = '您想执行哪些操作',choices = ['登录','注册','找回密码','退出'])
    if choice == '登录':
        if log_in():
            gui.msgbox(msg = '登录成功',title = '成功')
        else:
            continue
    elif choice == '注册':
        if log_up():
            gui.msgbox(msg = '注册成功',title = '成功')
        else:
            continue
    elif choice == '退出' or choice == None:
        a = 0
        break
    else:
        if findpassword():
            gui.msgbox(msg = '找回成功',title = '成功')
        else:
            continue
