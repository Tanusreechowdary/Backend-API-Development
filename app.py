from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
app.config["JSON_SORT_KEYS"] = False
CORS(app)

students = [
    {
        "id": 1,
        "name": "Rahul",
        "age": 20,
        "course": "Computer Science"
    },
    {
        "id": 2,
        "name": "Priya",
        "age": 21,
        "course": "Information Technology"
    }
]


@app.errorhandler(400)
def bad_request(error):
    return jsonify({"success": False, "error": "Bad request"}), 400


@app.errorhandler(404)
def not_found(error):
    return jsonify({"success": False, "error": "Resource not found"}), 404


@app.errorhandler(405)
def method_not_allowed(error):
    return jsonify({"success": False, "error": "Method not allowed"}), 405


@app.route("/")
def home():
    return jsonify({
        "success": True,
        "message": "Student Management API is running successfully.",
        "version": "1.0.0",
        "endpoints": {
            "get_all_students": "/students",
            "get_student_by_id": "/students/<id>",
            "create_student": "/students"
        }
    })


@app.route("/health")
def health_check():
    return jsonify({
        "success": True,
        "status": "healthy",
        "service": "student-management-api"
    })


@app.route("/students", methods=["GET"])
def get_students():
    return jsonify({
        "success": True,
        "count": len(students),
        "students": students
    })


@app.route("/students/<int:student_id>", methods=["GET"])
def get_student(student_id):
    for student in students:
        if student["id"] == student_id:
            return jsonify({
                "success": True,
                "student": student
            })

    return jsonify({
        "success": False,
        "error": f"Student with id {student_id} was not found"
    }), 404


@app.route("/students", methods=["POST"])
def add_student():
    data = request.get_json(silent=True)

    if not data or not isinstance(data, dict):
        return jsonify({
            "success": False,
            "error": "Request body must be a valid JSON object"
        }), 400

    name = data.get("name")
    age = data.get("age")
    course = data.get("course")

    if not name or not isinstance(name, str) or not name.strip():
        return jsonify({
            "success": False,
            "error": "Name is required and must be a non-empty string"
        }), 400

    if not isinstance(age, int) or isinstance(age, bool) or age <= 0 or age > 120:
        return jsonify({
            "success": False,
            "error": "Age must be a valid integer between 1 and 120"
        }), 400

    if not course or not isinstance(course, str) or not course.strip():
        return jsonify({
            "success": False,
            "error": "Course is required and must be a non-empty string"
        }), 400

    new_student = {
        "id": students[-1]["id"] + 1 if students else 1,
        "name": name.strip(),
        "age": age,
        "course": course.strip()
    }

    students.append(new_student)

    return jsonify({
        "success": True,
        "message": "Student added successfully",
        "student": new_student
    }), 201


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)