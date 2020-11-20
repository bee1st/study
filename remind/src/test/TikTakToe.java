package test;

import java.util.Scanner;

/* 틱택토
 * 1. 이차원 배열을 이용
 * 2. do while문으로 컴퓨터 첫 수는 math함수로 랜덤놓기
 * 3. x축 2개 같거나 y축 2개 같으면 2개 같은 축에 넣기 (0,0) (0,1) -> (0,2)에 넣게끔 if문
 * 
 */

public class TikTakToe {

	public static void main(String[] args) {
		//게임판
		int[][] board = new int[3][3];
		int x, y;

		//사용자 입력
		Scanner sc = new Scanner(System.in);


		//게임판 초기화
		for(int i = 0; i < 3; i++) {
			for(int j = 0; j < 3; j++)
				board[i][j] = ' ';			
		}


		for (int i = 0; i < 3; i++) {
			for (int j = 0; j < 3; j++) {
				System.out.println(board[i][j] + "\t");
			}
			System.out.println();
		}
	}
}
