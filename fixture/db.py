import mysql.connector
from model.group import Group
from model.contact import Contact


class DbFixture:
    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = mysql.connector.connect(host=host, database=name, user=user, password=password)
        # reset cache
        self.connection.autocommit = True

    def get_group_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name from group_list")
            for row in cursor:
                (id, name) = row
                list.append(Group(id=str(id), name=name))
        finally:
            cursor.close()
        return list

    def get_contact_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, lastname, address, email from addressbook where deprecated='0000-00-00 00:00:00'")
            for row in cursor:
                (id, firstname, lastname, address, email) = row
                list.append(Contact(id=str(id), firstname=firstname, lastname=lastname, address=address, email=email))
        finally:
            cursor.close()
        return list

    def destroy(self):
        self.connection.close()
