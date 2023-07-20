let arr = [4, 5, 10, 24, 3, 9]
let target = 8;

let ans = new map([]);
let um = new map([]);

let n = arr.length ;

function returnAns() {
    for(let i = 0; i< n; i++){    
    if( um[target -arr[i]]) {
    ans.first(um[target-arr[i]])
    ans.second(i)
    return ans	
    }
    else{
    um[arr[i]] =i;
        }
    }

  return [-1,-1]

}

console.log(returnAns())
