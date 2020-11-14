package BrainJava;

public class ArrayVatTest2 {

	public static void main(String[] args) {
		int arr[] = {1, 2, 3, 4, 5};
		printArray(arr);
		arr = null;
		printArray(arr);

	}
	static void printArray(int arr[]) {
		if(arr == null) {
			System.out.println("arr가 가리키는 객체는 없습니다");
		} else {
			for(int i : arr) {				
				System.out.println(i);

			}

		}

	}


}
