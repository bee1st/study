package jUniTest.ValidPW;

public class ValidPW {
	private String pwd;
	private boolean isValid;
	
	public boolean isValid(String pwd) {
		boolean result = false;
		int letterCnt = 0; //문자열
		int digitCnt = 0; //숫자
		
		for(int i = 0; i < pwd.length(); i++) { //글자수 길이만큼 반복
			char ch = pwd.charAt(i); //한글자씩 추출
			
			if(Character.isLetter(ch)) { //문자일때 1씩 증가
				letterCnt++; //문자 리턴
			}else if(Character.isDigit(ch)) { //숫자일때 1씩 증가
				digitCnt++; //숫자 리턴
			}
		}
		//유효성검사 .. 8자리 이상 + 문자 숫자 각 하나이상 
		if((pwd.length() >= 8) && letterCnt >= 1 && digitCnt >= 1) {
			result = true;
		}
		
		return result;
	}
	

}
