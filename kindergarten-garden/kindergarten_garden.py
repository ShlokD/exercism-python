plant_map = {
    'V': 'Violets',
    'R': 'Radishes',
    'C': 'Clover',
    'G': 'Grass'
}

students_default = ["Alice", "Bob", "Charlie", "David","Eve", "Fred", "Ginny", "Harriet","Ileana", "Joseph", "Kincaid", "Larry"]

class Garden(object):
    def __init__(self, diagram, students = students_default):
        if students:
            self.students = sorted(students)

        self.garden = {}
        rows = diagram.split("\n");
        cups = []
        for row in rows:
            cups.append([row[j:j + 2] for j in range(0, len(row), 2)])

        for student, plants in zip(self.students, zip(*cups)):
            self.garden[student] = ''.join(plants)

    def plants(self, student):
        return [plant_map[p] for p in self.garden[student]]

