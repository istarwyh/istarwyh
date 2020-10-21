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
86. Partition List[.](https://leetcode-cn.com/problems/partition-list/)


```java
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
        // 这该怎么从后往前遍历呢？所以不能采用原本的快排式循环交换解法了
        // 链表的缺点在于不好遍历，优点却在于可以一次迭代即可---因为结点可以拆开
    public ListNode partition(ListNode head, int x) {
        if( head == null ) return null;
        // 多使用额外的结点保存状态，这里保存最开始的
        ListNode before_head = new ListNode(0);
        ListNode before = before_head;
        ListNode after_head = new ListNode(0);
        ListNode after = after_head;
        while( head != null ){
            // 必须把等于的情况也放在第二段链表中！因为相等的情况是轴值应处于中间
            if( head.val >= x ){
                after.next = head;
                after = after.next;
            }else{
                before.next = head;
                before = before.next;
            }
            head = head.next;
        }
        after.next = null;

        before.next = after_head.next;
        return before_head.next;
    }
} 
```

<p align="center"> 
  Visitor count<br>
  <img src="https://profile-counter.glitch.me/istarwyh/count.svg" />
</p>
