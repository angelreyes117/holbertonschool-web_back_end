import fs from 'fs/promises';

/**
 * readDatabase(filePath)
 * - reads a CSV database file asynchronously
 * - returns a Promise that resolves to an object where keys are fields
 *   and values are arrays of firstnames in the order they appear
 * - rejects the promise with the error if file can't be read
 */
export async function readDatabase(filePath) {
  try {
    const content = await fs.readFile(filePath, 'utf8');
    const lines = content.split('\n').filter(Boolean);
    if (lines.length === 0) return {};

    const headers = lines[0].split(',');
    const idxFirstname = headers.indexOf('firstname');
    const idxField = headers.indexOf('field');

    if (idxFirstname === -1 || idxField === -1) {
      // If headers are unexpected, return empty object
      return {};
    }

    const result = {};

    for (let i = 1; i < lines.length; i++) {
      const line = lines[i].trim();
      if (!line) continue;
      const parts = line.split(',');
      const firstname = parts[idxFirstname] ? parts[idxFirstname].trim() : '';
      const field = parts[idxField] ? parts[idxField].trim() : '';

      if (!firstname || !field) continue;

      if (!result[field]) result[field] = [];
      result[field].push(firstname);
    }

    return result;
  } catch (err) {
    // propagate the error so callers can reject accordingly
    throw err;
  }
}
export default { readDatabase };
