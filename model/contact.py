from sys import maxsize


class Contact:

    def __init__(self, firstname=None, lastname=None, address=None, email=None, id=None,
                 homephone=None, mobilephone=None, workphone=None, secondaryphone=None, all_phones_from_home_page=None):
        self.firstname = firstname
        self.lastname = lastname
        self.address = address
        self.email = email
        self.id = id
        self.homephone = homephone
        self.mobilephone = mobilephone
        self.workphone = workphone
        self.secondaryphone = secondaryphone
        self.all_phones_from_home_page = all_phones_from_home_page

    def __repr__(self):
        return "%s:%s:%s:%s:%s" % (self.firstname, self.lastname, self.address, self.email, self.id)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.firstname == other.firstname and self.lastname == other.lastname \
               and self.address == other.address and self.email == other.email

    def id_or_max(contact):
        if contact.id:
            return int(contact.id)
        else:
            return int(maxsize)