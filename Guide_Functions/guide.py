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

    # Getter methods
    def get_id(self) -> str:
        return self.id

    def get_name(self) -> str:
        return self.name

    def get_experience(self) -> int:
        return self.experience

    def get_contact(self) -> dict:
        return self.contact

    def get_languages(self) -> list:
        return self.languages

    def get_availability(self) -> list:
        return self.availability

    # Setter methods
    def set_id(self, id: str) -> None:
        self.id = id
        return None

    def set_name(self, name: str) -> None:
        self.name = name
        return None

    def set_experience(self, experience: int) -> None:
        self.experience = experience
        return None

    def set_contact(self, number: str, email: str) -> None:
        self.contact = {"number": number, "email": email}
        return None

    def set_languages(self, languages: list) -> None:
        self.languages = languages
        return None

    def set_availability(self, availability: list) -> None:
        self.availability = availability
        return None

    # Method to update contact information
    def update_contact(self, number: str, email: str) -> None:
        self.set_contact(number, email)
        return None

    # Method to update languages
    def update_languages(self, languages: list) -> None:
        self.set_languages(languages)
        return None

    # Method to update availability
    def update_availability(self, availability: list) -> None:
        self.set_availability(availability)
        return None