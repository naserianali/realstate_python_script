from BaseModel import BaseModel


class User(BaseModel):
    def __init__(self, first_name, last_name, phone, *args, **kwargs):
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        super().__init__(*args, **kwargs)

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
