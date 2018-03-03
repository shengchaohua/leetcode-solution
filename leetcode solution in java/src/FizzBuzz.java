import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;

public class FizzBuzz {
	public List<String> fizzBuzz(int n) {
		List<String> list = new ArrayList<>();
		for (int i = 1; i <= n; i++) {
			if (i % 3 == 0 && i % 15 !=0) {
				list.add("Fizz");
			} else if (i % 5 == 0 && i % 15 != 0) {
				list.add("Buzz");
			} else if (i % 15 == 0) {
			    list.add("FizzBuzz");
			} else {
				list.add("" + i);
			}
		}
		return list;
	}
	
	public static void main(String[] args) {
		FizzBuzz fb = new FizzBuzz();
		List<String> list = fb.fizzBuzz(15);
		Iterator<String> iterator = list.iterator();
		while (iterator.hasNext()) {
			System.out.println(iterator.next());
		}
	}
}
