import json

from ape import *


def main():
    factory_addr = "0xed4EA68c9164a2a51d646CFb25BaD15B483E510d" # Polygon Vault, change to mainnet address if needed
    factory_abi = json.load(open("factory.abi"))
    factory = Contract(factory_addr, abi=factory_abi)

    params = factory.decode_input(load_bytes())[1]
    tokens = [params["borrowed_token"], params["collateral_token"]]
    factory.create_from_pool(
        tokens[1],
        tokens[0],
        params["A"],
        params["fee"],
        params["loan_discount"],
        params["liquidation_discount"],
        params["pool"],
        sender=accounts.test_accounts[0],
    )

    vault_index = factory.market_count() - 1
    new_vault_addr = factory.vaults(vault_index)
    print(f"New vault deployed to {new_vault_addr}")


def load_bytes():
    # Input data from 0x42526886AdB3b20A23A5A19C04E4bF81e9FEbb2B creation:
    # https://polygonscan.com/tx/0xc1ccd4fb9ae3f88ff7465f73d05026a1b124774471bc8c05459015114f10e90a
    return bytes.fromhex(
        "43da4b08000000000000000000000000361a5a4993493ce00f61c32d4ecca5512b82ce900000000000000000000000007ceb23fd6bc0add59e62ac25578270cff1b9f6190000000000000000000000000000000000000000000000000000000000000064000000000000000000000000000000000000000000000000001550f7dca70000000000000000000000000000000000000000000000000000013fbe85edc9000000000000000000000000000000000000000000000000000000d529ae9e86000000000000000000000000000036becdcbdf49255f366a45b861b4223b482d35e4"
    )
