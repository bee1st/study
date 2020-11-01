package Polymophism;

public class Hankook extends Tire{
	
	public Hankook() {}
	public Hankook(String Loc, int MaxRot) {
		super(Loc, MaxRot);
	}
	
	@Override
	public boolean roll() {
		++AccRot;
		if(MaxRot > AccRot) {
			System.out.println(Loc + "한국타이어 남은 수명" + (MaxRot - AccRot));
			return true;
		}else {
			System.out.println(Loc + "펑");
			return false;
		}
		
	}

}
