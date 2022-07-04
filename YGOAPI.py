import requests
import json

##test response not final
def main():
    card = input("Card: ")
    response = (requests.get(f"https://db.ygoprodeck.com/api/v7/cardinfo.php?name={card}")).json()
    data = response['data'][0]
    print(data['name'])
    #If a card exist in more than one set, prompt the user to choose a set, otherwise just display the one set and its price
    if len(data['card_sets']) > 1:
        print("more than one")
        setList = data['card_sets']
    else:
        cardSet = data['card_sets'][0]
        print(f"Set Name: {cardSet['set_name']} Set Code: {cardSet['set_code']} Set Price: {cardSet['set_price']}")

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
