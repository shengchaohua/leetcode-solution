public class ReshapeTheMatrix {
	public int[][] matrixReshape(int[][] nums, int r, int c) {
		int[][] results = new int[r][c];
		int numLength = 0;
		for (int i = 0; i < nums.length; i++) {
				numLength = numLength + nums[i].length;
		}
		if ( numLength != r*c ){
			return nums;
		} else {
			//core code
			int row = 0;//row of the array nums
			int column = 0;//column of the array nums
			for (int i = 0; i < r; i++) {
				for (int j =0; j < c; j++) {
					results[i][j] = nums[row][column];
					column++;
					if ( column >= nums[row].length ) {
						row++;
						column = 0;
					}
				}
			}
			return results;
		}
	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		ReshapeTheMatrix rtm = new ReshapeTheMatrix();
		int[][] nums = new int[][]{{1,2,3},{2,3,4}};
		int[][] results = rtm.matrixReshape(nums, 3, 2);
		for (int i = 0; i < results.length; i++) {
			for (int j = 0; j < results[i].length; j++) {
				System.out.print( results[i][j] + " ");
			}
			System.out.println();
		}
	}

}
