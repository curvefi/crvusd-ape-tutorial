# Lesson 4: Hexcode 

## [🎥 crvUSD Ape Tutorial Video 4 : Sophisticated Voter 🎬](https://youtu.be/Ckl8rmZbAtY)

Our fourth major tutorial for our Ape Framework involves an inductive process to step through decoding a Curve DAO vote via the Aragon contracts.

In particular, we’re hoping to elevate everybody to the “sophisticated voter” stage, as Curve occasionally asks for help from this elite class to “verify” DAO votes.

The [companion video](https://youtu.be/Ckl8rmZbAtY) walks through the derivation, or you may consult [this companion writeup](https://curve.substack.com/p/1eb18120-76df-4fff-b535-85fd4591da44)

Credit to mo for the docs and WormholeOracle for the script!

## Key Concepts

### HexBytes
A HexBytes object in Python represents binary data in a hexadecimal format

    from hexbytes import HexBytes
    hex_object = HexBytes("0xbabe")

### Convert Hex to Int
Convert a HexBytes object to an integer

    int(bytes_data.hex(), 16)

### Decode Input 
Decode the given calldata using this contract.

    Contract.decode_input(hex_bytes)


## Links

Calls for Sophisticated Voters
- [Example 1](https://twitter.com/CurveFinance/status/1664075002293919744)
- [Example 2](https://twitter.com/CurveFinance/status/1668555992999645185)

DAO Votes
- [Curve](https://dao.curve.fi/vote/ownership/573)
- [Convex](https://vote.convexfinance.com/#/proposal/0xa902f0a7a752c34c9db74f292bf80c5f937d84a57697dfd73faef31fb3d33dd9)

Docs
- [Curve Technical Docs](https://docs.curve.fi/references/deployed-contracts/#aragon)
- [Aragon Docs](https://devs.aragon.org/)

Deployments
- [Aragon Ownership](https://etherscan.io/address/0xe478de485ad2fe566d49342cbd03e49ed7db3356)
- [Aragon Agent](https://etherscan.io/address/0x40907540d8a6C65c637785e8f8B742ae6b0b9968A)
- [TriCryptoUSDT](https://etherscan.io/address/0xf5f5b97624542d72a9e06f04804bf81baa15e2b4)
- [TriCryptoLlama](https://etherscan.io/address/0x2889302a794da87fbf1d6db415c1492194663d13)
