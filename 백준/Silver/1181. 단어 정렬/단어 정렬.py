N = int(input())
List = []
for i in range(N):
    word = input()
    List.append(word)
sorted_list = set(List)
array = sorted(sorted_list, key=lambda x:(len(x),x))
for i in range(len(array)):
    print(array[i])