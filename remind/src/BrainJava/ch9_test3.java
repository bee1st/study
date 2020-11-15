package BrainJava;

import java.text.SimpleDateFormat;
import java.util.Calendar;
import java.util.GregorianCalendar;

public class ch9_test3 {

	public static void main(String[] args) {
		GregorianCalendar calendar = new GregorianCalendar();
		calendar.add(Calendar.DATE, 100);
		int year = calendar.get(Calendar.YEAR);
		int month = calendar.get(Calendar.MONTH) + 1;
		int day = calendar.get(Calendar.DAY_OF_MONTH);
		
		System.out.printf(year + "년" + month + "월" + day + "일");
		
		

	}

}
