import requests
import json

##test response not final
def main():
    response = (requests.get("https://db.ygoprodeck.com/api/v7/cardinfo.php")).json()
    data = response['data']
    #items in data request pull
    while True:
        #Start an infinite loop, keep the website's api in memory
        card = input("Card to lookup: ")
        for cardDict in data:
            if cardDict['name'] == card:
                print(f"Name: {cardDict['name']} Price: {cardDict['card_prices'][0]['tcgplayer_price']}")
        #After displaying card info based on card's name, ask if they want to lookup another card
        if input("Lookup another card? [Yes] or [No]: ").lower().strip().startswith('n'):
            break

if __name__ == '__main__':
    main()
