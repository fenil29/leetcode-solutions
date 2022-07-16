/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
 var topKFrequent = function (nums, k) {
    let numFrequencyCount = {}
    for (let x of nums) {
      if (x in numFrequencyCount) {
        numFrequencyCount[x] = numFrequencyCount[x] + 1
      } else {
        numFrequencyCount[x] = 1
      }
    }
    let listOfFrequencyCount = Object.keys(numFrequencyCount).map((key) => {
      return [key, numFrequencyCount[key]]
    })
    listOfFrequencyCount = listOfFrequencyCount.sort((x, y) => {
      return y[1] - x[1]
    })
    let ans = []
    for (let i = 0; i < k; i++) {
      ans.push(listOfFrequencyCount[i][0])
    }
    return ans
  }
  