import json
import requests


def get_results(uri):
    r = requests.get(uri)
    # test_data = {"students":[{"id":"1001","name":"Alice","score":65},{"id":"1002","name":"Bob","score":80}]}
    # students = test_data["students"]
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
