package BrainJava;

import java.io.DataOutputStream;
import java.io.FileOutputStream;
import java.io.IOException;

public class DataOutputExample1 {

	public static void main(String[] args) {
		DataOutputStream out = null;
		try {
			out = new DataOutputStream(new FileOutputStream("output1.dat"));
			int arr[] = {0,1,2,3,4,5,6,7,8,9};
			for(int i = 0; i < arr.length; i++) {
				out.writeInt(arr[i]);
			}
		} catch (IOException e) {
			System.out.println("파일을 출력할 수 없습니다.");
		}
		finally {
			try {
				out.close();
			} catch (Exception e) {
			}
		}

	}

}
