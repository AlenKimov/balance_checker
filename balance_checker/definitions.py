from pathlib import Path

ROOT_DIR         = Path(__file__).parent
LOG_DIR          = Path(ROOT_DIR,     "log")
OUTPUT_DIR       = Path(ROOT_DIR,     "output")
SETTINGS_DIR     = Path(ROOT_DIR,     "settings")
DOTENV_FILE      = Path(SETTINGS_DIR, ".env")
SETTINGS_TOML    = Path(SETTINGS_DIR, "settings.toml")
PUBLIC_KEYS_TXT  = Path(SETTINGS_DIR, "public_keys.txt")
PRIVATE_KEYS_TXT = Path(SETTINGS_DIR, "private_keys.txt")
MNEMONICS_TXT    = Path(SETTINGS_DIR, "mnemonics.txt")
