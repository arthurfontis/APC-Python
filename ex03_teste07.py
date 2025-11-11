def lists():
    listOne = []
    listTwo = []
    listMedias = []

    for i in range(10):
        number = int(input())
        if i < 5:
            listOne.append(number)
        else:
            listTwo.append(number)
    result_zip = zip(listOne, listTwo)
    list_tuple = list(result_zip)

    for a in list_tuple:
        media = (a[0] + a[1]) / 2
        listMedias.append(media)

    print(list_tuple)
    print(listMedias)


lists()