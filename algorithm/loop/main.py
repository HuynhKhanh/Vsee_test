def draw_pyramid():
    n = int(input())
    for i in range(n):
        chuoi = ''
        for j in range(n-i-1):
            chuoi += ' '
        for k in range(2 * i + 1):
            chuoi += '*'
        print(chuoi)


if __name__ == '__main__':
    draw_pyramid()

