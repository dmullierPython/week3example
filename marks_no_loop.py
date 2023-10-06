if __name__ == '__main__':
    # non loop version
    marks = []
    mark = input("enter mark 1 ")
    marks = marks + [mark]
    mark = input("enter mark 2 ")
    marks = marks + [mark]
    mark = input("enter mark 3 ")
    marks = marks + [mark]
    mark = input("enter mark 4 ")
    marks = marks + [mark]
    mark = input("enter mark 5 ")
    marks = marks + [mark]
    print("Marks are : ")
    print(marks)
    print("highest is ", max(marks))
    print("lowest is ", min(marks))