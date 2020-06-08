import file_manager
import model

name = ''


def show_manager():
    content = file_manager.read_file('students_pages.txt') % name
    while True:
        print(content)
        operator = input('请选择1-5')
        if operator == '1':
            add_student()
        elif operator == '2':
            show_student()
        elif operator == '3':
            #modify_student()
            pass
        elif operator == '4':
            delete_student()
        else:
            return


def add_student():
    x = file_manager.read_json(name + '.json', {})
    if not x:  # 若x是{}
        student = []
        num = 0
    else:
        student = x['all_student']
        num = x['num']
    while True:
        s_name = input('请输入学生姓名：')
        s_age = input('请输入年龄：')
        s_gender = input('请输入性别：')
        s_tel = input('请输入电话号码：')
        s_id = 'stu' + str(num)
        s = model.Student(s_id, s_name, s_age, s_gender, s_tel)

        student.append(s.__dict__)
        data = {'all_student': student, 'num': len(student)}
        # 写入文件
        file_manager.write_json(name + '.json', data)
        choice = input('添加成功！\n1.继续\n2.返回')
        if choice == '2':
            break


def show_student():
    x = input('1.查看所有学生\n2.根据姓名查找\n3.根据学号查找\n其他：返回\n请选择：')
    y = file_manager.read_json(name + '.json', {})  # 第二个参数是文件不存在时返回的默认值
    if not y:  # 如果文件不存在，则y是{}
        students = []
    else:
        students = y['all_student']
    # studnet=y.get('all_student',[])
    if not students:
        print('该老师还没有学生')
        return

    # 查询全部学生
    if x == '1':
        for student in students:
            print('学号：{s_id}，姓名：{name}，性别：{gender}，年龄：{age}，电话：{tel}'.format(**student))

    # 按照姓名查询
    elif x == '2':
        same_name_students = []
        s_name = input('请输入学生姓名：')
        for student in students:
            if student['name'] == s_name:
                same_name_students.append(student)
        for student in same_name_students:
            print('学号：{s_id}，姓名：{name}，性别：{gender}，年龄：{age}，电话：{tel}'.format(**student))

    # 按学号查询
    elif x == '3':
        same_id_students = []
        s_id = input('请输入s_id：')
        for student in students:
            if student['s_id'] == s_id:
                same_id_students.append(student)
        for student in same_id_students:
            print('学号：{s_id}，姓名：{name}，性别：{gender}，年龄：{age}，电话：{tel}'.format(**student))

    else:
        return


# def modify_student():
#    pass


def delete_student():
    num = input('1.按姓名删\n2.按学号删\n其他：返回\n请选择：')
    y = file_manager.read_json(name + '.json', {})
    all_students = y.get('all_student', [])
    if not all_students:
        print('该老师还没有学生')
        return
    if num == '1':
        key = 'name'
        value = input('请输入要删除的学生的名字：')
    elif num == '2':
        key = 's_id'
        value = input('请输入要删除的学生的id：')
    else:
        return

    students = list(filter(lambda s: s.get(key, '') == value, all_students))
    if not students:
        print('没有找到对应的学生')
        return

    # 显示所有符合查询条件的学生信息
    for i, s in enumerate(students):
        print('{} 学号：{s_id}，姓名：{name}，性别：{gender}，年龄：{age}，电话：{tel}'.format(i, **s))
    n = input('请输入需要删除的学生的标号（0~{}），q-返回'.format(i))#i=len(students)-1
    if not n.isdigit() or not 0 <= int(n) <= i:
        print('输入内容不合法')
        return

    # 将学生从all_students里删除
    all_students.remove(students[int(n)])
    y['all_student']=all_students
    file_manager.write_json(name+'.json',y)
