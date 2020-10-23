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
445. Add Two Numbers II[.](https://leetcode-cn.com/problems/add-two-numbers-ii/)


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
    // 如果不是转化为正常的int数相加,(然后又不采用位运算？),就只有采用从尾数进制的办法
        // 那么就需要借助辅助的数据结构，如栈
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        if( l1 == null || l2 == null ) return null;
        ArrayDeque<Integer> stack1 = new ArrayDeque<>();
        while( l1!= null ){
            stack1.push( l1.val );
            l1= l1.next;
        }
        ArrayDeque<Integer> stack2 = new ArrayDeque<>();
        while(l2 != null ){
            stack2.push( l2.val );
            l2 = l2.next;
        }

        int carry =0;
        int v1=0;
        int v2=0;
        ArrayDeque<Integer> resStack = new ArrayDeque<>();
        while( stack2.size() > 0 || stack1.size() > 0 ){
            if( stack1.size() > 0){
                v1 = stack1.pop();
            }
            if( stack2.size() > 0 ){
                v2 = stack2.pop();
            }
            int sum = v1+v2+carry;
            v1=0;v2=0;
            resStack.push(sum%10);
            carry = sum /10;
        }
        if( carry > 0 ) resStack.push( carry );
        ListNode head = new ListNode(resStack.pop() );
        ListNode p = head;
        while( resStack.size() > 0 ){
            p.next = new ListNode( resStack.pop());
            p = p.next;
        }
        return head;
    }
}
```

<p align="center"> 
  Visitor count<br>
  <img src="https://profile-counter.glitch.me/istarwyh/count.svg" />
</p>
