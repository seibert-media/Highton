from contact import Contact


class Company(Contact):
    """
        Feel free to work with this attributes.
        highrise_id,
        first_name,
        last_name,
        title,
        background,
        linkedin_url,
        avatar_url,
        company_id,
        company_name,
        created_at,
        updated_at,
        visible_to,
        owner_id,
        group_id,
        author_id,
        phone_numbers,
        email_addresses,
        subject_datas,
        tags
    """
    def save_data(self, company):
        self.highrise_id = company['id']

        for attr in [
            'author-id',
            'background',
            'created-at',
            'group-id',
            'owner-id',
            'updated-at',
            'visible-to',
            'name',
            'avatar-url',
        ]:
            setattr(self, attr.replace('-', '_'), company[attr])

        for attr in [
            'phone-numbers',
            'email-addresses',
            'addresses',
        ]:
            if hasattr(company['contact-data'], attr):
                getattr(self, 'set_' + attr.replace('-', '_'))(company['contact-data'][attr])

        for attr in [
            'subject_datas',
            'tags',
        ]:
            if hasattr(company, attr):
                getattr(self, 'set_' + attr.replace('-', '_'))(company[attr])