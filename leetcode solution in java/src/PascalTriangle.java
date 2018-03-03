import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class PascalTriangle {
	public List<List<Integer>> generate(int numRows) {
		List<List<Integer>> result = new ArrayList<>();
		if (numRows == 0) {
			return result;
		}
		result.add(Arrays.asList(1));
		if (numRows == 1) {
			return result;
		}
		
		for (int i = 0; i < numRows - 1; i++) {
			List<Integer> theResult = new ArrayList<>();
			for (int j = 0; j < result.get(i).size(); j++) {
				if (j == 0) {
					theResult.add(1);
				} else {
					theResult.add(result.get(i).get(j) + result.get(i).get(j - 1));
				}
			}
			theResult.add(1);
			result.add(theResult);
		}
		return result;
	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		PascalTriangle pascal = new PascalTriangle();
		System.out.println(pascal.generate(5));
	}

}
