
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        self._next_id = 1
        self._members = []
        # Inicializar la familia con los miembros dados
        self._initialize_family()

    def _initialize_family(self):
        # Miembros iniciales de la familia
        initial_members = [
            {
                "id": self._generate_id(),
                "first_name": "John",
                "last_name": self.last_name,
                "age": 33,
                "lucky_numbers": [7, 13, 22]
            },
            {
                "id": self._generate_id(),
                "first_name": "Jane",
                "last_name": self.last_name,
                "age": 35,
                "lucky_numbers": [10, 14, 3]
            },
            {
                "id": self._generate_id(),
                "first_name": "Jimmy",
                "last_name": self.last_name,
                "age": 5,
                "lucky_numbers": [1]
            }
        ]
        self._members.extend(initial_members)

    # No debes modificar este método
    def _generate_id(self):
        generated_id = self._next_id
        self._next_id += 1
        return generated_id

    def add_member(self, member):
        # Verificar si el miembro tiene un 'id', si no, generarlo
        if 'id' not in member or member['id'] is None:
            member['id'] = self._generate_id()
        # Asegurarse de que el 'last_name' sea el de la familia
        member['last_name'] = self.last_name
        self._members.append(member)

    def delete_member(self, id):
        # Eliminar el miembro con el 'id' proporcionado
        self._members = [m for m in self._members if m['id'] != id]

    def get_member(self, id):
        # Obtener el miembro con el 'id' proporcionado
        for member in self._members:
            if member['id'] == id:
                return member
        return None  # Si no se encuentra el miembro

    def get_all_members(self):
        return self._members
