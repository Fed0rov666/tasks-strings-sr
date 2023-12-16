def check_username(username):
    allowed_chars = set('abcdefghijklmnopqrstuvwxyz0123456789_')
    if all(char in allowed_chars for char in username):
        return 'OK'
    else:
        invalid_char = next(char for char in username if char not in allowed_chars)
        return f'Неверный символ: {invalid_char}'


username: str = input()

print(check_username(username))
