from ape import Contract
def main():
    crvusd_price_oracle = Contract('0xe5Afcf332a5457E8FafCD668BcE3dF953762Dfe7')
    crvusd_price = crvusd_price_oracle.price() / 10 ** 18
    print(f"Current Price: {crvusd_price}")
