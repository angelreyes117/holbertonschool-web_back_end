import { readDatabase } from '../utils.js';

class StudentsController {
  /**
   * GET /students
   * Display:
   * This is the list of our students
   * Number of students in FIELD: N. List: a, b, c
   */
  static async getAllStudents(req, res) {
    const dbFile = process.argv[2];
    try {
      const data = await readDatabase(dbFile);

      // Sort fields alphabetically case-insensitive
      const fields = Object.keys(data).sort((a, b) =>
        a.toLowerCase().localeCompare(b.toLowerCase()),
      );

      let output = 'This is the list of our students';
      for (const field of fields) {
        const list = data[field].join(', ');
        output += `\nNumber of students in ${field}: ${data[field].length}. List: ${list}`;
      }

      return res.status(200).send(output);
    } catch (err) {
      return res.status(500).send('Cannot load the database');
    }
  }

  /**
   * GET /students/:major
   * major must be CS or SWE
   * Respond: List: LIST_OF_FIRSTNAMES
   */
  static async getAllStudentsByMajor(req, res) {
    const { major } = req.params;

    if (major !== 'CS' && major !== 'SWE') {
      return res.status(500).send('Major parameter must be CS or SWE');
    }

    const dbFile = process.argv[2];
    try {
      const data = await readDatabase(dbFile);
      const list = data[major] || [];
      return res.status(200).send(`List: ${list.join(', ')}`);
    } catch (err) {
      return res.status(500).send('Cannot load the database');
    }
  }
}

export default StudentsController;
