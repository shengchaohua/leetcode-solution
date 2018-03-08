public class MoveZeros {
	public void moveZeroes(int[] nums) {
		int len = nums.length;
		for (int i = 0; i < len; i++) {
			if (nums[i] != 0) {
				continue;
			}
			int j = i;
			while (j < len && nums[j] == 0) {
				j++;
			}
			if (j < len) {
				int temp = nums[i];
				nums[i] = nums[j];
				nums[j] = temp;
			} else {
				break;
			}
		}
		for (int i = 0; i < len; i++) {
			System.out.print(nums[i] + " ");
		}
	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int[] nums = { 0, 1, 0, 3, 12, 11, 0, 9, 0};
		MoveZeros mz = new MoveZeros();
		mz.moveZeroes(nums);
	}

}
