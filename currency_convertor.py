import requests

API_KEY = 'your_api_key'  # Replace with your actual API key
BASE_URL = 'https://v6.exchangerate-api.com/v6'

def get_exchange_rate(api_key, base_currency, target_currency):
    url = f"{BASE_URL}/{api_key}/latest/{base_currency}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if data['result'] == 'success':
            return data['conversion_rates'].get(target_currency)
        else:
            print("Error in response:", data['error-type'])
    else:
        print("Failed to retrieve data:", response.status_code)
    return None

def convert_currency(api_key, amount, base_currency, target_currency):
    rate = get_exchange_rate(api_key, base_currency, target_currency)
    if rate:
        return amount * rate
    else:
        print("Conversion rate not found.")
        return None

def main():
    print("Currency Converter")
    amount = float(input("Enter amount: "))
    base_currency = input("Enter base currency (e.g., USD): ").upper()
    target_currency = input("Enter target currency (e.g., EUR): ").upper()

    converted_amount = convert_currency(API_KEY, amount, base_currency, target_currency)
    if converted_amount is not None:
        print(f"{amount} {base_currency} is equal to {converted_amount:.2f} {target_currency}")

if __name__ == "__main__":
    main()