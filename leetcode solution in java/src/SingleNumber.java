public class SingleNumber {
	public int findit(int[] nums) {
		boolean[] flag = new boolean[nums.length];
		for (int i = 0; i < nums.length; i++) {
			int j = i + 1;
			for ( ; j < nums.length && !flag[i]; j++) {
				if (nums[i] == nums[j]) {
					flag[i] = flag[j] = true;
					break;
				} 
			}
			if (j == nums.length) {
				return nums[i];
			}
		}
		return 0;
	}
	
	public int finditWithBit(int[] nums) {
		int result = 0;
		for (int num: nums) {
			result ^= num;
		}
		return result;
	}
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int[] A = {1,2,1,2,3,4,5,6,3,4,5};
		SingleNumber sn = new SingleNumber();
		System.out.println(sn.findit(A));
		System.out.println(sn.finditWithBit(A));
	}

}
