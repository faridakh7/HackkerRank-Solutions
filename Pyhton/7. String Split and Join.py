def split_and_join(line):
    result=""
    for i in line:
        if i==" ":
            result+= "-"
        else:
            result += i
    return result
