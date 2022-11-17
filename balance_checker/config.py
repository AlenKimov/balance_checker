from pydantic import BaseModel
from os import makedirs
from pathlib import Path
import toml

# Скрипты проекта
from definitions import SETTINGS_DIR

DOTENV_FILE      = Path(SETTINGS_DIR, '.env')
SETTINGS_TOML    = Path(SETTINGS_DIR, 'settings.toml')
PUBLIC_KEYS_TXT  = Path(SETTINGS_DIR, 'public_keys.txt')
PRIVATE_KEYS_TXT = Path(SETTINGS_DIR, 'private_keys.txt')
MNEMONICS_TXT    = Path(SETTINGS_DIR, 'mnemonics.txt')


class Settings(BaseModel):
    TIMEOUT: int = 30
    LIMIT: int = 8


settings = Settings()

# Создаю файлы с настройками по умолчанию
makedirs(SETTINGS_DIR, exist_ok=True)
with open(PUBLIC_KEYS_TXT, 'a'): pass
with open(PRIVATE_KEYS_TXT, 'a'): pass
with open(MNEMONICS_TXT, 'a'): pass
if not SETTINGS_TOML.exists():
    with open(SETTINGS_TOML, 'w', encoding='utf-8') as settings_toml:
        toml.dump(settings.dict(), settings_toml)


with open(SETTINGS_TOML, encoding='utf-8') as settings_toml:
    settings = Settings(**toml.load(settings_toml))

with open(PUBLIC_KEYS_TXT) as public_keys_txt:
    addresses = [address.strip() for address in public_keys_txt]

with open(PRIVATE_KEYS_TXT) as private_keys_txt:
    private_keys = [private_key.strip() for private_key in private_keys_txt]

with open(MNEMONICS_TXT) as mnemonics_txt:
    mnemonics = [mnemonic.strip() for mnemonic in mnemonics_txt]
