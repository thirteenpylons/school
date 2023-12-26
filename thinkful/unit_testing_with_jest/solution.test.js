const findLowestScoringStudent = require('../src/solution');

describe('findLowestScoringStudent', () => {
  test('returns the student with the lowest score', () => {
    const students = [
      { name: "Leo Yeon-Joo", score: 8.9 },
      { name: "Morgan Sutton", score: 7.4 },
      { name: "Natalee Vargas", score: 9.2 },
    ];
    expect(findLowestScoringStudent(students)).toEqual({ name: "Morgan Sutton", score: 7.4 });
  });

  test('returns null for an empty list', () => {
    expect(findLowestScoringStudent([])).toBeNull();
  });
});
