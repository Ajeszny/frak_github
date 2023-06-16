import re

with open("index2.html", "r") as src:
    html_text = src.read()

pattern = r'src=[\'"](.*?)[\'"]'

wrapped_text = re.sub(pattern, r"src='{% static \"\1\" %}'", html_text)
wrapped_text = wrapped_text.replace(r'\"', '"')

with open("index.html", "w") as src:
    src.write(wrapped_text)
