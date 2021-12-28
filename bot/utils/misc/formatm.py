def get_data(message):
    message = message.replace('\r\n', ' ')
    if '*' in message:
        number = message[message.find('*')+1:message.rfind('*')]
    else:
        number = message[message.find('Телефон  ')+8:message.rfind('  Имя')]
    name = message[message.find('Имя')+4:message.find('Регион')]
    city = message[message.find('Регион ')+7:message.find('Дата')].strip()
    text = message[message.find('Дата')+26:message.find('Цена')-4].strip()
    return {'number':number,'city':city,'question':text, 'name':name}