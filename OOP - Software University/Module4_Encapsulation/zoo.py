
from Project.animal import Animal
from Project.worker import Worker
 

class Zoo:

    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):

        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity

        self.animals = list()
        self.workers = list()

    def add_animal(self, animal: Animal, price):

        self.animal = animal
        self.price = price

        if self.__budget >= price  and self.animal_capacity > 0:
            self.__animal_capacity -= 1
            self.animals.append(self.animal)
            self.__budget -= self.price
            self.price = 0
            return f"{self.animal.name} /////TYPE OF ANIMAL///// added to the zoo"

        elif self.__budget < self.price and capacity > 0:
            return f"Not enough budget"

        else:
            return f"Not enough space for animal"

    def hire_worker(self, worker: Worker):
        self.worker = worker
        if self.__workers_capacity > 0:
            self.workers.append(self.worker)
            return f"{self.worker.name} the type/////TYPE OF WORKER//// hired succesfully "

        else:
            return f"Not enough space for worker "

    def fire_worker(self, worker_name: str):
        for i in len(self.workers):
            if worker_name == worker.name:
                deletion = int(i)
            else:
                deletion = 'NA'

        if deletion != 'NA':
            del self.workers[deletion]
            return f"{worker_name} fired successfully"
        else:
            return f"There is no {worker_name} in the zoo"

    def pay_workers(self):

        self.owed_salary_total = 0

        for worker in self.workers:
            self.owed_salary_total += worker.salary

        if self.owed_salary_total <= self.__budget:
            self.__budget -= self.owed_salary_total
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        else:
            return f"You have no budget to pay your workers. They  are unhappy."

    def tend_animals(self):

        self.total_cost_for_care = 0

        for animal in self.animals:
            self.total_cost_for_care += animal.money_for_care

        if self.__budget >= self.total_cost_for_care:
            self.__budget -= self.total_cost_for_care
            return f"You have tended all the animals. They are happy. Budet left {self.__budget}"
        else:
            return f"You have no budget to tend the animals. The ramaining budget is {self.__budget}"

    def profit(self, amount: int):
        self.__budget += amount


    def animals_status(self):
        result = f'You have {len(self.animals)} animals\n'
        result += self.__build_animal_str('Lion')
        result += self.__build_animal_str('Tiger')
        result += self.__build_animal_str('Cheetah')
        return result

    def workers_status(self):
        return f'You have {len(self.workers)} workers'


    def __build_animal_str(self, animal_type):
        filtered = []
        for animal in self.animals:
            if animal.__class__.__name__ == animal_type:
                filtered.append(animal)

        result = f'----- {len(filtered)} {animal_type}s:\n'

        for obj in filtered:
            result += repr(obj) + '\n'
        return result
