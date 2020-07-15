// solution 1: 暴力解，两层循环
// Time: n^2
var numIdenticalPairs = function(nums) {
    // ans变量记录总数
    // 如何声明新的变量: https://www.w3schools.com/js/js_variables.asp
    var ans = 0;

    // n变量记录nums长度
    // 如何获得array的长度: https://www.w3schools.com/jsref/jsref_length_array.asp
    var n = nums.length;

    // 两层循环
    for (var i = 0; i < n-1; i++) {
        for (var j = i+1; j < n; j++) {
            if (nums[i] == nums[j]) {
                ans ++;
            }
        }
    }

    // 返回ans
    return ans;
};


// solution2: hashmap，遍历数组，在每个位置上时寻找已经出现同值的次数
// Time: n
var numIdenticalPairs = function(nums) {
    // 创建一个hashmap: https://pietschsoft.com/post/2015/09/05/javascript-basics-how-to-create-a-dictionary-with-keyvalue-pairs
    var dict = {};

    // 使用count计数
    var count = 0;

    // 遍历nums
    // for of and for in: https://www.typescriptlang.org/docs/handbook/iterators-and-generators.html
    for (var num of nums) {
        // 检查value是否存在
        if (dict[num]) {
            count += dict[num];
            dict[num] += 1;
        } else {
            dict[num] = 1;
        }
    }

    // 返回count
    return count
};
