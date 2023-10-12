if __name__ == '__main__':
    NO_MARKS = 5
    marks = []
    for loop in range(NO_MARKS):
        mark = input("enter mark ")
        marks = marks + [mark]
    print("Marks are : ")
    print(marks)
    print("highest is ", max(marks))
    print("lowest is ", min(marks))