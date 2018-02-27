public class TwoSum{
    public int[] twoSum(int[] nums, int target) {
        int[] rs = new int[2];
        for (int i = 0; i < nums.length; i++) {
            for (int j = i + 1; j < nums.length; j++) {
                if (nums[i] + nums[j] == target){
                    rs[0] = i;
                    rs[1] = j;
                    break;
                } else {
                    continue;
                }
            }
        }
        return rs;
    }

    public static void main(String[] args) {
		int[] nums = new int[]{1, 2, 3, 4};
		int[] results = new int[2];
		TwoSum ts = new TwoSum();
		results = ts.twoSum(nums, 5);
		for (int i : results) {
			System.out.print(i + " ");
		}
	}
}
