// object Solution {
//   def findLHS(nums: Array[Int]): Int = {
//     var maxLen = 0
//     val allElement: Set[Int] = nums.toSet
//     allElement.foreach { target => 
//       val countTarget = nums.count(_ == target)
//       val countHigh = nums.count(_ == target + 1)
//       val countLow = nums.count(_ == target - 1)
//       if (countHigh != 0 || countLow != 0) {
//         maxLen = math.max(maxLen, math.max(countLow, countHigh) + countTarget)
//       }
//     }
//     maxLen
//   }
// }


// use hashmap 
object Solution {
  def findLHS(nums: Array[Int]): Int = {
    var maxLen = 0
    // create a map where each distinct element in nums is associated with the count of its occurrences in the array.
    val numCountMap = nums.groupMapReduce(identity)(_ => 1)(_ + _)
    for ((num, count) <- numCountMap) {
      if (numCountMap.contains(num + 1)) {
        val currLen = count + numCountMap(num + 1)
        maxLen = maxLen.max(currLen)
      }
    }
    maxLen
  }
}

// TODO: learn the syntax for val numCountMap = nums.groupMapReduce(identity)(_ => 1)(_ + _)