/**
 * @param {string[]} strs
 * @return {string[][]}
 */
 var groupAnagrams = function(strs) {
    let ans=[]
    let indexes={}
     for(let i in strs){
        str=sortString(strs[i])
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

var sortString = function(str){
    let charCount=[]
    for(let i in str){
        // console.log(str.charCodeAt(i))
        if(charCount[str.charCodeAt(i)]==undefined){
            charCount[str.charCodeAt(i)]=1
        }
        else{
            charCount[str.charCodeAt(i)]=charCount[str.charCodeAt(i)]+1
        }
    }
    let sortedStr=""
    for(let i in charCount){
        if(i!==undefined){
            sortedStr=sortedStr+String.fromCharCode(i).repeat(charCount[i])            
        }
    }
    return sortedStr
}
