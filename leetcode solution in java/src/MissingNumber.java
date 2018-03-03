public class MissingNumber {
	
	public int missingNumber(int[] nums) {
		int len = nums.length;
	    int sum = (0+len)*(len+1)/2;
	    for(int i=0; i<len; i++)
	        sum-=nums[i];
	    return sum;
    }
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		MissingNumber mn = new MissingNumber();
		int []nums = {0, 1, 3, 4, 2 ,6};
		System.out.println(mn.missingNumber(nums) );
	}

}
