import re

email = input("What's your email? ").strip()

if re.search(r"^\w+@(\w+\.)\w+\.edu$", email, re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")


# re.search(patterns, string, flags=0)
# re.match(pattern, string, flags=0)
# re.fullmatch(pattern, string, flags=0)
