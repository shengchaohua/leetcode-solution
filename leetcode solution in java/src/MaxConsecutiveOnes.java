public class MaxConsecutiveOnes {
	public int findMaxConsecutiveOnes(int[] nums) {
        int oneNum = 0;
        int tempNum = 0;
        int len = nums.length;
        for (int i = 0; i < len; i++) {
        	if (nums[i] == 1) {
        		tempNum = 1;
        		for (int j = i+1; j < len; j++) {
        			if (nums[j] == 1) {
        				tempNum += 1;
        			} else {
        				break;
        			}
        		}
        		oneNum = tempNum > oneNum ? tempNum : oneNum;
        	} 
        }
		
		return oneNum;
    }
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int[] nums = {1, 1, 0, 1, 0, 1, 1};
		MaxConsecutiveOnes mso = new MaxConsecutiveOnes();
		System.out.println(mso.findMaxConsecutiveOnes(nums));
	}

}
