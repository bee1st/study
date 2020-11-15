package BrainJava;

public class InheritanceExample4 {

	public static void main(String[] args) {
		BonusPointAccount obj = new BonusPointAccount("333-33-33333333", "콩쥐", 0, 0);
		obj.depoist(100000); // depoist 경로가 account 와 bonuspointaccount 가 있는데 bonus쪽으로 설정해야 값이 나온다
		System.out.println("잔액 : " + obj.balance);
		System.out.println("포인트 : " + obj.bonusPoint);

	}

}
