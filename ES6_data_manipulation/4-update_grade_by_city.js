export default function updateStudentGradeByCity(students, city, newGrades) {
    if (!Array.isArray(students) || !Array.isArray(newGrades)) {
        return [];
    }
    return students.map((student) => {
        if (student.location === city) {
            const grade = newGrades.find((grade) => grade.studentId === student.id);
            if (grade) {
                return { ...student, grade: grade.grade };
            }
        }
        return student;
    });
}
