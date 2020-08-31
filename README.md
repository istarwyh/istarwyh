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
import java.util.HashMap;
import java.util.Collection;
import java.util.Iterator;
class Solution {
    public int subarraysDivByK(int[] A, int K) {
        int len=A.length;
        // 定义为从索引0到i的和
        int preSum[] = new int[len];

        //利用hash表能够寻找组合的数目
        HashMap<Integer,Integer> map = new HashMap<>();
        
        preSum[0] = A[0];
        int tmp = preSum[0] % K;
        int preSumModK = tmp >=0 ? tmp : tmp+K;  
        map.put(preSumModK,1);

        //为了利用递推公式，从i=1开始.上面先对i==0的情况处理.
        for(int i=1;i<len;i++){

            preSum[i] = preSum[i-1] +  A[i];

            // 防止计算机计算preSumModK为负数的情况
            // 真的前置知识比较多！！
            tmp = preSum[i] % K;
            preSumModK = tmp >=0 ? tmp : tmp+K;

            if(map.containsKey(preSumModK)){
                map.put(preSumModK,map.get(preSumModK)+1);
            }else{
                map.put(preSumModK,1);
            }
        }

        int count =0;
        // 当presumModK为0，自己是本身就是一种满足条件的子数组组合；其他preSumModK只可能与相减为0 才能满足中间子数组被K整除
        // 所以加上其本身的组合数情况
        if(map.containsKey(0)){
           count +=  map.get(0);
        }

        Collection c = map.values();
        Iterator itr = c.iterator();
        while(itr.hasNext()){
            int cur = (Integer)itr.next();
            count += Combination(cur,2);
        }
        
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
