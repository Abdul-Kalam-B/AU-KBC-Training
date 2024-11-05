
from file1 import PersonManager

manager = PersonManager()

manager.load_data('data.txt')

print("Initial data from file:")
manager.display_all_people()

manager.add_person("David", 28)

manager.update_person_age("Alice", 35)

print("\nData after modifications:")
manager.display_all_people()

manager.save_data('data.txt')
