
public class SpecialCharacters {
	public boolean isOneBitCharacter(int[] bits) {
		int length = bits.length;
		if (bits[length - 1] == 1){
			return false;
		}
		int numOne = 0;
		for (int i = length - 2; i >= 0; i--) {
			if (bits[i] == 1) {
				numOne++;
				if (numOne == 2) {
					numOne = 0;
				}
			} else {
				break;
			}
		}
		return numOne == 0 ? true : false;
    }
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int[] bits = {1, 0, 0, 0};
		SpecialCharacters sc = new SpecialCharacters();
		System.out.println(sc.isOneBitCharacter(bits));
	}

}
