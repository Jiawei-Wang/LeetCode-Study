object Solution {
  def findRestaurant(list1: Array[String], list2: Array[String]): Array[String] = {
    val targetMap: Map[String, Int] = list1.zipWithIndex.toMap // turn list1 into key: string, value: index
    var ansMap: Map[Int, Array[String]] = Map.empty[Int, Array[String]] // empty hashmap 
    for (secondIndex <- 0 until list2.length) {
      val firstIndex: Int = targetMap.getOrElse(list2(secondIndex), -1)
      if (firstIndex != -1) {
        val combine = firstIndex + secondIndex
        ansMap.get(combine) match {
          case Some(array) => ansMap = ansMap.updated(combine, array :+ list2(secondIndex))
          case None => ansMap = ansMap.updated(combine, Array(list2(secondIndex)))
        }
      }
    }
    ansMap(ansMap.keys.min)
  }
}