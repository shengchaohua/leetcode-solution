public class ProductofArrayExceptSelf {
	public int[] productExceptSelf(int[] nums) {
		int length = nums.length;
		int[] leftProduct = new int[length];
		int[] rightProduct = new int[length];
		leftProduct[0] = 1;
		rightProduct[length-1] = 1;
		int[] result = new int[length];
		
		for (int i = 1; i < length; i++) {
			leftProduct[i] = nums[i-1] * leftProduct[i-1];
			rightProduct[length-1-i] = nums[length-i] * rightProduct[length-i];
		}
		
		for (int i = 0; i < length; i++) {
			int product = leftProduct[i] * rightProduct[i];
			result[i] = product;
		}
		return result;
	}
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		ProductofArrayExceptSelf product = new ProductofArrayExceptSelf();
		int[] nums = {1, 2, 3, 4};
		int[] res = product.productExceptSelf(nums);
		for (int num : res) {
			System.out.print(num + " ");
		}
	}
}
