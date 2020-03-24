import easygui as g     #GUI
import pickle as p      #写（读取）用户信息
import random           #随机二维码
import os               #用来写系统路径分割符和......

errortime = 0           #记录输入密码时错误次数。
find_score = 0          #记录找回密码时的分数
error_information = []  #记录用户找回密码时填错的选项

#登录
def log_in():
	#以只读二进制模式打开用户信息文件并读取
	f = open('s%s%User' % (os.pardir,os.sep),'bw')
	user = f.read()
	f.close()
	while 1:
		field = g.multpasswordbox(msg = '请输入账号密码',title = '\t登录\t',fields = ['*账号','*密码'])
	
		#判断用户是否退出程序
		if field == None:
			return False
		
		#判断账号密码是否为空
		if '' in field:
			msgbox(mag = '请输入账号和密码！')
			continue
	
		#判断账号是否存在
		if field not in user:
			msgbox('改账号不存在')
			field = g.multpasswordbox(msg = '请输入账号密码',title = '\t登录\t',fields = ['*账号','*密码'])
			continue
		
		#判断密码是否正确
		if not(field[1] == user[field[0]][5]):
			msgbox(msg = '密码输入错误！',title = '\tError\t')
			errortime += 1
			continue
			
		break    #莫得问题就跳出循环吧。
		
	return True
	
#找回密码
def findpassword():
	while 1:
		find_information = gui.multenterbox(msg = '请输入信息',title = '\t找回密码\t',fields = ['账号','用户名','真实姓名','邮箱'])
			
		# 判断是否取消
		if find_information = None:
			return False
		
		find_answer = enterbox(msg = user[5],title = '找回密码')
		if find_answer == user[6]:
			find_score += 2.5
			break
			
		# 检查账号是否存在
		for i in user:
			if i[0] = find_information[0]:
				break
		else:
			msgbox(msg = '账号不存在'title = 'Error')
			continue
				
		# 检查信息是否正确
		if not user[0] = find_information[0]:
			error_information.append('账号')
		else:
			find_score += 1
		if not user[1] = find_information[1]:
			error_information.append('用户名')
		else:
			find_score += 1
		if not user[2] = find_information[2]:
			error_information.append('真实姓名')
		else:
			find_score += 1
		if not user[3] = find_information[3]:
			error_information.append('邮箱')
		else:
			find_score += 1
		
		# 判断找回是否成功
		if find_score >= 6:
			msgbox(msg = '找回成功！',title = '成功！')
			msgbox(msg = user[find_information[0]],title = '成功！')
			break
		else:
			msgbox(msg = '找回失败...\n以下选项填写错误：\ns%' % error_information,title = '失败')
			continue
			
def 	
			
			
			