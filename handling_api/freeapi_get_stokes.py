import requests

def fetch_stokes_name(url):
    response = requests.get(url)
    row_data = response.json()

    if row_data["success"] and "data" in row_data:
        stokes_details = row_data["data"]
        company_name = stokes_details["data"][0]["Name"]
        market_cap = stokes_details["data"][0]["MarketCap"]
        return [company_name, market_cap]
    else:
        raise Exception("Stocks fetched failed !\n")

def main():
    url = "https://api.freeapi.app/api/v1/public/stocks?page=1&limit=2&inc=Symbol%2CName%2CMarketCap%2CCurrentPrice&query=tata"
    try:
        company_is, market_cap_is = fetch_stokes_name(url)
        print(f"company_name: {company_is}\nmarket_cap: {market_cap_is}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()


