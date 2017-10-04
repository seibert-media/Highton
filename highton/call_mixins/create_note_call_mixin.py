from highton.call_mixins import Call


class CreateNoteCallMixin(Call):
    """
    A mixin to create a Note to inherited class
    These could be: people || companies || kases || deals

    """

    def add_note(self, body):
        """
        Create a Note to current object

        :param body: the body of the note
        :type body: str
        :return: newly created Note
        :rtype: Tag
        """
        from highton.models.note import Note
        created_id = self._post_request(
            endpoint=self.ENDPOINT + '/' + str(self.id) + '/' + Note.ENDPOINT,
            data=self.element_to_string(
                Note(body=body).encode()
            )
        ).headers.get('Location').replace('.xml', '').split('/')[-1]
        return Note.get(created_id)
