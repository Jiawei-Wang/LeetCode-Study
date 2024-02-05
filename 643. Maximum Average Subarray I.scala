object Solution {
  def findMaxAverage(nums: Array[Int], k: Int): Double = {
    var globalMax = nums.take(k).sum // start with first k element 
    var currentTotal = globalMax
    for (index <- k until nums.length) {
      currentTotal += nums(index) - nums(index-k)
      globalMax = math.max(globalMax, currentTotal)
    }  
    globalMax.toDouble/k
  }
}