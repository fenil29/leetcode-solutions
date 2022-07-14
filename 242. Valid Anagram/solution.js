/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isAnagram = function (s, t) {
  let charCount = {}
  for (let char of s) {
    // console.log(char)
    if (char in charCount) charCount[char] = charCount[char] + 1
    else charCount[char] = 1
  }
  for (let char of t) {
    // console.log(char)
    if (char in charCount) {
      if (charCount[char] == 1) {
        delete charCount[char]
      } else {
        charCount[char] = charCount[char] - 1
      }
    } else {
      return false
    }
  }
  // console.log(Object.keys(charCount).length)
  return Object.keys(charCount).length == 0
}
