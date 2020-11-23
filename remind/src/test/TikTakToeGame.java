package test;

import java.util.Scanner;

public class TikTakToeGame {
	
	
	void start() {
		Board board = new Board();
		Order order = new Order();
		Scanner sc = new Scanner(System.in);
		
		board.initialize();
		order.initialize();
		
		while (true) {
			int currentOrder = order.getCurrentOrder();
			System.out.print(currentOrder + "번 입력 (0~9) : ");
			int a = sc.nextInt();
			int b = sc.nextInt();
			if(board.isEmpty(a, b)) {
				if (currentOrder == 1) {
					board.setPoint(a,  b, "[0]");
				} else if(currentOrder == 2) {
					board.setPoint(a, b, "[X]");
				}
				if (board.checkWinningGame(a, b) != 0) {
					System.out.println("User " + currentOrder + " 승리");
					break;
				}
				order.next();
			} else {
				System.out.println("입력 불가");
			}

			board.print();
		}
	}
}
