# 집합은 중복이 안됨, 순서가 없음

my_set = {1,2,3,4,5,5,5,5}
print(my_set)

java = {"유재석", "양세형", "김종국"}
python = set(["유재석"])

# 교집합
print(java & python)
print(java.intersection(python))

# 합집합
print(java | python)
print(java.union(python))

# 차집합
print(java - python)
print(java.difference(python))