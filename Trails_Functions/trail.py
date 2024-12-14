class Trails:
    def __init__(self, id, name, island, council, coordinates,
                 difficulty, extension, form, description):
        self.id = id
        self.name = name
        self.island = island
        self.council = council
        self.coordinates = coordinates
        self.difficulty = difficulty
        self.extension = extension
        self.form = form
        self.description = description

    # Getter methods
    def get_id(self) -> int:
        return self.id

    def get_name(self) -> str:
        return self.name

    def get_island(self) -> str:
        return self.island

    def get_council(self) -> str:
        return self.council

    def get_coordinates(self) -> str:
        return self.coordinates

    def get_difficulty(self) -> str:
        return self.difficulty

    def get_extension(self) -> str:
        return self.extension

    def get_form(self) -> str:
        return self.form

    def get_description(self) -> str:
        return self.description

    # Setter methods
    def set_id(self:None, id:int) -> None:
        self.id = id
        return None
    def set_name(self, name:str) -> None:
        self.name = name
        return None
    def set_island(self, island:str) -> None:
            self.island = island
            return None
    def set_council(self, council:str) -> None:
            self.council = council
            return None
    def set_coordinates_GPS(self, coordinates:str) -> None:
            self.coordinates = coordinates
            return None
    def set_difficulty(self, difficulty:str) -> None:
            self.difficulty = difficulty
            return None
    def set_extension(self, extension:str) -> None:
            self.extension = extension
            return None
    def set_form(self, form:str) -> None:
            self.form = form
            return None
    def set_description(self, description:str) -> None:
            self.description = description
            return None
    def format(self):
        return (f"{self.get_id()};{self.get_name()};{self.get_island()};{self.get_council()}"
                f";{self.get_coordinates()};{self.get_difficulty()};{self.get_extension()};"
                f"{self.get_form()};{self.get_description()}")