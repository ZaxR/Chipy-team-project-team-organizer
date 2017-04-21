class Person(object):
    persondict = {}

    def __init__(self, name, lines):
        self.name = name
        self.lines = lines
        if self.name in Person.persondict:
            print("{name} was already added. Value has been updated from {value1} to {value2}.".format(
                    name=self.name, value1=Person.persondict[self.name], value2=self.lines))
        Person.persondict.update({self.name: self.lines})

    def removePerson(self):
        pass


class Teams(object):
    teamlist = []

    def __init__(self):
        self.sortedpersonlist = sorted(Person.persondict.items(), key=lambda k: k[1])

    def createTeams(self):
        while len(self.sortedpersonlist) > 4:
            Teams.teamlist.append([self.sortedpersonlist.pop(0)[0],
                                   self.sortedpersonlist.pop(0)[0],
                                   self.sortedpersonlist.pop()[0],
                                   self.sortedpersonlist.pop()[0]]
                                  )
        Teams.teamlist.append(self.sortedpersonlist)  # todo needs to be fixed
        for team in Teams.teamlist:
            print(team)


class Room(object):
    pass


if __name__ == '__main__':
    response = input("Do you want to add another person (y/n)?: ")
    while response == "y":
        name = input("What's the person's name?: ")
        lines = input("How many lines of code has " + name + " written?: ")
        Person(name, lines)
        response = input("Do you want to add another person? y/n")

    Teams().createTeams()
