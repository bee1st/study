<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
<style>
	#btn {
		width:150px;
		height:40px;
		border:1px solid #f15672;
		background:pink;
		color:black;
	}
</style>
<script>
	function check(my)
	{
		if(my.pwd.value != my.pw2.value)
			{
			alert("비번이 틀립니다.");
			return false;
			}
		else
			return true;
	}
	function pwd_check(my)
	{
		if(my.pwd.value != my.pw2.value)
		{
			document.getElementById("msg").innerText="비번이 틀립니다.";
			document.getElementById("msg").style.color="red";
			
		}
		else
		{
			document.getElementById("msg").innerText="비번이 일치합니다.";
			document.getelementById("msg").style.color="blue";
		}
	}
</script>
</head>
<body>  <!-- document.폼.title.value  =>  my.name.value -->
	<form method="post" action="write_ok.jsp" onsubmit="return check(this)">
		<table width="600" align="center">
			<tr>
				<td>제목</td>
				<td><input type="text" name="title"></td>
			</tr>
			<tr>
				<td>작성자</td>
				<td><input type="text" name="name"></td>
			</tr>
			<tr>
				<td>내용</td>
				<td><textarea cols="40" rows="5" name="content"></textarea></td>
			</tr>
			<tr>
				<td>비밀번호</td>
				<td><input type="password" name="pwd"></td>
			</tr>
			<tr>
				<td>비밀번호 확인</td>
				<td><input type="password" name="pwd2" onkeyup="pwd_check(this)"></td>
					<span id="msg"></span>
			</tr>
			<tr>
				<td colspan="2" align="center">
					<button id="btn">저장하기</button>
				</td>
			</tr>
		</table>
</form>
</body>
</html>