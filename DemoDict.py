# DemoDict.py

d = dict(a=1, b=2, c=3)

print(d)
print(type(d))

color = {"apple":"red", "banna":"yellow"}
print(color)
print(type(color))

# 반복구문
for item in color.items():
    print(item)

# 키과 값으로 받기
# 중단점(Break Point)
for k,v in color.items():
    print(k,v)

# 입력
color["kiwi"] = "green"
print(color)
print("---삭제---")
del color["apple"]
print(color)
