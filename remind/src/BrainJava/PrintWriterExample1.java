package BrainJava;

import java.io.IOException;
import java.io.PrintWriter;
import java.util.GregorianCalendar;

public class PrintWriterExample1 {

	public static void main(String[] args) {
		PrintWriter writer = null;
		try {
			writer = new PrintWriter("output.txt");
			writer.println(" 	*** 성적표 ***		");
			writer.printf("%3s : %3d %3d %3d %5.1f %n", "이승혜", 92, 87, 98, 91.3f);
			writer.printf("%3s : %3d %3d %3d %5.1f %n", "최지영", 92, 87, 98, 91.3f);
			writer.printf("%3s : %3d %3d %3d %5.1f %n", "김미경", 92, 87, 98, 91.3f);
			writer.printf("작성일자 : %1$tY년 %1$tm월 %1$td일", new GregorianCalendar());
		} catch (IOException e) {
			System.out.println("파일로 출력할 수 없습니다.");
		} finally {
			try {
				writer.close();
			}
			catch(Exception e) {

			}
		}


	}

}
