// 题意：将4个数字两两组合（任何case均有效），然后将组合成的2个两位数相加，求全局最小值
object Solution {
  def minimumSum(num: Int): Int = { // num.toString.map(_ - '0')：将一个四位数变成一个包含4个int的list object（'3' - '0' = 3）
    num.toString.map(_ - '0').sorted.toList match {
      case List(i1, i2, i3, i4) => (i1 + i2) * 10 + i3 + i4
      case _ => ??? // will result in a compile-time error indicating that an implementation is missing
    }
  }
}