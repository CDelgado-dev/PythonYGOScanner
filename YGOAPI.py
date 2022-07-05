import requests
import json
import re

setCodeRegex = re.compile('[a-z0-9]{3,5}-[a-z0-9]{3,5}')

##test response not final
def main():
    
    #response = (requests.get(f"https://db.ygoprodeck.com/api/v7/cardinfo.php?name={card}")).json()  #My next idea is to grab all the cards info at the beginning again and let the user choose to lookup another card without grabbing data from the website
    response = (requests.get("https://db.ygoprodeck.com/api/v7/cardinfo.php")).json()
    data = response['data']  #The data variable is a list of dictionaries from ygoprodeck.com...
    #Each dictionary is for one card name, with card varients getting data in the set they came in under the 'card_sets' key
    print("""-=Yu-Gi-Oh Card Scanner=-
*Searches for card and displays their price
*using data provided by ygoprodeck.com
*The script can use the card name or
*set code (ID under card's picture)""")
    while True:   #Start infinite loop, that way script only needs to be started once and the website isn't spammed with too many requests
        card = input("Card or Set Code: ").lower().strip()   #ask user what card they want to lookup
        cardsFound = 0  #used to tell the user if their search term didn't match anything
        if setCodeRegex.match(card):  #if the search term looks like a set code, search for that instead
            for cardDict in data:
                if 'card_sets' in cardDict.keys():
                    for i in range(len(cardDict['card_sets'])):
                        if card == cardDict['card_sets'][i]['set_code'].lower():
                            print(f"Set Name: {cardDict['card_sets'][i]['set_name']} | Set Price: ${float(cardDict['card_sets'][i]['set_price']):.2f} | Set Code: {cardDict['card_sets'][i]['set_code']} | Set Rarity: {cardDict['card_sets'][i]['set_rarity']}")
                            if float(cardDict['card_sets'][i]['set_price']) == 0:  #If the set has 0.0 for the price show the user the other price the website gave us
                                print(f"TCGPlayer Price*: {float(cardDict['card_prices'][0]['tcgplayer_price']):.2f}")
                                print("*The website provides other prices that aren't part of their 'set' data")

        else:         # if the search term doesn't look like a set code, search for the card name normally
            for cardDict in data:        #each card has their own dictionary of data
                if card == cardDict['name'].lower():
                    cardsFound += 1
                    #If a card exist in more than one set, prompt the user to choose a set, otherwise just display the one set and its price
                    if len(cardDict['card_sets']) > 1:
                        setList = cardDict['card_sets']

                        for cardSetDict in range(len(setList)):  #Displays the set key name to user to allow them to select one in the lookupset variable
                            print(f"  {cardSetDict} -=- Set Code: {setList[cardSetDict]['set_code']} Set Name: {setList[cardSetDict]['set_name']}")
                        print("This card has more than one set, you can select which set\n using the leading number (ie 12) or with the set code. Otherwise just hit Enter to see all")
                        lookupset = input(f"Number [0-{len(setList) - 1}] or Set Code or just hit <Enter> to see all: ").strip() #displays 0-34 for example to help the user, will also accept exact set codes, since user has that info on card
                        for cardSet in range(len(setList)):  #Lil reminder setList is a list variable, I thought it was also a dictionary and was trying to interact with it the wrong way
                            if lookupset == str(cardSet) or lookupset == setList[cardSet]['set_code']:
                                print(f"Set Name: {setList[cardSet]['set_name']} | Set Price: ${float(setList[cardSet]['set_price']):.2f} | Set Code: {setList[cardSet]['set_code']} | Set Rarity: {setList[cardSet]['set_rarity']}")
                                if float(setList[cardSet]['set_price']) == 0:  #If the set has 0.0 for the price show the user the other price the website gave us
                                    print(f"TCGPlayer Price*: {float(cardDict['card_prices'][0]['tcgplayer_price']):.2f}")
                                    print("*The website provides other prices that aren't part of their 'set' data")
                            elif not lookupset: #If the user didn't input anything and just hit enter, display all
                                print(f"Set Name: {setList[cardSet]['set_name']} | Set Price: ${float(setList[cardSet]['set_price']):.2f} | Set Code: {setList[cardSet]['set_code']} | Set Rarity: {setList[cardSet]['set_rarity']}")
                    else:
                        cardSet = cardDict['card_sets'][0]
                        print(f"Set Name: {cardSet['set_name']} | Set Price: ${float(cardSet['set_price']):.2f} | Set Code: {cardSet['set_code']} | Set Rarity: {cardSet['set_rarity']}")
                        if float(cardSet['set_price']) == 0:  #Again, If the set has 0.0 for the price show the user the other price the website gave us
                            print(f"TCGPlayer Price*: {float(cardDict['card_prices'][0]['tcgplayer_price']):.2f}")
                            print("*The website provides other prices that aren't part of their 'set' data")
            if cardsFound == 0:
                print("No Cards found, check spelling and try again")
        if input("Lookup another card? [Yes] or [No]: ").lower().strip().startswith('n'):
            break

if __name__ == '__main__':
    main()
