Abbreviate a Two Word Name


def abbrev_name(name):
    my_list = name.split()
    list_name = my_list[0]
    list_surname = my_list[1]
    
    return (list_name[0] + "." + list_surname[0]).upper()