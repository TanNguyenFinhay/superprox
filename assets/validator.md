# VALIDATORS

🐧 Required OS: Ubuntu 22.04   |   🐍 Required Python: Python 3.10

## Compute Requirements


⚙️ Assumptions

Miners: 256 total, evenly distributed across active validators

Machines per Miner: At least 3 (2 traffic generators + 1 king)

Active Validator Scenario: Only 1 validator is active

➡️ Resulting Load:
1 validator × 256 miners × 3 machines = 768 simultaneous SSH connections

| Resource  | Minimum Requirement   |
|-----------|-----------------------|
| VRAM      | None                  |
| vCPU      | 16 vCPU               |
| RAM       | 32 GB                 |
| Storage   | 150 GB                |
| Network   | >= 1 Gbps             |


## 🔧 Installation

1. Update system packages and install Python pip/venv :

```bash
sudo apt update && sudo apt install python3-pip -y && sudo apt install python3-venv -y
```

2. Install npm and pm2 for process management :

```bash
sudo apt install npm -y && sudo npm install -g pm2 
```

3. Create and activate virtual environment :

```bash
python3 -m venv tp && source tp/bin/activate
```

4. Clone the repository and install the required pip dependencies :

```bash
git clone https://github.com/shugo-labs/tensorprox.git
cd tensorprox
pip install -r requirements.txt
```

## 🧩 Configuration

1. Before running a validator, you will need to create a .env.validator environment file. It is necessary for you to provide the following :

```text
NETUID = # The subnet UID (integer)
SUBTENSOR_NETWORK = # The network name [test, finney, local]
SUBTENSOR_CHAIN_ENDPOINT = # The chain endpoint [test if running on test, finney if running on main, custom endpoint if running on local]
WALLET_NAME = # Name of your wallet (coldkey)
HOTKEY = # Name of your hotkey associated with above wallet
AXON_PORT = # TCP Port Number. The port must be open
```

3. Also, make sure to include your WANDB_API_KEY in the .env file :

```text
WANDB_API_KEY="YOUR_API_KEY"
```

## 🖥️ Running

1. After creating the above environment file, run :

```bash
pm2 start "python3 neurons/validator.py" --name validator
```

2. Check if the instance is correctly running :

```bash
pm2 list
```

3. To see logs :

```bash
pm2 logs validator
```
