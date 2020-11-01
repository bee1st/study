이름, 전번, 아이디, 비번, 나이, 이메일, 닉네임

create table 테이블명(
	컬럼명 타입(크기),
	컬럼명 타입(크기) [제약조건],
	컬럼명 타입(크기) [constraint 제약조건명 제약조건],
	컬럼명 타입(크기) [constraint 제약조건명 제약조건 default 기본값]
	);

--회원테이블
create table member(
	mno 	number(5) constraint member_mno_pk primary key,
	mname 	varchar2(30),
	mid varchar2(20), 
	mpwd varchar2(20),
	mdate date default sysdate
	);


--insert into member values(mno, mname, mid, mpwd, mdate);
insert into member 
values(eno_seq.nextval, '홍1', 'hid', '1234', sysdate);
insert into member 
values(eno_seq.nextval, '홍2', 'aid', '1234', sysdate);
insert into member 
values(eno_seq.nextval, '홍3', 'bid', '1234', sysdate);



update member
set mname = '홍new1', mpwd = '111'
where mno = 8002;

delete from member where mno = 8002;

--회원테이블 삭제
drop table member;

select mno, mname, mid, mpwd, mdate from member;

