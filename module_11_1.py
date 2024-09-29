import requests


url = 'https://requests.readthedocs.io/en/latest/index.html'
response = requests.get(url)
print(response.text)


# Запросы позволяют чрезвычайно легко отправлять запросы HTTP / 1.1.
# Нет необходимости вручную добавлять строки запроса к вашим URL-адресам или кодировать данные POST в форме.
# Поддержка и объединение пулов HTTP-соединений выполняются на 100% автоматически благодаря urllib3.
