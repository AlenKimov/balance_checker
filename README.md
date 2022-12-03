# Web3 Balance Checker
Checks address balances using DeBank API.

VERSION 1.0.0

## [ENG] Installation and use
1. Download and install [Python 3.10.8](https://www.python.org/downloads/release/python-3108/).
   - Check the "Add python.exe to PATH" box.
2. Run `install.bat`: this file will install the missing libraries in the virtual environment, as well as create files with default settings. The installation may take a few minutes.
3. Set the script's settings.
4. Run `start.bat`: this file will start the script.

### Settings
The script settings are located in the `./balance_checker/settings` folder.

The basic settings are contained in `settings.toml`:
```toml
# Timeout between requests:
TIMEOUT = 30
# Number of addresses per request:
LIMIT = 8
```

The addresses, private keys and mnemonic phrases whose balances you want to check are set in the following files:
- `public_keys.txt`
- `private_keys.txt`
- `mnemonics.txt`

### Output data
The script saves all data on wallets with balances in the folder `./balance_checker/output` in the formats `.toml` and `.json`.

## [РУС] Установка и использование
1. Скачиваем и устанавливаем [Python 3.10.8](https://www.python.org/downloads/release/python-3108/).
   - Ставим галочку напротив "Add python.exe to PATH".
2. Запускаем `install.bat`: этот файл установит отсутствующие библиотеки в виртуальное окружение, а также создаст папку с настройками по умолчанию. Установка может занять несколько минут.
3. Задаем настройки скрипта.
4. Запускаем `start.bat`: этот файл запустит скрипт.

### Настройка
Настройки скрипта находятся в папке `./balance_checker/settings`.

Основные настройки содержаться в `settings.toml`:
```toml
# Таймаут между запросами:
TIMEOUT = 30
# Количество адресов за запрос:
LIMIT = 8
```

Адреса, приватные ключи и мнемонические фразы, балансы которых требуется проверить, задаются в следующих файлах:
- `public_keys.txt`
- `private_keys.txt`
- `mnemonics.txt`

### Выходные данные
Скрипт сохраняет все данные о кошельках с балансами в папку `./balance_checker/output` в форматах `.toml` и `.json`.