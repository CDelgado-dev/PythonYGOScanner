import requests
import json
import re

setCodeRegex = re.compile('[a-z0-9]{3,5}-[a-z0-9]{3,5}')

##test response not final
def main():
    
    #response = (requests.get(f"https://db.ygoprodeck.com/api/v7/cardinfo.php?name={card}")).json()  #My next idea is to grab all the cards info at the beginning again and let the user choose to lookup another card without grabbing data from the website
    response = (requests.get("https://db.ygoprodeck.com/api/v7/cardinfo.php")).json()
    data = response['data']
    while True:
        card = input("Card: ").lower().strip()
        cardsFound = 0
        if setCodeRegex.match(card):
            #for cardDict in data:

                #TODO
                #for cardSet in range(len())
            print("Set Code Detected")
        else:
            for cardDict in data:
                if card == cardDict['name'].lower():
                    cardsFound += 1
                    #If a card exist in more than one set, prompt the user to choose a set, otherwise just display the one set and its price
                    if len(cardDict['card_sets']) > 1:
                        setList = cardDict['card_sets']

                        for cardSetDict in range(len(setList)):  #Displays the set key name to user to allow them to select one in the lookupset variable
                            print(f"  {cardSetDict} -=- Set Code: {setList[cardSetDict]['set_code']} Set Name: {setList[cardSetDict]['set_name']}")
                        print("This card has more than one set, you can select which set using the leading number (ie 12)\nor with the set code. Otherwise just hit Enter to see all")
                        lookupset = input(f"Number [0-{len(setList) - 1}] or Set Code or just hit <Enter> to see all: ").strip() #displays 0-34 for example to help the user, will also accept exact set codes, since user has that info on card
                        for cardSet in range(len(setList)):  #Lil reminder setList is a list variable, I thought it was also a dictionary and was trying to interact with it the wrong way
                            if lookupset == str(cardSet) or lookupset == setList[cardSet]['set_code']:
                                print(f"Set Name: {setList[cardSet]['set_name']} | Set Price: ${float(setList[cardSet]['set_price']):.2f} | Set Code: {setList[cardSet]['set_code']} | Set Rarity: {setList[cardSet]['set_rarity']}")
                            if not lookupset: #If the user didn't input anything and just hit enter, display all
                                print(f"Set Name: {setList[cardSet]['set_name']} | Set Price: ${float(setList[cardSet]['set_price']):.2f} | Set Code: {setList[cardSet]['set_code']} | Set Rarity: {setList[cardSet]['set_rarity']}")
                    else:
                        cardSet = cardDict['card_sets'][0]
                        print(f"Set Name: {cardSet['set_name']} | Set Price: ${float(cardSet['set_price']):.2f} | Set Code: {cardSet['set_code']} | Set Rarity: {cardSet['set_rarity']}")
            if cardsFound == 0:
                print("No Cards found, check spelling and try again")
        if input("Lookup another card? [Yes] or [No]: ").lower().strip().startswith('n'):
            break

if __name__ == '__main__':
    main()
