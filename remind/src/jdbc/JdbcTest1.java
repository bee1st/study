package jdbc;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLDataException;
import java.sql.SQLException;

public class JdbcTest1 {

	private Connection con;
	private PreparedStatement ps = null;
	private ResultSet rs;
	private String driver = "oracle.jdbc.driver.OracleDriver";
	private String ip = "localhost";
	private String port = "1521";
	private String sid = "xe";	
	private String url = "jdbc:oracle:thin:@" + ip + ":" + port + ":" + sid;
	private String user = "scott";
	private String pass = "tiger";
	private String sql = "";
	private char type = 's';

	public JdbcTest1(String sql, char type) {
		this.sql = sql;
		this.type = type;
		this.db();
	}

	private void db() throws NullPointerException {
		try {
			Class.forName(this.driver);
			System.out.println("driver 연결 성공");

			this.con = DriverManager.getConnection(this.url, this.user, this.pass);
			System.out.println("DB 연결 성공");

			switch(this.type) {
				case 's' :
					this.select();
					break;
				case 'u' :
					this.update();
					break;
				case 'i' :
					this.insert();
					break;
				case 'd' :
					this.delete();
					break;
			}

			if (rs != null)
				rs.close();
			if (ps != null)
				ps.close();
			if (con != null)
				con.close();
		} catch (ClassNotFoundException e) {
			e.printStackTrace();
		} catch (SQLDataException e) {
			e.printStackTrace();
		} catch (SQLException e) {
			e.printStackTrace();
		} catch (Exception e) {
			e.printStackTrace();
		}
	}

	private void select() throws SQLException {
		ps = con.prepareStatement(sql);
		rs = ps.executeQuery();

		while(rs.next()) {
			System.out.printf("%d, %s, %s, %d, %s, %d, %d, %d\n", rs.getInt("empno"), rs.getString("ename"), rs.getString("job"), rs.getInt("mgr"), rs.getDate("hiredate"), rs.getInt("sal"), rs.getInt("comm"), rs.getInt("deptno"));
		}
	}

	private void update() throws SQLException {
		ps = con.prepareStatement(sql);
		int cnt = ps.executeUpdate();

		System.out.printf("%d 건 update\n", cnt);
	}

	private void insert() throws SQLException {
		ps = con.prepareStatement(sql);
		ps.setInt(1, 8080);
		ps.setString(2, "둘리");
		ps.setString(3, "백수");
		ps.setInt(4, 8000);
		ps.setInt(5, 30);
		int cnt = ps.executeUpdate();

		System.out.printf("%d 건 insert\n", cnt);
	}

	private void delete() throws SQLException {
		ps = con.prepareStatement(sql);
		ps.setInt(1, 8080);
		ps.setInt(2, 9999);

		int cnt = ps.executeUpdate();

		System.out.printf("%d 건 delete\n", cnt);
	}

	public static void main(String[] args) {
		try {
			String sql = "select empno, ename, job, mgr, hiredate, nvl(sal, 9) sal, nvl(comm, 0) comm, deptno from emp";
			char type = 's';
			System.out.println("-------------------------------------------------");
			JdbcTest1 db = new JdbcTest1(sql, type);

			sql = "update emp set comm = 90000";
			type = 'u';
			System.out.println("-------------------------------------------------");
			db = new JdbcTest1(sql, type);

			sql = "select empno, ename, job, mgr, hiredate, nvl(sal, 9) sal, nvl(comm, 0) comm, deptno from emp";
			type = 's';
			System.out.println("-------------------------------------------------");
			db = new JdbcTest1(sql, type);

			sql = "insert into emp(empno, ename, job, sal, deptno) values (?, ?, ?, ?, ?)";
			type = 'i';
			System.out.println("-------------------------------------------------");
			db = new JdbcTest1(sql, type);

			sql = "select empno, ename, job, mgr, hiredate, nvl(sal, 9) sal, nvl(comm, 0) comm, deptno from emp where empno = 8080";
			type = 's';
			System.out.println("-------------------------------------------------");
			db = new JdbcTest1(sql, type);

			sql = "delete from emp where empno in (?, ?)";
			type = 'd';
			System.out.println("-------------------------------------------------");
			db = new JdbcTest1(sql, type);
		} catch (NullPointerException e) {
			e.printStackTrace();
		} catch (Exception e) {
			e.printStackTrace();
		}
	}

}