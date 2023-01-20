N = int(input())
member = []
for _ in range(N):
    age, name = map(str, input().split())
    age = int(age)
    member.append((age, name))
sorted_member = sorted(member, key=lambda x: x[0])
for mem in sorted_member:
    print(mem[0], mem[1])