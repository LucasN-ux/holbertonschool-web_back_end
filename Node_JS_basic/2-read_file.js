function countStudents(path) {
    const fs = require('fs');
    fs.readFile(path, 'utf-8', (err, data) => {
        if (err) {
            throw new Error('Cannot load the database');
        }
        const lines = data.split('\n').slice(1);
        const students = {};
        lines.forEach(line => {
            if (line) {
                const [firstName, lastName, age, field] = line.split(',');
                if (!students[field]) {
                    students[field] = [];
                }
                students[field].push(firstName);
            }
        });
        const totalStudents = lines.filter(line => line).length;
        console.log(`Number of students: ${totalStudents}`);
        for (const field in students) {
            console.log(`Number of students in ${field}: ${students[field].length}. List: ${students[field].join(', ')}`);
        }
    });
}
module.exports = countStudents;