public class MaxConsecutiveOnes {
	/**
	 * @author shengchaohua
	 * @param nums
	 * @return max consecutive ones  
	 */
	public int findMaxConsecutiveOnes(int[] nums) {
        int max = 0;
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
        		max = tempNum > max ? tempNum : max;
        	} 
        }
		return max;
    }
	
	public int findMaxConsecutiveOnes_better(int[] nums) {
        int max = 0;
        int sum = 0;
        for(int i = 0 ; i< nums.length; i ++){
            sum += nums[i];
            if(nums[i] == 0) {   // reset sum to zero when encounters zeros
                sum = 0;
            } else {                // keep update max
                max = Math.max(max, sum);
            }
        }
        return max;
    }
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int[] nums = {1, 1, 0, 1, 0, 1, 1};
		MaxConsecutiveOnes mso = new MaxConsecutiveOnes();
		System.out.println(mso.findMaxConsecutiveOnes(nums));
	}

}
