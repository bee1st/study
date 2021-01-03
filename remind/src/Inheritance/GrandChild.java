package Inheritance;

public class GrandChild extends Parent{
	
	public void g1() {System.out.println("손자호출1");}
	public void g2() {System.out.println("손자호출2");}
	
	@Override
	public void p3() {System.out.println("오버라이드p3");}

}
