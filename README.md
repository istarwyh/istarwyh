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
219. Contains Duplicate II[.](https://leetcode-cn.com/problems/contains-duplicate-ii/)


```java
class Solution {
    /**
    * 面向指针解题处处需要进行防御式编程
    */
    public boolean containsNearbyDuplicate(int[] nums, int k) {
        // 对所有有引用的家伙都不要掉以轻心啊！！
        if( nums == null || nums.length == 0 ) return false;
        // 维护滑动窗口同时维护映射
        HashSet<Integer> set = new HashSet();
        int l = 0;
        int r = l + k;
        while( r >= nums.length ) r--;

        for( int i=0;i < r+1 ;i++ ){
            if( set.contains( nums[i] ) ) return true;
            set.add( nums[i] );
        }
        // 以长度为限界，维护长度
        while( r < nums.length ){
            set.remove( nums[ l ] );
            r++;
            if( r >= nums.length ) break;

            if( set.contains( nums[r] ) ) return true;
            else{
                l++;
                set.add( nums[r] );     
            }
        }
        return false;
    }
    /**
    * 这种方法不显式用指针,直接维护长度就不用防御指针
    */
//      public boolean containsNearbyDuplicate(int[] nums, int k) {
//          HashSet<Integer> set = new HashSet();
//          for( int i=0;i<nums.length;i++ ){
//              if( set.contains( nums[i] ) ) return true;
//              set.add( nums[i] );
//             //  其实距离为k,有k+1个元素
//              if( set.size() == k+1 ){
//                  set.remove( nums[i-k] );
//              }
//          }
//          return false;
//      }
// }
```

<p align="center"> 
  Visitor count<br>
  <img src="https://profile-counter.glitch.me/istarwyh/count.svg" />
</p>
