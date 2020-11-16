package BrainJava;

import java.io.EOFException;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.ObjectInputStream;
import java.util.Calendar;
import java.util.GregorianCalendar;

public class ObjectInputExample1 {

	public static void main(String[] args) {
		ObjectInputStream oi = null;
		try {
			oi = new ObjectInputStream(new FileInputStream("output.dat"));
			while(true) {
				GregorianCalendar calendar = (GregorianCalendar) oi.readObject();
				int year = calendar.get(Calendar.YEAR);
				int month = calendar.get(Calendar.MONTH) + 1;
				int date = calendar.get(Calendar.DATE);
				System.out.println(year + "/" + month + "/" + date);
			}
		} 
		catch (FileNotFoundException e) {
			System.out.println("파일이 존재하지 않습니다");
		}
		catch (EOFException e) {
			System.out.println("끝");
		}
		catch (IOException e) {
			System.out.println("파일을 읽을 수 없습니다");
		}
		catch (ClassNotFoundException e) {
			System.out.println("해당 클래스가 존재하지 않습니다.");
		}
		finally {
			try {
				oi.close();
			} catch (Exception e) {
			}
		}
		

	}

}
