"""""
Write a function that takes a list of strings and prints them, one per line, in a rectangular frame. For example the list
["Hello", "World", "in", "a", "frame"] gets printed as:

* * * * *
* Hello *
* World *
* In    *
* A     *
* Frame *
* * * * *
"""""

def frame(list_of_strings):
    maxLength = len(list_of_strings[0])

    for string in list_of_strings:
        if len(string) > maxLength:
            maxLength = len(string)

    print("* " * (int(maxLength / 2) + 3))

    for string in list_of_strings:
        print("* " + string + " " * (maxLength - len(string)) + " *")

    print("* " * (int(maxLength/2) + 3))

frame(["Hello", "World", "in", "a", "frame"])