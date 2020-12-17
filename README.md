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
        for( int i=0;i<a.length;i++ ){
            max = max > a[i] ? max : a[i];
            min = min > a[i] ? a[i] : min;
        }
        int range = max - min + 1;
        int[] countArray = new int[range];
        //计数排序思想,放到对应的位置上
        for (int i = 0; i < a.length; i++) {
            countArray[a[i] - min]++;
        }
        int count = 0;
        int maxCount = 0;
        int startIndex = 0;
        int endIndex  = 0;
        int maxNearDifference = 0;
        // 做映射后,差值即数没有被映射的0的数目
        for (int i = 0; i < countArray.length; i++) {
            if (countArray[i] == 0) {
                if (count == 0) {
                    startIndex = i-1;
                }
                count++;
            }else {
                count = 0;
            }
            if (count > maxCount) {
                maxCount = count;
                
                endIndex = i+1;
            }
            //考虑到每一次更新后的情况，需要取绝对值以示长度
            maxNearDifference = Math.max(maxNearDifference, Math.abs(endIndex - startIndex));
        }  
        return maxNearDifference ;
    }
```

<p align="center"> 
  Visitor count<br>
  <img src="https://profile-counter.glitch.me/istarwyh/count.svg" />
</p>
