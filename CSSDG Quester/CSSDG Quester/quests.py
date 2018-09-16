
import gspread
import pprint
import time
import random
from oauth2client.service_account import ServiceAccountCredentials
import datetime

class Rarities:
    IMPOSIBIL = 15
    LEGENDAR = 35
    EPIC = 50
    COMUN = 100
    


# Pretty printer pp.pprint()
pp = pprint.PrettyPrinter()

# Google sheet inits
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']

creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)


###############################################
class Quest(object):
    def __init__(self, id = None, type = None, rarity = None, time = None, status = None, title = None, text = None, xp = None,sectCoins = None, rank = None):
        self.id = id
        self.type = type
        self.rarity = rarity
        self.time = time
        self.status = status
        self.title = title
        self.text = text
        self.xp = xp
        self.sectCoins = sectCoins
        self.rank = rank
    


def getActiveQuests():
    return "quest obj list with the active quests"

# Returns the rarity to look into quests by %of drop
def getRandomRarity():
    r = random.randint(1,100)

    if r <= Rarities.IMPOSIBIL:
        return "IMPOSIBIL"
    elif r <= Rarities.LEGENDAR:
        return "LEGENDAR"
    elif r <= Rarities.EPIC:
        return "EPIC"
    else:
        return "COMUN"


def getRandomQuest():
    rarity = getRandomRarity()
    quests = getQuestsByRarity(rarity)

    # Pick a random quest 
    r = random.randint(0, quests.__len__() - 1)
    # If the quest status is false run the function again, return a quest when it finds one that isnt false
    if quests[r].status == 'FALSE':
        getRandomQuest()
    
    return quests[r]


# Returns a list with all the quests that match the rarity
def getQuestsByRarity(rarity):
    quests = []
    sheet = client.open('QUESTURI').sheet1
    cell_list = sheet.get_all_values()
    i = 0
    while i < sheet.row_count:
        # [i][2] is the value for rarity in sheets
        if cell_list[i][2] == rarity:
            quests.append(Quest(cell_list[i][0], cell_list[i][1], cell_list[i][2], cell_list[i][3], cell_list[i][4], cell_list[i][5], cell_list[i][6], cell_list[i][7], cell_list[i][8], cell_list[i][9]))
        i+=1
    return quests

# Returns the quest that matches the id
def getQuestByID(id):
    quest = None
    sheet = client.open('QUESTURI').sheet1
    cell_list = sheet.get_all_values()
    i = 0
    while i < sheet.row_count:
        # [i][0] is the value for id in sheets
        if cell_list[i][0] == id:
            quest = Quest(cell_list[i][0], cell_list[i][1], cell_list[i][2], cell_list[i][3], cell_list[i][4], cell_list[i][5], cell_list[i][6], cell_list[i][7], cell_list[i][8], cell_list[i][9])
        i+=1
    return quest






# Saves the id of the quest and the time/date it was started
def startRandomQuest():
    sheet = sheet = client.open('QUESTURI')
    sheet = sheet.get_worksheet(1)
    quest = getRandomQuest()
    date = datetime.datetime.now()
    sheet.append_row([quest.id, date.day, date.hour])
    # TODO: Add all the active quests into the database to keep track of them
    # TODO: Save the time you started the quest in the database, remove the quest when time runs out

if __name__ == '__main__':    
    # Test
    i = 0
    while i < 10:
        quest = getRandomQuest()
        print(quest.id, quest.rank, quest.type, quest.rarity, quest.status, quest.title)
        i+= 10
    print("Test completed succesfully")
    pass