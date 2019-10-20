email_subject = "Your order is ready \ngo for it\nhere you go"
from_address = "from@provider.com"
to_address = "to@provider.com"
name = "Ali"

message = """
    From: {}
    To: {}

    Hi, {}
    {subject}
""".format(from_address,to_address,name,subject = email_subject.replace("\n","\n" + " " * 4))
print(message)