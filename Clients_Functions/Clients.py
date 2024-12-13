class Visits:
    def __init__(self, name, country, gender, age_group, date, satisfaction, trail):
        self.name = name
        self.country = country
        self.gender = gender
        self.age_group = age_group
        self.date = date
        self.satisfaction = satisfaction
        self.trail = trail

    def getName(self):
        return self.name

    def getCountry(self):
        return self.country

    def getGender(self):
        return self.gender

    def getAgeGroup(self):
        return self.age_group

    def getDate(self):
        return self.date

    def getSatisfaction(self):
        return self.satisfaction

    def getTrail(self):
        return self.trail

    def setName(self, name):
        self.name = name
        return None

    def setCountry(self, country):
        self.country = country
        return None

    def setGender(self, gender):
        self.gender = gender
        return None

    def setAgeGroup(self, age_group):
        self.age_group = age_group
        return None

    def setDate(self, date):
        self.date = date
        return None

    def setSatisfaction(self, satisfaction):
        self.satisfaction = satisfaction
        return None

    def setTrail(self, trail):
        self.trail = trail
        return None

    def format(self):
        return (f"{self.name};{self.country};{self.gender};{self.age_group};"
                f"{self.date};{self.satisfaction}")