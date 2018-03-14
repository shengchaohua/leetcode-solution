import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class ArrayPartitionI {
	public int arrayPairSum(int[] nums){
		int res = 0;
		List<Integer> list = new ArrayList<>();
		for (int i = 0; i < nums.length; i++){
			list.add( nums[i] );
		}
		list.sort(null);
		for(int i = 0; i < list.size(); i = i+2){
			res = res + list.get(i);
		}
		return res;
	}
	
	public int arrayPairSumBetter(int[] nums){
		Arrays.sort(nums);
		int res = 0;
		for(int i = 0; i < nums.length; i = i+2){
			res = res + nums[i];
		}
		return res;
	}
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		ArrayPartitionI aPartitionI = new ArrayPartitionI();
		int[] nums = {10, 9, 8, 7, 6, 5, 4, 3, 2, 1};
		System.out.println(aPartitionI.arrayPairSum(nums));
		System.out.println(aPartitionI.arrayPairSumBetter(nums));
	}

}
