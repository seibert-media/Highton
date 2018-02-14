from highton.call_mixins import Call


class UpdateCallMixin(Call):
    """
    A mixin to update a singe object of an highrise endpoint

    """

    def update(self):
        """
        Updates the object

        :return:
        :rtype: response
        """
        return self._put_request(
            data=self.element_to_string(
                self.encode()
            ),
            endpoint=self.ENDPOINT + '/' + str(self.id)
        )
