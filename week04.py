import random


class Node:
       def __init__(self, data, link=None):
           self.data = data
           self.link = link

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if not self.head:
            self.head = Node(data)
            return
        current = self.head
        while current.link:
            current = current.link
        current.link = Node(data)


    def search(self, target):
        current = self.head
        while current.link:
            if target == current.data:
                return f"{target}을 찾았습니다"
            else:
                current = current.link
        return f"{target}은 링크드 리스트에 존재 하지 않습니다."


    def __str__(self):
        current = self.head
        out_texts = ""
        while current is not None:
            out_texts = out_texts + f"{current.data} -> "
            current = current.link
        return out_texts + "END"


# ll = LinkedList()
# ll.append(8)
# ll.append(10)
# ll.append(-9)
# print(ll)
# print(ll.search(-9))

ll = LinkedList()
for _ in range(20):
    ll.append(random.randint(1,30))
print(ll)
print(ll.search(8))