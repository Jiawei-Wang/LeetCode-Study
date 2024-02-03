object Solution {
  def findIndices(nums: Array[Int], indexDifference: Int, valueDifference: Int): Array[Int] = {
    for (i <- 0 until nums.length) {
      for (j <- i + indexDifference until nums.length) {
        if (math.abs(nums(i) - nums(j)) >= valueDifference) {
          return Array(i, j)
        }
      }
    }
    Array(-1, -1) // No such indices found
  }
}

object Solution {
  def findIndices(nums: Array[Int], indexDifference: Int, valueDifference: Int): Array[Int] = {
    val result = (0 until nums.length).flatMap { i =>
      val validIndices = (i + indexDifference until nums.length).filter { j => 
        math.abs(nums(i) - nums(j)) >= valueDifference
      }
      validIndices.headOption.map(j => Array(i, j))
    }
    result.headOption.getOrElse(Array(-1, -1))
  }
}