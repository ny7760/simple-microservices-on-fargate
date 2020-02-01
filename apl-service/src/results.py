import json
import requests


def get_results(uri):
    r = requests.get(uri)
    students = r.json()["students"]
    return_students = []
    for student in students:
        if student["score"] > 70:
            student.setdefault("isPassed", True)
            return_students.append(student)
        else:
            student.setdefault("isPassed", False)
            return_students.append(student)

    return_json = json.dumps({"addedStudents": return_students})

    return return_json


if __name__ == '__main__':
    print(get_results('http://db-service/students'))
