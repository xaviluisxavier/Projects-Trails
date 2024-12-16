class Guide:
    def __init__(self, id: str, name: str, experience: int, number: str, email: str, languages: list, availability: list):
        # Constructor to initialize a Guide object with given attributes
        self.id = id
        self.name = name
        self.experience = experience
        self.contact = {
            "number": number,
            "email": email
        }
        self.languages = languages
        self.availability = availability

    # Property decorators for read-only access to attributes
    @property
    def id(self):
        return self.id

    # Property decorator with setter for id attribute
    @id.setter
    def id(self, value):
        self.id = value

    @property
    def name(self):
        return self.name

    @property
    def experience(self):
        return self.experience

    @property
    def contact(self):
        return self.contact

    @property
    def languages(self):
        return self.languages

    @property
    def availability(self):
        return self.availability

    # Method to update contact information
    def update_contact(self, number: str, email: str):
        self.contact["number"] = number
        self.contact["email"] = email

    # Method to update languages
    def update_languages(self, languages: list):
        self.languages = languages

    # Method to update availability
    def update_availability(self, availability: list):
        self.availability = availability
