package BrainJava;

public class ThreeArrays {
	static int arr1[];
	static {
		arr1 = new int[10];
		for(int i = 0; i < arr1.length; i++) {
			arr1[i] = i + 1;
		}
	}
	static int arr2[];
	static {
		arr2 = new int[10];
		for(int i = 0; i < arr2.length; i++) {
			arr2[i] = (i + 1) * 10000;
		}
	}
	static int arr3[];
	static {
		arr3 = new int[10];
		for(int i = 0; i < arr3.length; i++) {
			arr3[i] = arr1[i] + arr2[i];
		}
	}

}
