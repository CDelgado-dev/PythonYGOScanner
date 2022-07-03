import requests
import json

##test response not final
def main():
    response = requests.get("https://db.ygoprodeck.com/api/v7/cardinfo.php")
    print(response.json())

if __name__ == '__main__':
    main()
