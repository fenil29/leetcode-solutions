/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
 var twoSum = function(nums, target) {
    let seen={}
    for(let i=0;i<nums.length;i++){
        if(seen[target-nums[i]]!=undefined) return [i,seen[target-nums[i]]]
        else seen[nums[i]]=i
    }
};