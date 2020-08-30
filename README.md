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
a solution for find  all of the subsets of an array:

```java

import java.util.HashMap;
import java.util.Collection;
import java.util.Iterator;
class Solution {
    public int subarraysDivByK(int[] A, int K) {
        int len=A.length;
        // 定义为从索引0到i的和
        int preSum[] = new int[len];
        preSum[0] = A[0];
        for(int i=1;i<len;i++){
            preSum[i] =preSum[i-1] +  A[i];
        }
        HashMap<Integer,Integer> map = new HashMap<>();
        int count0 =0;
        for(int i=0;i<len;i++){
            int preSumModK = preSum[i] % K;
            // 处理preSumModK为负的情况
            if(preSumModK < 0)
                preSumModK += K;
            if(map.containsKey(preSumModK)){
                map.put(preSumModK,map.get(preSumModK)+1);
            }else if(preSumModK ==0 ){
                //如果第一次出现 前缀和余K值 
                count0 ++;
            }else{
                map.put(preSumModK,1);
            }
        }
        int count =0;
       Collection c = map.values();
       Iterator itr = c.iterator();
       while(itr.hasNext()){
           count += Combination((Integer)itr.next(),2);
       }
       count += count0;
        return count;
    }
    private static int Combination(int n,int k){
        //按需要改造了组合数的计算,只有一个前缀和时,除了
        if(n ==1)
            return 0;
        if(k==0 || k==n){
            return 1;
        }else{
            return Combination(n-1,k) + Combination(n-1,k-1);
        }
    }
}
```

<p align="center"> 
  Visitor count<br>
  <img src="https://profile-counter.glitch.me/istarwyh/count.svg" />
</p>
