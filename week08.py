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

def search(root, target):
    current = root
    while True:
        if target == current.data:
            return f"{target}를 찾았습니다."
        elif target < current.data:
            if current.left is None:
                return f"{target}를 찾지 못했습니다."
            current = current.left
        else:
            if current.right is None:
                return f"{target}를 찾지 못했습니다."
            current = current.right


if __name__ == "__main__":
    numbers  = [10, 15, 8, 3, 9]
    # numbers = [10, 15, 8, 3, 9, 1, 7, 100]
    root = None

    # 1번 원소 부터 마지막 원소 까지
    for number in numbers:
        root = insert(root, number)

print("BST 구성 완료")

post_order(root)
print()
print(search(root, 10))


