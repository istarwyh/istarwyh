### Hi there 👋

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

If you want to know more about me, welcome to see [my online resume](https://istarwyh.github.io/)! Thank you!

## Other
a solution for find the k samllest numbers in the array:
```java
import java.util.Scanner;
import java.util.Random;
import java.util.Arrays;
class Solution {
    private static final Random rand = new Random();
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);
        int n = input.nextInt();
        int[] arr = new int[n];
        for(int i = 0;i<n;i++){
            arr[i] = input.nextInt();
        }
        int k = input.nextInt();
        int[] result = new Solution().getMinK(arr,k);
        for(int a : result){
            System.out.println(a);
        }
        input.close();
    }
    /**
     * 找到无序数组最小的k个数,k不越界
     */
    public int[] getMinK(int[] arr,int k) {
        //最小的k个数的边界即是第(len-k)大的数
        //且这个数将被放到正确的位置的上并返回其索引
        int len = arr.length;
        int kth = this.findKthLargest(arr,len-k);
        return Arrays.copyOf(arr,kth);
    }
    /**
     * 找到第k大的数
     */
    public int findKthLargest(int[] nums, int k) {
        int lo=0;
        int hi=nums.length-1;
        if(lo >= hi) return lo;

        int target_index = nums.length-k;
        while(true){
            int i= this.partition(nums,lo,hi);
            if(i == target_index)//当pivot前面有k个大于轴值得元素时,轴值就是答案
                return i;
            else if(i > target_index)//如果大于目标的位置,因为从小到大排列,说明还在左边
                hi = i-1;
            else 
                lo =i+1;
        }
    }
    
    public int partition(int[] nums,int lo,int hi){
        if(lo>=hi) return lo;// 为了防止传进来的已经指针相遇
        int i = lo;
        int j = hi+1;
        
        int random = lo + rand.nextInt(hi - lo);
        swap(nums,lo,random);
        int pivot = nums[lo];//可以通过随机选择轴值来降低平均时间复杂度
                                //但是因为底下++i的关系,轴值必须选择最低位
        while(true){
            while(less(nums[++i],pivot)) if(i == hi) break;//找到大于pivot的跳出
            while(less(pivot,nums[--j])) if(j == lo) break;
            if(i>=j ) break;//划分的一趟完成
            swap(nums,i,j);
        }
        swap(nums,lo,j);
        return j;
    }
    public static boolean less(int a,int b){
        return a>b ? false : true;
    }
    public static void swap(int[] nums,int j,int i){
        int temp=nums[j];
        nums[j]=nums[i];
        nums[i]=temp;
    }
}
```

<p align="center"> 
  Visitor count<br>
  <img src="https://profile-counter.glitch.me/istarwyh/count.svg" />
</p>
