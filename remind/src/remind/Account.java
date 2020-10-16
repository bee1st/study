package remind;

public class Account {
	private String bunho;
	private String name;
	private int jango;
	
	public Account(String bunho, String name, int jango) {
		this.bunho = bunho;
		this.name = name;
		this.jango = jango;
	}
	
	
	public void setBunho(String bunho) {
		this.bunho = bunho;
	}
	public void setName(String name) {
		this.name = name;
	}
	public void setJango(int jango) {
		this.jango = jango;
	}
	
	public String getBunho() {
		return this.bunho;
	}
	
	public String getName() {
		return this.name;
	}
		
	public int getJango() {
		return this.jango;
	}
	
	
}
