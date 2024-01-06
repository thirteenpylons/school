function getRandomNumber() {
    // Math.floor(Math.random() * 100) generates a random number
    const randomNumber = Math.floor(Math.random() * 100);
    const min = 10;
    try {
        if (randomNumber < min) {
            throw `Random number is too small! ${randomNumber} is less than ${min}!`;
        } else {
            console.log(`The random number is: ${randomNumber}.`);
        }
    } catch (error) {
        console.log(`An error occurred: ${error}`);
    }
}


/*
Error-handling basics: Try and catch
Instructions

To complete this practice problem, follow the instructions below.

getCarColor()

Write a function called getCarColor that takes in a car object like in the 
example below. It should return car's color. Use try and catch so that if 
accessing the color raises an error, the function returns "Color unknown".

The function must use the try and catch syntax.
For a valid car, it should return the car's color.
If accessing the color fails, the function should catch the 
error and return "Color unknown".
let car = { make: "Honda", model: "Civic", color: "Slate Grey" };
getCarColor(car); // "Slate Grey"
getCarColor(undefined); // "Color unknown"
Tips

You may complete this challenge on your own machine before uploading it to Qualified.
Reference the related lesson for help on completing this practice problem.
*/
function getCarColor(car) {
    try {
        return car.color;
    } catch (error) {
        return "Color unknown";
    }
}

//do not remove
module.exports = getCarColor;
