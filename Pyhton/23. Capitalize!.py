def solve(s):

    free_list = []
    mylist = s.split(' ')
    for char in mylist:
        free_list.append(char.capitalize())
    final = (' ').join(free_list)
    return final

