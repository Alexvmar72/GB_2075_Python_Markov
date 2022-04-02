import re


def email_parse(email: str) -> dict:
    RE_MAIL = re.compile(r'(?P<username>\w+)@(?P<domain>\w+\.\w{2,})', re.IGNORECASE)
    subtotal = RE_MAIL.findall(email)
    if subtotal == [] or email.count("@") > 1:
        raise ValueError(f'wrong email: {email}')
    else:
        subtotal_2 = RE_MAIL.finditer(email)
        for element in subtotal_2:
            return element.groupdict()


if __name__ == '__main__':
    email_parse('someone@geekbrains.ru')
    #email_parse('someone@geekbrainsru')
    #email_parse('someone@geekbrains.info')
    email_parse('someone@geekb@rains.rules')