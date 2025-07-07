import time

def quick_sort(data, drawData, timeTick):
    quick_sort_algo(data, 0, len(data) - 1, drawData, timeTick)

def quick_sort_algo(data, head, tail, drawData, timeTick):
    if head < tail:
        partition_idx = partition(data, head, tail, drawData, timeTick)
        quick_sort_algo(data, head, partition_idx - 1, drawData, timeTick)
        quick_sort_algo(data, partition_idx + 1, tail, drawData, timeTick)

def partition(data, head, tail, drawData, timeTick):
    border = head
    pivot = data[tail]

    drawData(data, getColorArray(len(data), head, tail, border, border))
    time.sleep(timeTick)

    for j in range(head, tail):
        if data[j] < pivot:
            drawData(data, getColorArray(len(data), head, tail, border, j, True))
            time.sleep(timeTick)
            data[border], data[j] = data[j], data[border]
            border += 1
        drawData(data, getColorArray(len(data), head, tail, border, j))
        time.sleep(timeTick)

    drawData(data, getColorArray(len(data), head, tail, border, tail, True))
    time.sleep(timeTick)
    data[border], data[tail] = data[tail], data[border]
    return border

def getColorArray(length, head, tail, border, currIdx, isSwapping=False):
    colorArray = []
    for i in range(length):
        if i >= head and i <= tail:
            colorArray.append("gray")
        else:
            colorArray.append("white")

        if i == tail:
            colorArray[i] = "blue"
        elif i == border:
            colorArray[i] = "red"
        elif i == currIdx:
            colorArray[i] = "yellow"

        if isSwapping and (i == border or i == currIdx):
            colorArray[i] = "green"

    return colorArray
