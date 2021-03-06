import random
import string
russian_alphabet_upper = 'ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮЁ'
russian_alphabet_lower = 'йцукенгшщзхъфывапролджэячсмитьбюё'


def generate_string_full(length: int, eng_upper: bool, eng_lower: bool, rus_upper: bool, rus_lower: bool, digits: bool, special_sym: bool) -> str:
    if length < 5000000:
        result = ''.join(random.choice((string.ascii_uppercase if eng_upper is True else '') +
                                       (string.ascii_lowercase if eng_lower is True else '') +
                                       (string.digits if digits is True else '') +
                                       (string.punctuation if special_sym is True else '') +
                                       (russian_alphabet_upper if rus_upper is True else '') +
                                       (russian_alphabet_lower if rus_lower is True else '')) for i in range(length))
    else:
        result = ''.join(random.choice((string.ascii_uppercase if eng_upper is True else '') +
                                       (string.ascii_lowercase if eng_lower is True else '') +
                                       (string.digits if digits is True else '') +
                                       (string.punctuation if special_sym is True else '') +
                                       (russian_alphabet_upper if rus_upper is True else '') +
                                       (russian_alphabet_lower if rus_lower is True else '')) for i in range(5000000))
        result = result*round(length/5000000)

    return result


def generate_string_short(length: int, eng_letters: bool, digits: bool, special_sym: bool) -> str:
    if length < 5000000:
        result = ''.join(random.choice((string.ascii_letters if eng_letters is True else '') +
                                       (string.digits if digits is True else '') +
                                       (string.punctuation if special_sym is True else '')) for i in range(length))
    else:
        result = ''.join(random.choice((string.ascii_letters if eng_letters is True else '') +
                                       (string.digits if digits is True else '') +
                                       (string.punctuation if special_sym is True else '')) for i in range(500000))
        result = result*round(length/5000000)

    return result


def generate_integer(length: int) -> int:
    if length < 5000000:
        result = int(''.join(random.choice(string.digits)
                     for i in range(length)))
    else:
        result = ''.join(random.choice(string.digits) for i in range(5000000))
        result = int(result*round(length/5000000))

    return result


if __name__ == '__main__':
    print(generate_string_full(100, False, True, False, False, True, True))
    print(generate_string_short(25, True, True, False))
    print(generate_integer(150))
