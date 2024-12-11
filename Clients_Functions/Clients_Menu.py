from idlelib.iomenu import encoding

import Clients
from datetime import datetime

class Visits:
    def __init__(self, st="trails.csv", tf = "clients.csv") -> None:
        self.visit = tf
        self.trails = st

    def saveVisits(self, tr):
        file = open(self.visit, "a", encoding="utf-8")
        file.write(tr)

    def findTrail(self):
        while True:
                id = int(input("Enter the id of the trail: "))
                if len(str(id)) != 4:
                    print("Enter a valid trail id")
                else:
                    break
        with open(self.trails, "r", encoding="utf-8") as file:
            lines = file.readlines()
            for line in lines:
                if str(id) in line.strip().split(";")[8]:
                    self.trails = line.strip().split(";")[0]
        print(f"Trails {self.trails} founded")