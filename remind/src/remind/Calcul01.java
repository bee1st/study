package Study;

public class Calcul01 {
	
	void  plus(long x, long y) {
		long result = 0;
		result = x + y;
		System.out.println(result);
	}
		
	int  plus(int x, int y) {
		int result = 0;
		result = x + y;
		return result;	
		
	}
		
	void a() {
		System.out.println("a()");
		b(); 
	}
	
	void b() {
		System.out.println("b()");
	}
		
	void powerOn () {
		System.out.println("powerOn()호출성공-전원을 켭니다");
	}
		
	void powerOff () {
		System.out.println("powerOff()호출성공-전원을 켭니다");
	}
		
	int add(int x, int y) {
		
		int result = 0;
		result = x + y;
		System.out.println(result);
		return result;
	}
		
	double add(double x, double y) {
		
		double result = 0;
		result = x + y;
		System.out.println(result);
		return result;
	}
	
	double divide(double x, double y) {
		
		double result = 0.0;
		result = x/y;
		System.out.println(result);
		return result;
	}
	
	double divide(int x, double y) {
		
		double result = 0.0;
		result = x/y;
		System.out.println(result);
		return result;
	}
	
	double divide(double y, int x) {
		System.out.println("0.0");
		return 0.0;
	}
	
}
