'''
使用字典+自定义函数实现批量替换
'''

# 保存映射关系的函数,函数的主要功能是通过字典实现的
def replace_city(city_name):
    '''
    {"abc":123, "aaa":456}["abc"] 
    方括号中的字符串"abc"被称作字典的下标。通过下标，我们可以获得字典的值。
    通过这一行代码，你可以取出直接使用字典的值，而不需要对字典进行声明，也不需要为字典再起一个变量名。
    '''
    return {
        "GUANGDONG":"广东省",
        "HEBEI":"河北省",
        "HUNAN":"湖南省",
        "HANGZHOU":"杭州市"
    }[city_name]

# 根据映射关系实现批量循环
def replace_multi(strings, replaced_string):
    for pinyin_city in strings:
        replaced_string = replaced_string.replace(
            pinyin_city,replace_city(pinyin_city))
    return replaced_string
    
# 哪些城市要替换
citys = ("GUANGDONG", "HUNAN")

# 需要替换的字符串
string1 = """
GUANGDONG，简称“粤”，中华人民共和国省级行政区，省会广州。
因古地名广信之东，故名“GUANGDONG”。位于南岭以南，南海之滨，
与香港、澳门、广西、HUNAN、江西及福建接壤，与海南隔海相望。"""

string2 = replace_multi(citys, string1)
print(string2)
