#check queue is full
def is_queue_full() -> bool:
    global SIZE, rear, front

    # Case 1: If the rear is not at the last index
    if rear != SIZE - 1:
        return False # queue is not full

    # Case 2: If rear is at the last index and front is -1,
    elif rear == SIZE - 1 and front == -1:
        return True # queue is truly full

    # Case 3: (some elements were dequeued),
    else:
        # Shift each element one position to the left
        for i in range(front + 1, SIZE):
            queue[i - 1] = queue[i]
            queue[i] = None
        # Shift front and rear one position to the left
        front = front - 1
        rear = rear - 1
        return False # queue is not full

# check queue is empty
def is_queue_empty() -> bool:
    global SIZE, front, rear
    if front == rear:
        return True
    else:
        return False

# enqueue method
def en_queue(data):
    global rear
    if is_queue_full(): #check queue is full
        print("queue is full")
        return None
    else:
        rear = rear + 1
        queue[rear] = data

# dequeue method
def de_queue():
    global front
    if is_queue_empty(): #check queue is full
        print("queue is empty")
        return None
    else:
        front += 1
        data = queue[front]
        queue[front] = None
        return data

#peek method
def peek():
    global front
    if is_queue_empty(): #check queue is full
        print("queue is empty")
        return None
    else:
        return queue[front + 1]


SIZE =  int(input("input queue size : "))
queue = [None for _ in range(SIZE)]
front = -1
rear = -1

if __name__ == "__main__":
    while(True):
        menu = input("enqueue(i), dequeue(e), peek(v), end(x) : ")
        if menu == 'x' or menu == 'X':
            print("program end")
            break
        elif menu == 'i' or menu == 'I':
            en_queue(input("input data : "))
            print(queue)
        elif menu == 'e' or menu == 'E':
            print(f"output data {de_queue()}")
            print(queue)
        elif menu == 'v' or menu == 'V':
            print(f"cheak data {peek()}")
            print(queue)
        else:
            print(f"{menu} is undefinded, please check your select")