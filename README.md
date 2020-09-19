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
Given a string, sort it in decreasing order based on the frequency of characters[.](https://leetcode-cn.com/problems/word-pattern/)


```java
import java.util.Map.Entry;
class Solution {
       public String frequencySort(String s) {
        if( s == null ) return null;
        if( s.length() == 0) return s;
        int len = s.length();
        HashMap<Character,Integer> map = new HashMap<>();
        for( int i =0;i<len;i++){
            Character c = s.charAt(i);
            map.put(c, map.getOrDefault(c,0)+1 );
        }
        Iterator iter = map.entrySet().iterator();
        StringBuilder sb = new StringBuilder();
        if( iter.hasNext()) {
            Entry maxNode = (Entry) iter.next();
            do {
                while (iter.hasNext()) {
                    Entry curNode = (Entry) iter.next();
                    if ((Integer) maxNode.getValue() < (Integer) curNode.getValue()) {
                        maxNode = curNode;
                    }
                }
                for (int i = 0; i < (Integer) maxNode.getValue(); i++) {
                    sb.append(maxNode.getKey());
                }
                map.remove((Character) maxNode.getKey());

                iter = map.entrySet().iterator();
                if (iter.hasNext()) {
                    maxNode = (Entry) iter.next();
                }
            } while (map.size() > 0);

            return sb.toString();
        }
        return null;
    }
}
```

<p align="center"> 
  Visitor count<br>
  <img src="https://profile-counter.glitch.me/istarwyh/count.svg" />
</p>
