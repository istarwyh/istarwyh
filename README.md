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
Given an array A of integers, return the number of (contiguous, non-empty) subarrays that have a sum divisible by K:


```java
class Solution {
    public int subarraysDivByK(int[] A, int K) {
        int len=A.length;
        // 定义为从索引0到i的和
        int preSum[] = new int[len];

        //如果前缀和本身就是0，因为需要对0的情况单独计数，因此是大于等于0
        preSum[0] = A[0];      
        int tmp = preSum[0] % K;
        int preSumModK = tmp >=0 ? tmp : tmp+K;  

        int[] preSumModKs = new int[10000];
        preSumModKs[preSumModK]++;

        //为了利用递推公式，从i=1开始。上面先对i==0的情况处理。
        for(int i=1;i<len;i++){
            preSum[i] = preSum[i-1] +  A[i];

            // 防止计算机计算preSumModK为负数的情况
            tmp = preSum[i] % K;
            preSumModK = tmp >=0 ? tmp : tmp+K;

            preSumModKs[preSumModK]++;
        }

        int count =0;
        // 当presumModK为0，自己是本身就是一种满足条件的子数组组合
        count += preSumModKs[0];

        for(int a : preSumModKs)
            count += Combination(a,2);
        
        return count;
    }

    private static long Combination(int n,int m){

        if(m==0)
            return 1;
        if (m==1) 
            return n;
        if(m>n/2)
            return Combination(n,n-m);
        if(n>1)
            return Combination(n-1,m)+Combination(n-1,m-1);  
        return 0;
    }
}
```

<p align="center"> 
  Visitor count<br>
  <img src="https://profile-counter.glitch.me/istarwyh/count.svg" />
</p>
