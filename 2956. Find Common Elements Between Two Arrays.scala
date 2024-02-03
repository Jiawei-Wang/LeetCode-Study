object Solution {
    def findIntersectionValues(nums1: Array[Int], nums2: Array[Int]): Array[Int] = {
        val set1 = nums1.toSet
        val set2 = nums2.toSet
        val counter1 = nums1.count(set2.contains)
        val counter2 = nums2.count(set1.contains)
        Array(counter1, counter2)
    }
}