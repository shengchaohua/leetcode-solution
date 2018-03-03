public class ReverseStringII {
	public String reverseStr(String s, int k) {
		StringBuilder result = new StringBuilder();
		char[] sArray = s.toCharArray();
		int len = sArray.length;
		for (int i = 0; i < sArray.length; i += k) {
			if (i/k % 2 == 0) {
				int start = len - 1 -i < k - 1 ? len - 1 - i : k - 1; 
				for (int counter = start; counter >= 0 ; counter--) {
					result.append(sArray[i + counter]);
				}
			} else {
				int end = len - 1 - i < k - 1? len - 1 -i : k - 1;
				for (int counter = 0 ; counter <= end; counter++) {
					result.append(sArray[i + counter]);
				}
			}
		}
		return result.toString();
	}


	public static void main(String[] args) {
		// TODO Auto-generated method stub
		String s = "abcdefghij";
		ReverseStringII rs = new ReverseStringII();
		System.out.println(rs.reverseStr(s, 2));
	}
}
