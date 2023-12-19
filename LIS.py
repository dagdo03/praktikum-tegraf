def find_lis(arr):
    n = len(arr)
    lis = [1] * n
    previous_indices = [-1] * n 

    for i in range(1, n):
        for j in range(0, i):
            if arr[i] > arr[j] and lis[i] < lis[j] + 1:
                lis[i] = lis[j] + 1
                previous_indices[i] = j

    max_length = max(lis)
    max_index = lis.index(max_length)

    lis_sequence = []
    while max_index >= 0:
        lis_sequence.append(arr[max_index])
        max_index = previous_indices[max_index]

    lis_sequence.reverse()
    return max_length, lis_sequence




if __name__ == '__main__':
    lis_length = None
    lis_elements = None

    input_array = input('input_array')
    arr = list(map(int, input_array.split(',')))
    lis_length, lis_elements = find_lis(arr)
    print(lis_length)
    print(lis_elements)