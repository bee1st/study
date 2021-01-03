package BrainJava;

import java.util.Random;

public class ch9_test4 {

	public static void main(String[] args) {
		int arr[] = {1, 2, 3, 4, 5};
		Random random = new Random();
		int index = random.nextInt(5);
		System.out.println(arr[index]);
		

	}

}
