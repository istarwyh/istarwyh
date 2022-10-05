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

If you want to know more about me, welcome to see [my online resume](https://istarwyh.github.io/resume-it)! Thank you!😄

## Recent Practice
[143. Reorder List](https://leetcode-cn.com/problems/reorder-list/)

### Solution:

```java

    public void reorderList(ListNode head) {
        if (head == null || head.next == null)
            return;
        ListNode splitNode = getFirstPartEndNodeAsSplitNode(head);
        ListNode secondPartStartNode = splitNode.next;
        ListNode l1 = getFirstPartHeadNode(head,splitNode);
        ListNode l2 = getSecondPartHeadNode(secondPartStartNode);
        merge(l1, l2);
    }

    /**
     *将要反转的链表看为两部分,返回第一部分尾结点
     */
    public ListNode getFirstPartEndNodeAsSplitNode(ListNode head){
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
     * @return ListNode
     */
    public ListNode getFirstPartHeadNode(ListNode head, ListNode endNode) {
        endNode.next = null;
        return head;
    }

    public ListNode getSecondPartHeadNode(ListNode head) {
        if (head == null)
            return null;
        ListNode prev = null;
        ListNode cur = head;
        while (cur != null) {
            final ListNode next = cur.next;

            pointToPreNode(prev, cur);

            prev = cur;
            cur = next;
        }
        return prev;
    }

    private void pointToPreNode(ListNode prev, ListNode cur) {
        cur.next = prev;
    }

    /**
     * 交替相连接结点,新链表 以 l1 为头结点
     * @param l1 head所在的链表，同时也是切割后第一部分链表
     * @param l2 切割后第二部分链表
     */
    public void merge(ListNode l1, ListNode l2) {
        while (l1 != null && l2 != null) {
            final ListNode l1Next = l1.next, l2Next = l2.next;
            jointInTurn(l1, l2, l1Next,l2Next);

            l1 = l1Next;
            l2 = l2Next;
        }
    }

    private void jointInTurn(ListNode l1, ListNode l2, ListNode l1Next,ListNode l2Next) {
        l1.next = l2;
        // when l1Next is null, we don't need to joint them in turn just pointing to end node -- l2Next
        if(l1Next == null){
            l2.next = l2Next;
        }else {
            l2.next = l1Next;
        }
    }
```
### Test
```java
class LinkedListTest {

    private LinkedList linkedList;
    private ListNode node1;

    private ListNode oddNodeListHead;
    private ListNode evenNodeListHead;

    @BeforeEach
    void setUp() {
        linkedList = new LinkedList();
        node1 = new ListNode(1);
        oddNodeListHead = ListNode.createNodeList(1, 2, 3, 4, 5);
        evenNodeListHead = ListNode.createNodeList(1, 2, 3, 4);
    }

    @Nested
    class ReorderList{

        /**
         * Actually it is difficult to verify do nothing in {@link  LinkedList#reorderList(ListNode)}
         * when we don't know what exact implement in it
         */
        @Test
        void should_do_nothing_when_input_head_is_null() {
            linkedList.reorderList(null);
        }

        @Test
        void should_return_the_same_when_input_one_node(){
            ListNode input = node1;
            linkedList.reorderList(input);
            assertSame(node1,input);
        }

        @Test
        void should_pass_when_the_length_is_odd(){
            linkedList.reorderList(oddNodeListHead);

            assertEquals("{ val:1  next:{ val:5  next:{ val:2  next:{ val:4  next:{ val:3  next:null}}}}}",
                    oddNodeListHead.toString());
        }

        @Test
        void should_pass_when_the_length_is_even(){
            linkedList.reorderList(evenNodeListHead);

            assertEquals("{ val:1  next:{ val:4  next:{ val:2  next:{ val:3  next:null}}}}",
                    evenNodeListHead.toString());
        }

        @Nested
        class GetFirstPartEndNodeAsSplitNode{

            @Test
            void should_get_first_part_end_node_as_split_node_when_the_length_is_odd(){
                ListNode splitNode = linkedList.getFirstPartEndNodeAsSplitNode(oddNodeListHead);
                assertEquals("{ val:2  next:{ val:3  next:{ val:4  next:{ val:5  next:null}}}}",splitNode.toString());
            }

            @Test
            void should_get_first_part_end_node_as_split_node_when_the_length_is_even(){
                ListNode splitNode = linkedList.getFirstPartEndNodeAsSplitNode(evenNodeListHead);
                assertEquals("{ val:2  next:{ val:3  next:{ val:4  next:null}}}",splitNode.toString());
            }
        }

        @Nested
        class GetFirstPart{
            @Test
            void should_cult_to_first_part(){
                ListNode firstPart = linkedList.getFirstPartHeadNode(oddNodeListHead, oddNodeListHead.next);
                assertEquals("{ val:1  next:{ val:2  next:null}}",firstPart.toString());
            }
        }

        @Nested
        class GetSecondPart {

            @Test
            void should_directly_reverse_odd_list(){
                ListNode listNode = linkedList.getSecondPartHeadNode(oddNodeListHead);
                assertEquals("{ val:5  next:{ val:4  next:{ val:3  next:{ val:2  next:{ val:1  next:null}}}}}",
                        listNode.toString());
            }

            @Test
            void should_directly_reverse_even_list(){
                ListNode listNode = linkedList.getSecondPartHeadNode(evenNodeListHead);
                assertEquals("{ val:4  next:{ val:3  next:{ val:2  next:{ val:1  next:null}}}}",
                        listNode.toString());
            }
        }

        @Nested
        class Merge{

            @Test
            void should_joint_two_node_List_in_turn_with_order_even_odd(){
                linkedList.merge(evenNodeListHead,oddNodeListHead);
                assertEquals("{ val:1  next:{ val:1  next:{ val:2  next:{ val:2  next:{ val:3  " +
                                "next:{ val:3  next:{ val:4  next:{ val:4  next:{ val:5  next:null}}}}}}}}}",
                        evenNodeListHead.toString());
            }

            @Test
            void should_joint_two_node_List_in_turn_with_order_odd_even(){
                linkedList.merge(oddNodeListHead,evenNodeListHead);
                assertEquals("{ val:1  next:{ val:1  next:{ val:2  next:{ val:2  next:{ val:3  " +
                                "next:{ val:3  next:{ val:4  next:{ val:4  next:{ val:5  next:null}}}}}}}}}",
                        oddNodeListHead.toString());
            }
        }
    }
}
```

<p align="center"> 
  Visitor count<br>
  <img src="https://profile-counter.glitch.me/istarwyh/count.svg" />
</p>
