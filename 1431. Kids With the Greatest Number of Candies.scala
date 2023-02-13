// 找到array中最大值，减去extraCandies获得阈值，所有阈值以上的元素对应Boolean array中元素为true，阈值以下为false
object Solution {
  def kidsWithCandies(candies: Array[Int], extraCandies: Int): List[Boolean] = {
    // map: https://www.geeksforgeeks.org/scala-map-method/
    candies.map(_ + extraCandies >= candies.max).toList
  }
}