#DemoList.py

colors = ["red","blue","green"]

print(len(colors))
print(colors)
print(colors[0])
print(type(colors))

# 디버그
# 중단점을 먼저 지정
# step by step
for item in colors:
    print(item)

colors.append("white")
print(colors)
colors.append("pink")
print(colors)

colors +=["red"]
print(colors)
colors += "red"
print(colors)

colors.remove("red")
print(colors)
colors.append("yellow")
print(colors)

#set를 연습
a={1,2,3,3}
b={3,4,4,5}
print(a)
print(b)
print(a.union(b))
print(a.intersection(b))


#tuple은 주로 묶어서 처리
#초록색, 바구나 , 빨간색 바구니
tp = (1,2,3)
print(tp)
print(type(tp))
print(len(tp))


#함수 정의(보통은 하나의 값을 리턴)
#여려개를 묶어서 Tuple로 리턴
def calc(a,b):
    return a+b, a*b

