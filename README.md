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
160. Intersection of Two Linked Lists[.](https://leetcode-cn.com/problems/intersection-of-two-linked-lists/)


```java
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
 // 对于相交的问题，结成环就可以使用快慢指针了-->但是快指针指向慢指针的时候一定是交点吗？你是无法证明的
    // 无法证明的东西即使对了也还是不要尝试了
public class Solution {
     public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
         if( headA == null || headB ==null ) return null;

        ListNode l1 = headA;
        ListNode l2 = headB; 
        while( l1 != l2){
            l1 = l1!=null ? l1.next : headB;
            l2 = l2!=null ? l2.next : headA;
        }
    
        return l1;
    }
}}
}
```

<p align="center"> 
  Visitor count<br>
  <img src="https://profile-counter.glitch.me/istarwyh/count.svg" />
</p>
