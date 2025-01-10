import os
import sys
from PIL import Image, ImageDraw, ImageFont

def GraphCreator(data):

    width, height = 860, 600
    image = Image.new('RGBA', (width, height), (22,22,30,255))
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype('./Fonts/TT Octosquares Trial Bold.ttf',30)
    fontSmall = ImageFont.truetype('./Fonts/TT Octosquares Trial Bold.ttf', 25)
    fontSmaller = ImageFont.truetype('./Fonts/TT Octosquares Trial Bold.ttf', 15)

    Classes = data['statsClasses'] #player class
    MainData = data['match_stats'] #Gold,Kills,Deaths,Assists,Dmg,IdPlayersInTeam
    Objectives = data['dragons']
    GoldAndCsIn14 = data['DataW14']
    matchs = data['match']

    #print(Classes)
    #print(MainData)
    #print(Objectives)
    #print(GoldAndCsIn14)
    #print(tag)

    print(matchs)


    BackGround = Image.open('./ImageToUse/Win.png').convert('RGBA')
    image.paste(BackGround, (-5, 25), BackGround)

    DMG_graph = Image.open('./Graphs/finalDmgWithChamp.png').convert('RGBA')
    DMG_graph = DMG_graph.resize((400, 267))
    image.paste(DMG_graph, (450, 280), DMG_graph)

    GOLD_graph = Image.open('./Graphs/Gold.png').convert('RGBA')
    GOLD_graph = GOLD_graph.resize((400, 236))
    image.paste(GOLD_graph, (455, 40), GOLD_graph)

    x1, y1 = 25, 25
    x2, y2 = 420, 110

    # Wymiary tekstu
    bbox  = draw.textbbox((0, 0), str(matchs['BlueTag'] + " " + matchs['BlueScore'] + " - " + matchs['RedScore'] + " " + matchs['RedTag']), font=font)
    text_width = bbox [2] - bbox [0]  # Szerokość tekstu
    text_height = bbox[3] - bbox[1]

    # Oblicz współrzędne, aby wyśrodkować tekst w obrębie prostokąta
    rect_width = x2 - x1
    rect_height = y2 - y1

    # Obliczanie przesunięcia, aby tekst był wycentrowany w prostokącie
    x = x1 + (rect_width - text_width) // 2
    y = y1 + (rect_height - text_height) // 2

    draw.text((x+7, y+17), str(matchs['BlueTag'] + " " + matchs['BlueScore'] + " - " + matchs['RedScore'] + " " + matchs['RedTag']), fill='white', font=font, align='center')

    RedGold = MainData['RedGold']
    BlueGold = MainData['BlueGold']
    RedKDA = (MainData['KillRed']+MainData['AssistsRed'])/MainData['DeathsRed']
    BlueKDA = (MainData['KillBlue']+MainData['AssistsBlue'])/MainData['DeathsBlue']
    RedKDA = round(RedKDA,2)
    BlueKDA = round(BlueKDA,2)


    #Drawing TeamGold Text
    draw.text((150, 177), "Team Gold", fill='black', font=fontSmall, align='center')
    draw.text((25, 177), str(RedGold), fill='black', font=fontSmall, align='center')

    text_bbox = draw.textbbox((0, 0), str(BlueGold), font=font)
    text_width = text_bbox[2] - text_bbox[0]  # Szerokość tekstu
    text_x_position = 450 - text_width  # Dopasowanie do prawej

    draw.text((text_x_position, 177), str(BlueGold), fill='black', font=fontSmall, align='center')


    # Drawing TeamKDA Text
    draw.text((150, 240), "Team KDA", fill='white', font=fontSmall, align='center')
    draw.text((25, 240), str(RedKDA), fill='white', font=fontSmall, align='center')

    text_bbox = draw.textbbox((0, 0), str(BlueKDA), font=font)
    text_width = text_bbox[2] - text_bbox[0]  # Szerokość tekstu
    text_x_position = 440 - text_width  # Dopasowanie do prawej

    draw.text((text_x_position, 240), str(BlueKDA), fill='white', font=fontSmall, align='center')


    DragonBlue = Objectives['DragonBlue']
    DragonRed = Objectives['DragonRed']
    for dragon in DragonBlue:
        if dragon == "ELDER_DRAGON":
            DragonBlue.remove(dragon)
    for dragon in DragonRed:
        if dragon == "ELDER_DRAGON":
            DragonRed.remove(dragon)
    HordeBlue = Objectives['HordeBlue']
    HordeRed = Objectives['HordeRed']
    BaronBlue = Objectives['BaronBlue']
    BaronRed = Objectives['BaronRed']

    # Drawing Drakes Text
    draw.text((175, 305), "Drakes", fill='black', font=fontSmall, align='center')
    for i in range(len(DragonBlue)):
        dragonBlue = Image.open('./ImageToUse/' + DragonBlue[i] + '.png').convert('RGBA')
        dragonBlue = dragonBlue.resize((32, 32))
        image.paste(dragonBlue, (15 + 40 * i, 307), dragonBlue)
    for i in range(len(DragonRed)):
        dragonRed = Image.open('./ImageToUse/' + DragonRed[i] + '.png').convert('RGBA')
        dragonRed = dragonRed.resize((32, 32))
        image.paste(dragonRed, (410 - 40 * i, 307), dragonRed)

    # Drawing Grabs Text
    draw.text((160, 370), "Voidgrubs", fill='white', font=fontSmall, align='center')
    draw.text((25, 370), str(HordeBlue), fill='white', font=fontSmall, align='center')
    draw.text((410, 370), str(HordeRed), fill='white', font=fontSmall, align='center')

    # Drawing Elder Text
    draw.text((170, 433), "Nashors", fill='black', font=fontSmall, align='center')
    draw.text((25, 433), str(BaronBlue), fill='black', font=fontSmall, align='center')
    draw.text((410, 433), str(BaronRed), fill='black', font=fontSmall, align='center')


    CSW14 = GoldAndCsIn14['CSW14']
    #print(CSW14)
    classes = ['Stats1', 'Stats2', 'Stats3', 'Stats4', 'Stats5', 'Stats6', 'Stats7', 'Stats8', 'Stats9', 'Stats10']
    WinTeam = []
    LoseTeam = []
    WinTeam = CSW14[5:]
    LoseTeam = CSW14[:5]

    #print(WinTeam)
    #print(LoseTeam)
    WinCsIn14 = 0
    LoseCsIn14 = 0

    for i in WinTeam:
        WinCsIn14 = WinCsIn14 + i

    for i in LoseTeam:
        LoseCsIn14 = LoseCsIn14 + i

    #print(WinCsIn14/5)
    #print(LoseCsIn14/5)

    # Drawing Avarage cs in 14 Text
    draw.text((150, 500), "Avg. CS@14", fill='white', font=fontSmall, align='center')
    draw.text((25, 505), str(WinCsIn14/5), fill='white', font=fontSmaller, align='center')

    text_bbox = draw.textbbox((0, 0), str(RedGold), font=font)
    text_width = text_bbox[2] - text_bbox[0]  # Szerokość tekstu
    text_x_position = 485 - text_width  # Dopasowanie do prawej

    draw.text((text_x_position+30, 505), str(LoseCsIn14/5), fill='white', font=fontSmaller, align='center')


    #Paste LEAGUE logo
    #EDU = EDU.resize((120, 33))
    #image.paste(LEAGUE, (150, 550), LEAGUE)

    LEAGUE = Image.open('./ImageToUse/riftlegends_logo.png').convert('RGBA')
    LEAGUE = LEAGUE.resize((90, 47))
    #image.paste(LEAGUE, (150, 545), LEAGUE)
    image.paste(LEAGUE, (150, 545), LEAGUE)

    #Paste CASTER logo
    PHE = Image.open('./ImageToUse/PHE_LOGO.png').convert('RGBA')
    PHE = PHE.resize((40, 40))
    image.paste(PHE, (650, 545), PHE)

    # Paste Antosss_ logo
    Antosss = Image.open('./ImageToUse/Antosss__White.png').convert('RGBA')
    Antosss = Antosss.resize((120, 50))
    #image.paste(Antosss, (500, 550), Antosss)
    image.paste(Antosss, (390, 545), Antosss)

    # image.show()
    image.save('./Image/PostGameGraph.png')
