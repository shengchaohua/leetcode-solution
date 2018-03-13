import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class DegreeOfAnArray {
	public int findShortestSubArray(int[] nums) {
        // 建立map, 统计每个数字的频率
		Map<Integer, Integer> numFreq = new HashMap<>();
        for (int num : nums) {
        	numFreq.put(num, numFreq.getOrDefault(num, 0)+1);
        }
        
        // 寻找频率最大的所有数字
        int maxFreq = 0;
        List<Integer> list = new ArrayList<>();
        for (Map.Entry<Integer, Integer> item : numFreq.entrySet()) {
        	if (item.getValue() > maxFreq) {
        		list.clear();
        		list.add(item.getKey());
        		maxFreq = item.getValue();
        	} else if (item.getValue() == maxFreq) {
        		list.add(item.getKey());
        	}
        }
        
        // 计算频率最大的数字的距离，取最小
        int smallertLen = Integer.MAX_VALUE;
        for (int i = 0; i < list.size(); i++) {
        	int mostFreqNum = list.get(i); 
	        int low = 0;
	    	int high = nums.length-1;
	    	
	        while (nums[low] != mostFreqNum)
	        	low++;
	        while (nums[high] != mostFreqNum)
	        	high--;
	        int len = high-low+1;
	        smallertLen =  len < smallertLen ? len : smallertLen;
        }
        return smallertLen;
    }
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int[] nums = {1,2,2,3,1,4,2};
		DegreeOfAnArray de = new DegreeOfAnArray();
		System.out.println(de.findShortestSubArray(nums));
	}

}
