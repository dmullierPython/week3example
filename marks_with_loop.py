if __name__ == '__main__':
    marks = []
    for loop in range(5):
        mark = input("enter mark ")
        marks = marks + [mark]
    print("Marks are : ")
    print(marks)
    print("highest is ", max(marks))
    print("lowest is ", min(marks))