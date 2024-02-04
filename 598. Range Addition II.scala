object Solution {
  def maxCount(m: Int, n: Int, ops: Array[Array[Int]]): Int = {
    if (!ops.isEmpty) {
      ops.map(_(0)).min * ops.map(_(1)).min // ops.map(_(0)) is ops.map(arr => arr(0))
    } else {
      m*n
    }
  }
}