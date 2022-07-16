/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
var topKFrequent = function (nums, k) {
  let indexOfnum = {}
  let frequencyCount = [...Array(nums.length + 1)].map((x) => [])
  let ans = []
  for (let x of nums) {
    if (x in indexOfnum) {
      frequencyCount[indexOfnum[x] + 1].push(x)
      frequencyCount[indexOfnum[x]] = frequencyCount[indexOfnum[x]].filter(
        (num) => num !== x,
      )
      indexOfnum[x] = indexOfnum[x] + 1
    } else {
      frequencyCount[1].push(x)
      indexOfnum[x] = 1
    }
  }
  let count = 0
  for (let i = frequencyCount.length - 1; i > 0; i--) {
    if (frequencyCount[i].length > 0) {
      for (let y of frequencyCount[i]) {
        ans.push(y)
        count++
        if (count == k) {
          return ans
        }
      }
    }
  }
}
