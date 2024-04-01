import requests


def fetch_quote():
    try:
        response = requests.get("https://api.forismatic.com/api/1.0/?method=getQuote&format=json&lang=en")
        data = response.json()
        if 'quoteText' in data and 'quoteAuthor' in data:
            return data['quoteText'], data['quoteAuthor']
        else:
            return "Failed to fetch a quote", "Unknown"
    except Exception as e:
        return "Failed to fetch a quote", str(e)


def main():
    print("Fetching a random quote...")
    quote, author = fetch_quote()
    print("\nQuote:")
    print(quote)
    print(author)


if __name__ == "__main__":
    main()
