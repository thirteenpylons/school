/*
Error-handling basics: Writing errors
Instructions

To complete this practice problem, you will do the following:

Update the code so that instead of calling console.error() for each error, 
it pushes the errors into the errors array.
Update the code so that if there are any errors, the code throws the array of errors.
Tips

You may complete this challenge on your own machine before uploading it to Qualified.
Reference the related lesson for help on completing this practice problem.
*/

function secretPasscode(code) {
    let errors = [];
    if (code.length < 14) {
        errors.push("Code is too short!");
    }
    if (code.length > 14) {
        errors.push("Code is too long!");
    }
    if (!code.includes("-")) {
        errors.push("Code is missing a '-'.");
    }
    if (code !== "jWhyYFh-eTx3qt") {
        errors.push("Code is incorrect.");
    }
  
    if (errors.length) {
      throw errors;
    }
    return true;
  }
  
  module.exports = secretPasscode;
  