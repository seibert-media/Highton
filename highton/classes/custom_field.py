

class SubjectData:
    def __init__(
        self,
        highrise_id,
        value,
        subject_field_id,
        subject_field_label,
    ):
        self.highrise_id = highrise_id.pyval
        self.value = value.pyval
        self.subject_field_id = subject_field_id.pyval
        self.subject_field_label = subject_field_label.pyval
