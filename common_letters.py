# Find out common letters between two strings

def common_letters():
    first_string = input("Enter first string : ")
    second_string = input("Enter second string : ")

    s1 = set(first_string)
    s2 = set(second_string)
    c_letters = s1 & s2
    print(s1, s2)
    print(c_letters)


# common_letters()


# SECOND METHOD
def common_letters_2():
    first_string = input("Enter first string : ")
    second_string = input("Enter second string : ")

    i = []

    for ch in first_string:
        if ch not in second_string or ch in i:
            pass
        else:
            i.append(ch)

    print(i)


common_letters_2()
