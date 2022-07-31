/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function (s) {
  let collection = []
  for (let i of s) {
    if (i == '(' || i == '{' || i == '[') {
      collection.push(i)
    } else {
      if (
        (i == ')' && collection[collection.length - 1] == '(') ||
        (i == '}' && collection[collection.length - 1] == '{') ||
        (i == ']' && collection[collection.length - 1] == '[')
      ) {
        collection.pop()
      } else {
        return false
      }
    }
  }
  return collection.length == 0 ? true : false
}
