package BrainJava;

import java.io.DataOutputStream;
import java.io.FileOutputStream;
import java.io.IOException;

public class ch10_test2 {

	public static void main(String[] args) {
		DataOutputStream out = null;
		try {
			out = new DataOutputStream(new FileOutputStream("output.txt"));
			out.writeInt(7);
			out.writeInt(5);
			out.writeDouble(17.5);
		} catch (IOException e) {
			System.out.println("파일로 출력할 수 없습니다");
		}
		finally {
			try {
				out.close();
			}
			catch(Exception e) {

			}
		}

	}

}
