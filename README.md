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
Given a pattern and a string s, find if s follows the same pattern[.](https://leetcode-cn.com/problems/word-pattern/)


```java
class Solution {
    // #290 是基于维护单射定义的解法,即a->b,有在甲方a必有b，在乙方有b必有a；
    // #205 尝试采用先解决多射再比较的问题
        // -->不管怎么样还是需得到映射关系，于是引入HashMap实属无奈
    public boolean isIsomorphic(String s, String t) {
        // if( s.length() != t.length() ) return false;
        int[] mapS = new int[128];
        int[] mapT = new int[128];

        HashMap<Character,Character> map = new HashMap<>();
        for( int i=0;i<s.length();i++){
            char c1  = s.charAt(i);
            mapS[c1]++;
            char c2 = t.charAt(i);
            mapT[c2]++;

            if( mapS[c1]>1 ||  mapT[c2]>1  ){
                // 当已经建立映射时，c1与c2 应该同步变化
                    // 尝试失败，没有办法定义所谓的同步变化。当已经建立映射，不能判断
                if( mapS[c1] != mapT[c2])
                    return false;
                else if( mapT[ map.get(Character.valueOf(c1)).charValue() ] != mapS[c1] )
                    return false;
            }
            map.put( Character.valueOf(c1), Character.valueOf(c2) );

        }
        return true;
    }
}

```

<p align="center"> 
  Visitor count<br>
  <img src="https://profile-counter.glitch.me/istarwyh/count.svg" />
</p>
