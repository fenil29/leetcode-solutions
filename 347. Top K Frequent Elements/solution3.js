/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
var topKFrequent = function (nums, k) {
  let frequencyCountByIndex = [...Array(nums.length + 1)].map((x) => [])
  let numFrequencyCount = {}
  let ans = []
  for (let x of nums) {
    if (x in numFrequencyCount) {
      numFrequencyCount[x] = numFrequencyCount[x] + 1
    } else {
      numFrequencyCount[x] = 1
    }
  }
  for (let [x, y] of Object.entries(numFrequencyCount)) {
    frequencyCountByIndex[y].push(x)
  }
  let count = 0
  for (let i = frequencyCountByIndex.length - 1; i >= 0; i--) {
    for (let y of frequencyCountByIndex[i]) {
      ans.push(y)
      count++
      if (count == k) {
        return ans
      }
    }
  }
}
