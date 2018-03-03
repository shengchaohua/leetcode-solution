

public class NextGreaterElementI {
	public int[] nextGreaterElement(int[] nums1, int[] nums2) {
		int[] index = getIndex(nums1, nums2);
		int[] results = new int[nums1.length];
		// Find next 
		for (int i = 0; i < nums1.length; i++) {
			for (int j = index[i]; j < nums2.length; j++) {
				if (nums1[i] < nums2[j]){
					results[i] = nums2[j];
					break;
				} else if (j+1 == nums2.length) {
					results[i] = -1;
				} else {
					continue;
				}
			}
		}
		return results;
	}
	
	public int[] getIndex(int[] findNums, int[] nums) {
		int[] index = new int[findNums.length]; // remember the index: the number of findNums in nums
		// find the index
		for (int i = 0; i < findNums.length; i++) {
			for (int j = 0; j < nums.length; j++) {
				if (findNums[i] == nums[j]) {
					index[i] = j;
				}
			}
		}
		return index;
	}
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		NextGreaterElementI ng = new NextGreaterElementI();
		int[] nums1 = {4,2};
		int[] nums2 = {1,2,3,4};
		int[] results = ng.nextGreaterElement(nums1, nums2);
		for (int i : results) {
			System.out.print(i + " ");
		}
	}
}
