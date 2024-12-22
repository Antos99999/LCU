import matplotlib.pyplot as plt
from PIL import Image, ImageDraw, ImageFont
import os
from main import *
from DictionaryIdToName import *
from ImageDownloader import *

def DMGGraph(stats):
    os.makedirs("./Image", exist_ok=True)

    width, height = 900, 600
    image = Image.new('RGBA', (width, height), (255, 255, 255, 0))
    draw = ImageDraw.Draw(image)

    font = ImageFont.truetype('./Fonts/TT Octosquares Trial Bold.ttf', 40)
    plt.figure(figsize=(10, 7))

    # Usunięcie zbędnych osi i etykiet
    plt.rcParams['axes.spines.left'] = False
    plt.rcParams['axes.spines.right'] = False
    plt.rcParams['axes.spines.top'] = False
    plt.rcParams['axes.spines.bottom'] = False

    plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1, wspace=0.4, hspace=0.4)

    # Plot 1
    plt.subplot(1,2,1)

    classes = ['Stats1', 'Stats2', 'Stats3', 'Stats4', 'Stats5', 'Stats6', 'Stats7', 'Stats8', 'Stats9', 'Stats10']

    y = []
    x = []
    champID = []
    champName = []
    for i in classes:
        tmpY = stats[i].name
        tmpX = stats[i].dmg
        champID.append(stats[i].champ)
        y.append(tmpY)
        x.append(tmpX)

    #print(champID)

    champName = ChangeIdToName(champID)

    #print(champName)

    ImageDownload(champName)

    y1 = y[:5]
    x1 =  x[:5]

    plt.barh(y1, x1,height=0.3,color='aqua',align='center')

    plt.gca().invert_yaxis()

    plt.tick_params(axis='y', which='both', left=False, right=False, labelleft=False, labelright=False, bottom=False, labelbottom=False)
    plt.tick_params(axis='x', which='both', left=False, right=False, labelleft=False, labelright=False, bottom=False,
                    labelbottom=False)

    # Plot 2
    plt.subplot(1,2,2)
    y2 = y[5:]
    x2 = x[5:]

    plt.barh(y2, x2,height=0.3,color='orangered',align='center')
    #for index, value in enumerate(x2):
        #print(value)
    #    plt.text(value+200, index, str(value), va='center',fontweight='bold',ha='right')

    plt.gca().invert_xaxis()
    plt.gca().invert_yaxis()

    plt.tick_params(axis='y', which='both', left=False, right=False, labelleft=False, labelright=False, bottom=False, labelbottom=False)
    plt.tick_params(axis='x', which='both', left=False, right=False, labelleft=False, labelright=False, bottom=False,
                    labelbottom=False)

    plt.savefig('Graphs/dmg.png', bbox_inches='tight', facecolor='none', transparent=True)

    #print(champName)
    for i in range(10):
        if i < 5:
            champIcon = Image.open('./ChampionsImg/'+champName[i]+'.png').convert('RGBA')
            champIcon = champIcon.resize((70,70))
            image.paste(champIcon,(5,34+117*i),champIcon)
            draw.text((85,63+117*i),str(x[i]),fill='white',font=font)
        else:
            champIcon = Image.open('./ChampionsImg/' + champName[i] + '.png').convert('RGBA')
            champIcon = champIcon.resize((70, 70))
            image.paste(champIcon, (825, 34+117*(i-5)), champIcon)
            text_bbox = draw.textbbox((0, 0), str(x[i]), font=font)
            text_width = text_bbox[2] - text_bbox[0]  # Szerokość tekstu
            text_x_position = 749 + 70 - text_width  # Dopasowanie do prawej
            draw.text((text_x_position, 63 + 117 * (i-5)), str(x[i]), fill='white', font=font, align ="right")
    DMG_graph = Image.open('./Graphs/dmg.png').convert('RGBA')
    DMG_graph = DMG_graph.resize((750,572))
    image.paste(DMG_graph,(75,0),DMG_graph)
    # image.show()
    image.save("./Graphs/finalDmgWithChamp.png")
    #for index, value in enumerate(x1):
        #print(value)
    #    plt.text(value+200, index, str(value),va='center',fontweight='bold')