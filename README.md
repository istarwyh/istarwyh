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
49. Group Anagramst[.](https://leetcode-cn.com/problems/group-anagrams/)


```java
class Solution {
    // 题目主要考选取什么标准的能力，选取什么标准呢？
        //  Anagram意思是这两个单词中字母的出现频率一样
            // 这个意思是我需要把这些单词化成可以量化的指标，并把这些指标作为key即分类的标准来分类
       public List<List<String>> groupAnagrams(String[] strs) {
        if (strs == null) return null;
        if (strs.length == 0) return new ArrayList<>();

        HashMap<StrPattern, List<String>> map = new HashMap<>(16);
        for (String str : strs) {
            StrPattern strP = new StrPattern(str);
            if (map.containsKey(strP)) {
                List<String> v = map.get(strP);
                v.add(str);
                map.put(strP, v);
            } else {
                List<String> l = new ArrayList<>();
                l.add(str);
                map.put(strP, l);
            }
        }
        return new ArrayList<>(map.values());
    }

    static class StrPattern{
        Integer[] freq;
        // 重定义它自己的hashCode,并提出来作为属性以在重写hashCode()与equals()时都用到
        int hashCode;
        public  StrPattern(String str) {
             this.freq = new Integer[26];
            Arrays.fill(freq, 0);
            for (int i = 0; i < str.length(); i++) {
                freq[str.charAt(i) - 'a'] ++;
            }
            this.hashCode = Arrays.toString(freq).hashCode();
        }
        @Override
        public int hashCode() {
            // 同样内容的freq[]只有转成String了才能避免总是新对象的悲剧，String常量池牛！
            return hashCode;
        }

        // @Override
        // public boolean equals(Object obj) {
        //     StrPattern o = (StrPattern)obj;
        //     if( this.freq.length != o.freq.length ) return false;
        //     for( int i=0;i<o.freq.length;i++){
        //         if(!this.freq[i].equals(o.freq[i])) return false;
        //     }
        //     return true;
        // }
        
        @Override
        public boolean equals(Object obj) {
            StrPattern o = (StrPattern)obj;
            return this.hashCode == o.hashCode;
        }
    }

}
```

<p align="center"> 
  Visitor count<br>
  <img src="https://profile-counter.glitch.me/istarwyh/count.svg" />
</p>
