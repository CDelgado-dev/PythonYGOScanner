import requests
import json

##test response not final
def main():
    response = (requests.get("https://db.ygoprodeck.com/api/v7/cardinfo.php")).json()
    data = response['data']
    #print("Type:", type(response))
    #items in data request pull
    card = input("Card to lookup: ")
    for x in data:
        if x['name'] == "card":
            print(x)
        #print("Name of Card: %s" % (x['name']))
        #print("\n")
        


    #print("ID: ", response['data'] )

if __name__ == '__main__':
    main()
