import  array
def move_zeros(l):
    zero_index = 0
    for i in range(len(l)):
        n = l[i]
        if n != 0:
            l[zero_index] = n
            if zero_index != i:
                l[i] = 0
            zero_index += 1
    return l

l = [99, 0, -7, 0, 16]
move_zeros(l)
print(l)