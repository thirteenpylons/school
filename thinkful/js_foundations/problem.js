/*

  When any of the following function's parameters reference `products`, they are referencing an array full of objects with the following shape:
   {
     name: "Court Sneaker",
     priceInCents: 8800,
     availableSizes: [ 0, 2, 4, 6, 10, 12, 16 ]
   }
   
  When any of the following function's parameters reference `product`, they are referencing an object with the above shape.
*/

function printablePrice(priceInCents) {
    const amount = (priceInCents / 100).toFixed(2);
    return `$${amount}`;
  }
  
  function chooseItemByNameAndSize(products, name, size) {
    let selected = null;
    // write your solution here. See the hint in the instructions if you need help.
    
    return selected;
  }
  
  
  function calculateTotal(cart) {
    let result = 0;
    // write your solution here. See the hint in the instructions if you need help.
    
    return result;
  }
  
  function printReceipt(cart) {
    const total = calculateTotal(cart);
    // write your solution here. See the hint in the instructions if you need help.
  
    return result + `Total: ${printablePrice(total)}`;
  }
  
  module.exports = {
    chooseItemByNameAndSize,
    calculateTotal,
    printReceipt,
  };
  