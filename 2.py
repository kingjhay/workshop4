# ex 1
string_upper_list = []
string_list = ["jae", "zeus", "jaem", "marc", "ryu"]

for string in string_list:
    # string jae
    string_upper_list.append(string.upper()) #string JAE
print("string_upper_list", string_upper_list)


string_list = ["jae", "zeus", "jaem", "marc", "ryu"]
string_upper_list = [string.upper() for string in string_list]
print("string_upper_list", string_upper_list)

# ex 2
number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = [number for number in number_list if number > 5]
print ("result",result)

result = []
number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for number in number_list:
    if number > 5:
        result.append(number)
print ("result",result)


# ex 3
number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
mod_number = [0 if number % 2 == = else 1 for number in number_list]
print ("mod_number",mod_number)

number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
mod_number = []
for number in number_list:
    if number % 2 == 0:
        mod_number.append(0)
    else:
        mod_number.append(1)
print ("mod_number",mod_number)
#จงแสดง "rat"
animal = ["cat", "bat", "rat", "dog"]
print(______)

#จงแก้ไขข้อมูลจาก "cat" เป็น "hen"
animal = ["cat", "bat", "rat", "dog"]
_______ = _______

#จงเพิ่ม "hen" ไปยัง animal list
animal = ["cat", "bat", "rat", "dog"]
_______

#จงเพิ่ม "hen" ไประหว่าง "rat" กับ "ิิdog"
animal = ["cat", "bat", "rat", "dog"]
_______

#จงลบ "rat" จาก list
animal = ["cat", "bat", "rat", "dog"]
_______

#จงแสดงตัวสุดท้ายของ animal
animal = ["cat", "bat", "rat", "dog"]
_______

#จงแสดงจำนวนของ animal
animal = ["cat", "bat", "rat", "dog"]
_______