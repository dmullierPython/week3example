import statistics
if __name__ == '__main__':
    NO_MARKS = 5
    marks = []
    while True:
        while True:
            mark = input("enter mark ")
            if not mark:
                break
            mark = int(mark)
            if 0 <= mark <= 100: #in java if (mark >0 && mark <=100)
                break
        if not mark:
            break
        marks = marks + [mark]
    print("Marks are : ")
    print(marks)
    print("highest is ", max(marks))
    print("lowest is ", min(marks))
    print("the median is", statistics.median(marks))