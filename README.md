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
82. Remove Duplicates from Sorted List II[.](https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list-ii/)


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
       public ListNode deleteDuplicates(ListNode head) {
        if( head  == null ) return null;
        ListNode preHead = new ListNode(-1);
        preHead.next = head;
        ListNode curNode = preHead;
        while( curNode.next != null && curNode.next.next != null ){
            if( curNode.next.val == curNode.next.next.val ){
//            定义curNode.next一定是满足条件的那个结点
                ListNode tmpNode = curNode.next;
//            结束循环后,tmpNode要么是尾结点,要么是重复结点的尾结点
                while( tmpNode != null && tmpNode.next != null && tmpNode.val == tmpNode.next.val){
                    tmpNode = tmpNode.next;
                }
//            仅仅跳过当前重复的结点,curNode的指向的依旧是可能重复的结点
                curNode.next = tmpNode.next;
            }else {
//            当确认不是重复结点的时候,当前指针再后移
                curNode = curNode.next;
            }
        }
        ListNode res = preHead.next;
        preHead.next = null;
        return res;
    }

}
```

<p align="center"> 
  Visitor count<br>
  <img src="https://profile-counter.glitch.me/istarwyh/count.svg" />
</p>
