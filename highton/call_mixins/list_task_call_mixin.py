from highton.call_mixins import Call
from highton import fields


class ListTaskCallMixin(Call):
    """
    A mixin to get all tasks of inherited class
    These could be: people || companies || kases || deals

    """

    def list_tasks(self):
        """
        Get the tasks of current object

        :return: the tasks
        :rtype: list
        """
        from highton.models.task import Task

        return fields.ListField(
            name=self.ENDPOINT,
            init_class=Task
        ).decode(
            self.element_from_string(
                self._get_request(
                    endpoint=self.ENDPOINT + '/' + str(self.id) + '/' + Task.ENDPOINT,
                ).text
            )
        )
