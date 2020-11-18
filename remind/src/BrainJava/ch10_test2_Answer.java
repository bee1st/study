package BrainJava;

import java.io.DataInputStream;
import java.io.EOFException;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;

public class ch10_test2_Answer {

	public static void main(String[] args) {
		DataInputStream in = null;
		try {
			in = new DataInputStream(new FileInputStream("output.txt"));
			int num1 = in.readInt();
			int num2 = in.readInt();
			double num3 = in.readDouble();
			System.out.println(num1);
			System.out.println(num2);
			System.out.println(num3);
		}catch (FileNotFoundException e){
			System.out.println("파일이 존재하지 않습니다.");

		}catch (EOFException e) {
			System.out.println("끝");
		}catch (IOException e) {
			System.out.println("파일을 읽을수 없습니다.");
		}
		finally {
			try {
				in.close();
			}
			catch(Exception e) {
			}
		}

	}

}
