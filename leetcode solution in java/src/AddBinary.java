public class AddBinary {

	public String addBinary(String a, String b) {
		StringBuilder builder = new StringBuilder();
		int jinwei = 0;
		for (int i = a.length() - 1, j = b.length() - 1; i >= 0 || j >= 0;) {
			int aInt = i >= 0 ? a.charAt(i--) - '0' : 0;
			int bInt = j >= 0 ? b.charAt(j--) - '0' : 0;
			int bitSum = aInt + bInt + jinwei;
			if (bitSum == 0 || bitSum == 1) {
				builder.append(bitSum);
				jinwei = 0;
			} else {
				builder.append(bitSum % 2);
				jinwei = 1;
			}
		}
		if (jinwei == 1) {
			builder.append("1");
		}
		return builder.reverse().toString();
	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		AddBinary ab = new AddBinary();
		System.out.println(ab.addBinary("111101", "1111"));
	}

}
