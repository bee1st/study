package remind;

public class arr {
	public static void main(String[] args) {
		int[] a = new int[10];
		int[] b = new int[10];
		for(int i = 0; i < a.length;i++) {
			a[i] = (int)(Math.random()*a.length);
			System.out.print(a[i]);
		}
		
		System.out.println();
		for(int i = 0; i < b.length; i++) {
			b[a[i]]++;
		}
		for(int i = 0; i < a.length; i++) {
			System.out.println(i + "의 갯수 = " + b[i]);
		}
	}


}
