from fixture.orm import ORMFixture


db = ORMFixture(host='127.0.0.1', name='addressbook', user='root', password='')

try:
    contacts = db.get_contact_list()
    for item in contacts:
        print(item)
    print(len(contacts))
finally:
    pass # db.destroy()

