from highton.call_mixins import Call


class DeleteTagCallMixin(Call):
    """
    A mixin to delete a tag to inherited class
    These could be: people || companies || kases || deals

    """

    def delete_tag(self, tag_id):
        """
        Deletes a Tag to current object

        :param tag_id: the id of the tag which should be deleted
        :type tag_id: int
        :return: newly created Tag
        :rtype: Tag
        """
        from highton.models.tag import Tag
        created_id = self._delete_request(
            endpoint=self.ENDPOINT + '/' + str(self.id) + '/' + Tag.ENDPOINT + '/' + str(tag_id),
        ).headers.get('Location').split('/')[-1]
        return Tag.get(created_id)
