import xml.sax

"""
A simple parser to present XML data in a user-friendly manner.
"""


class StudentHandler(xml.sax.ContentHandler):
    """initializes the child attributes from the xml.sax module"""
    def __init__(self):
        super().__init__()
        self.CurrentData = ""
        self.Student = ""
        self.DepartmentOwnerId = ""
        self.LastName = ""
        self.FirstName = ""
        self.BirthDate = ""
        self.Gender = ""
        self.CitizenshipCountryCode = ""
        self.ProfileType = ""
        self.PrimaryMajor = ""

    # Call when an element starts
    def startElement(self, tag, attributes):
        self.CurrentData = tag
        if tag == "Student":
            print("****Student****")
            campusId = attributes["campusId"]
            print("campusId:", campusId)


    # Call when an elements ends
    def endElement(self, content):
        if self.CurrentData == "DepartmentOwnerId":
            print("Department Owner ID:", self.DepartmentOwnerId)
        elif self.CurrentData == "LastName":
            print("Last Name:", self.LastName)
        elif self.CurrentData == "FirstName":
            print("First Name:", self.FirstName)
        elif self.CurrentData == "BirthDate":
            print("BirthDate:", self.BirthDate)
        elif self.CurrentData == "Gender":
            print("Gender:", self.Gender)
        elif self.CurrentData == "CitizenshipCountryCode":
            print("Citizenship Country Code:", self.CitizenshipCountryCode)
        elif self.CurrentData == 'ProfileType':
            print('ProfileType:', self.ProfileType)
        elif self.CurrentData == 'PrimaryMajor':
            print('PrimaryMajor:', self.PrimaryMajor)
            print('\n')
        self.CurrentData = ""
     

    # Call when a character is read
    def characters(self, content):
        if self.CurrentData == "DepartmentOwnerId":
            self.DepartmentOwnerId = content
            if content == "": # find a blank DeptID
                raise ValueError
        elif self.CurrentData == "LastName":
            self.LastName = content
        elif self.CurrentData == "FirstName":
            self.FirstName = content
        elif self.CurrentData == "BirthDate":
            self.BirthDate = content
        elif self.CurrentData == "Gender":
            self.Gender = content
        elif self.CurrentData == "CitizenshipCountryCode":
            self.CitizenshipCountryCode = content
        elif self.CurrentData == 'ProfileType':
            self.ProfileType = content
        elif self.CurrentData == 'PrimaryMajor':
            self.PrimaryMajor = content


if (__name__ == "__main__"):
    # create an XMLReader
    parser = xml.sax.make_parser()

    # override the default ContextHandler
    Handler = StudentHandler()
    parser.setContentHandler(Handler)

    parser.parse("fsaAtlas_xml/NewSASStudentDrop.xml")




