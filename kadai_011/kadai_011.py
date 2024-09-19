#for文で記載した場合
'''array = ["水","金","地","火","木","土","天","海","冥"]

for i in range(0,18):
    num = i
    if num > 8:
        num -= 9
    print(array[num])
'''
#while文で記載した場合
array = ["水","金","地","火","木","土","天","海","冥"]
i = 0
while i != 18:
    num = i
    if num > 8:
        num -= 9
    print(array[num])
    i += 1