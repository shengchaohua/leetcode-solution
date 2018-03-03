

import java.util.ArrayList;
import java.util.Iterator;

public class MajorityElement {
	public static int majorityElement(int[] nums) {
		int thisTime = 0;
		int result = 0;
		for (int i = 0; i < nums.length; i++) {
			if (thisTime == 0) {
				result = nums[i];
				thisTime = 1;
			} else {
				if (nums[i] == result) {
					thisTime++;
				} else {
					thisTime--;
				}
			}
		}
		return result;
	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int[] nums = {1,2,2,3,2};
		MajorityElement me = new MajorityElement();
		System.out.println(me.majorityElement(nums));
	}

}
