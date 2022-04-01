text = "hello"
parts = ["<p>", text, "</p>"]
print("".join(parts))

words = ["hello", "world"]
parts = ["<ul>"]
for w in words:
    parts.append(f" <li>{w}</li>")
parts.append("</ul>")
print("\n".join(parts))

"""
Part of the code above would be working in very limited scenario with only 
few lines of code and eventhough we can forget on closing some elements etc. 
Its better to have builder handling all of these things for us, 
"""


class HtmlElement:
    indent_size = 2

    def __init__(self, name="", text=""):
        self.name = name
        self.text = text
        self.elements = []

    def __str(self, indent):
        lines = []
        i = ' ' * (indent * self.indent_size)
        lines.append(f'{i}<{self.name}>')

        if self.text:
            i1 = ' ' * ((indent + 1) * self.indent_size)
            lines.append(f'{i1}{self.text}')

        for e in self.elements:
            lines.append(e.__str(indent + 1))

        lines.append(f'{i}</{self.name}>')
        return '\n'.join(lines)

    def __str__(self):
        return  self.__str(0)

class HtmlBuilder:
    def __init__(self, root_name):
        self.root_name = root_name
        self.__root = HtmlElement(name = root_name)