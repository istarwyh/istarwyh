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
a solution for find  all of the subsets of an array:

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
    // 这里头结点是存值的结点
    public ListNode reverseList(ListNode head) {
        if( head == null )
            return head;
// 对于链表类问题,多设指针可以来保存状态,以便更新
        ListNode pre = null;
        ListNode cur = head;
        // 当前的指针需要判断其是否为空,才进行下一步
        while(cur != null){
            ListNode nextNode = cur.next;
            // 反转
            cur.next = pre;
            // 更新,即是直接挪动指针而不是改变指向
            pre = cur;
            // 保存的下一个结点的状态派上用场
            cur = nextNode;

        }
        // 最后cur一定是空,所以指向头结点的是pre
        return pre;
    }
}
```

<p align="center"> 
  Visitor count<br>
  <img src="https://profile-counter.glitch.me/istarwyh/count.svg" />
</p>
