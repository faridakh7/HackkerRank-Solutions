if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    for key, value in student_marks.items():
        if key == query_name:
            adder = 0
            for v in value:
                adder += v
            result = adder/len(value)


print('{0:.{1}f}'.format(result, 2))
