from highton.call_mixins import Call


class DeleteCallMixin(Call):
    """
    A mixin to delete a single object of a highrise endpoint

    """

    def delete(self):
        """
        Deletes the object

        :return:
        :rtype: None
        """
        return self._delete_request(endpoint=self.ENDPOINT + '/' + str(self.id))
