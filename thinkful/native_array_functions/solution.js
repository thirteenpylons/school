/*

Advanced functions: Map, filter, find
Instructions

To complete this practice problem, you will need to get all the tests to pass. 
To do so, complete the following:

Complete each function as described below.
Use the suggested native array methods in each function, as described.
This practice problem shouldn't take you longer than about 25 minutes. 
If you spend longer than that, reach out for help!

Dataset

Assume for all of the following problems that parks refers to a dataset that 
looks similar to the following.

const parks = [
  {
    name: "Canyonlands",
    areaInSquareKm: 1366.2,
    location: { state: "Utah" },
  },
  {
    name: "Crater Lake",
    areaInSquareKm: 741.5,
    location: { state: "Oregon" },
  },
  {
    name: "Zion",
    areaInSquareKm: 595.9,
    location: { state: "Utah" },
  },
];
findParkByName()

Use the find() method to return the object of the park with the matching name. 
Otherwise, the function should return null.

findParkByName(parks, "Zion"); //> { name: "Zion", ... }
getBigParkNames()

Use the filter() and the map() method to return the names of all parks with a 
size greater than or equal to the given size.

getBigParkNames(parks, 700); //> [ "Canyonlands", "Crater Lake" ]
Tips

You may complete this challenge on your own machine before uploading it to Qualified.
Reference the related lesson for help on completing this practice problem.
*/

/*
  Complete the functions below as detailed in the instructions.

  When one of the function parameters refers to a `park`, 
  assume it is an object of the following shape:
  {
    name: "Acadia",
    areaInSquareKm: 198.6,
    location: {
      state: "Maine"
    }
  }
*/

function findParkByName(parks, name) {
    const foundPark = parks.find(park => park.name === name);
    return foundPark || null;
}

function getBigParkNames(parks, minSize) {
    return parks.filter(park => park.areaInSquareKm >= minSize).map(park => park.name);
}

module.exports = {
  findParkByName,
  getBigParkNames,
};
