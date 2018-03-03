import java.util.HashSet;
import java.util.Set;

public class DistributeCandies {
	public int distributeCandies(int[] candies) {
        Set<Integer> set = new HashSet<>();
        for (int i = 0; i < candies.length; i++) {
			set.add(candies[i]);
		}
        if ( set.size() > candies.length/2 ) {
			return candies.length/2;
		} else {
			return set.size();
		}
    }
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int[] candies = new int[]{1,1,2,2,3,3,4,4,4,4};
		DistributeCandies dCandies = new DistributeCandies();
		System.out.println( dCandies.distributeCandies(candies) );
	}

}
