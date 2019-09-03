##首先合并多个密码库为一个

f = open(r"E:\Python Projects\wifi_craking\birthday.txt",'r')

key_birthday = f.read()

f.close()


f = open(r"E:\Python Projects\wifi_craking\common.txt",'r')

key_common = f.read()

##print(key_common)

f.close()


f = open(r"E:\Python Projects\wifi_craking\english.txt",'r')

key_english = f.read()

f.close()


f = open(r"E:\Python Projects\wifi_craking\other-0.txt",'r')

key_other_0 = f.read()

f.close()


f = open(r"E:\Python Projects\wifi_craking\other-1.txt",'r')

key_other_1 = f.read()

f.close()


f = open(r"E:\Python Projects\wifi_craking\other-2.txt",'r')

key_other_2 = f.read()

f.close()


f = open(r"E:\Python Projects\wifi_craking\0_key_all.txt",'w')

f.writelines(key_birthday)

f.writelines(key_common)

f.writelines(key_english)

f.writelines(key_other_0)

f.writelines(key_other_1)

f.writelines(key_other_2)

f.close()















































