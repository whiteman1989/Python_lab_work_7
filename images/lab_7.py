class Person:
    def __init__(self, first_name, second_name, score = 0):
        self.first_name = first_name
        self.second_name = second_name
        self.score = score

    def __del__(self):
        print('Ви отримали стипендію', self.get_fullname())

    def get_info(self):
        return 'Name: '+self.get_fullname()+', Score: '+str(self.score)

    def get_fullname(self):
        return self.first_name+' '+self.second_name

group = [Person('Олег','Трофимов',75),Person('Олексій', 'Утюгов', 90), Person('Олена', 'Карасьова', 87)]

for student in group:
    print(student.get_info())

input()
