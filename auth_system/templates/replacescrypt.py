import re
filenames = ["index.html", "index2.html", "info.html", "infopl.html", "other.html", "otherpl.html", "programs.html", "programspl.html", "py.html", "pypl.html"]

for filename in filenames:

    with open(filename, "r") as src:
        html_text = src.read()

    pattern = r'src=[\'"](.*?)[\'"]'

    wrapped_text = re.sub(pattern, r"src='{% static \"\1\" %}'", html_text)
    wrapped_text = wrapped_text.replace(r'\"', '"')
    wrapped_text = wrapped_text.replace(r"\'", "'")

    pattern = r'href=[\'"](.*?)[\'"]'

    wrapped_text = re.sub(pattern, r"href='{% static \"\1\" %}'", wrapped_text)
    wrapped_text = wrapped_text.replace(r'\"', '"')
    wrapped_text = wrapped_text.replace(r"\'", "'")

    wrapped_text = "{%load static%}" + wrapped_text

    print(wrapped_text)

    with open(filename, "w") as src:
        src.write(wrapped_text)
