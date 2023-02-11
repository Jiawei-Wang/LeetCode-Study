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


// 解法2：逐层除3，直到不能继续为止
object Solution {
  import scala.annotation.tailrec
  @tailrec
	def isPowerOfThree(n: Int): Boolean = {
		n match {
      // 一个int分为以下几种情况
      case 0 => false
		  case 1 => true
		  case _ if n % 3 == 0 => isPowerOfThree(n / 3)
		  case _ => false // 不能整除3的数字，或者负数，均不符合条件
    }
  }
}


// 解法3
object Solution {
  def isPowerOfThree(n: Int): Boolean = {
    Integer.toString(n, 3).matches("^10*$")

    // Integer.toString(a, b)：将a以b进制展示
    // Integer.toString(3, 2) = "11"
    // 最后使用Regex来进行检查
  }
}