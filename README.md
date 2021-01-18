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
[143. Reorder List](https://leetcode-cn.com/problems/reorder-list/)


```java
 public void reorderList(ListNode head) {
        if (head == null || head.next == null)
            return;
        ListNode endNode1 = getSplitNode(head);
        ListNode startNode2 = endNode1.next;
        ListNode l1 = getFirstPart(head,endNode1);
        ListNode l2 = reverseListAsSecondPart(startNode2);
        merge(l1, l2);
    }
    private ListNode getSplitNode(ListNode head){
        ListNode prev = null, slow = head, fast = head;
        while (fast != null && fast.next != null) {
            prev = slow;
            slow = slow.next;
            fast = fast.next.next;
        }
        return prev;
    }

    /**
     * 切割得到第一部分链表
     * @param head 链表原始头结点
     * @param endNode 切割后第一部分链表尾结点
     * @return
     */
    private ListNode getFirstPart(ListNode head, ListNode endNode) {
//        注释上写why
//        保证第一部分与第二部分切断联系
        endNode.next = null;
        return head;
    }

    private ListNode reverseListAsSecondPart(ListNode head) {
        if (head == null)
            return null;
        ListNode prev = null;
        ListNode curr = head;
        ListNode nextTemp = null;
        while (curr != null) {
            nextTemp = curr.next;
            curr.next = prev;

            prev = curr;
            curr = nextTemp;
        }
        return prev;
    }

    /**
     *
     * @param l1 head所在的链表，同时也是切割后第一部分链表
     * @param l2 切割后第二部分链表
     */
    private void merge(ListNode l1, ListNode l2) {
        while (l1 != null) {
            ListNode n1 = l1.next, n2 = l2.next;
            l1.next = l2;
            if (n1 == null) {
                break;
            }
            l2.next = n1;
            l1 = n1;
            l2 = n2;
        }
    }
```

<p align="center"> 
  Visitor count<br>
  <img src="https://profile-counter.glitch.me/istarwyh/count.svg" />
</p>
