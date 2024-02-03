object Solution {
  def sumCounts(nums: List[Int]): Int = {
    // get all subarrays
    val subarrays: List[List[Int]] = nums.indices.flatMap { i =>
      nums.indices.drop(i).flatMap { j =>
        List(nums.slice(i, j+1))
      }
    }.toList

    // count distinct values
    val distinctCounts: List[Int] = subarrays.map(_.distinct.size)

    val sumOfSquares: Int = distinctCounts.map(count => count * count).sum
    sumOfSquares
  }
}