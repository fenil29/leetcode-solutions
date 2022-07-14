/**
 * @param {string[]} strs
 * @return {string[][]}
 */
 var groupAnagrams = function(strs) {
    let ans=[]
    let indexes={}
     for(let i in strs){
        str=strs[i].split('').sort().join('')
        if(str in indexes){
            ans[indexes[str]].push(strs[i])
        }
        else{
            ans.push([strs[i]])
            indexes[str]=ans.length-1
        }
    }
    return ans    
}
