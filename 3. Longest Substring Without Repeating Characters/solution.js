/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function (s) {
  let maxLength = 0
  let start = 0
  let uniqueChar = {}
  for (let i = 0; i < s.length; i++) {
    char = s[i]
    if (char in uniqueChar) {
      start = Math.max(start, uniqueChar[char] + 1)
      uniqueChar[char] = i
    } else {
      uniqueChar[char] = i
    }
    maxLength = Math.max(maxLength, i - start + 1)
  }
  return maxLength
}
