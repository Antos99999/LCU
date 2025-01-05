
# Simple Post Game Graphic

This simple app use LCU to collect and visual data from game


## Usage

To correct work you need to have open League Client in which you have the match you want to visualize in your match history
1. Install [release](https://github.com/Antos99999/LCU/releases) which are created for you (tag should by patchVAppVarsion_LeagueTag) - if you want special release just for you, please contact me
2. Download folder (with files) [ImageToUse](https://github.com/Antos99999/LCU/tree/master/ImageToUse) AND [Fonts](https://github.com/Antos99999/LCU/tree/master/Fonts) - put them in the same folder where you have .exe file (without them app will not work)
4. In first input put your match ID (only number)
5. In secound input put winner team tag (max 8 characters)
6. Click button "Save ID"
7. Image should apper in Image folder as PostGameGraph.png

**NOTE**\
I recommended to put .exe file in separeted folder (for example on Desktop/LCUCreator), because program will create some extra folders to data storage (mostly images)

The app works on patches backwards (but the match still needs to be in the match history, but it doesn't work on replays (from a separate .rofl file). This happens because when viewing a game from a file, Vanguard must be stopped, which prevents the Legaue Client from running, which is required for the application to work properly.

App support both custome and official games (ranked, games with tournametn code). If the game mode is custom, it is recommended that players arrange themselves in the lobby from top to bot - otherwise the damage dealt graph will not be displayed correctly (the graph will still be correct, but the application is currently unable to set a custom display order players, so it is possible that the order of players will be different than top to bot)

**IMPORTANT**\
The match you want to visualize must be either in your game history, or you must have the post-match graphics running in the client (the one that is displayed after the end of the game)

If major changes occur in the game (such as adding a new champion, adding a new item, new season, removing an item), the application may not function properly. Implementing the appropriate changes should not take much time (a few days at most). If there is no appropriate release, please contact me via Discord (Antos99999)


## League Tags

- EDU Espotrs Uczelnie -> EDU
- Rift Legends -> RFT


## Features

- Custome order of player in damage graph
- Improved error and exceptions handling

## Used By

This project is used by:

- [Polski Hub Esportowy](https://x.com/PLHubEsportowy) in [EDU Esports Uczelnie](https://x.com/edu_esports)
- [Whiteers Cup](https://x.com/WhiteersCup)
- By [me](https://x.com/antosss_) in [Rift Legends](https://x.com/RiftLegendsPL)




## Authors

- @Antos99999 [(Github)](https://www.github.com/Antos999)/[(x.com)](https://x.com/antosss_)



