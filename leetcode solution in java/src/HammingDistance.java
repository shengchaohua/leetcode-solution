public class HammingDistance {
	public int hammingDistance(int x, int y) {
		String xBinary = Integer.toBinaryString(x);
		String yBinary = Integer.toBinaryString(y);
		int xBinarylength = xBinary.length();
		int yBinaryLength = yBinary.length();
		int hammingDist = 0;

		if (yBinaryLength >= xBinarylength) {
			for (int i = 0; i < yBinaryLength - xBinarylength; i++) {
				xBinary = "0" + xBinary;
			}
		} else {
			for (int i = 0; i < xBinarylength - yBinaryLength; i++) {
				yBinary = "0" + yBinary;
			}
		}

		for (int i = 0; i < yBinary.length(); i++) {
			if (xBinary.charAt(i) != yBinary.charAt(i)) {
				hammingDist++;
			} else {
				continue;
			}
		}
		return hammingDist;
	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		HammingDistance hd = new HammingDistance();
		System.out.println(hd.hammingDistance(8, 1));
	}

}
