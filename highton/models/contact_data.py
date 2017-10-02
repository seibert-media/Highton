from highton.models import HightonModel
from highton.highton_constants import HightonConstants
from highton import fields


class ContactData(
    HightonModel
):
    """
    :ivar id: fields.IntegerField(name=HightonConstants.ID)
    :ivar phone_numbers: fields.ListField(name=HightonConstants.PHONE_NUMBERS, init_class=PhoneNumber)
    :ivar twitter_accounts: fields.ListField(name=HightonConstants.TWITTER_ACCOUNTS, init_class=TwitterAccount)
    :ivar web_addresses: fields.ListField(name=HightonConstants.WEB_ADDRESSES, init_class=WebAddress)
    :ivar email_addresses: fields.ListField(name=HightonConstants.EMAIL_ADDRESSES, init_class=EmailAddress)
    :ivar addresses: fields.ListField(name=HightonConstants.ADDRESSES, init_class=Address)
    :ivar instant_messenger: fields.ListField(name=HightonConstants.INSTANT_MESSENGERS, init_class=InstantMessenger)

    """
    TAG_NAME = HightonConstants.CONTACT_DATA

    def __init__(self, **kwargs):
        from highton.models import (
            PhoneNumber,
            TwitterAccount,
            WebAddress,
            EmailAddress,
            Address,
            InstantMessenger,
        )

        self.phone_numbers = fields.ListField(name=HightonConstants.PHONE_NUMBERS, init_class=PhoneNumber)
        self.twitter_accounts = fields.ListField(name=HightonConstants.TWITTER_ACCOUNTS, init_class=TwitterAccount)
        self.web_addresses = fields.ListField(name=HightonConstants.WEB_ADDRESSES, init_class=WebAddress)
        self.email_addresses = fields.ListField(name=HightonConstants.EMAIL_ADDRESSES, init_class=EmailAddress)
        self.addresses = fields.ListField(name=HightonConstants.ADDRESSES, init_class=Address)
        self.instant_messenger = fields.ListField(name=HightonConstants.INSTANT_MESSENGERS, init_class=InstantMessenger)

        for key, value in kwargs.items():
            setattr(self, key, value)
