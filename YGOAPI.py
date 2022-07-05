import requests
import json

##test response not final
def main():
    card = input("Card: ")
    response = (requests.get(f"https://db.ygoprodeck.com/api/v7/cardinfo.php?name={card}")).json()  #My next idea is to grab all the cards info at the beginning again and let the user choose to lookup another card without grabbing data from the website
    if 'data' in response.keys(): #Added check to see if we were sent data, ie if card doesn't exist. This will probably be removed when we switch back to grabbing all card data
        data = response['data'][0]
    else: 
        data = None  
    #If a card exist in more than one set, prompt the user to choose a set, otherwise just display the one set and its price
    if not data:
        return
    elif len(data['card_sets']) > 1:
        print("This card has more than one set, you can select which set using the leading number (ie 00)\nor with the set code. Otherwise just hit Enter to see all")
        setList = data['card_sets']

        for cardSetDict in range(len(setList)):  #Displays the set key name to user to allow them to select one in the lookupset variable
            print(f"  {cardSetDict} -=- Set Code: {setList[cardSetDict]['set_code']} Set Name: {setList[cardSetDict]['set_name']}")
        lookupset = input(f"Number [0-{len(setList) - 1}] or Set Code or just hit <Enter> to see all: ").strip() #displays 0-34 for example to help the user, will also accept exact set codes, since user has that info on card
        for cardSet in range(len(setList)):  #Lil reminder setList is a list variable, I thought it was also a dictionary and was trying to interact with it the wrong way
            if lookupset == str(cardSet) or lookupset == setList[cardSet]['set_code']:
                print(f"Set Name: {setList[cardSet]['set_name']} Set Price: {setList[cardSet]['set_price']} Set Code: {setList[cardSet]['set_code']} Set Rarity: {setList[cardSet]['set_rarity']}")
            if not lookupset: #If the user didn't input anything and just hit enter, display all
                print(f"{cardSet}")
    else:
        cardSet = data['card_sets'][0]
        print(f"Set Name: {cardSet['set_name']} Set Price: {cardSet['set_price']} Set Code: {cardSet['set_code']} Set Rarity: {cardSet['set_rarity']}")

    #for x in data:
    #    print(x['name'])
    ##items in data request pull
    #while True:
    #    #Start an infinite loop, keep the website's api in memory
    #    card = input("Card to lookup: ")
    #    for cardDict in data:
    #        if cardDict['name'] == card:
    #            print(f"Name: {cardDict['name']} Price: {cardDict['card_prices'][0]['tcgplayer_price']}")
    #    #After displaying card info based on card's name, ask if they want to lookup another card
    #    if input("Lookup another card? [Yes] or [No]: ").lower().strip().startswith('n'):
    #        break

if __name__ == '__main__':
    main()
