class Solution {
    /**
     * @param {number[]} nums
     * @return {number[]}
     */
    productExceptSelf(nums) {
        //first find the prefix,i.e. multiply  
        //numbers to the left of current index

        let arr = [1];
        for(let i =1;i <nums.length;i++){
            arr.push(nums[i-1] * arr[i-1]);
        }
        console.log(arr);
        //next find the sufix, i.e. multiply  
        //numbers from the right of current index
        let sufix_product = 1;
        for(let i = nums.length -2;i >=0;i--){
          sufix_product *= nums[i+1];
          arr[i] *=sufix_product;
        }

        return arr;


    }
}
