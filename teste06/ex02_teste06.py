def among():
    playerList = []
    creawmatesList = []
    qntd = int(input())
    for _ in range(qntd):
        username = input()
        playerList.append(username)
    impostor = input()
    impostoresList = impostor.split()
    for player in playerList:
        if player not in impostoresList:
            creawmatesList.append(player)
    print(*creawmatesList)

among()
        