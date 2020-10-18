package self.jdbc.ex1;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;

public class Program {

	public static void main(String[] args) throws ClassNotFoundException, SQLException {
		
		String url = "jdbc:oracle:thin:@localhost:1521/xe";
		String sql1 = "SELECT * FROM NOTICE";
		
		Class.forName("oracle.jdbc.driver.OracleDriver"); //드라이버 로드
		Connection con = DriverManager.getConnection(url, "happy", "day"); //연결 얻기
		Statement st = con.createStatement(); //statement 객체 생성
		ResultSet rs = st.executeQuery(sql1); //객체의 결과를 ResultSet이나 int에 받기
		
		if(rs.next()) {
		String title = rs.getString("TITLE");
		System.out.println(title);
		}
		
		rs.close();
		st.close();
		con.close();

	
	}


}
