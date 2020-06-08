import file_manager
import time
import student_manager


def start():
    print('runing...')
    content = file_manager.read_file('welcome.txt')
    while True:
        operator = input(content + '\n' + '请选择1-3')
        if operator == '1':
            print('您选择了登录')
            time.sleep(2)
            login()
        elif operator == '2':
            print('即将为您注册...')
            time.sleep(2)
            register()
        elif operator == '3':
            print('正在退出...')
            time.sleep(3)
            print('退出成功！欢迎下次使用')
            break
        else:
            print('输入有误！')


def register():
    data = file_manager.read_json('data.json', {})
    # print(data,type(data))
    while True:
        teacher_name = input('请输入账号（3~6位）')
        if not 3 <= len(teacher_name) <= 6:
            print("账号不符合要求，请重新输入！")
        else:
            break
    if teacher_name in data:
        print('注册失败！该用户已经注册！')
    while True:
        password = input('请输入密码（6~12位）')
        if not 6 <= len(password) <= 12:
            print("账号不符合要求，请重新输入！")
        else:
            break

    # 用户名和密码都输入正确后，需要保存起来
    data[teacher_name] = password
    file_manager.write_json('data.json', data)


def login():
    data = file_manager.read_json('data.json', {})
    teacher_name = input('请输入老师的账号：')
    if teacher_name not in data:
        print('登录失败！该账号没有注册！')
        return
    password = input('请输入密码：')
    if data[teacher_name] == password:
        print('登录成功！')
        student_manager.name = teacher_name
        student_manager.show_manager()
    else:
        print('密码错误，登录失败！')


start()
