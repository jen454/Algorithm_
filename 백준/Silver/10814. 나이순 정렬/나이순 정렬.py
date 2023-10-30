N = int(input())
List = []
for i in range(N):
    age,name = input().split()
    List.append((int(age),name))
sorted_list = sorted(List, key=lambda x:(x[0]))
for i in range(len(List)):
    print(sorted_list[i][0], sorted_list[i][1])