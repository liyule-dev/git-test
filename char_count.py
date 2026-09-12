# 字符串字符统计
# 题目：接收用户输入的一段任意字符串，统计并输出其中英文字母、数字、空格、其他字符分别有多少个。
# 示例：输入  Hello World! 123 ，输出：字母10个，数字3个，空格2个，其他字符1个。
# 考察点：字符串遍历、if多分支判断、计数器变量、输入输出
# 进阶挑战：不区分大小写，额外统计每个字母出现的次数。
input_str=input("请输入一段任意字符串：")
letter_count=0
digit_count=0
space_count=0
other_count=0
letter_dict={}
for char in input_str:
    if char.isalpha():
        letter_count+=1
        char_lower=char.lower()
        letter_dict[char_lower]=letter_dict.get(char_lower, 0)+1
    elif char.isdigit():
        digit_count+=1
    elif char.isspace():
        space_count+=1
    else:
        other_count+=1
print(f"字母{letter_count}个，数字{digit_count}个，空格{space_count}个，其他字符{other_count}个。")
print("每个字母出现的次数：")
for letter, count in letter_dict.items():
    print(f"{letter}:{count}次",end=" ")