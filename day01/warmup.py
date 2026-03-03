nums = [3, 1, 4]
nums.append(2)
nums.remove(1)
nums.sort()
print("nums:",nums)

student = {"name": "ZhangSan", "score": 90}
student["score"] = 95
print("student:",student)
print("get age default:", student.get("age", 0))

s = " hello,world "
print(s.strip())
print(s.strip().split(","))
print("-".join(["a", "b", "c"]))

total = 0
for i in range(1,6):
    total += i
print("sum 1 .. 5 =", total)

text = "  apple , banana , cherry "
result = [x.strip() for x in text.strip().split(",")]
print(result)