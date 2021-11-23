'''数据表记录包含表索引和数值（int范围的正整数），请对表索引相同的记录进行合并，即将相同索引的数值进行求和运算，输出按照key值升序进行输出。


提示:
0 <= index <= 11111111
1 <= value <= 100000

输入描述：
先输入键值对的个数n（1 <= n <= 500）
然后输入成对的index和value值，以空格隔开

输出描述：
输出合并后的键值对（多行）

'''

if __name__ == '__main__':
    n = int(input())
    list1 =[]
    for one in range(n):
        key_value = input()
        key1 = int(key_value.split(" ")[0])
        value1 = int(key_value.split(" ")[1])
        list1.append((key1,value1))
    dict1 = {}
    for list in list1:
        if list[0] in dict1.keys():
            dict1[list[0]] = dict1[list[0]] + list[1]
        else:
            dict1[list[0]] = list[1]
    for i in sorted(dict1.keys()):
        print(i,dict1[i])
