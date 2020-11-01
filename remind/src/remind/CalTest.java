package remind;

import java.util.Scanner;

public class CalTest {

	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in); //입력

		String[] Oper = {"+","-","*","/"}; //연산자 배열에 저장

		String input = null;
		int oper = 5, number = 0;
		long num1 = 0l, num2 = 0l; 
		double sum = 0;

		top : while(true){
			switch(number) {
			case 0:
				System.out.println("계산할 두 숫자를 연산자와 함께 입력하세요.(ex : 1+1)");
				break;
			case 1:
				System.out.println("누적 계산할 숫자를 단항식으로 입력하세요.(ex : *2)");
				break;
			} //입력방식 설명, 초기값 0
			
			input = sc.nextLine();
			String[] save = new String[input.length()]; //계산식을 저장할 배열 생성
			
			for(int i = 0; i < input.length() ; i++){
				save[i] = input.substring(i, i+1); //배열에 숫자, 연산자 저장

				if(input.substring(i, i+1).equals(".")){
					System.out.println("[오류] 계산식에 실수가 포함됩니다.");
					continue top;
				} //오류검사
				else if(input.substring(i, i+1).equals(" ")){
					System.out.println("[오류] 계산식에 공백이 포함됩니다.");
					continue top;
				} //오류검사
			}

			for(int i = 0; i < Oper.length ; i++) {
				for(int j = 0; j < input.length() ; j++) {
					if(Oper[i].equals(save[j])){
						oper = i; //연산자 위치 찾기
						if(number == 0)
						num1 = Integer.parseInt(input.substring(0, j)); //배열에 입력값1 저장
						num2 = Integer.parseInt(input.substring(j + 1, input.length())); //배열에 입력값2 저장
					}
				}
			}

			if(oper == 5){
				System.out.println("[오류] 입력양식을 지켜주시기 바랍니다.");
				continue;
			}//각종 오류 검사
			else if(num2 == 0 && oper == 3){
				System.out.println("[주의] 연산 하려는 숫자에 0이 포함됩니다.");
				continue;
			}//0으로 나눠지는경우와 01같은 숫자 검사

			switch(Oper[oper]){
			case "+":
				sum = num1 + num2;
				break;
			case "-":                     
				sum = num1 - num2;
				break;
			case "*":
				sum = num1 * num2;
				break;
			case "/":
				sum = (float)num1 / (float)num2;
				break;
			} //계산

			switch(oper){
			case 3:
				System.out.printf("%d %s %d = %,.1f\n",num1, Oper[oper], num2, sum);
				break;
			default :
				System.out.printf("%d %s %d = %,.0f\n",num1, Oper[oper], num2, sum);
				break;
			} //계산결과 출력

			oper = 5; //리셋 

			next : while(true) {
				System.out.println("처음으로(0) 누적 계산(1) 끝내기(x)");
				input = sc.nextLine();

				switch(input) {
				case "0" :
					number = 0;
					break next; //이전 결과값 0으로 만들기
				case "1" :
					number = 1;
					num1 = (int)sum;
					break next; // 누적 계산
				case "x":
					System.out.printf("계산결과 : %.0f <계산기 종료>",sum);
					break top;
				default :
					System.out.println("입력 오류!");
					break;
				}
			}

		}
		sc.close();

	}

}