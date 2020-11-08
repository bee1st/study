package jUniTest.valid;


public class Fibo {

	public static void main(String[] args) {
		Fibo f1 = new Fibo();
		System.out.println(f1.fibo1(0));
		System.out.println(f1.fibo1(1));
		System.out.println(f1.fibo1(2));
		System.out.println(f1.fibo1(3));
		System.out.println(f1.fibo1(5));
		System.out.println(f1.fibo2(20));
	}
	

	public int fibo1(int n) {
		//1. 반복문 이용
		if(n == 0) {
			return 0;
		}
		else if(n == 1) {
			return 1;
		}else {
			int result = 0;
			int a = 0, b = 1;
			for(int i = 2; i <= n; i++) {
				result = a + b;
				a = b;
				b = result;
			}
			return result;
		}
		

	}//fibo1
	
	//2.재귀함수 이용
	public int fibo2(int n) {
		if(n == 1 || n == 2) {
			return 1;
		}
		return fibo2(n - 2) + fibo2(n - 1); //fibo2(0-2) + fibo2(0-1)
	
	}//fibo2
	

}


