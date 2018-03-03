public class RemoveDuplicatesFromSortedArray {	
	public static int removeDuplicates(int[] nums) {  
        int len = nums.length;  
        if (len == 0)  
            return 0;  
        int count = 1;  
        for (int i = 1; i < len; i++) {  
            if (nums[i] == nums[i - 1]) {  
                continue;  
            }else{  
                nums[count] = nums[i];  
                count++;  
            }  
        }  
        return count;  
    }
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int [] nums = {1,1,1,2,2,2};
		System.out.println(removeDuplicates(nums));
	}

}
