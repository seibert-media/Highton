from highton.call_mixins import Call


class CreateTagCallMixin(Call):
    """
    A mixin to create a tag to inherited class
    These could be: people || companies || kases || deals

    """

    def add_tag(self, name):
        """
        Create a Tag to current object

        :param name: the name of the tag
        :type name: str
        :return: newly created Tag
        :rtype: Tag
        """
        from highton.models.tag import Tag
        created_id = self._post_request(
            endpoint=self.ENDPOINT + '/' + str(self.id) + '/' + Tag.ENDPOINT,
            data=self.element_to_string(
                Tag(name=name).__dict__.get('name').encode()
            )
        ).headers.get('Location').replace('.xml', '').split('/')[-1]
        return Tag.get(created_id)
