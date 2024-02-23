# Lesson 6: Llama Lend

## [🎥 crvUSD Ape Tutorial Video 6 : Llama Lend 🎬](https://youtu.be/cvK4Ax9jF1Y)

This video walks through how to deploy a one way lending vault using Ape Framework to the new Curve Llama Lend.

The video was recorded before mainnet deployment, and demonstrates how to deploy a vault using a test deployment on Polygon.  You can replace the Polygon addresses with the new Ethereum addresses as desired.

An ape deployment script with all the critical console commands needed to launch a vault is included under src/scripts/launch_vault.py

## APE POLYGON SETUP
The following commands may be needed to prepare your environment for Polygon

> ape plugins install polygon 
> export POLYGONSCAN_API_KEY=<your_key>

## LLAMA LEND REPO
Clone the github repository into your environment 

> git clone git@github.com:curvefi/curve-stablecoin.git
> git fetch --all
> git checkout -b lending origin/lending


## VYPER INSTALL
Vyper can be easily installed using pip

> pip install vyper

Specific releases can also be installed

> pip install vyper==0.3.10

## FETCH ABI FROM VYPER
Vyper can display compilation output in several formats.
Pass --help to see all possible outputs. To read a contract's ABI:

> vyper <filename> -f abi

## DECODE INPUT
Decode the given calldata using this contract.

> Contract.decode_input(hex_bytes) 


## Links

Git Repositories
 - [Deployment details](https://github.com/curvefi/curve-stablecoin/blob/lending/deployment-logs/oneway-lending.log)

Ethereum Deployment Addresses
 - [AMM implementation](https://etherscan.io/address/0x4f37395BdFbE3A0dca124ad3C9DbFe6A6cbc31D6)
 - [Controller implementation](https://etherscan.io/address/0x5473B1BcBbC45d38d8fBb50a18a73aFb8B0637A7)
 - [Vault implementation](https://etherscan.io/address/0x596F8E49acE6fC8e09B561972360DC216f1c2A1f)
 - [Pool price oracle implementation](https://etherscan.io/address/0x9164e210d123e6566DaF113136a73684C4AB01e2)
 - [Monetary Policy implementation](https://etherscan.io/address/0xa7E98815c0193E01165720C3abea43B885ae67FD)
 - [Gauge implementation](https://etherscan.io/address/0x00B71A425Db7C8B65a46CF39c23A188e10A2DE99)
 - [Factory](https://etherscan.io/address/0xc67a44D958eeF0ff316C3a7c9E14FB96f6DedAA3)

Polygon Test Deployment Addresses
 - [Factory](https://polygonscan.com/address/0xed4ea68c9164a2a51d646cfb25bad15b483e510d)


