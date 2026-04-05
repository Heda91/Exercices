"""
You are given an integer N followed by N email addresses. Your task is to print a list containing only valid
email addresses in lexicographical order.

Valid email addresses must follow these rules:
- It must have the {username@websitename.extension} format type.
- The username can only contain letters, digits, dashes and underscores [a-z],[A-Z],[0-9],[_-].
- The website name can only have letters and digits [a-z],[A-Z],[0-9].
- The extension can only contain letters [a-z],[A-Z].
- The maximum length of the extension is 3.
"""
import sys, re

sys.stdin = open("Validating Email Addresses With a Filter.txt")  # to delete


def fun(s) -> bool:
    return re.fullmatch(r'\A[\w-]+[@]{1}[a-zA-Z0-9]+[.]{1}[a-zA-Z]{1,3}\Z', s) is not None


def filter_mail(emails):
    return list(filter(fun, emails))


data = str(sys.stdin.buffer.read(), 'utf-8').splitlines()
emails = data[1:]
filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)
