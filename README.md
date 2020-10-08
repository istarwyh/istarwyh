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
16. 3Sum Closest[.](https://leetcode-cn.com/problems/3sum-closest/)


```java
class Solution {
    // 仍然是O(n2)然后加一起剪枝
        //因为剪枝，代码冗余是很多的,但是因为逻辑稍微有些不一样，目前不知道怎样去抽象
    public int threeSumClosest(int[] nums, int target) {
        // 题设说了至少有一个解，这里不防御了
        Arrays.sort(nums);
        int resGap = Integer.MAX_VALUE;
        int res = target;
        // 剪枝操作1：最后不足三个数时已经可以跳出
        for( int i=0;i<nums.length-2;i++ ){
            while( i != 0 &&  i< nums.length && nums[i] == nums[i-1] ) i++;
            if( i >= nums.length - 2 ) break;
            
            // 剪枝操作2：target小于最小值,后续只能远离
            int min = nums[i]+nums[i+1]+nums[i+2];
            if( target < min ){
                int absGap = Math.abs( min -target );
                if( resGap > absGap){
                    resGap = absGap;
                    res = min;
                }
                continue;
            }
            // 剪枝操作3：target大于最大值,后续只能远离
            int max = nums[i]+nums[nums.length-1]+nums[nums.length-2];
            if( target > max ){
                int absGap = Math.abs( max -target );
                if( resGap > absGap){
                    resGap = absGap;
                    res = max;
                }
                continue;
            }

            int j = i+1;
            int k= nums.length-1;
            while( j<k ){
                int tmpSum = nums[i]+nums[j]+nums[k];
                int tmpGap = tmpSum-target;
                int absTmp = Math.abs(tmpGap);
                if ( resGap > absTmp ){
                    resGap = absTmp;
                    res = tmpSum;
                } 
                int minGap = 0;
                if( tmpGap > minGap ){
                    k--;
                }else if( tmpGap < minGap ){
                    j++;
                }else{
                    // 题目说的至少一个解包括了接近到两者相等的情况
                    // 剪枝操作4：直接返回也是一个
                    return target;
                }
                while( j != i+1 && j<k && nums[j] == nums[j-1] ) j++;
                while( k != nums.length-1 && j<k && nums[k] == nums[k+1] ) k--;
                if( j>= k ) break;
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
