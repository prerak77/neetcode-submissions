class Solution {
    /**
     * @param {string[]} strs
     * @returns {string}
     */
    
    encode(strs) {

        let final_str = "";

        for(let i=0; i<strs.length;i++){
            let str_length = strs[i].length;
            let str_add = str_length+ "#"+ strs[i];
            final_str += str_add;
        }
        return final_str;
    }

    /**
     * @param {string} str
     * @returns {string[]}
     */
    decode(str) {

        function isNumber(str) {
            return !isNaN(str) && str.trim() !== "";
        }

        let final_arr = [];
        for(let i =0;i<str.length;i++){
            if(isNumber(str[i])){
                let len_str = "";
                while(str[i] != "#"){
                    len_str +=str[i];
                    i++;
                }
                console.log(len_str);
                let str_inner = "";
                //move 1 ahead to skip the #
                i++;
                for(let j = 0;j < len_str;j++){
                    str_inner += str[i];
                    i++;
                }
                i--;
                final_arr.push(str_inner);
            }
        }
        return final_arr;

    }
}
