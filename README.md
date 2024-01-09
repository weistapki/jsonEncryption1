# 🛡️ jsonEncryption1

Проект для шифрования и дешифрования данных JSON с использованием библиотеки `cryptography` в Python.

## Установка

1. Клонируйте репозиторий: `git clone https://github.com/weistapki/jsonEncryption1`
2. Перейдите в каталог проекта: `cd jsonEncryption1`
3. Установите зависимости: `pip install -r requirements.txt`

## Использование

Пример использования шифрования:

```python
from cryptography.fernet import Fernet
import json

# Создание ключа для шифрования
key = Fernet.generate_key()

# Инициализация объекта шифрования
cipher_suite = Fernet(key)

# Подготовка данных для шифрования
data_to_encrypt = {
    "login": "Alice",
    "password": "C00peR"
}

# Преобразование данных в формат bytes для шифрования
json_data = json.dumps(data_to_encrypt)
bytes_data = json_data.encode('utf-8')

# Шифрование данных
cipher_data = cipher_suite.encrypt(bytes_data)

# Преобразование зашифрованных данных в строку для сохранения или передачи
cipher_text = cipher_data.decode('utf-8')
print(f'Cipher Text: {cipher_text}')

# Дешифрование данных
# Преобразование зашифрованной строки в формат bytes для дешифрования
decipher_text = cipher_text.encode('utf-8')
decipher_data = cipher_suite.decrypt(decipher_text)

# Декодирование и преобразование данных обратно в JSON
decrypted_data = decipher_data.decode('utf-8')
json_decrypted_data = json.loads(decrypted_data)
print(f'Decrypted Data: {json_decrypted_data}')
