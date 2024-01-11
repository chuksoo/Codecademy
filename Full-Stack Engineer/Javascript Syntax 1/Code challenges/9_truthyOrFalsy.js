// It can be hard to keep track of what’s truthy or falsy in JavaScript. Write a function, truthyOrFalsy(), that takes in any value and returns true if that value is truthy and false if that value is falsy.
const truthyOrFalsy = (value) => {
  if (value) {
    return true;
  }
  return false;
};

/*
// As a function declaration:
function truthyOrFalsy(value) {
    if (value) {
        return true
    } else {
        return false
    }
}

// Using a ternary: 
const truthyOrFalsy = value => value ? true : false 
*/
