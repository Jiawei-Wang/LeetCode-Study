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
