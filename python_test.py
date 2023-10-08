import re
def isStrongPassword(password):
    # 长度不少于8个字符
    lenRegex = re.compile(r'.{8,}', re.DOTALL)
    # 至少有一位数字
    numRegex = re.compile(r'\d')
    # 同时包含大写和小写字符
    strRegex = re.compile(r'[a-z].*[A-Z]|[A-Z].*[a-z]')

    ret = True
    for i in range(len(password)):
        if lenRegex.search(password[i]) and numRegex.search(password[i])\
            and strRegex.search(password[i]):
            print('password: ' + password[i] + ' OK')
        else:
            print('password: ' + password[i] + ' FAILED')
            ret = False

    return ret
# 输入的密码
password = ['Asasf15safd', 'sfdsdgssaf', '25315612124', 'sfAsa1', 'AssvD152fff']
isStrongPassword(password)
