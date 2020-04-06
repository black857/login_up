import easygui as gui   #GUI
import pickle           #写（读取）用户信息
import random           #随机验证码
import os               #用来写系统路径分割符和......

#以只读二进制模式打开用户信息文件并读取
os.chdir('E:\\python\\learnpython\\login_up')
reload()

errortime = 0                                                                             #记录输入密码时错误次数。
find_score = 0                                                                            #记录找回密码时的分数
error_information = []                                                                    #记录用户找回密码时填错的选项
user_presence = False                                                                     #记录找回密码和注册时账号是否存在
fields_find = ['账号','用户名','真实姓名','邮箱']                                         #记录找回密码时的选项
fields_logup = ['账号','用名户','真实姓名','邮箱','密码','找回密码时的问题','问题的答案'] # 注册时的选项
listcodes = os.listdir(r'E:/python/learnpython/login_up/code')                            #记录验证码的列表



#登录
def log_in():
    global errortime
    while True:
        fields_imfor_login = gui.multpasswordbox(msg = '请输入账号密码',title = '\t登录\t',fields = ['*账号','*密码'])

        #判断用户是否退出程序
        if fields_imfor_login == None:
            return False
		
        #判断账号是否为纯数字
        if not fields_imfor_login[0].isdigit():
            gui.msgbox('账号只可以包含数字')
            continue
        
        #判断账号密码是否为空
        if '' in fields_imfor_login:
            gui.msgbox(msg = '请输入账号和密码！')
            continue
	
        #判断账号是否存在
        if fields_imfor_login[0] not in user:
            gui.msgbox('改账号不存在')
            continue
		
		#判断密码是否正确
        if not(fields_imfor_login[1] == user[fields_imfor_login[0]] [4]):
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
    global find_score,user_presence,user,user_presence
    while 1:
        find_information = gui.multenterbox(msg = '请输入信息',title = '\t找回密码\t',fields = fields_find)
			
		# 判断是否取消
        if find_information == None:
            return False

        # 检查账号是否存在
        for i in user.keys():
            if i == str(find_information[0]):
                break
        else:
            gui.msgbox(msg = '账号不存在',title = 'Error')
            continue
		
        # 检查找回密码的问题是否正确
        find_answer = gui.enterbox(msg = user[find_information[0]][5],title = '找回密码')
        if find_answer == user[find_information[0]][6]:
            find_score += 2.5
        for i in range(4):
            if user[find_information[0]][i] != find_information[i]:
                error_information.append(fields_find[i])
            else:
                find_score += 1

		# 判断找回是否成功
        if find_score >= 5:
            msg = ''    # 暂时显示用户信息的列表
            
            # 输出用户信息
            for i in range(7):
                msg += fields_logup[i] + ':' + user[find_information[0]][i] + '\n'
            gui.msgbox(msg = msg,title = '成功！')
            del msg
            return True
        
        else:
            # 提示错误的选项
            gui.msgbox(msg = '找回失败...\n以下选项填写错误：\n%s' % error_information,title = '失败')
            continue

# 注册 
def  log_up():
    global user,user_presence
    while 1:
        # 收集用户信息
        fields_imfor_logup = gui.multenterbox(msg = '请输入信息',title = '注册',fields = fields_logup)
        # 判断用户是否取消
        if fields_imfor_logup == None:
            return False
        # 确认用户是否存在
        for each_user in user.values():
            if fields_imfor_logup[0] == each_user[0]:
                gui.msgbox(msg = '这个账号太受欢迎，换一个吧！',title = '....')
                user_presence = True
                break
            if each_user[1] == fields_imfor_logup[1]:
                print('hahaha')
                gui.msgbox(msg = '这个用户名太受欢迎，换一个吧！',title = '....')
                user_presence = True
                break
        if user_presence:
            continue
        user_presence = False
        
        # 检查用户信息是否合法
        if not fields_imfor_logup[0].isdigit():
            gui.msgbox('账号只能由数字组成。')
            continue
        if '@' not in fields_imfor_logup[3]:
            gui.msgbox('邮箱不正确。')
            continue
        
        # 记录信息
        if captcha():
            user[fields_imfor_logup[0]] = fields_imfor_logup
            reload('wb')
            pickle.dump(user,f)
            return True
        else:
            break

# 修改用户信息
def modift():
    while 1:
        temp = gui.passwordbox(msg = '输入您想修改的账号及其密码',title = '----三思而后行----')
        if captcha():
            # 验证账号密码
            for i in user.keys():
                if i == temp[0]:
                    # 检验密码
                    if user[4] = temp[2]:
                        # 登录成功
                    else:
                        # 失败
                else:
                    gui.msgbox(msg = '')
            # 进入修改
        
        else:
            continue    
        
# 用于初始化用户信息
def reload(mode = 'rb'):
    f = open('User',mode)
    user = pickle.load(f)
    f.close()

# 用于生成验证码
def captcha():
    while 1:
        # 随机验证码
        code = random.choice(listcodes)
        # 输入验证码
        index_code = gui.enterbox(msg = '输入验证码',title = '注册',image = 'code%s%s' % (os.sep,code))
            
        # 检查验证码是否为空 或 用户是否取消
        if index_code == None:
            return False

        # 检查验证码
        if index_code == code[:4]:
            return True
        else:
            gui.msgbox(msg = '验证码输入有误',title = '错误')



# 用户选择
while 1:
    choice = gui.choicebox(msg = '您想执行哪些操作',choices = ['登录','注册','找回密码','退出'])
    if choice == '登录':
        if log_in():
            gui.msgbox(msg = '登录成功',title = '成功')
        else:
            continue
    elif choice == '注册':
        if log_up():
            gui.msgbox('注册成功！！') 
        else:
            continue
    elif choice == '退出' or choice == None:
        a = 0
        break
    else:
        if not findpassword():
            continue