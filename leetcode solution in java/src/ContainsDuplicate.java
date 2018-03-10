import java.util.HashSet;
import java.util.Set;

public class ContainsDuplicate {
	public boolean containsDuplicate(int[] nums) {
		Set<Integer> set = new HashSet<>();
		boolean flag = false;
		for (int num : nums) {
			if (set.contains(num)) {
				flag = true;
			}
			set.add(num);
		}
		return flag;
    }
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		ContainsDuplicate cd = new ContainsDuplicate();
		int[] nums = {1, 2, 3, 4, 4};
		System.out.println(cd.containsDuplicate(nums));
	}

}
