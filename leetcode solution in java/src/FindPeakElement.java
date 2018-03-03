public class FindPeakElement {
	public int findPeak(int[] nums) {
		int len = nums.length;
		if (len == 0) {
			return -1;
		}
        if (len == 1) {
            return 0;
        } 
        if (len == 2) {
            return nums[0] > nums[1] ? 0 : 1;
        }
        
		for (int i = 1; i <= len - 1; i++) {
			if (nums[i] > nums[i-1]){        
            	continue;
            } else {
            	return i-1;
            }
		}
		return len-1;
	}
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int[] nums = {1,2,1,3,4,5,7,6};
		FindPeakElement find = new FindPeakElement();
		System.out.println(find.findPeak(nums));
	}

}
