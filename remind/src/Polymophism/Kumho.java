package Polymophism;

public class Kumho extends Tire{
	
	public Kumho () {}
	public Kumho(String Loc, int MaxRot) {
		super(Loc, MaxRot);
	}
	
	@Override
	public boolean roll() {
		++AccRot;
		if(MaxRot > AccRot) {
			System.out.println(Loc + "금호타이어 남은 수명 : " + (MaxRot - AccRot));
			return true;
		} else {
			System.out.println(Loc + "펑");
			return false;
		}
	}

}
