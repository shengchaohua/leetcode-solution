public class ReverseInteger {
	public int reverse(int x) {
		boolean isNegative = false;
		if (x < 0) {
			isNegative = true;
			x = -x;
		}
		String xStr = "" + x;
		int len = xStr.length();
		int res = 0;
		for (int i = 0; i < len; i ++) {
			res = res + Character.getNumericValue(xStr.charAt(i)) * (int)Math.pow(10, i);
			int num = (int)(res / Math.pow(10, i));
			if (num != xStr.charAt(i) - 48) { // ×Ö·û×ª»»³ÉÊı×Ö
				return 0;
			}
		}
		return isNegative ? -res : res;
	}
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		ReverseInteger ri = new ReverseInteger();
		int[] nums = {123, -123, 0, 100, -100, 1534236469};
		for (int num : nums) {
			System.out.println(ri.reverse(num));
		}
	}

}
