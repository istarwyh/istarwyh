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
剑指 Offer 48. 最长不含重复字符的子字符串 LCOF[.](https://leetcode-cn.com/problems/add-two-numbers-ii/)


```java
class Solution {
   public int lengthOfLongestSubstring(String s) {
        if( s == null || s.length() == 0) return 0;
        int[] freq= new int[128];

        int left = 0;
        int right = 0;
        freq[ s.charAt(0)]++;
        int res = 1;
        while(left <= right ){
            // 先扩张
            while( right+1 < s.length() && freq[s.charAt(right+1)] != 1){
                right++;
                freq[s.charAt(right)]++;
            }
            int len = right-left+1;
            if( right+1 >= s.length()){
                return Math.max(res, len);
            }
            if(freq[s.charAt(right+1)] == 1){
                res = Math.max(res, len);
            }
            // 再往前踏一步
            right++;
            int cur = s.charAt(right);
            freq[cur]++;
            // 然后收缩到要求的无重复内
            while( freq[ cur ] >= 2 ){
                freq[s.charAt(left) ]--;
                left++;
            }
        }
        return res;
    }
}
```

<p align="center"> 
  Visitor count<br>
  <img src="https://profile-counter.glitch.me/istarwyh/count.svg" />
</p>
