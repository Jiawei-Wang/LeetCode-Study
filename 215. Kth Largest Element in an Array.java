// 解法1：library
class Solution {
    public int findKthLargest(int[] nums, int k) {
        // sort the array
        Arrays.sort(nums);

        // return the k-th largest
        return nums[nums.length - k];
    }
}


// priority queue
class Solution {
    public int findKthLargest(int[] nums, int k) {
        // PQ: https://www.geeksforgeeks.org/priority-queue-class-in-java-2/
        PriorityQueue<Integer> pq = new PriorityQueue<>();

        for(int val : nums) {
            pq.offer(val);
            if(pq.size() > k) {
                pq.poll();
            }
        }
        return pq.peek();
    }
}


// solution3: TODO


// solution4: TODO
