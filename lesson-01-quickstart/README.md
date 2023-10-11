# Lesson 1: Quickstart

## [🎥 crvUSD Ape Tutorial Video 1 : Quickstart 🎬](https://youtu.be/MA7CrH3kNFo)

This lesson covers the basic setup needed to interact with $crvUSD.

Curve contracts are not deployed to any testnet.  In order to interact with Curve contracts, it is recommended to fork the mainnet and simulate transactions against the live contract deployment.

Getting the right mix of plugins is sometimes tricky for new users.  The quickstart lesson here is designed to get you up and running against a mainnet fork in a matter of minutes.

## Instructions

First, create a virtual environment within your working directory

    virtualenv ape-venv
    source ape-venv/bin/activate

Install Ape

    pip install eth-ape

Initialize your environment

    ape init

Edit your ape-config.yaml to look like the following (or copy from the repository)

    name: curve_quickstart
    plugins:
      - name: alchemy
      - name: foundry
      - name: etherscan

    ethereum:
      default_network: mainnet-fork
      mainnet_fork:
        default_provider: foundry
        transaction_acceptance_timeout: 600
    foundry:
      fork:
        ethereum:
          mainnet:
            upstream_provider: alchemy

Install plugins

    ape plugins install .

Congrats, you are ready to go! You can confirm this entire setup works by executing the following script to check the current oracle price of crvUSD, stored in the repository's [src/](src/) directory at [scripts/curve_price.py](src/scripts/curve_price.py)

    ape run scripts/curve_price.py

The full set of instructions can be found in the [instructions.txt](src/instructions.txt) file in the [src/](src/) directory.  The instructions file can also be executed to run all the steps.

**Ape Documentation and Resources:**

Written

 * [Ape Docs](https://docs.apeworx.io/)
 * [Ape Framework Academy](https://academy.apeworx.io/)
 * [Porting a Project from Brownie to Ape](https://academy.apeworx.io/articles/porting-brownie-to-ape)
 * [ApeWorX: The New Python Framework on the Block](https://blog.chain.link/apeworx-python-vyper/)A

Video
 * [How to Use Ape Framework and Installation](https://www.youtube.com/watch?v=GOWjaavBUfQ)
 * [How to Port Your Brownie Project to Ape Framework](https://www.youtube.com/watch?v=ebVmSVcebwg)
