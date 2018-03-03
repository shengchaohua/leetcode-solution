

public class DetectCapital {
	public boolean detect(String word) {
		if (word == null)
			return false;
		if (word.length() <= 1)
			return true;
		boolean firstFlag = Character.isUpperCase(word.charAt(0));
		boolean secondFlag = Character.isUpperCase(word.charAt(1));
		if (firstFlag && secondFlag) {
			int i = 2;
			for (; i < word.length(); i++) {
				if (Character.isLowerCase(word.charAt(i))) {
					return false;
				}
			}
			if (i == word.length()) {
				return true;
			}
		} else if (firstFlag == false && secondFlag == true) {
			return false;
		} else {
			int i = 2;
			for (; i < word.length(); i++) {
				if (Character.isUpperCase(word.charAt(i))) {
					return false;
				}
			}
			if (i == word.length()) {
				return true;
			}
		}
		return false;
	}
	
	public static boolean detectBetter(String word) {
		int numUpper = 0;
        for (int i=0;i<word.length();i++)
            if (Character.isUpperCase(word.charAt(i))) numUpper++;
        if (numUpper == 1) return Character.isUpperCase(word.charAt(0));
        return numUpper == 0 || numUpper == word.length();
	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		DetectCapital dc = new DetectCapital();
		System.out.println(dc.detect("Ss"));
	}

}
