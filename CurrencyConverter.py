from requests import get
from pprint import PrettyPrinter
from tkinter import *

BASE_URL =  "https://free.currconv.com/"
API_KEY = "970b760dfd21aa95d8ed"

printer = PrettyPrinter()

def get_currencies():
    endpoint = f"api/v7/currencies?apiKey={API_KEY}"
    url = BASE_URL + endpoint
    data = get(url).json()['results']

    data=list(data.items())
    data.sort()

    return data


def print_currencies(currencies):
    for name, currency in currencies:
        name = currency['currencyName']
        _id_ = currency['id']
        symbol = currency.get("currencySymbol","")
        print(f"{_id_} - {name} - {symbol}")


def exchange_rate(currency1, currency2):
    endpoint = f"api/v7/convert?q={currency1}_{currency2}&compact=ultra&apiKey={API_KEY}"
    url = BASE_URL + endpoint
    data = get(url).json()
    
    if len(data) == 0:
        print("invalid currencies.")
        return

    rate = list(data.values())[0]
    print(f"{currency1} -> {currency2} = {rate}")

    return rate

def convert(currency1, currency2, amount):
    rate = exchange_rate(currency1, currency2)
    if rate is None:
        return

    try:
        amount = float(amount)
    except:
        print("Invalid amount...")
        return

    converted_amount = rate * amount
    print(f"{amount} {currency1} is equal to {converted_amount} {currency2}")
    return converted_amount


def main():
    currencies = get_currencies()

    print("WELCOME! this is Currency Converter")
    print("LIST ~ shows all the currencies")
    print("CONVERT ~ it does the conversion of the entered currencies")
    print("RATE ~ shows the exchange rate of the currencies entered")
    print()

    while True:
        command = input("Enter a command (q to quit): ").lower()

        if command == "q":
            break
        elif command == "list":
            print_currencies(currencies)
        elif command == "convert":
            currency1 = input("Enter currency id you want to convert from: ").upper()
            amount = input("Enter an amount in {currency1}: ")
            currency2 = input("Enter currency id to convert into: ").upper()
            convert(currency1, currency2, amount)
        elif command == "rate":
            currency1 = input("Enter currency id you want to convert from: ").upper()
            currency2 = input("Enter currency id to convert into: ").upper()
            exchange_rate(currency1, currency2)
        else:
            print("Unknown command")

main()