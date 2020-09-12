if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    new_arr = list(dict.fromkeys(arr))
    new_arr.sort()
    print(new_arr[-2])
