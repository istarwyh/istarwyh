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
1044. Longest Duplicate Substring[.](https://leetcode-cn.com/problems/longest-duplicate-substring/)


```java
import java.util.HashSet;

class Solution {
    public static void main(String[] args) {
        System.out.println(new Solution().longestDupSubstring("banana"));
    }
    public String longestDupSubstring(String S) {
        // if( S == null || S.length() == 0 ) return 0;
        int n = S.length();
        // 1.设最大重复子串的长度为k,则字符串S中重复子串长度分布为1,2...k,并且k...n-1中皆无重复子串
        // 2.重复子串的判断与模式串匹配的不同点在于其必须与其他子串判断后才能得出结果,因此需要有效地列举出一个判断集合。自然地，按每个固定的长度列举出该长度下的所有的子串判断集合不失为一种策略。
        // 3.固定的长度k可以视作是滑动的窗口长度,从而以O(n)的时间遍历长度k内所有的子串
        // 4.但是对子串s1,s2是否重复的判断如果只是逐个比对字符,每一次的时间复杂度即O(Min(s1,s2));因此诞生了Rabin-Karp算法对字符串当作多项式求和进行rolling_hash,正好结合滑动窗口可以以O(1)得到每个字符串的hash值,从而使得比较s1,s2的时间复杂度降至O(1)
        // 5.RK算法将小写字母组成的字符串看作是26个小写字母对应的ASCII值写成的26进制数,将26进制数转换为10进制数之后的数值便是特征值h：
        // 不考虑整数溢出,初始nums[pre] == 0, h == 0, nums[next] == nums[0]:
        // h = ( h - nums[pre]*26^(len-1) ) * 26 + nums[next]*26^0
        // 当考虑Java编程条件下的整数溢出以及存取特征值的效率,必须对特征值做hash处理,采用传统取余操作。根据生日悖论--某个特定数的出现概率低,但是两个重复特征数的出现概率却高,因此为了保证低碰撞概率,
        // 模数应大于等于特征数的平方根的数量级。因为n最大为10^5长度,所以最大的特征数数量级应该是26*26^(10^5-1)，所以为了保证完全不碰撞应当选取模数＞2^(5*316),
        // 这是做不到的。。。而又考虑到余数也会参与运算,为防止越界，尽可能选取较大的模数2^32。如果发现相等了可以再采用O(Max(s1,s2))的时间复杂度比较它们：
        // modules = 2^32,并利用同余定理,考虑到可能出现负数,最后公式拆为两步：
        // h = ( h*26%modules - nums[pre]*26^len% modules) + modules)%modules,h = (h + nums[next]*26^0)%modules
        // 然而！！26^(len-1)还是会越界！！,因此对于这个中间数依然需要做取余操作

        // 由1可知最后的结果可以视作是从一个有序数列中找到k,因此采用二分法,初始的长度mid = left + (rignt-left)/2,结束条件是当查找区间耗尽
        // 传统二分查找是找到符合条件的数就返回
        // 但这里不同在于需要找到符合判断条件的最大的值，因此左边界充当了 扩大 符合判断条件边界范围的任务
        S2Pattern s2p = new S2Pattern(S);
//        重复子串查长度取值区间[left,right]
        int left = 1;
        int right = n-1;
        // 重复子串的起始位置
        int start = -1;
//        二分结束条件为区间无效
        while( left <= right ){
            int k = left + (right - left )/2;
            int tmp;
            if( ( tmp =  this.existDup(s2p,k) )!= -1 ){
                // 下一步k应该从k+1开始尝试
                left = k+1;
                start = tmp;
            }else{
                // 如果不符合,逐步缩小区间
                right = k-1;
            }
        }
        return start != -1 ? S.substring(start,start+left-1) : "";
    }
    public int existDup( S2Pattern s2p,int k ){
        long h = 0;
        for( int i = 0;i<k;i++ ){
            h = ( h*s2p.scale + s2p.nums[i])  % s2p.modules;
        }
        HashSet<Long> seen = new HashSet<>();
        seen.add(h);
        long scaleK = 1 ;
        for( int i=1;i <= k ;i++) scaleK = ( scaleK * s2p.scale) % s2p.modules;
        for( int i=1;i + k -1<s2p.nums.length ;i++ ){
            h = (h*s2p.scale - s2p.nums[i-1] * scaleK + s2p.modules) % s2p.modules;
            h = (h + s2p.nums[ i + k -1 ]) % s2p.modules;
            if( seen.contains(h)) return i;
            else{
                seen.add(h);
            }
        }
        return -1;
    }
    static class S2Pattern{
        int[] nums;
        int scale;
        long modules;
        public S2Pattern(String s){
            this.nums = new int[s.length()];
            for( int i=0;i<s.length();i++ ){
                nums[ i ] = s.charAt(i)-'a';
            }
            this.modules = (long)Math.pow(2,38);
            this.scale = 26;
        }
    }

}
```

<p align="center"> 
  Visitor count<br>
  <img src="https://profile-counter.glitch.me/istarwyh/count.svg" />
</p>
