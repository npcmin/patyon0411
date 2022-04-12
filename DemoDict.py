# DemoDict.py
a = (1,2,3)
b = list(a)
print(b)
b.append(4)
print(b)

#딕셔너리 연습
color = {"apple":"red", "banana":"yellow"}
print(type(color))
print(color["apple"])

#반복구문
for item in color.items():
    print(item)

for k,v in color.items():
    print(k,v)

device = {"아이폰":5, "아이패드":10, "윈도우타블렛":20}
print(device)

device["맥프레"] = 15
device["아이폰"] = 6
print(device)

