/*

Array sort exercises
Now, practice using sort to sort arrays.

Each of these exercises asks you to return the sorted array.

Sort list of words

Write a method, sortWords, that takes in an array of strings and 
returns an array with those strings sorted alphabetically.

Sort numbers

Write a method, sortNumbers, that takes in an array of numbers and returns 
the numbers sorted least to greatest.

Example:

sortNumbers([56, -2, 3, 102]) //=> [-2, 3, 56, 102]
Sort numbers, backwards

Write a method, largestFirst, that takes in an array of numbers and 
returns the numbers sorted greatest to least (the opposite of the previous function).

Example:

sortNumbers([56, -2, 3, 102]) //=> [102,56,3,-2]
Sort objects by a property

Write a function, sortFlowersByZone, that takes in an array of flower 
objects and sorts them by their hardinessZone.

Example:

let flowers = [
  {
    name: "Pink Coneflower",
    zone: 6
  },
  {
    name: "Scarlet Phlox",
    zone: 2
  },
  {
    name: "Carnations",
    zone: 4
  },
  {
    name: "Hyacinths",
    zone: 3
  },
  {
    name: "Hydrangeas",
    zone: 5
  }
]
sortFlowersByZone(flowers) /*=> [
  {
    name: "Scarlet Phlox",
    zone: 2
  },
  {
    name: "Hyacinths",
    zone: 3
  },
  {
    name: "Carnations",
    zone: 4
  },
  {
    name: "Hydrangeas",
    zone: 5
  },
  {
    name: "Pink Coneflower",
    zone: 6
  },
]
*/
/*
Sort strings by length

Write a function, sortByLength, that takes in an array of strings and 
returns the strings sorted by length, with the shortest first.

Example:

sortByLength(["Scarlet Phlox", "Hyacinths", "Carnations", "Hydrangeas", "Pink Coneflower"]) 
/* => [
  'Hyacinths',
  'Carnations',
  'Hydrangeas',
  'Scarlet Phlox',
  'Pink Coneflower'
]
*/

function sortWords(words) {

}

function sortNumbers(numbers) {

}

function largestFirst(numbers) {

}

function sortFlowersByZone(flowers) {

}

function sortByLength(strings) {

}

module.exports = {
  sortWords,
  sortNumbers,
  largestFirst,
  sortFlowersByZone,
  sortByLength,
};