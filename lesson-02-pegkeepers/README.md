# Lesson 2: Peg Keepers

## [🎥 crvUSD Ape Tutorial Video 2 : Peg Keepers 🎬](https://youtu.be/MZn3Z0YTWyA)

This lesson drills down on migrating scripts from brownie to ape.  Brownie and ape mostly work similarly, but this lesson shows off a few idiosyncrasies.

The lesson also focuses on $crvUSD Peg Keepers.  Peg keepers play a crucial role in maintaining the stability of the $crvUSD stablecoin.  Peg Keepers are uniquely authorized to mint new $crvUSD for the purpose of trading into and out of their associated pools. 

The [script](src/scripts/pegkeeper.py) in this unit demonstrates more about how the Peg Keepers trade and one means by which you may interact with the contracts.

Within the scripts directory we also include the [original brownie script](src/scripts/pegkeeper-brownie.py) and a log of [key diffs](src/scripts/ape_brownie_diffs.txt).

## Key Concepts

### Running a Script

Running a script in Ape is akin to Brownie:

    ape run <script_name>

### Imports

Don't forget to rename brownie to ape in your imports.  
Most imports in ape are similar to their counterparts in brownie

    from ape import <modules>

### Transaction Parameters

Brownie used curly bracket syntax to pass transaction parameters

     target.foo(..., {'from': addr, 'value': 10 ** 18})

Ape passes these as arguments after contract parameters.
Most keys carry the same name, but The "from" key is renamed as sender

    target.foo(..., sender = addr, value = 10 ** 18)

### Accounts

In Brownie, forked mainnets were prepopulated directly with test accounts.

    alice = accounts[0]

Ape tests handle accounts in the same manner.
Ape scripts require testnet accounts load as follows:

    alice = accounts.test_accounts[0]


## Links

- [crvUSD Peg Keeper Docs](https://docs.curve.fi/crvUSD/pegkeeper/)
- [Ape Academy: Porting Brownie to Ape](https://academy.apeworx.io/articles/porting-brownie-to-ape)
- [Ape Documentation: Accounts](https://docs.apeworx.io/ape/stable/userguides/accounts.html)


