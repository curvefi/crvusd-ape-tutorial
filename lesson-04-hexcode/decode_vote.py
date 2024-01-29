import warnings

from ape import Contract
from hexbytes import HexBytes

warnings.filterwarnings("ignore")

# the vote ID you wish to decrypt
VOTE_ID = 573

# address of the contract where the vote was created
# https://docs.curve.fi/references/deployed-contracts/#aragon

VOTING_ADDRESS = "0xe478de485ad2fe566d49342cbd03e49ed7db3356"


def main(vote_id=VOTE_ID):
    aragon = Contract(VOTING_ADDRESS)
    script = HexBytes(aragon.getVote(vote_id)["script"])

    # Start looping through data after the prefix
    idx = 4

    while idx < len(script):
        # Grab the first target address
        target = Contract(script[idx : idx + 20])
        idx += 20
        length = int(script[idx : idx + 4].hex(), 16)

        # Grab the length of the variable data
        idx += 4
        calldata = script[idx : idx + length]
        idx += length
        fn, inputs = target.decode_input(calldata)

        # Get calldata
        inputs = list(inputs.values())
        if calldata[:4].hex() == "0xb61d27f6":
            agent_target = Contract(inputs[0])
            fn, inputs = agent_target.decode_input(inputs[2])
            print(
                f"Call via agent ({target}):\n ├─ To: {agent_target}\n"
                f" ├─ Function: {fn}\n └─ Inputs: {inputs}\n"
            )
        else:
            print(
                f"Direct call:\n ├─ To: {target}\n ├─ Function: {fn}\n └─ Inputs: {inputs}"
            )
