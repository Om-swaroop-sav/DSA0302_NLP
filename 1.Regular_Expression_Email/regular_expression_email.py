import re
text = "My email is test@gmail.com"
if re.search(r'\w+@\w+\.\w+', text):
    print("Email found")
else:
    print("Email not found")
