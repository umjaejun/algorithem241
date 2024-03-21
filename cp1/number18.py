# 문제 18번 
# (1) 파이썬의 리스트를 이용해 이를 구현하라.
"""
node = int(input("노드의 개수: "))
mylist = []

for i in range(node):
    data = int(input("노드 %d의 데이터: "%(i+1)))
    mylist.append(data)

print("리스트의 내용: ", mylist)
"""

# (2) 단순연결리스트 구조(그림 1.10(b))를 이용해 이를 구현하라.

class Node:
    def __init__(self, data, link):
        self.data = data
        self.link = link

def pList(front, CList="연결 리스트: "):
    print(CList, end="")
    n = front
    while n != None :
        print(n.data, end="->")
        n = n.link
    print()

front = None # 연결 리스트의 앞부분
back = None # 연결 리스트의 뒷부분
num = int(input("노드의 개수: "))
for i in range(num):
    data = int(input("노드 %d의 데이터: "%(i+1)))
    n = Node(data, None)
    if front == None :
        front = back = n # 연결 리스트가 없다면 처음 생성 
    else :
        back.link = n
        back = n
pList(front)