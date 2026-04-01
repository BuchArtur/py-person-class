class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people_data: list) -> list:
    Person.people = {}

    for p_dict in people_data:
        Person(p_dict["name"], p_dict["age"])

    result = []
    for p_dict in people_data:
        name = p_dict["name"]
        instance = Person.people[name]

        spouse_key = "wife" if "wife" in p_dict else "husband"
        spouse_name = p_dict.get(spouse_key)

        if spouse_name:
            setattr(instance, spouse_key, Person.people[spouse_name])

        result.append(instance)

    return result
