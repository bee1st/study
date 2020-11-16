package BrainJava;

import java.io.FileOutputStream;
import java.io.IOException;
import java.io.ObjectOutputStream;
import java.util.GregorianCalendar;

public class ObjectOutputExample1 {

	public static void main(String[] args) {
		ObjectOutputStream out = null;
		try {
			out = new ObjectOutputStream(new FileOutputStream("output.dat"));
			out.writeObject(new GregorianCalendar(2020, 0, 14));
			out.writeObject(new GregorianCalendar(2020, 0, 15));
			out.writeObject(new GregorianCalendar(2020, 0, 16));
		} 
		catch (IOException ioe) {
			System.out.println("파일을 출력 할 수 없습니다.");
		}
		finally {
			try {
				out.close();
			} catch (Exception e) {
			}
		}

	}

}
