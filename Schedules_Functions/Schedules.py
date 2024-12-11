class Schedules:
    def __init__(self,trail, guide, checkin, checkout):
        self.trail = trail
        self.guide = guide
        self.checkin = checkin
        self.checkout = checkout

    #getters
    def getTrail(self):
        return self.trail
    def getGuide(self):
        return self.guide
    def getCheckin(self):
        return self.checkin
    def getCheckout(self):
        return self.checkout

    #setters
    def setTrail(self, trail):
        self.trail = trail
        return self
    def setGuide(self, guide):
        self.guide = guide
        return self
    def setCheckin(self, checkin):
        self.checkin = checkin
        return self
    def setCheckout(self, checkout):
        self.checkout = checkout
        return self

    def format(self):
        return f'{self.trail};{self.guide};{self.checkin};{self.checkout};\n'