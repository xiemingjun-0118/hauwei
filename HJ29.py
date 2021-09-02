'''
字符串加解密
1、对输入的字符串进行加解密，并输出。

2、加密方法为：

当内容是英文字母时则用该英文字母的后一个字母替换，同时字母变换大小写,如字母a时则替换为B；字母Z时则替换为a；

当内容是数字时则把该数字加1，如0替换1，1替换2，9替换0；

其他字符不做变化。

3、解密方法为加密的逆过程。


本题含有多组样例输入。
输入描述：
输入说明
输入一串要加密的密码
输入一串加过密的密码

输出描述：
输出说明
输出加密后的字符
输出解密后的字符
'''

def jiami(str1):
    s=''
    #当内容是英文字母时则用该英文字母的后一个字母替换，同时字母变换大小写,如字母a时则替换为B；字母Z时则替换为a
    for one in str1:
        if one.isalpha():
            if one == 'Z':
                s = s + 'a'
            elif one == 'z':
                s = s + 'A'
            else:
                s = s + chr(ord(one.swapcase()) + 1)
        elif one.isdigit():
            if int(one) == 9:
                s = s+'0'
            else:
                s = s+str(int(one)+1)
        else:
            s=s+one
    return s

def jiemi(str1):
    s=''
    #解密方法为加密的逆过程
    for one in str1:
        if one.isalpha():
            if one == 'A':
                s = s + 'z'
            elif one == 'a':
                s = s + 'Z'
            else:
                s = s + chr(ord(one.swapcase())-1)
        elif one.isdigit():
            if int(one) == 0:
                s = s+'9'
            else:
                s = s+str(int(one)-1)
        else:
            s=s+one
    return s

if __name__ == '__main__':
    # s1 = input("输入一串要加密的密码:")
    # print(jiami(s1))
    # s2 = input("输入一串要解密的密码:")
    # s2 = '5H706q4ZyqmI30wao78ES57M5xxT9gQ8k23b2wC61uy919OY0Ih44NLKSn0vq8c3KN'
    print(jiami(s2))
