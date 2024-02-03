object Solution {
  def findPeaks(mountain: Array[Int]): List[Int] = {
    mountain
      .zip(mountain.indices) // each element of mountain is paired with its index in the resulting tuples
      .sliding(3) // a sliding window of size 3 over the zipped array. Each window will contain three consecutive elements from the zipped array.
      .collect {
        case Array((prev, prevIndex), (curr, currIndex), (next, nextIndex))
          if curr > prev && curr > next => currIndex
      }
      .toList
  }
}