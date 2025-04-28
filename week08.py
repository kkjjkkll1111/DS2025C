def post_order(node):
    if node:
        post_order(node.left)
        post_order(node.right)
        print(node.data, end=" -> ")

class TreeNode:
    def __init__(self):
        self.left = None
        self.right = None
        self.data = None

def insert(root, value):
    new_node = TreeNode()
    new_node.data = value

    if root is None: # first node
        return  new_node

    current = root
    while True: # second node ~ last node
        if value < current.data:
            if current.left is None:
                current.left = new_node
                break
            current = current.left # move
        else:
            if current.right is None:
                current.right = new_node
                break
            current = current.right # move
    return root


if __name__ == "__main__":
    numbers  = [10, 15, 8, 3, 9]
    # numbers = [10, 15, 8, 3, 9, 1, 7, 100]
    root = None

    # 1번 원소 부터 마지막 원소 까지
    for number in numbers:
        root = insert(root, number)

print("BST 구성 완료")

post_order(root)

# find_number = int(input())
# current = root
# while True:
#     if find_number == current.data:
#         print(f"{find_number}를 찾았습니다.")
#         break
#     elif find_number < current.data:
#         if current.left is None:
#             print(f"{find_number}를 찾지 못했습니다.")
#             break
#         current = current.left
#     else:
#         if current.right is None:
#             print(f"{find_number}를 찾지 못했습니다.")
#             break
#         current = current.right
