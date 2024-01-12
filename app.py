from flask import Flask, request
from flask import jsonify, render_template
app = Flask(__name__)

lessons = [
    {"id": 1, "name": "Python programming", "credits": 5},
    {"id": 2, "name": "Java programming", "credits": 4},
    {"id": 3, "name": "TypeScript programming", "credits": 3},
    {"id": 4, "name": "C++ programming", "credits": 1},
];

@app.route('/')
def hello_world():
    return 'Hello, World! Now my app is running locally!!!! Yeah!!!!!!!!!!!!!!!!!'

@app.route('/lessons')
def get_lessons():
    return jsonify(lessons);

@app.route('/create-lesson')
def create_lesson():
    name = request.args["name"];
    credits = request.args["credits"];
    id = len(lessons)+1;
    newLesson = {"id": id, "name": name, "credits": credits};
    lessons.append(newLesson);
    return jsonify(lessons);

@app.route('/delete/<lesson_id>', methods=["GET"])
def delete_lesson(lesson_id):
    for lesson in lessons:
        if lesson["id"] == int(lesson_id):
            lessons.remove(lesson);
    return render_template("delete-success.html", lesson_id = lesson_id)


if __name__ == "__main__":
    app.run();
