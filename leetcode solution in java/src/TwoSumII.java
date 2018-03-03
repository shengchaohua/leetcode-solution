import java.util.HashMap;

public class TwoSumII {
	public int[] twoSum(int[] numbers, int target) {
		HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();
		int[] res = new int[2];
		for (int i = 0; i < numbers.length; ++i) {
			map.put(numbers[i], i);
		}
		for (int i = 0; i < numbers.length; ++i) {
			int t = target - numbers[i];
			if (map.containsKey(t) && map.get(t) != i) {
				res[0] = i+1;
				res[1] = map.get(t)+1;
				break;
			}
		}
		return res;
	}

	public static void main(String[] args) {
		TwoSumII ts = new TwoSumII();
		int[] nums = {2, 7, 11, 15};
		int[] res = ts.twoSum(nums, 9); 
		System.out.println(res[0] + " " + res[1]);
	}
}
