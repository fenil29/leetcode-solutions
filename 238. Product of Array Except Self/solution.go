
func productExceptSelf(nums []int) []int {
	ans := make([]int, len(nums))
	totalProduct := 1
	ans[0] = 1
	for i := 0; i < len(nums)-1; i++ {
		totalProduct = totalProduct * nums[i]
		ans[i+1] = totalProduct
	}
	totalProduct = 1
	for i := len(nums) - 1; i > 0; i-- {
		totalProduct = totalProduct * nums[i]
		ans[i-1] = ans[i-1] * totalProduct
	}
	return ans
}