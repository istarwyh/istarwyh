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
Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n)[.](https://leetcode-cn.com/problems/minimum-window-substring)


```java
public class Solution {
    public static void main(String[] args) {
        char[] chars = {'a','b','c'};
        new Solution().printSub(chars);
    }
    public void printSub(char[] chars){

        /**
         * 以集合{a,b,c}为例，
         * 于是对所有的子集也可以采用二进制编码的方式：
         * 000 == null
         * 001 == a
         * 010 == b
         * ...
         * 111 == cba
         * 如果想要提取出这样二进制编码代表的子集信息（如打印出来），
         * 只需要元素编码与子集编码做“&”运算，来判断在每个被编码的子集中元素是否出现，
         * 001 & 011 == 001 == a[1<<i的i] == a[0] == a
         * 010 & 011 == 010 == a[1<<i的i] == a[1] == b
         * 100 & 011 == 000
         * 所以这个编码为011的子集则为 a，b
         *
         */
        int len = chars.length;
        int totalNum = (1 << len) ;
        for(int i=0;i<totalNum;i++){
            for( int j = 0; j<len; j++ ){
                int mask = 1 << j;
                if( (i & mask) != 0){
                    System.out.print( chars[j]);
                }
            }
            System.out.println();
        }


    }
 }

```

<p align="center"> 
  Visitor count<br>
  <img src="https://profile-counter.glitch.me/istarwyh/count.svg" />
</p>
