from highton.call_mixins import Call
from highton import fields


class ListTagCallMixin(Call):
    """
    A mixin to get all tags of inherited class
    These could be: people || companies || kases || deals

    """

    def list_tags(self):
        """
        Get the tags of current object

        :return: the tags
        :rtype: list
        """
        from highton.models.tag import Tag
        return fields.ListField(
            name=self.ENDPOINT,
            init_class=Tag
        ).decode(
            self.element_from_string(
                self._get_request(
                    endpoint=self.ENDPOINT + '/' + str(self.id) + '/' + Tag.ENDPOINT,
                ).text
            )
        )
