class Contact:
    def __init__(self, first_name, last_name, email_address):
        self.first_name = first_name
        self.last_name = last_name
        self.email_address = address = email_address

    def add_phone_number(self, telephone_num):
        self.add_phone_number = telephone_num
    
    def __str__(self):
        return '{0}, {1},<{2}>'.format(self.first_name, self.last_name, self.email_address)
    
class Email:
    def __init__(self, recipients, subject, body):

        self.recipients = recipients
        self.subject = subject
        self.body = body

