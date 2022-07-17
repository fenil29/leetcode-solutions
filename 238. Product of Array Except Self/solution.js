/**
 * @param {number[]} nums
 * @return {number[]}
 */

var productExceptSelf = function (nums) {
  let ans = [1]
  let totalProduct = 1
  for (let i = 0; i < nums.length - 1; i++) {
    totalProduct = totalProduct * nums[i]
    ans[i + 1] = totalProduct
  }
  totalProduct = 1
  for (let i = nums.length - 1; i > 0; i--) {
    totalProduct = totalProduct * nums[i]
    ans[i - 1] = ans[i - 1] * totalProduct
  }
  return ans
}
