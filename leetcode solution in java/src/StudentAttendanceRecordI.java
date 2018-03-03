public class StudentAttendanceRecordI {
	public boolean checkRecord(String s) {
		int Anum = 0;
		int continuousLnum = 0;
		for (int i = 0; i < s.length(); i++) {
			if (s.charAt(i) == 'P') {
				continue;
			} else if (s.charAt(i) == 'A') {
				Anum++;
			} else if (s.charAt(i) == 'L') {
				int thisLnum = 1;
				i++; // move to the next index
				for ( ; i < s.length() && s.charAt(i) == 'L'; i++) {
					thisLnum++;
				}
				i--; // move to previous index
				continuousLnum = thisLnum > continuousLnum ? thisLnum : continuousLnum; 
			}
		}
		if (Anum <= 1 && continuousLnum <= 2) {
			return true;
		}
		return false;
	}
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		StudentAttendanceRecordI student = new StudentAttendanceRecordI();
		System.out.println(student.checkRecord("LLLLAALL"));
	}

}
