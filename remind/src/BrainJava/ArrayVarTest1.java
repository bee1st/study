package BrainJava;

public class ArrayVarTest1 {

	public static void main(String[] args) {
		int arr1[] = {1, 2, 3};
		int arr2[] = arr1;
		
		for(int i = 0; i < arr2.length; i++) {
			System.out.println(arr2[i]); //1,2,3
		}
		arr2[1] = 7;
		for(int i = 0; i < arr1.length; i++) {
			System.out.println(arr1[i]); //1,7,3
		}

	}

}
