package BrainJava;

import java.io.PrintWriter;
import java.util.GregorianCalendar;

public class PrintStreamExample1 {

	public static void main(String[] args) {
		System.out.println(" 	*** 성적표 ***		");
		System.out.printf("%3s : %3d %3d %3d %5.1f %n", "이승혜", 92, 87, 98, 91.3f);
		System.out.printf("%3s : %3d %3d %3d %5.1f %n", "최지영", 92, 87, 98, 91.3f);
		System.out.printf("%3s : %3d %3d %3d %5.1f %n", "김미경", 92, 87, 98, 91.3f);
		System.out.printf("작성일자 : %1$tY년 %1$tm월 %1$td일", new GregorianCalendar());

	}

}
