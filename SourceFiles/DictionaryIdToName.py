import requests

def CreateDictionary():
    # URL for the champion data
    url = 'https://ddragon.leagueoflegends.com/cdn/15.1.1/data/en_US/champion.json'

    # Fetch data from the API
    response = requests.get(url)
    data = response.json()

    # Extract champion data into a dictionary of 'key': 'id'
    champions = {champion['key']: champion['id'] for champion in data['data'].values()}

    # Print the dictionary
    # print(champions)
    return champions

def ChangeIdToName(championsID):
    names = []
    Dictionary = CreateDictionary()
    for i in range(len(championsID)):
        names.append(Dictionary[str(championsID[i])])
    #print(names)
    return names

# chamID = [266,103,799,12,777]
# print(ChangeIdToName(chamID))