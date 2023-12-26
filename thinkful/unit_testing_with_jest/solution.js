/*

Testing: Unit testing with Jest
Instructions

To complete this practice problem, you will need to build a function and write 
tests for that function. You should not spend more than 30 minutes on this exercise. 
Reach out for help if you need it!

If you're working on the challenge on your local machine, make sure to run npm 
install to install the development dependencies. You can run npm test to run the tests.

findLowestScoringStudent()

Complete the function findLowestScoringStudent() in the src/main.js file so that, 
when given a list of students, it returns the student with the lowest score. 
If there are multiple students with the same lowest score, return any one of them. 
If the given list of students is empty, return null.

const students = [
  { name: "Leo Yeon-Joo", score: 8.9 },
  { name: "Morgan Sutton", score: 7.4 },
  { name: "Natalee Vargas", score: 9.2 },
];

findLowestScoringStudent(students); //> { name: "Morgan Sutton", score: 7.4 }
Tests

As you are building the function, write tests for your code in test/solution.test.js. 
You will want to cover at least the following cases.

A non-empty student list is given (that is, an object is returned). 
Use the toEqual syntax for this test.
An empty student list is given (that is, null is returned). 
Use the toBe syntax for this test.
Note: Remember that Qualified will show that the tests that you wrote are passing 
but our submission tests will be different than your tests. 
Make sure that you meet the requirements above so that the submission tests pass.

Tips

You may complete this challenge on your own machine before uploading it to Qualified.
Reference the related lesson for help on completing this practice problem.
*/

function findLowestScoringStudent(students) {
    if (students.length === 0) {
      return null;
    }
  
    let lowestScoringStudent = students[0];
  
    for (let student of students) {
      if (student.score < lowestScoringStudent.score) {
        lowestScoringStudent = student;
      }
    }
  
    return lowestScoringStudent;
}
  
module.exports = findLowestScoringStudent;
