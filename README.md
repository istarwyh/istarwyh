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
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.[.](https://leetcode-cn.com/problems/3sum)


```java
class Solution {
   // 1.这里就要用到#1的第一种解法了！其实是属于快排类解法，不断找到需要的指针进行判断。
    
    // 而这题比#1简单就简单在它不需要返回索引！因此排序前不需要想办法保留索引位置。
        // nums.length < 3000 ,所以其实O(n2)也可以接受？但这是要返回组合，而不是返回次数。
        // 能不能用map降低O(n)？--> 做不到。因为对于三个都要得到的指针，至少得遍历其中两个指针，这样还是O(n2)
  public List<List<Integer>> threeSum(int[] nums) {
        if( nums == null ) return null;
        if( nums.length < 3 ) return new ArrayList<>();
        List<List<Integer>> ll = new ArrayList<>();
        Arrays.sort( nums );
        for( int i=0 ;i<nums.length;i++){
            while( i != 0 && i< nums.length &&  nums[i] == nums[i-1] ){ i++;}
            if( i > nums.length-1 ) break;

            this.match(i,nums,ll);

            if(nums[i] > 0) break;
        }
        return ll;
    }
    public void match(int i, int[] nums,  List<List<Integer>> ll){
        int j = i+1;
        int k = nums.length-1;
        while( j < k ){
            while( j != i+1 && j<k && nums[j] == nums[j-1] ){ j++;}
            while( k != nums.length-1 && j<k && nums[k] == nums[k+1] ){ k--;}
            if( j >= k ){ break;}
            if( nums[i] + nums[j] + nums[k] < 0){
                j++;
            }else if( nums[i] + nums[j] + nums[k] > 0 ) {
                k--;
            }else{
                ll.add( new ArrayList<>( Arrays.asList(nums[i] , nums[j] , nums[k])));
                j++;
                k--;
            }
        }
    }
}
```

<p align="center"> 
  Visitor count<br>
  <img src="https://profile-counter.glitch.me/istarwyh/count.svg" />
</p>
