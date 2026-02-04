import requests

def fetch_data():
    url = "https://api.publicapis.org/entries"
    response = requests.get(url)
    return response.json()

def analyze_data(data):
    entries = data.get("entries", [])
    total = len(entries)
    print(f"Total APIs found: {total}")

def main():
    data = fetch_data()
    analyze_data(data)

if __name__ == "__main__":
    main()
