

# Used to convert list representations of states and actions to string representations
def convert_list_to_string(lst):
    s = ""
    for row in lst:
        for element in row:
            s += str(element)
        s += ","
    return s[:-1]


# Used to convert string representations of states and actions to list representations
def convert_string_to_list(string):
    lst = []
    rows = string.split(",")
    for row_string in rows:
        row = []
        for element in row_string:
            row.append(int(element))
        lst.append(row)
    return lst
