class Cow:

    image = None
    name = None
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def get_image(self):
        return self.image

    def set_image(self, image):
        self.image = image

