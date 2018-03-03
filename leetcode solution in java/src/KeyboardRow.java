import java.util.ArrayList;

public class KeyboardRow {
	final String[] keyboardChar = { "zxcvbnmZXCVBNM", "asdfghjklASDFGHJKL", "qwertyuiopQWERTYUIOP" };

	public String[] findWords(String[] words) {
		ArrayList<String> results = new ArrayList<>();
		for (String res : words) {
			int currentRow = getRow(res.charAt(0));
			boolean found = true;
			for (char c: res.toCharArray()) {
				if (keyboardChar[currentRow].indexOf(c) == -1) {
					found = false;
					break;
				}
			}
			if (found) {
				results.add(res);
			}
		}
		return results.toArray(new String[results.size()]);
	}

	public int getRow(char c) {
		for (int i = 0; i < keyboardChar.length; i++) {
			if (keyboardChar[i].indexOf(c) > -1) {
				return i;
			}
		}
		return -1;
	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		KeyboardRow kb = new KeyboardRow();
		String[] words = {"Hello", "Alaska", "Dad", "Peace"};
		String[] results = kb.findWords(words);
		for (String string : results) {
			System.out.print( string + " ");
		}
	}

}
