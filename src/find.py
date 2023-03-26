def find(value, text):
    keys, num = [], 0
    for key in text.text:
        if (key == value): num += 1; keys.append(f'{key}, {num}')
    return ' '.join(keys) if (num != 0) else 'Not found'
