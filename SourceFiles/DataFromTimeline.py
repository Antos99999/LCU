def match_timeline(match_timestamp,k):
    GoldKoniec = 0
    Minuty = []
    GoldCoMinute = []
    GoldW14 = 0
    csW14 = 0
    jglCS = 0

    # Parsing data from JSON
    #match_timestamp = timestamp.json()

    for i in range(len(match_timestamp['frames'])):
        for j in range(len(match_timestamp['frames'][i]['participantFrames'])):
            player = match_timestamp['frames'][i]['participantFrames'][str(j + 1)]['participantId']
            if str(player) == str(k):
                gold = match_timestamp['frames'][i]['participantFrames'][str(j + 1)]['totalGold']
                cs = match_timestamp['frames'][i]['participantFrames'][str(j + 1)]['minionsKilled']
                jglCS = match_timestamp['frames'][i]['participantFrames'][str(j + 1)]['jungleMinionsKilled']
                timestamp = round(int(match_timestamp['frames'][i]['timestamp']) / 60000)  # co jedną minute
                GoldCoMinute.append(gold)
                Minuty.append(timestamp)
                GoldKoniec = GoldCoMinute[-1]
                if i == 14:
                    GoldW14 = gold
                    csW14 = cs + jglCS

    # print(Minuty)
    # print(GoldCoMinute)
    # print(GoldW14)
    # print(GoldKoniec)
    # print(csW14)
    return GoldKoniec, Minuty, GoldCoMinute, GoldW14, csW14
