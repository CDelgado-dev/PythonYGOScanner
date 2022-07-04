import requests
import json

##test response not final
def main():
    response = (requests.get("https://db.ygoprodeck.com/api/v7/cardinfo.php")).json()
    data = response['data']
    #print("Type:", type(response))
    #items in data request pull
    while True:
        card = input("Card to lookup: ")
        for cardDict in data:
            if cardDict['name'] == card:
                print(f"Name: {cardDict['name']} Price: {cardDict['card_prices'][0]['tcgplayer_price']}")
        if not input("Lookup another card? [Yes] or [No]: ").lower().strip().startswith('y'):
            break
        #print("Name of Card: %s" % (x['name']))
        #print("\n")

    #print("ID: ", response['data'] )

if __name__ == '__main__':
    main()
