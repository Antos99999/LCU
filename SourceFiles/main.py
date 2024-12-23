from lcu_driver import Connector
import os
from os import path
import sys
from DataFromTimeline import match_timeline
import PySimpleGUI as sg
from dmgGraph import DMGGraph
import matplotlib.pyplot as plt
from FinallGraphCreator import GraphCreator

connector = Connector()

class Stats:
    def __init__(self,id,name,dmg,kill,death,assists,champ,team):
        self.id = id
        self.name = name
        self.dmg = dmg
        self.kill = kill
        self.death = death
        self.assists = assists
        self.champ = champ
        self.team = team

async def match_history(connection):
    RedGold = 0
    BlueGold = 0
    KillRed = 0
    KillBlue = 0
    AssistsRed = 0
    AssistsBlue = 0
    DeathsRed = 0
    DeathsBlue = 0
    totalDamageDealtToChampions = []
    SummonerArray = []
    stats_instances = {}
    teamBlue = []
    teamRed = []

    # Match ID
    #ID = 7228897664
    global ID

    # Connect via LCU Driver
    matchID = await connection.request('get', '/lol-match-history/v1/games/' + str(ID))

    # Close connection if data not found
    if matchID.status == 404:
        await connection.request('post', '/exit')
        exit(1)


    # Parsing data from JSON
    match_data = await matchID.json()

    # Reading data
    for i in range(len(match_data['participants'])):
        if (i < 5):
            #print(i)
            nazwaKlasy = f"Stats{i+1}"
            RedGold = RedGold + match_data['participants'][i]['stats']['goldEarned']
            KillRed = KillRed + match_data['participants'][i]['stats']['kills']
            AssistsRed = AssistsRed + match_data['participants'][i]['stats']['assists']
            DeathsRed = DeathsRed + match_data['participants'][i]['stats']['deaths']
            totalDamageDealtToChampions.append(match_data['participants'][i]['stats']['totalDamageDealtToChampions'])
            #teamRed
            # Tworzenie instancji Stats
            stats_instances[nazwaKlasy] = Stats(
                match_data['participants'][i]['participantId'],
                match_data['participantIdentities'][i]['player']['gameName'],
                match_data['participants'][i]['stats']['totalDamageDealtToChampions'],
                KillRed,
                DeathsRed,
                AssistsRed,
                match_data['participants'][i]['championId'],
                match_data['participants'][i]['stats']['win']
            )
        else:
            #print(i)
            nazwaKlasy = f"Stats{i+1}"
            BlueGold = BlueGold + match_data['participants'][i]['stats']['goldEarned']
            KillBlue = KillBlue + match_data['participants'][i]['stats']['kills']
            AssistsBlue = AssistsBlue + match_data['participants'][i]['stats']['assists']
            DeathsBlue = DeathsBlue + match_data['participants'][i]['stats']['deaths']
            totalDamageDealtToChampions.append(match_data['participants'][i]['stats']['totalDamageDealtToChampions'])
            stats_instances[nazwaKlasy] = Stats(
                match_data['participants'][i]['participantId'],
                match_data['participantIdentities'][i]['player']['gameName'],
                match_data['participants'][i]['stats']['totalDamageDealtToChampions'],
                KillRed,
                DeathsRed,
                AssistsRed,
                match_data['participants'][i]['championId'],
                match_data['participants'][i]['stats']['win']
            )

    for i in range(len(match_data['participantIdentities'])):
        player = match_data['participantIdentities'][i]['participantId']
        if i < 5:
            teamBlue.append(player)
        else:
            teamRed.append(player)

    # print(teamBlue)
    # print(teamRed)

    #for nazwa, instancja in stats_instances.items():
        #print(nazwa)
        #print(instancja.id)
        #print(instancja.name)
        #print(instancja.dmg)
        #print(instancja.kill)
        #print(instancja.death)
        #print(instancja.assists)
        #print(instancja.champ)
        #print(instancja.team)

    # Prepare data for return
    result = {
        "RedGold": RedGold,
        "BlueGold": BlueGold,
        "KillRed": KillRed,
        "KillBlue": KillBlue,
        "AssistsRed": AssistsRed,
        "AssistsBlue": AssistsBlue,
        "DeathsRed": DeathsRed,
        "DeathsBlue": DeathsBlue,
        "TotalDamageDealtToChampions": totalDamageDealtToChampions,
        "SummonerArray": SummonerArray,
        "teamBlue": teamBlue,
        "teamRed": teamRed
    }

    # Printing data
    # print("GoldR: " + str(RedGold))
    # print("GoldB: " + str(BlueGold))
    # print("KillR: " + str(KillRed))
    # print("KillB: " + str(KillBlue))
    # print("AssistR: " + str(AssistsRed))
    # print("AssistsB: " + str(AssistsBlue))
    # print("DeathsR: " + str(DeathsRed))
    # print("DeathsB: " + str(DeathsBlue))

    return result, stats_instances

async def GraphCreate(connection):
    os.makedirs("./Graphs", exist_ok=True)
    os.makedirs("./Image", exist_ok=True)
    os.makedirs("./ChampionsImg", exist_ok=True)
    global ID

    GoldW14 = []
    CSW14 = []

    timestamp = await connection.request('get', '/lol-match-history/v1/game-timelines/' + str(ID))

    # Close connection if data not found
    if timestamp.status == 404:
        await connection.request('post', '/exit')
        exit(1)

    # Parsing data from JSON
    timeline = await timestamp.json()

    y_final_blue = []
    y_final_red = []
    x_temp_blue = []
    y_temp_blue = []
    x_temp_red = []
    y_temp_red = []

    y_diff = []
    y_diff_add = []
    y_diff_odd = []


    for k in range(1,11):
        if k <= 5:
            x = match_timeline(timeline,k)[1]
            x_temp_blue.append(x)
            y = match_timeline(timeline,k)[2]
            y_temp_blue.append(y)
            g = match_timeline(timeline,k)[3]
            GoldW14.append(g)
            cs = match_timeline(timeline,k)[4]
            CSW14.append(cs)
        else:
            x = match_timeline(timeline,k)[1]
            x_temp_red.append(x)
            y = match_timeline(timeline,k)[2]
            y_temp_red.append(y)
            g = match_timeline(timeline, k)[3]
            GoldW14.append(g)
            cs = match_timeline(timeline, k)[4]
            CSW14.append(cs)

    x = x_temp_blue[0]

    for element in zip(*y_temp_blue):
        y_final_blue.append(sum(element))

    for element in zip(*y_temp_red):
        y_final_red.append(sum(element))

    for a, b in zip(y_final_blue, y_final_red):
        # Obliczenie różnicy i dodanie do listy differences
        y_diff.append(a - b)

    for i in range(len(y_diff)):
        if y_diff[i] >= 0:
            y_diff_add.append(y_diff[i])
            y_diff_odd.append(0)
        elif y_diff[i] <= 0:
            y_diff_odd.append(y_diff[i])
            y_diff_add.append(0)

    #print((max(y_diff_add)/500)*500)
    #print((min(y_diff_odd)/500)*500)


    max_val = round(max(y_diff_add)/500)*500
    min_val = round(min(y_diff_odd)/500)*500

    plt.figure(figsize=(10, 6))

    plt.xlim(0, len(x))
    plt.xticks(range(0, len(x) - 1))
    plt.yticks(range(int(min_val)-500, int(max_val)+500,500))

    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)
    plt.gca().spines['left'].set_visible(False)
    plt.gca().spines['bottom'].set_visible(False)

    # Usuwanie kresk (ticks) na osi x
    plt.tick_params(axis='x', which='both', bottom=False, top=False, labelbottom=True,colors='white')

    # Usuwanie kresk (ticks) na osi y
    plt.tick_params(axis='y', which='both', left=False, right=False, labelleft=True, pad=10,colors='white')

    plt.plot(x, y_diff_add,marker = '.', color = 'aqua')
    plt.fill_between(x, y_diff_add, 0, color = 'aqua')
    plt.plot(x, y_diff_odd,marker = '.', color = 'orangered')
    plt.fill_between(x, y_diff_odd, 0, color = 'orangered')
    plt.savefig('Graphs/Gold.png',bbox_inches='tight',facecolor='none',transparent=True)
    #plt.show()

    result = {
        "GoldW14": GoldW14,
        "CSW14": CSW14
    }
    return result

def GUI():
    layout = [[sg.Text("Enter match ID")],
              [sg.InputText(key='-INPUT-')],
              [sg.Text("Enter blue team tag"),sg.Text("                                                  Enter red team tag")],
              [sg.InputText(key='-INPUT2-'),sg.InputText(key='-INPUT3-')],
              [sg.Text("Enter blue team score"),sg.Text("                                               Enter red team score")],
              [sg.InputText(key='-INPUT4-'),sg.InputText(key='-INPUT5-')],
              [sg.Button('Save', enable_events=True), sg.Button('Cancel')]]
    window = sg.Window('LCU Post Game', layout)
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':
        window.close()
        raise SystemExit
    elif event == 'Save':
        ID = values['-INPUT-']
        BlueTag = values['-INPUT2-']
        RedTag = values['-INPUT3-']
        BlueScore = values['-INPUT4-']
        RedScore = values['-INPUT5-']
        if not ID.isdigit():
            sg.popup('ERROR - Only numbers are allowed')
            window.close()
            exit(1)

    match = {
        'BlueTag': BlueTag,
        'RedTag': RedTag,
        'BlueScore': BlueScore,
        'RedScore': RedScore
    }

    window.close()
    return ID, match

async def DragonType(connection,teamBlue,teamRed):
    global ID

    timestamp = await connection.request('get', '/lol-match-history/v1/game-timelines/' + str(ID))

    # Close connection if data not found
    if timestamp.status == 404:
        await connection.request('post', '/exit')
        exit(1)

    # Parsing data from JSON
    timeline = await timestamp.json()

    #print("test")

    DragonBlue = []
    DragonRed = []
    HordeBlue = 0
    HordeRed = 0
    BaronBlue = 0
    BaronRed = 0

    for frame in range(len(timeline['frames'])):
        #print(frame)
        for event in range(len(timeline['frames'][frame]['events'])):
            #print(timeline['frames'][frame]['events'][event]['type'])
            if timeline['frames'][frame]['events'][event]['type'] == 'ELITE_MONSTER_KILL' and timeline['frames'][frame]['events'][event]['monsterType'] == 'DRAGON' and timeline['frames'][frame]['events'][event]['killerId'] in teamBlue:
                DragonBlue.append(timeline['frames'][frame]['events'][event]['monsterSubType'])
            elif timeline['frames'][frame]['events'][event]['type'] == 'ELITE_MONSTER_KILL' and timeline['frames'][frame]['events'][event]['monsterType'] == 'DRAGON' and timeline['frames'][frame]['events'][event]['killerId'] in teamRed:
                DragonRed.append(timeline['frames'][frame]['events'][event]['monsterSubType'])

            if timeline['frames'][frame]['events'][event]['type'] == 'ELITE_MONSTER_KILL' and timeline['frames'][frame]['events'][event]['monsterType'] == 'HORDE' and timeline['frames'][frame]['events'][event]['killerId'] in teamBlue:
                HordeBlue = HordeBlue + 1
            elif timeline['frames'][frame]['events'][event]['type'] == 'ELITE_MONSTER_KILL' and timeline['frames'][frame]['events'][event]['monsterType'] == 'HORDE' and timeline['frames'][frame]['events'][event]['killerId'] in teamRed:
                HordeRed = HordeRed + 1

            if timeline['frames'][frame]['events'][event]['type'] == 'ELITE_MONSTER_KILL' and timeline['frames'][frame]['events'][event]['monsterType'] == 'BARON_NASHOR' and timeline['frames'][frame]['events'][event]['killerId'] in teamBlue:
                BaronBlue = BaronBlue + 1
            elif timeline['frames'][frame]['events'][event]['type'] == 'ELITE_MONSTER_KILL' and timeline['frames'][frame]['events'][event]['monsterType'] == 'BARON_NASHOR' and timeline['frames'][frame]['events'][event]['killerId'] in teamRed:
                BaronRed = BaronRed + 1

    # print(DragonBlue)
    # print(DragonRed)
    # print(HordeBlue)
    # print(HordeRed)
    # print(ElderBlue)
    # print(ElderRed)
    # print(BaronBlue)
    # print(BaronRed)

    result = {
        'DragonBlue': DragonBlue,
        'DragonRed': DragonRed,
        'HordeBlue': HordeBlue,
        'HordeRed': HordeRed,
        'BaronBlue': BaronBlue,
        'BaronRed': BaronRed,
    }

    return result

def main():
    # Variable to pass ID match
    global ID
    # Repeat try except block with valid match ID
    while True:
        try:
            ID, matchS = GUI()
            #print(ID)
            #print(match)
            break
        except SystemExit:
            exit(0)
        except:
            sg.popup('Error - Invalid match ID')
            exit(0)

    try:
        @connector.ready
        async def match(connection):
            match_stats = await match_history(connection)
            statsClasses, match_stats = match_stats[1], match_stats[0]
            teamBlue = match_stats['teamBlue']
            teamRed = match_stats['teamRed']

            dragons = await DragonType(connection,teamBlue,teamRed)

            match_time = await GraphCreate(connection)

            DMGGraph(statsClasses)
            DataToFinallGraph = {
                'statsClasses': statsClasses,
                'match_stats': match_stats,
                'dragons': dragons,
                'DataW14': match_time,
                'match': matchS
            }

            GraphCreator(DataToFinallGraph)
            sg.popup("Graphic create! To find it go to Image folder")

        connector.start()
    except:
        sg.popup("Error - match ID not found")
        exit(1)

if __name__ == "__main__":
    main()



