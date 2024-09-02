# Signum Feeds

This package contains reporting tools and datafeeds for Signum Oracle.

# Contracts
- [SignumFlex](https://scan.9mm.pro/address/0x25baEbFAc231836bd5AFd1F211f6E8306f2BCC1e?tab=contract)
- [Autopay](https://scan.9mm.pro/address/0x5CBcA25A8CD90d7b80Ba40a67E40E4D027738743?tab=contract)
- [Governance](https://scan.9mm.pro/address/0x7F0c51a9dC0AAf30247dEb14C696BF7e75a6C139?tab=contract)
- [SignumToken](https://scan.9mm.pro/address/0x410a1Cb708e0724d1f9013EE31945E5E3F978a44?tab=contract)

# How to Install Signum
This is a step by step guide for how to install Signum Feeds using the command line. Signum Feeds is an open source client based on a fork of Tellor’s Telliot Feeds for interacting with the Signum oracle. The methods outlined here were confirmed on a fresh installation of Ubuntu 20.04 LTS. Individual commands will differ with other environments (particularly for installing python 3.9), but the process is relatively similar for setting up Telliot on Mac (requires homebrew). You may use powershell if you’re familiar with using python on windows or use WSL (ubuntu 20.04) for better compatibility with this guide.

# Prerequisites:
- A computer, virtual machine, or windows subsystem for linux running ubuntu version 20.04. (other versions are probably fine, but 20.04 was used for testing this guide)
- A PulseChain address that has SRB tokens and native tokens (gas) for the network on which you want to report oracle data.
The Guide
- This is a beginner-friendly guide. Familiarity with the command line will be helpful, but otherwise no assumptions are made about your technical skills. We will go over in detail the commands necessary to:
• Install python 3.9 (Signum Feeds will not work with other versions like 3.8 or 3.10)
• Create a python virtual environment
• Install Signum Feeds
• Configure RPC endpoints
• Verify Installation


# Let’s get started!
Install python3.9
1) Check your python version with the command:
```
python3 -V
```
This will output your current version of python3. For example: [Python 3.8.10]. Make a note of your current version for step 4.

2) Download the python repository for ubuntu:
```
sudo add-apt-repository ppa:deadsnakes/ppa
```

3) Install Python 3.9:
```
sudo apt install python3.9
```
Python 3.9 is now installed. Now, let’s make sure that it’s the default python version on our machine.

4) Configure versions. Enter the following command, but replace “/usr/bin/python3.8” with your current version if different. (for example use “/usr/bin/python3.10” if you got 3.10 from step 1).
```
sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.8 1
```
Set python3.9 as option 2:
```
sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.9 2
```
Finally, check your available versions:
```
sudo update-alternatives --config python3
```
Press enter to confirm python3.9, or select the option for python 3.9.

5) Finally, double check your python version with:
```
python3 -V
```
Important: If you’ve completed the steps and your python3 version is anything other than 3.9.xx, you will not be able to use signum. Please make sure you are running python 3.9 before you continue.

# Create a Python Virtual Environment
A python virtual environment is like a container where Signum Feeds will be installed on your machine. Working in a virtual environment is not mandatory, but it helps in avoiding dependency conflicts if you plan on using the computer/VM for running other python software.

1)Install venv:
```
sudo apt-get install python3.9-venv
```

2) Create a python virtual environment directory called tenv:
```
python3 -m venv tenv
```

3) Activate the virtual environment:
```
source tenv/bin/activate
```


# Install Signum Feeds
1) Clone the signum-core repo:
```
git clone https://github.com/AvantgardeBlockchainSolutions/signum-core
```
2) Clone the signum-feeds repo:
```
git clone https://github.com/AvantgardeBlockchainSolutions/signum-feeds
```
3) Change directory (cd) into the signum-feeds folder that you just downloaded:
```
cd signum-feeds
```
4) Install signum-feeds with the command:
```
pip install -e .
```
5) Change directory to the signum core folder with
```
cd ..
```
and then
```
cd signum-core
```
6) Install signum-core with the command:
```
pip install -e .
```


# Configure a mainnet RPC Endpoint
1) Create the Signum configuration files:
```
telliot config init
```
2) Edit endpoints.yaml. Since this guide works for an ubuntu machine, we will use a cli based text editor called nano. Open endpoints.yaml with:
```
nano telliot/endpoints.yaml
```
Please note: Windows users using WSL and tenv, your endpoints.yaml file will be located in the root of your disk.
```
cd /home/yourusername
nano telliot/endpoints.yaml
```

Use the arrow keys to navigate the document and edit the mainnet node endpoint URL to match your own. Signum requires that you configure at least the Pulsechain mainnet endpoint for its functionality. (You may add endpoints for other networks also if you have those ready.)
If you make a mistake, exit the document with [ctrl+x]  [n] (don’t save changes) and press enter to confirm. Then open the document and start editing again.
When you’re done editing and you want to save your changes, use [ctrl+x]  [y] and press enter to confirm.

# Verify Installation
We can now check if Telliot was installed correctly with the command:
```
telliot –-help
```
If Telliot was installed properly, you should be presented with a list of commands that can be executed with telliot.

# Configure Reporting Accounts
First, we will set the account(s) that we want to use for staking SRB and reporting. The telliot account command is used with the following format:
```
telliot account add PulsechainAccount 0xblahblahmyPrivateKey 369
```
You can replace “PulsechainAccount” with any name you choose for your reporting account.

Replace “0xblahblahmyPrivateKey” with your reporting wallet’s private key.

The “369” indicates that you want to use this account for reporting on network Id 369: Pulsechain Mainnet.

You will be prompted to set a password for your account. If you ever forget the password, you can simply create another account with the correct information. You can see a list of your accounts and their public addresses with the command:
```
telliot account find
```
Accounts can be deleted with:
```
telliot account delete AccountName
```

# Using Signum to submit a PLS/USD Spot Price (Ignoring Profitability)
This is the exciting part! We’re going to start signum, confirm the configuration, and enter our account password. Signum will deposit our stake automatically, fetch the PLS/USD price data from multiple APIs, find the median value, and submit that value to the Signum database.

Start signum with this command:
```
telliot report -a PulsechainAccount -qt pls-usd-spot -p YOLO -ncr
```
Here’s what it means: You want to report the query type PLS/USD spot (-qt pls-usd-spot), you don’t care about checking for profit (-p YOLO), and you’re not listening for autopay tips (-ncr (no check rewards)). Remember to replace “PulsechainAccount” with your Signum account name if different.

# Running Signum to Submit Values on an Interval (Ignoring Profitability)
Start Signum with this command:
```
telliot report -a PulsechainAccount -qt pls-usd-spot -p YOLO -ncr -wp 3600
```
Here’s what it means: you want to report the query type PLS/USD spot (-qt pls-usd-spot), you don’t care about checking for profit (-p YOLO), you’re not listening for autopay tips (-ncr (no check rewards)), and you want to submit once every hour. The -wp (wait period) flag allows you to set the interval for reporting in seconds (there are 3600 seconds in 1 hour).

Note: Even if you’ve increased your stake, you may still be in reporter lock after your first report. If so, the log will inform you with a print like this:

INFO | telliot_feeds.reporters.tellor_360 | Currently in reporter lock. Time left: 0:12:13

Feel free to wait, or grab some more SRB to stake so that you can report more often.

# Running Signum to Listen for Autopay Tips (Profitability)

A “tip” on the Signum network represents a request for oracle data, and the first reporter to submit the requested data can claim a (usually small amount of) SRB.

Signum can be used to listen for these tips and submit the requested data automatically. As it listens, Signum will check the status of the network and calculate profitability. The reporter can configure signum with a custom profit threshold with the [-p] flag. If the [-p] flag is left out, signum will only submit when the tip is 2x the gas cost (100% profit).

Again, please use this functionality at your own risk. Profits are possible but not guaranteed.

Start Signum with this command:
```
telliot report -a PulsechainAccount -p 50 -wp 60
```
Here’s what it means: You want to check to see if there is a profitable tip every 60 seconds (-wp 60), and you want to make sure that you make at least a %50 profit after gas cost (-p 50).

Note: A wait period of 60 seconds is recommended if you’re using a RPC service like infura. This will limit your node calls so that you don’t have to pay subscription fees. If you’re not worried about making too many node calls the [-wp] flag can be left out.

# Running Signum Conditionally
Report new price only when price change is over a percentage threshold.
Start Signum with this command:
```
telliot conditional -a PulsechainAccount -qt pls-usd-spot -pc 0.001
```
Here's what it means: You want to report conditionally the pls-usd spot price, but only if the percent change (-pc) is greater than 0.10%.

Report new price whenever the current price is 24 hours old.
Start Signum with this command:
```
telliot conditional -a PulsechainAccount -qt pls-usd-spot -st 86400
```

# Report Commands
```
Options:
  -a, --account TEXT              Name of account used for reporting, staking,
                                  etc. More info: run `telliot account --help`
                                  [required]
  -u, --unsafe / -sf, --safe      Disables config confirmation prompts
  -gl, --gas-limit INTEGER        use custom gas limit
  -mf, --max-fee FLOAT            use custom maxFeePerGas (gwei)
  -pf, --priority-fee FLOAT       use custom maxPriorityFeePerGas (gwei)
  -bf, --base-fee FLOAT           use custom baseFeePerGas (gwei)
  -gp, --gas-price INTEGER        use custom legacy gasPrice (gwei)
  -pwd, --password TEXT
  -tx, --tx-type TEXT             choose transaction type (0 for legacy txs, 2
                                  for EIP-1559)
  -mnb, --min-native-token-balance FLOAT
                                  Minimum native token balance required to
                                  report. Denominated in ether.
  -gm, --gas-multiplier INTEGER   increase gas price for legacy transaction by
                                  this percentage (default 1%) ie 5 = 5%
  -mpfr, --max-priority-fee-range INTEGER
                                  the maximum range of priority fees to use in
                                  gwei (default 3 gwei)
  -qt, --query-tag [trb-usd-spot|ohm-eth-spot|vsq-usd-spot|bct-usd-spot|dai-usd-spot|ric-usd-spot|idle-usd-spot|mkr-usd-spot|sushi-usd-spot|matic-usd-spot|usdc-usd-spot|gas-price-oracle-example|eur-usd-spot|snapshot-proposal-example|eth-usd-30day_volatility|numeric-api-response-example|diva-protocol-example|string-query-example|pls-usd-spot|eth-usd-spot|btc-usd-spot|tellor-rng-example|twap-eth-usd-example|ampleforth-uspce|ampleforth-custom|albt-usd-spot|rai-usd-spot|xdai-usd-spot|eth-btc-spot|evm-call-example|avax-usd-spot|aave-usd-spot|badger-usd-spot|bch-usd-spot|comp-usd-spot|crv-usd-spot|doge-usd-spot|dot-usd-spot|eul-usd-spot|fil-usd-spot|gno-usd-spot|link-usd-spot|ltc-usd-spot|shib-usd-spot|uni-usd-spot|usdt-usd-spot|yfi-usd-spot|mimicry-crypto-coven-tami|mimicry-nft-index-usd|mimicry-nft-index-eth|mimicry-mashup-example|steth-btc-spot|steth-usd-spot|reth-btc-spot|reth-usd-spot|wsteth-usd-spot|wsteth-eth-spot|op-usd-spot|grt-usd-spot|cny-usd-spot|eth-jpy-spot|brl-usd-spot|corn-usd-custom|rice-usd-custom|wheat-usd-custom|soy-usd-custom|ousd-usd-spot|oeth-eth-spot|wld-usd-spot|sweth-usd-spot|diva-usd-spot|cbeth-usd-spot|wbeth-usd-spot|oeth-usd-spot|pyth-usd-spot|ogv-eth-spot|brc20-ordi-usd-spot|meth-usd-spot|wbtc-usd-spot|mnt-usd-spot|usdy-usd-spot|wmnt-usd-spot|btc-bal-example|btc-bal-current-example|evm-bal-example|evm-bal-current-example|primeeth-eth-spot|usdm-usd-spot|wusdm-usd-spot|sdai-usd-spot|sfrax-usd-spot|frax-usd-spot|gyd-usd-spot|leth-usd-spot|frxeth-usd-spot|filecid-query-example|ezeth-usd-spot|weeth-usd-spot|wrseth-usd-spot|rseth-usd-spot|mode-usd-spot|tlos-usd-spot|tara-usd-spot]
                                  select datafeed using query tag
  -wp, --wait-period INTEGER      wait period between feed suggestion calls
  --submit-once / --submit-continuous
  -s, --stake FLOAT               ❗Telliot will automatically stake more TRB
                                  if your stake is below or falls below the
                                  stake amount required to report. If you
                                  would like to stake more than required,
                                  enter the TOTAL stake amount you wish to be
                                  staked. For example, if you wish to stake
                                  1000 TRB, enter 1000.
  -cr, --check-rewards / -ncr, --no-check-rewards
                                  If the --no-rewards-check flag is set, the
                                  reporter will not check profitability or
                                  available tips for the datafeed unless the
                                  user has not selected a query tag or used
                                  the random feeds flag.
  -p, --profit TEXT               lower threshold (inclusive) for expected
                                  percent profit
  --skip-manual-feeds BOOLEAN     skip feeds that require manual value input
                                  when listening to tips
  -b, --build-feed                build a datafeed from a query type and query
                                  parameters
  -rngts, --rng-timestamp INTEGER
                                  timestamp for Tellor RNG
  -dpt, --diva-protocol BOOLEAN   Report & settle DIVA Protocol derivative
                                  pools
  -dda, --diva-diamond-address TEXT
                                  DIVA Protocol contract address
  -dma, --diva-middleware-address TEXT
                                  DIVA Protocol middleware contract address
  -custom-token, --custom-token-contract TEXT
                                  Address of custom token contract
  -custom-oracle, --custom-oracle-contract TEXT
                                  Address of custom oracle contract
  -custom-autopay, --custom-autopay-contract TEXT
                                  Address of custom autopay contract
  -rf, --random-feeds / -nrf, --no-random-feeds
                                  Reporter will use a random datafeed from the
                                  catalog.
  --rng-auto / --rng-auto-off
  -spwd, --signature-password TEXT
  --ignore-tbr / --include-tbr    optionaly ignore time based rewards in
                                  profit calculations. relevant only on eth-
                                  mainnet/eth-testnets
  -sa, --signature-account TEXT   Name of signature account used for reporting
                                  with Flashbots.
  --help                          Show this message and exit.
```

# Conditional Commands
```
Options:
  -a, --account TEXT              Name of account used for reporting, staking,
                                  etc. More info: run `telliot account --help`
                                  [required]
  -u, --unsafe / -sf, --safe      Disables config confirmation prompts
  -gl, --gas-limit INTEGER        use custom gas limit
  -mf, --max-fee FLOAT            use custom maxFeePerGas (gwei)
  -pf, --priority-fee FLOAT       use custom maxPriorityFeePerGas (gwei)
  -bf, --base-fee FLOAT           use custom baseFeePerGas (gwei)
  -gp, --gas-price INTEGER        use custom legacy gasPrice (gwei)
  -pwd, --password TEXT
  -tx, --tx-type TEXT             choose transaction type (0 for legacy txs, 2
                                  for EIP-1559)
  -mnb, --min-native-token-balance FLOAT
                                  Minimum native token balance required to
                                  report. Denominated in ether.
  -gm, --gas-multiplier INTEGER   increase gas price for legacy transaction by
                                  this percentage (default 1%) ie 5 = 5%
  -mpfr, --max-priority-fee-range INTEGER
                                  the maximum range of priority fees to use in
                                  gwei (default 3 gwei)
  -qt, --query-tag [trb-usd-spot|ohm-eth-spot|vsq-usd-spot|bct-usd-spot|dai-usd-spot|ric-usd-spot|idle-usd-spot|mkr-usd-spot|sushi-usd-spot|matic-usd-spot|usdc-usd-spot|gas-price-oracle-example|eur-usd-spot|snapshot-proposal-example|eth-usd-30day_volatility|numeric-api-response-example|diva-protocol-example|string-query-example|pls-usd-spot|eth-usd-spot|btc-usd-spot|tellor-rng-example|twap-eth-usd-example|ampleforth-uspce|ampleforth-custom|albt-usd-spot|rai-usd-spot|xdai-usd-spot|eth-btc-spot|evm-call-example|avax-usd-spot|aave-usd-spot|badger-usd-spot|bch-usd-spot|comp-usd-spot|crv-usd-spot|doge-usd-spot|dot-usd-spot|eul-usd-spot|fil-usd-spot|gno-usd-spot|link-usd-spot|ltc-usd-spot|shib-usd-spot|uni-usd-spot|usdt-usd-spot|yfi-usd-spot|mimicry-crypto-coven-tami|mimicry-nft-index-usd|mimicry-nft-index-eth|mimicry-mashup-example|steth-btc-spot|steth-usd-spot|reth-btc-spot|reth-usd-spot|wsteth-usd-spot|wsteth-eth-spot|op-usd-spot|grt-usd-spot|cny-usd-spot|eth-jpy-spot|brl-usd-spot|corn-usd-custom|rice-usd-custom|wheat-usd-custom|soy-usd-custom|ousd-usd-spot|oeth-eth-spot|wld-usd-spot|sweth-usd-spot|diva-usd-spot|cbeth-usd-spot|wbeth-usd-spot|oeth-usd-spot|pyth-usd-spot|ogv-eth-spot|brc20-ordi-usd-spot|meth-usd-spot|wbtc-usd-spot|mnt-usd-spot|usdy-usd-spot|wmnt-usd-spot|btc-bal-example|btc-bal-current-example|evm-bal-example|evm-bal-current-example|primeeth-eth-spot|usdm-usd-spot|wusdm-usd-spot|sdai-usd-spot|sfrax-usd-spot|frax-usd-spot|gyd-usd-spot|leth-usd-spot|frxeth-usd-spot|filecid-query-example|ezeth-usd-spot|weeth-usd-spot|wrseth-usd-spot|rseth-usd-spot|mode-usd-spot|tlos-usd-spot|tara-usd-spot]
                                  select datafeed using query tag
  -wp, --wait-period INTEGER      wait period between feed suggestion calls
  --submit-once / --submit-continuous
  -s, --stake FLOAT               ❗Telliot will automatically stake more TRB
                                  if your stake is below or falls below the
                                  stake amount required to report. If you
                                  would like to stake more than required,
                                  enter the TOTAL stake amount you wish to be
                                  staked. For example, if you wish to stake
                                  1000 TRB, enter 1000.
  -cr, --check-rewards / -ncr, --no-check-rewards
                                  If the --no-rewards-check flag is set, the
                                  reporter will not check profitability or
                                  available tips for the datafeed unless the
                                  user has not selected a query tag or used
                                  the random feeds flag.
  -p, --profit TEXT               lower threshold (inclusive) for expected
                                  percent profit
  --skip-manual-feeds BOOLEAN     skip feeds that require manual value input
                                  when listening to tips
  -pc, --percent-change FLOAT     Price change percentage for triggering a
                                  report. Default=0.01 (1%)
  -st, --stale-timeout INTEGER    Triggers a report when the oracle value is
                                  stale. Default=85500 (23.75 hours)
  --help                          Show this message and exit.
```
