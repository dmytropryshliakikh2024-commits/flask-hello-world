function addCourseObject(courseList, course) {
    // Check if courseList is an array
    if (!Array.isArray(courseList)) {
        throw new Error("First argument must be an array");
    }

    // Check if course is an object
    if (typeof course !== 'object' || course === null) {
        throw new Error("Second argument must be an object");
    }

    // Add the course object to the courseList array
    courseList.push(course);

    return courseList;
}