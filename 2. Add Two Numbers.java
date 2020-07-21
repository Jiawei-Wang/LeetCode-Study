/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;           // 创建一个指向下一个node的指针：https://www.cs.cmu.edu/~pattis/15-1XX/15-200/lectures/linkedlists/index.html
 *     ListNode() {}            // 默认的constructor：https://stackoverflow.com/questions/18099127/java-entity-why-do-i-need-an-empty-constructor/18099352
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }       // 以上是两个method，将传入的值和指针给当前所在node
 * }
 */

class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode dummyHead = new ListNode(0);   // 创建dummyhead，赋值为0
        ListNode p = l1, q = l2, curr = dummyHead;  // 让p，q，curr分别指向l1，l2，dummyhead
        int carry = 0;  // 用来保存进位
        while (p != null || q != null) {    // 每个linkedlist的最末尾是一个值为null的node
            int x = (p != null) ? p.val : 0;    // 这句话意思是：如果没到末尾，则加上数字，如果已到末尾，则加0（因为另一个linkedlist还没走到头）
            int y = (q != null) ? q.val : 0;
            int sum = carry + x + y;
            carry = sum / 10;
            curr.next = new ListNode(sum % 10);     // 从dummyhead开始，下一个node的值设为l1，l2该位置上node的值之和的个位数字
            curr = curr.next;       // 指针往后移动一位
            if (p != null) p = p.next;
            if (q != null) q = q.next;
        }
        if (carry > 0) {
            curr.next = new ListNode(carry);    // 如果循环结束后carry还有值（也就是说最后一个node获得了大于10的数字），则再加一个node
        }
        return dummyHead.next;      // 从dummyhead的后一位开始
    }
}
