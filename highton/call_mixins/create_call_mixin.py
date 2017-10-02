from highton.call_mixins import Call


class CreateCallMixin(Call):
    """
    A mixin to retrieve a single object of a highrise endpoint

    """

    def create(self):
        """
        Creates the object

        :return: the created object
        :rtype: object
        """

        # In the header.location there is the newly created object so get the id out of the url
        created_id = self._post_request(
            data=self.element_to_string(self.encode())
        ).headers.get('Location').split('/')[-1]
        return self.get(created_id)
