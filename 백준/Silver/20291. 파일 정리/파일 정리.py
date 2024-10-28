import sys

N = int(sys.stdin.readline().strip())
file_dict = {}

for _ in range(N):
    file = sys.stdin.readline().strip().split('.')[1]
    if file not in file_dict:
        file_dict[file] = 1
    else:
        file_dict[file] += 1
        
file_list = list(file_dict.keys())
file_list.sort()

for i in file_list:
    print(i, file_dict[i])