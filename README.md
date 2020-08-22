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
 /**
 *本题拆解为三步,一是范围内反转,二是连接尾部,三是找准并连接头部
 *本题启示:因为链表的不可直接访问性,可以通过设立多个结点保留位置信息
 */
class Solution {
    public ListNode reverseBetween(ListNode head, int m, int n) {
        if(head == null )
            return head;

        ListNode pre;
        ListNode cur=head;
        if(m==1){
            pre = null;
        }else{
            pre =head;
            //移动m-2次
            for(int i=0;i<m-2;i++){
                pre=pre.next;
            }
        }
        //通过创立结点保留初始pre的位置
        ListNode preStart = pre;
        //移动m-1次
        for(int i=0;i<m-1;i++){
            cur = cur.next;
        }
        //保留初始结点的位置,即在pre的后一个
        ListNode start = cur;

        ListNode end = head;
        //end设定为 反转后在最后一个结点的下一位
        for(int i=0;i<n;i++){
            end = end.next;
        }
        while(cur != end){
            //nextNode是工具人, 看它的生命周期也就知道了
            ListNode nextNode = cur.next;
            cur.next = pre;
            pre = cur;
            cur = nextNode;
        }
        
        start.next = end;

        // preStart为空说明head一定也反向了,那么新的头结点反转到了移动后的pre
        if(preStart == null){
            return pre;
        }else{
            //如果头结点没有反向,那么头结点还是头结点
            preStart.next = pre;
            return head;
        }

    }
}

```

<p align="center"> 
  Visitor count<br>
  <img src="https://profile-counter.glitch.me/istarwyh/count.svg" />
</p>
