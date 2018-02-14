from highton.call_mixins import Call
from copy import deepcopy


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
        this = deepcopy(self)
        this.party = None
        return self._put_request(
            data=self.element_to_string(
                this.encode()
            ),
            endpoint=self.ENDPOINT + '/' + str(self.id)
        )
