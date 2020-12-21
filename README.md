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
计数排序求无序数组相邻最大差值


```java
 public static Integer getMaxAdjustDifference(int[] a) {
        int max = a[0];
        int min = a[0];
        for( int num : a){
            max = Math.max(max, num);
            min = Math.min(min,num);
        }
        // find the max & min to save some space
        int range = max- min +1 ;
        int[] mapArr = new int[range];
        // 按照本身的大小进行映射，因此相互之间的差值即相互距离的远近
        for( int i=0;i<a.length;i++){
            mapArr[ a[i]-min ] = a[i];
        }
        // 而相互的距离又是没有被赋值的，即数组初始化后0的个数
        // 计数0的个数
        int maxZeroCount = 0;
        int zeroCount = 0;
        boolean isFirstNotZero = false;
        for (int j : mapArr) {
            if (j != 0) {
                isFirstNotZero = true;
            }
            if (isFirstNotZero && j == 0) {
                zeroCount++;
            } else {
                maxZeroCount = Math.max(maxZeroCount, zeroCount);
                zeroCount = 0;
            }
        }
        // 相邻差值为映射后0的个数+1
        return maxZeroCount+1;
    }
```

<p align="center"> 
  Visitor count<br>
  <img src="https://profile-counter.glitch.me/istarwyh/count.svg" />
</p>
