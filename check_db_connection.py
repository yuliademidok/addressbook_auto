from fixture.orm import ORMFixture
from model.group import Group


db = ORMFixture(host='127.0.0.1', name='addressbook', user='root', password='')

try:
    contacts = db.get_contacts_not_in_groups(Group(id='164'))
    for item in contacts:
        print(item)
    print(len(contacts))
finally:
    pass # db.destroy()

