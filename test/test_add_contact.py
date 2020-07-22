from model.contact import Contact


def test_add_contact(app, db, check_ui):
    old_contacts = db.get_contact_list()
    contact = Contact(firstname="Tom", lastname="Tompson", address="Noname Street", email="test@test.com")
    app.contact.create(contact)
    new_contacts = db.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
