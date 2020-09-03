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
Given a string s, find the length of the longest substring without repeating characters[.](https://leetcode-cn.com/problems/longest-substring-without-repeating-characters)


```java
import java.lang.Math;
class Solution {
    /**
    *ASCII的字符只有256个，所以可以映射为数组下标，实现查找效率为O(1)
    */
    public int lengthOfLongestSubstring(String s) {
        int l = 0;
        int r =-1;
        int[] freq = new int[256];
        int res = 0;
        int len = s.length();
        while(l < len){
            if( r+1 < len && freq[s.charAt(r+1)] == 0 ){
                r++;
                //刚纳入在区间之内的元素，区间内出现频率随之增大
                freq[s.charAt(r)]++;
                
            }else{
                //当要把元素排除在区间之外，区间内出现频率随之缩小
                freq[s.charAt(l)]--;
                l++;
            }
            res = Math.max(res,r-l+1);
        }
        return res;
    }
}
```

<p align="center"> 
  Visitor count<br>
  <img src="https://profile-counter.glitch.me/istarwyh/count.svg" />
</p>
