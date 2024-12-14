class Guide:
    def __init__(self, id: str, name: str, experience: int, number: str, email: str, languages: list, availability: list):
        # Constructor to initialize a Guide object with given attributes
        self._id = id
        self._name = name
        self._experience = experience
        self._contact = {
            "number": number,
            "email": email
        }
        self._languages = languages
        self._availability = availability

    # Property decorators for read-only access to attributes
    @property
    def id(self):
        return self._id

    # Property decorator with setter for id attribute
    @id.setter
    def id(self, value):
        self._id = value

    @property
    def name(self):
        return self._name

    @property
    def experience(self):
        return self._experience

    @property
    def contact(self):
        return self._contact

    @property
    def languages(self):
        return self._languages

    @property
    def availability(self):
        return self._availability

    # Method to update contact information
    def update_contact(self, number: str, email: str):
        self._contact["number"] = number
        self._contact["email"] = email

    # Method to update languages
    def update_languages(self, languages: list):
        self._languages = languages

    # Method to update availability
    def update_availability(self, availability: list):
        self._availability = availability
