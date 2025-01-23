
def find_max(st):
    """return the maximum element"""

    current_max = st[0]

    for i in range (1, len(st)):
        if st[i] > current_max:
            current_max = st[i]
    

    return current_max

test_list = [2112*i % 2024 for i in range(10000)]

print(find_max(test_list))
