import re

def check_email(address):
    pattern = r"^\S+@\S+.\S+$"
    return re.match(pattern, address) is not None

if __name__ == '__main__':
    print(check_email("bro@gmail.com"))
    print(check_email("poiqewfopiqure.com"))
