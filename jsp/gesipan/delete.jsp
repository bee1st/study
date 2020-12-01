<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@page import="java.sql.*" %>    
<%
	// DB 연결
	Class.forName("com.mysql.jdbc.Driver");
	String db="jdbc:mysql://localhost:3306/pkc";
	String userid="root";
	String pw="1234";
	Connection conn=DriverManager.getConnection(db,userid,pw);
	
	//request 값 가져오기
	String pwd = request.getParameter("pwd");
	String id = request.getParameter("id");
	
	//DB에 있는 비밀번호 가져오기
		//쿼리생성
		String sql = "select pwd from gesipan where id =" +id;
		//심부름꾼
		Statement stmt = conn.createStatement();
		//실행 후 ResultSet
		ResultSet rs = stmt.executeQuery(sql);
		rs.next();
	if(pwd.equals(rs.getString("pwd")))
	{
	//쿼리생성
	sql = "delete from gesipan where id =" + id;
	//심부름꾼 생성
	stmt = conn.createStatement();
	//쿼리 실행
	stmt.executeUpdate(sql);
	//이동
	response.sendRedirect("list.jsp");
	}
	else 
	{
	response.sendRedirect("content.jsp?id=" + id + "&chk=1");
	}
%>
<%
	stmt.close();
	conn.close();
%>
	