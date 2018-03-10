
public class SpecialCharacters {
	public boolean isOneBitCharacter(int[] bits) {
		int oneNum = 0;
		for (int i = bits.length - 2; i >= 0; i--) {
			if (bits[i] == 1) {
				oneNum++;
				oneNum %= 2;
			} else {
				break;
			}
		}
		return oneNum == 0;
    }
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int[] bits = {1, 0, 0, 0};
		SpecialCharacters sc = new SpecialCharacters();
		System.out.println(sc.isOneBitCharacter(bits));
	}

}
