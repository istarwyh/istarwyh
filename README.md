### Hi! Nice to meet you! 👋

<!--
**istarwyh/istarwyh** is a ✨ _special_ ✨ repository because its `README.md` (this file) appears on your GitHub profile.

Here are some ideas to get you started:

- 🔭 I’m currently working on ...
- 🌱 I’m currently learning ...
- 👯 I’m looking to collaborate on ...
- 🤔 I’m looking for help with ...
- 💬 Ask me about ...
- 📫 How to reach me: ...
- 😄 Pronouns: ...
- ⚡ Fun fact: ...
-->



## About Me


[![Top Langs](https://github-readme-stats.vercel.app/api/top-langs/?username=istarwyh&hide=css&layout=compact)](https://github.com/anuraghazra/github-readme-stats)[![wangyihui's github stats](https://github-readme-stats.vercel.app/api?username=istarwyh "![wangyihui's github stats")](https://github.com/istarwyh)

If you want to know more about me, welcome to see [my online resume](https://istarwyh.github.io/)! Thank you!😄

## Resent Practice
2. Add Two Numbers[.](https://leetcode-cn.com/problems/add-two-numbers/)


```java
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
//  当使用链表表示数字
//         数字可能有前置0吗？
//         数字是负数，符号位应该怎么办？
// 这种在天文数字中可能会出现，无论是因子还是结果，最后都只能用链表存储
    // 因此应直接考虑对于链表结点本身的相加而不走系统的相加过程
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        if( l1 == null || l2 == null ) return null;
        ListNode head = null;
        ListNode p = null;
        int carry = 0;
        while( l1 != null || l2 != null ){
            int v1 = l1 == null ? 0 : l1.val;
            int v2 = l2 == null ? 0 : l2.val;
            int sum = v1+v2+carry;
            if( head == null ){
                // 余数取末尾
                head = new ListNode(sum % 10);
                p = head;
            }else{
                // 除法取上位
                p.next = new ListNode(sum % 10 );
                p = p.next;
            }
            carry = sum / 10;
            l1 =  l1 == null ? l1 : l1.next;
            l2 =  l2 == null ? l2 : l2.next;
        }
        if( carry > 0 ){
            p.next = new ListNode( carry);
        }
        return head;
    }
}
```

<p align="center"> 
  Visitor count<br>
  <img src="https://profile-counter.glitch.me/istarwyh/count.svg" />
</p>
