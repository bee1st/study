package Polymophism;

public class Tire {
	
	public int MaxRot;
	public int AccRot;
	public String Loc;
	
	public Tire() {}
	public Tire(String Loc, int MaxRot){
		this.Loc = Loc;
		this.MaxRot = MaxRot;
		
	}
	
	public boolean roll() {
		++AccRot;
		if(MaxRot > AccRot) {
		System.out.println(Loc + "타이어 수명은 : " + (MaxRot - AccRot));
		return true;
		}else {
			System.out.println("** " + Loc + "펑" + " **");
			return false;
		}
	}

}
