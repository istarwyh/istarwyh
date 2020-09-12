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
    static class Pattern{
        String str;
        int[] freq;
        int groove;

        Pattern(String str, boolean isIni){
            this.str = str;
            this.freq = new int[256];
            this.groove  = 0;
            if(isIni) {
                for (int i = 0; i < str.length(); i++) {
                    this.freq[str.charAt(i)]++;
                }
                for(int a : freq){
                    if(a != 0)
                        this.groove++;
                }
            }
        }
    }

    public String minWindow(String s, String t) {
        Pattern p2s = new Pattern(s,false);
        Pattern p2t = new Pattern(t,true);
        int l = 0;
        int r = -1;
        int[] resIndex = this.find2Shrink(p2s,p2t,l,r);
        l = resIndex[0];
        r = resIndex[1];
        // 对找不到的情况做判断
        if( r == -1) return "";

        String res = p2s.str.substring(l,r+1);
        // 对结果集进行判断
        if( l >= p2s.str.length() ){
            return res;
        }else{
            do{
              resIndex = this.break2circle(p2s,p2t,l,r);
              l = resIndex[0];
              r = resIndex[1];
              // 如果不用找了
              if( l == r ) return res;
              // 对找不到的情况做判断
              if( r == -1 ) return res;

              if(res.length() > r-l+1) {
                  res = p2s.str.substring(l,r+1);
              }
            }while ( l < p2s.str.length());
        }
        return res;
    }

    /**
     *
     * @param p2s
     * @param p2t
     * @param l
     * @param r
     * @return 从当前l开始，找到满足p2t的模式条件下最小的窗口
     */
    private  int[] find2Shrink(Pattern p2s,Pattern p2t,int l, int r){
        // 对于这个函数的功能定义，允许l >= r
        //find & expand
        while( r+1 < p2s.str.length()){
            r++;
            int curIndex =  p2s.str.charAt(r);
            p2s.freq[curIndex]++;
            if( p2s.freq[curIndex] == p2t.freq[curIndex] ){
                p2s.groove++;
            }
            if(p2s.groove == p2t.groove) break;
        }
        //shrink
        int tail = p2s.str.charAt(l);
        while( l < r ){

            // 然后 不断缩小直到满足窗口条件，不能再去掉任何一个
            // 以及 没有踩中槽说明它是多余的，可以去掉
            if( p2s.freq[tail] > p2t.freq[tail] || p2t.freq[tail] <= 0){
                p2s.freq[tail]--;
                l++;
                tail = p2s.str.charAt(l);
            }else{
                break;
            }
        }
        if( p2s.groove == p2t.groove ){
            return new int[]{l,r};
        }else{
            return  new int[]{-1,-1};
        }
    }

    /**
     *
     * @param p2s
     * @param p2t
     * @param l
     * @param r
     * @return 在保障循环不变量的情况下做一个强制l前移的动作，以找到最小的满足模式的窗口
     */
    private int[] break2circle(Pattern p2s, Pattern p2t,int l,int r){
        // 维护循环不变量的定义
        // 传参的时候一定要做校验！！对于这个函数的功能定义，不允许l >= r
        if(l + 1 > r) return new int[]{l,l};
        // 强制破坏边界
        int tail = p2s.str.charAt(l);
        if( p2s.freq[tail] == p2t.freq[tail]){
            p2s.groove--;
        }
        p2s.freq[tail]--;
        l++;
        //circle
        return this.find2Shrink(p2s,p2t,l,r);
    }
 }
```

<p align="center"> 
  Visitor count<br>
  <img src="https://profile-counter.glitch.me/istarwyh/count.svg" />
</p>
