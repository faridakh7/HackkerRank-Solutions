def swap_case(s):
    result=""
    for i in s:
        if i.islower():
            result+=i.upper()
        else:
            result+=i.lower()
    return result

