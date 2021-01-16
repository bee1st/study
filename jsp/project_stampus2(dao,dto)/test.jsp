<%@ page language="java" contentType="text/html; charset=UTF-8"
	pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core"%>
<jsp:include page="header.jsp" />

<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
<style>
td {
	border: 1px solid #cccccc
}
</style>
</head>
<body>
<section id="fboard_write_form">
<div class="container">
<div class="row">
<div class="fboard_write">
	<h2>자유게시판</h2>
	<form method="post" action="board_write_ok.jsp">
		<table width="600">
			<tr>
				<td>제목</td>
				<td cols="30"><input type="text" name="title"></td>
				<td>사진 첨부</td>
				<td><input type="file" name="fboard_img"></td>
			</tr>
		</table>
		<table width="600">
			<tr>
				<td height="400"><textarea cols="80" rows="30" name="content"></textarea></td>
			</tr>
			<tr>
				<td colspan="2" align="center"><input type="submit" value="글쓰기"></td>
			</tr>
		</table>
	</form>
</div>
</div>
</div>
</section>
</body>
<jsp:include page="footer.jsp" />