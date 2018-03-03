public class PlusOne {
	public int[] plusOne(int[] digits) {
		int n = digits.length;
        for (int i = digits.length - 1; i >= 0; --i) {
            if (digits[i] < 9) {
                digits[i]++;
                return digits;
            }
            digits[i] = 0;
        }
        int[] res = new int[n + 1];
        res[0] = 1;
        return res;
	}
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		PlusOne po = new PlusOne();
		int[] digits = {9,9,9,9};
		int[] result = po.plusOne(digits);
		for (int num: result) {
			System.out.print(num + " ");
		}
	}

}
