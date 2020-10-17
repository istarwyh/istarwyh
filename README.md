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
220. Contains Duplicate III[.](https://leetcode-cn.com/problems/contains-duplicate-iiI/)


```java
import java.util.TreeSet;
class Solution {
    public boolean containsNearbyAlmostDuplicate(int[] nums, int k, int t) {
        TreeSet<Long> set = new TreeSet<>();
        for( int i=0;i<nums.length;i++ ){
            if( this.isOk(set,nums,i,t) )
                return true;
            set.add((long) nums[i] );
            // 直接以长度维护，不显式使用指针好得多啊
            if( set.size() > k ){
                set.remove( (long) nums[i-k] );
            }
        }
        return false;
    }
    // 面向指针解题处处需要防御（@）
    // public boolean containsNearbyAlmostDuplicate(int[] nums, int k, int t) {
    //     if( nums == null || nums.length == 0 ) return false;
    //     int l = 0;
    //     int r = l+k;
    //     while( r >= nums.length ) r--;//@1
    //     // 默认自然排序
    //     TreeSet<Long> set = new TreeSet<>();
    //     for( int i=0; i < r+1 ; i++ ){
    //         if(  this.isOk(set,nums,i,t) )
    //             return true;
    //         else
    //             set.add(Long.valueOf( nums[i] ) );
    //     } 
    //     while( r < nums.length ){
    //         set.remove( (long)nums[l] );
    //         r++;
    //         if( r >= nums.length ) break;//@2

    //         if( this.isOk(set,nums,r,t) )
    //             return true;
    //         else{
    //             l++;
    //             set.add( Long.valueOf( nums[r] ));            
    //         }
    //     }
    //     return false;
    // }
    public boolean isOk( TreeSet<Long> set,int[] nums,int i,int t){
        // TreeSet里寻找比给定数小的最大值ceiling方法或者比给定数大的最小值floor方法
        // 正整数与负整数都有可能越界
        long boundL = (long)nums[i]- (long)t;
        long boundR = (long)nums[i]+ (long)t;
        return set.ceiling(boundL) !=null && set.ceiling(boundL) <= boundR; 
    }
}
```

<p align="center"> 
  Visitor count<br>
  <img src="https://profile-counter.glitch.me/istarwyh/count.svg" />
</p>
