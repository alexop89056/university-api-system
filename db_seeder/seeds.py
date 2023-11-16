from django_seed import Seed
from api.models import Student
from api.models import Teacher


def students():
    seeder = Seed.seeder()
    seeder.add_entity(Student, 30)
    inserted_pks = seeder.execute()


def teachers():
    seeder = Seed.seeder()
    seeder.add_entity(Teacher, 30)
    inserted_pks = seeder.execute()
