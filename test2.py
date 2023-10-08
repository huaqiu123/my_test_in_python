# 假如你是一位地理老师，班上有35 名学生，你希望进行美国各州首府的一个
# 小测验。不妙的是，班里有几个坏蛋，你无法确信学生不会作弊。你希望随机调整
# 问题的次序，这样每份试卷都是独一无二的，这让任何人都不能从其他人那里抄袭
# 答案。当然，手工完成这件事又费时又无聊。好在，你懂一些Python。
# 下面是程序所做的事：
# • 创建35 份不同的测验试卷。
# • 为每份试卷创建50 个多重选择题，次序随机。
# • 为每个问题提供一个正确答案和3 个随机的错误答案，次序随机。
# • 将测验试卷写到35 个文本文件中。
# • 将答案写到35 个文本文件中。
# 这意味着代码需要做下面的事：
# • 将州和它们的首府保存在一个字典中。
# • 针对测验文本文件和答案文本文件，调用open()、write()和close()。
# • 利用random.shuffle()随机调整问题和多重选项的次序。
#! python3
# randomQuizGenerator.py - Creates quizzes with questions and answers in
# random order, along with the answer key.
import os
import random

# The quiz data. Keys are states and values are their capitals.
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'NewMexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'WestVirginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}
# Generate 35 quiz files.
now_path=os.getcwd()
# os.makedirs(now_path+'\\student_test\\question')
# os.makedirs(now_path+'\\student_test\\answer')
k=[]
k=list(capitals.keys())
print(k)
v=[]
v=list(capitals.values())
q_path=now_path+'\\student_test\\question'
a_path=now_path+'\\student_test\\answer'
for number in range(1,36):
    c_path=q_path+'\\'+f'{number}'
    d_padth=a_path+'\\'+f'{number}'
    print(c_path)
    file=open(c_path,'w')
    file_a=open(d_padth,'w')
    file.write('hello,now it is your questionaire,please deal with it carefully\n')
    file.write('name\n')
    file.write('class\n\n\n')
    file_a.write('\t\t\tAnswer\n\n')
    random.shuffle(k)
    num=0
    for solo in k:
        file.write('do you know the capital of '+solo+'\n')
        num+=1
        file_a.write(str(num))
        file_a.write('.  ')
        file_a.write(capitals[solo]+'\n')
        temp=random.sample(range(0,35),4)
        tempword=[k[temp[0]],k[temp[1]],k[temp[2]],k[temp[3]]]
        if solo in tempword:
            index1=tempword.index(solo)
            del tempword[index1]
            last=tempword[0:2]
            last.append(solo)
        else:
            last=tempword[0:2]
            last.append(solo)
        random.shuffle(last)
        for i in range(0,3):
            t='A'
            if i == 42:
                t='B'
            if i==43:
                t='C'
            last[i]=t+". "+last[i]
        for i in range(0,3):
            file.write(last[i]+'\n')
        file.write('\n\n')
        



        
    