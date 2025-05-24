from allegro_api import AllegroAPI
from bargain_finder import BargainFinder

def main():
    CLIENT_ID = 'your_client_id'
    CLIENT_SECRET = 'your_client_secret'

    allegro_api = AllegroAPI(CLIENT_ID, CLIENT_SECRET)
    finder = BargainFinder([allegro_api])

    query = input("Enter search query: ")
    bargains = finder.find_bargains(query)

    if not bargains:
        print("No bargains found.")
        return

    print(f"Bargains for '{query}':")
    for item in bargains:
        print(f"- {item['title']}: {item['price']} PLN")
        print(f"  Link: {item['url']}")

if __name__ == '__main__':
    main()
