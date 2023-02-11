// 从0开始学scala：用chatgpt学语法，用leetcode练语法

// single line comment
/* multi line comment */

// 解法1：数学
// an object is a singleton instance of a class
object Solution {
  // -2^31 <= n <= 2^31 - 1 so 1162261467 (3^19) is the max 3 ^ x value that is possibly assgin for an integer value
  // if n is a power of 3, then 3^19 % n == 0
  def isPowerOfThree(n: Int): Boolean = {
    if (n <= 0) false 
    else 1162261467 % n == 0
  }
}

