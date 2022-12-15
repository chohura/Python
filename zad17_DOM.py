'Sparsuj przygotowanego XML (parserem SAX i DOM) i go zmodyfikuj np. zmień wartość któregoś tag’a i zapisz do nowego pliku'

import xml.dom.minidom


if __name__ == '__main__':
    dom = xml.dom.minidom.parse('filexml.xml')
    people = dom.documentElement
    students = people.getElementsByTagName('student')
    for student in students:
        print(f"\nStudent: {student.getAttribute('id')}")

        imie = student.getElementsByTagName('imie')[0].childNodes[0].nodeValue
        nazwisko = student.getElementsByTagName('nazwisko')[0].childNodes[0].nodeValue
        numer = student.getElementsByTagName('numer')[0].childNodes[0].nodeValue

        print(f"Imie: {imie}")
        print(f"Nazwisko: {nazwisko}")
        print(f"Numer: {numer}")