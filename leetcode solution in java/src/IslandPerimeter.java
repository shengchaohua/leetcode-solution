import com.sun.org.apache.bcel.internal.generic.LAND;

public class IslandPerimeter {
    public int calPerimeter(int[][] grid) {
    	int lineNum = grid.length;
    	int columnNum = grid[0].length;
    	int[][] perimeter = new int[lineNum][columnNum];
    	int perimeterSum = 0;
    	for (int i = 0; i < lineNum; i++) {
    		for (int j = 0; j < columnNum; j++) {
    			int length = 0;
    			if (grid[i][j] == 0) { // 判断是水
    				length = j < columnNum - 1 && grid[i][j+1] == 1 ? length +1 : length; // 右边是陆地就加一
    				length = i < lineNum - 1 && grid[i+1][j] == 1 ? length +1: length;   // 下边是陆地就加一
    			} else { // 判断是陆地
    				length = j == 0 ? length + 1 : length;
    				length = j == columnNum - 1 ? length + 1 :length;
    				length = i == 0 ? length + 1 :length;   // 陆地在边界上则加一
    				length = i == lineNum - 1 ? length + 1 :length; 
    				length = j < columnNum - 1 && grid[i][j+1] == 0 ? length+1 : length;  // 右边是水加一
    				length = i < lineNum - 1 && grid[i+1][j] == 0 ? length+1 : length;    // 下边是水加一
    			}
    			perimeter[i][j] = length;
    		}
    	}
    	for ( int i = 0; i < perimeter.length; i++) {
    		for (int j = 0; j < perimeter[0].length; j++) {
    			perimeterSum += perimeter[i][j];
    		}
    	}
    	return perimeterSum;
    }
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int[][] grid1 = { 
				{0,1,0,0},
				{1,1,1,0},
				{0,1,0,0},
				{1,1,0,0}};
		int[][] grid2 = {{1,0}};
		IslandPerimeter land = new IslandPerimeter();
		System.out.println(land.calPerimeter(grid1));
		System.out.println(land.calPerimeter(grid2));
	}
}
