__all__ = ['get_ecosystem_config']

from dotenv import load_dotenv
load_dotenv()

def get_ecosystem_config(ecosystem):
    configs = {
        "sol": {
            "vault_env": "SOL_VAULT_ID",
            "default_dest": "",
            "decimals": 1_000_000_000,  # lamports
            "unit_name": "SOL"
        },
        "evm": {
            "vault_env": "EVM_VAULT_ID",
            "default_dest": "0x249f0D3F49C3918be70445f32aA52D97442DD16C",
            "decimals": 1_000_000_000_000_000_000,  # wei
            "unit_name": "ETH"
        },
        "sui": {
            "vault_env": "SUI_VAULT_ID",
            "default_dest": "",
            "decimals": 1_000_000_000,  # mist
            "unit_name": "SUI"
        },
        "ton": {
            "vault_env": "TON_VAULT_ID",
            "default_dest": "",
            "decimals": 1_000_000_000,  # nanotons
            "unit_name": "TON"
        },
        "apt":{
            "vault_env": "APTOS_VAULT_ID",
            "default_dest": "",
            "decimals": 100_000_000, # octa
            "unit_name": "APT"
        },
        "btc":{
            "vault_env": "BTC_VAULT_ID",
            "default_dest": "",
            "decimals": 100_000_000, # satoshis
            "unit_name": "BTC"
        }
    }
    return configs.get(ecosystem)
