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
    for (let product of products) {
      if (product.name === name && product.availableSizes.includes(size)) {
        selected = product;
        break;
      }
    }
    return selected;
  }
  
  function calculateTotal(cart) {
    let result = 0;
    for (let name in cart) {
      const item = cart[name];
      result += item.quantity * item.priceInCents;
    }
    return result;
  }
  
  function printReceipt(cart) {
    const total = calculateTotal(cart);
    if (!total) return null;
  
    let result = "";
    for (let name in cart) {
      const { quantity, priceInCents } = cart[name];
      const amount = printablePrice(quantity * priceInCents);
      result += `${quantity}x${name} - ${amount}\n`;
    }
  
    return result + `Total: ${printablePrice(total)}`;
  }
  
  module.exports = {
    chooseItemByNameAndSize,
    calculateTotal,
    printReceipt,
  };
  