from twilio.rest import Client


def send_sms(contact, message):
    """
    Send sms to the given number

    :param message: The message to be sent to the number
    :return: None
    """
    account_sid = "ACcd667f6f6e95aac7ccca9b6e03638198"
    auth_token = "04bdceaf5721cbca7668b7da4212ea18"
    client = Client(account_sid, auth_token)

    client.messages.create(body=message, to="+65"+contact, from_="+13142000173")

    print("SMS has been sent t  o " + "+65"+contact)