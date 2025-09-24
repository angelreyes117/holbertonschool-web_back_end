const fs = require('fs');

const countStudents = (path) => {
  if (!fs.existsSync(path)) {
    throw new Error('Cannot load the database');
  }
  const FileContents = fs.readFileSync(path, 'utf8');
  let arr = FileContents.toString().split(/\r?\n/);
  arr = arr.filter((line) => line !== '');
  arr.shift();
  console.log(`Number of students: ${arr.length}`);
  const locateCS = arr.filter((line) => line.endsWith('CS')).map((line) => {
    const CSpeeps = line.split(',');
    return CSpeeps[0];
  });
  console.log(`Number of students in CS: ${locateCS.length}. List: ${locateCS.join(', ')}`);
  const locateSWE = arr.filter((line) => line.endsWith('SWE')).map((line) => {
    const SWEpeeps = line.split(',');
    return SWEpeeps[0];
  });
  console.log(`Number of students in SWE: ${locateSWE.length}. List: ${locateSWE.join(', ')}`);
};
module.exports = countStudents;
