import sys

def get_path(size, step):
    result = []
    index = 0
    while True:
        result.append(str(index + 1))
        index = index + step - 1
        if index >= size:
            index = index % size
        if index == 0:
            break
        index = (index + 1) % size
    return ''.join(result)

if __name__ == "__main__":
    n1 = int(sys.argv[1])
    m1 = int(sys.argv[2])
    n2 = int(sys.argv[3])
    m2 = int(sys.argv[4])

    path1 = get_path(n1, m1)
    path2 = get_path(n2, m2)

    print(path1 + path2)

