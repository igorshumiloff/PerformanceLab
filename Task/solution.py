import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Использование: python solution.py <файл с числами>")
        sys.exit(1)

    file_path = sys.argv[1]

    nums = []
    with open(file_path, 'r') as f:
        for line in f:
            line = line.strip()
            if line:
                nums.append(int(line))

    if not nums:
        print("Массив пустой")
        sys.exit(1)

    sorted_nums = sorted(nums)
    n = len(sorted_nums)
    if n % 2 == 1:
        target = sorted_nums[n // 2]
    else:
        target = sorted_nums[n // 2 - 1]

    moves = sum(abs(x - target) for x in nums)

    if moves > 20:
        print("20 ходов недостаточно для приведения всех элементов массива к одному числу")
    else:
        print(moves)
