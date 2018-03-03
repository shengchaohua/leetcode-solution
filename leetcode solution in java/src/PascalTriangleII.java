import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class PascalTriangleII {
	public List<Integer> getRow(int rowIndex) {
		List<Integer> list = Arrays.asList(1);
		if (rowIndex == 0) {
			return list;
		}
		for (int i = 0; i < rowIndex; i++) {
			List<Integer> result = new ArrayList<>();
			for (int j = 0; j < list.size(); j++) {
				if (j == 0) {
					result.add(1);
				} else {
					result.add(list.get(j) + list.get(j - 1));
				}
			}
			result.add(1);
			list = result;
		}
		return list;
	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		PascalTriangleII pascal = new PascalTriangleII();
		for (int i = 0; i <= 10; i++) {
			System.out.println(pascal.getRow(i));
		}
	}
}
