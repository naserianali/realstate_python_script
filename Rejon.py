from BaseModel import BaseModel


class Rejon(BaseModel):
    def __init__(self, name, *args, **kwargs):
        self.name = name
        super().__init__(*args, **kwargs)
