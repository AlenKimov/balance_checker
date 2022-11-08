# Web3 Balance Checker
Checks address balances using [DeBank API](https://docs.open.debank.com/en/).

## Установка и использование
1. Скачиваем и устанавливаем [Python 3.10.8](https://www.python.org/downloads/release/python-3108/).
   - Ставим галочку напротив "Add python.exe to PATH".
2. Запускаем `install.bat`: этот файл установит отсутствующие библиотеки в виртуальное окружение, а также создаст файлы с настройками по умолчанию. Установка может занять несколько минут.
3. Задаем настройки скрипта.
4. Запускаем `start.bat`: этот файл запустит скрипт.

### Настройка
Настройки скрипта находятся в папке `./balance_checker/settings`.

Адреса, приватные ключи и мнемонические фразы, балансы которых требуется проверить, задаются в следующих файлах:
- `public_keys.txt`
- `private_keys.txt`
- `mnemonics.txt`