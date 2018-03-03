import java.util.ArrayList;
import java.util.List;

public class ArrayPartitionI {
	public int arrayPar(int[] nums){
		int sum = 0;
		List<Integer> list = new ArrayList<>();
		for (int i = 0; i < nums.length; i++){
			list.add( nums[i] );
		}
		list.sort(null);
		for(int i = 0; i < list.size(); i = i+2){
			sum = sum + list.get(i);
		}
		return sum;
	}
	
	public int arrayPar_insertSort(int[] nums){
		for (int i = 1; i < nums.length; i++) {
			int temp = nums[i];
			// insert nums[i] into sorted sequence nums[0, 1, 2, ... , i-1]
			int j = i - 1;
			while( j >= 0 && nums[j] > temp){
				nums[j+1] = nums[j];
				j--;
			}
			nums[j+1] = temp;
		}
		int sum = 0;
		for(int i = 0; i < nums.length; i = i+2){
			sum = sum + nums[i];
		}
		return sum;
	}
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		ArrayPartitionI aPartitionI = new ArrayPartitionI();
		int[] nums = {10, 9, 8, 7, 6, 5, 4, 3, 2, 1};
		System.out.println(aPartitionI.arrayPar(nums));
		System.out.println(aPartitionI.arrayPar_insertSort(nums));
	}

}
