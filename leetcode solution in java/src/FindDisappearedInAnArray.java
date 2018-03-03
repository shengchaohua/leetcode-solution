import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

public class FindDisappearedInAnArray {
	public List<Integer> findDisappearedNumbers(int[] nums) {
		Set<Integer> set = new HashSet<>();
		List<Integer> list = new ArrayList<>();
		for(int i=0; i<nums.length; i++) {
			set.add(nums[i]);
		}
		
		for(int i=0; i<nums.length; i++) {
			if( !set.contains(i+1) ){
				list.add(i+1);
			}
		}
        return list;
    }
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		FindDisappearedInAnArray fd = new FindDisappearedInAnArray();
		int []nums = {4,3,2,7,8,2,3,1,2};
		System.out.println( fd.findDisappearedNumbers(nums) );
	}

}
