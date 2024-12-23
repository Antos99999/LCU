import os
import requests

def ImageDownload(champList):
    #print("Test")

    DownloadedChamipon = []
    championsPath = 'ChampionsImg/'
    ItemsInPath = os.listdir(championsPath)
   # print(ItemsInPath)

    for i in ItemsInPath:
        #file_name = os.path.basename(i)
        file = os.path.splitext(i)[0]
        DownloadedChamipon.append(file)

    #print(DownloadedChamipon)
    #print(champList)

    for i in champList:
        if i in DownloadedChamipon:
            #print("Jest!")
            continue
        else:
            #print("Dodany!")
            url = 'https://ddragon.leagueoflegends.com/cdn/14.24.1/img/champion/'+str(i)+'.png'
            response = requests.get(url)
            with open("ChampionsImg/" + str(i) + ".png", "wb") as file:
                file.write(response.content)
            DownloadedChamipon.append(i)

    # print(DownloadedChamipon)


# champ = ['Chogath', 'Elise', 'Kennen', 'Corki', 'Renata', 'Aatrox', 'Zed', 'Viktor', 'Caitlyn', 'Maokai']
# ImageDownload(champ)