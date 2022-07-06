/**
 * @param {character[][]} grid
 * @return {number}
 */
 var numIslands = function(grid) {
    // Write your code here.
  let isVisited=[]
  let noCols=grid[0].length
  let noRows=grid.length
  let ans=[]
  // isVisited=Array(noRows).fill(Array(noCols).fill(false))
  isVisited=new Array(noRows).fill(0).map(() => new Array(noCols).fill(0));

  for(let i=0;i<noRows;i++){
      for(let j=0;j<noCols;j++){
          if(grid[i][j]==1 && isVisited[i][j]!=true){
              // return visit(matrix,isVisited,i,j,noCols,noRows)
              ans.push(visit(grid,isVisited,i,j,noCols,noRows))
          }
      }
  }
  return ans.length
};


function visit(matrix,isVisited,x,y,noCols,noRows){
  let queue=[]
  let lengthOfRiver=0
  queue.push([x,y])
      isVisited[x][y]=true
  while(queue.length>0){
  
      let [i,j]=queue.shift()
  
      lengthOfRiver++
  // console.log(i,j)
      // console.log(isVisited)
      if((i-1)>=0 && matrix[i-1][j]==1  && isVisited[i-1][j]!=true){
              isVisited[i-1][j]=true
          queue.push([i-1,j])
      }
          if((j-1)>=0 && matrix[i][j-1]==1  && isVisited[i][j-1]!=true){
                  isVisited[i][j-1]=true
          queue.push([i,j-1])
      }
          if((i+1)<noRows && matrix[i+1][j]==1  && isVisited[i+1][j]!=true){
                  isVisited[i+1][j]=true
          queue.push([i+1,j])
      }
          if((j+1)<noCols && matrix[i][j+1]==1  && isVisited[i][j+1]!=true){
                  isVisited[i][j+1]=true
          queue.push([i,j+1])
      }
  }
  return lengthOfRiver
}

