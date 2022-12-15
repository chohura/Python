import xml.sax

class StudentRegister(xml.sax.ContentHandler):

    def startElement(self, tag, attr):
        self.current = tag
        if tag == "student":
            print(f"\n-- Student {attr['id']}")

    def characters(self, tag):
        if self.current == "imie":
            self.imie = tag
        elif self.current == "nazwisko":
            self.nazwisko = tag
        elif self.current == "numer":
            self.numer = tag

    def endElement(self, tag):
        if self.current == "imie":
            print(f"Imie: {self.imie}")
        elif self.current == "nazwisko":
            print(f"Nazwisko: {self.nazwisko}")
        elif self.current == "numer":
            print(f"Numer: {self.numer}")
        self.current = ""


def main():
    handler = StudentRegister()
    parser = xml.sax.make_parser()
    parser.setContentHandler(handler)
    parser.parse('filexml.xml')


if __name__ == '__main__':
    main()