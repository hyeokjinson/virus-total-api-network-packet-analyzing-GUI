# Virus Total API 활용한 네트워크 패킷 분석 GUI 프로그램
This is a python script for importing data to MySql database using .csv, .xls, or xlsx. It requires MySQLdb interface for python and xlrd package for reading data and formatting information from older Excel files.

2019년도 창의적공학설계
최종보고서
(설계 주제명: Destination IP 덤프를 통한 VIRUSTOTAL 자동 분석)







2019년 6월 13일

	목차



1	설계목적	
1.1	설계의 주제	
1.2	기존 유사제품의 기능 설명 및 분석	
1.3	설계의 개요	
2	기능적 요구사항	
2.1	기능별 특징	
2.2	외부 인터페이스 요구사항	
2.2.1	사용자 인터페이스	
2.2.2	소프트웨어 인터페이스	
3	설계내용	
3.1	전체 시스템구성	
3.2	상위 설계	
3.3	상세 설계	
4	구현 결과	
4.1      개발 환경	
4.2	동작 시스템 환경	
4.3	구현 결과	
4.4.2	기능별 시험 결과.	
5     프로그램 기대효과	








1. 설계 목적 
1.1설계의 주제

- 목적지 IP 값을 네트워크 패킷을 덤프하여 가져와 virus total api로 보내 유해한 정보나 파일을 가져오는지 확인해주는 프로그램

1.2	기존 유사제품의 기능 설명 및 분석

* 아이싱어

아이싱어(Icinga)는 사용자가 네트워크, 서버, 애플리케이션을 안전하고 신뢰할 수 있는 방식으로 모니터링할 수 있게 해주는 인프라 및 서비스 모니터링 툴을 제공한다.
아이싱어는 호스트와 서비스를 확인하고 사용자에게 상태를 알리는 오픈소스 시스템이다. 아이싱어는 나기오스(Nagios)에서 나왔지만 나기오스보다 개발주기가 더 민첩한 것처럼 보인다.

1.3	설계의 개요

- 관리자 모드로 로그인하여 로그인에 성공하면 메인 GUI를 볼 수 있다.
사용자의 네트워크 패킷을 가져와 목적지 ip 주소를 가져와 위험사이트에 접속한 이력이 있는지 확인한다.
- 네트워크가 패킷(목적지 IP) 을 보내는 것을 실시간으로 확인 한다.




2. 기능적 요구사항 

2.1	기능별 특징

가. 네트워크 연결 실시간 확인 기능
- 네트워크가 패킷을 보내는 것을 실시간으로 확인 한다.
(실시간으로 보내어지는 목적지 IP값을 txt 파일로 저장)

나. 부여된 ID와 password를 입력시 프로그램 실행 기능
-개발자가 정의한 ID,password를 입력하여 로그인 시 자동으로 프로그램을 실행 시켜준다.

다. 목적지 IP정보를 가져와 VIRUSTOTAL API에 보내는 기능

라. 들어가는 홈페이지 URL을 VIRUSTOTAL에 보내어 취약점이 있거나 바이러스가 있는지 확인 후 결과 값 시각화.(위험한 ip 접속시 결과값 ip보여주기)

마.네트워크 트래픽 그래프 기능
네트워크의 실시간 다운로드 초당 다운로드 속도를 그래프로 보여준다. 

2.2	외부 인터페이스 요구사항

2.2.1사용자 인터페이스(GUI)
입력: 사용자가 버튼 클릭:사용자가 버튼을 클릭하여 네트워크 패킷을 덤프할 수 있게 해준다.
출력:시스템이 사용자가 필요로하는 목적지 IP 결과를 표시
2.2.2	소프트웨어 인터페이스
실행하기 위한 환경:python3.7,pyqt5 Package





3	설계내용
3.1	전체 시스템구성

3.1.1 전체적인 시스템 흐름도

![image01](https://user-images.githubusercontent.com/13067686/90976141-8562cb00-e575-11ea-9717-def933a8e07e.png)


				<전체 시스템 흐름도>

1.외부 들어오는 IP를 덤프하여 log.txt에 저장
2.log.txt를 출력
3.virustotal API에서 log.txt 읽기
4.log.txt값들을 15초에 하나씩 VT Server에보내기 
5.VT Server에서 온 결과값들을 result.csv에 저장
6. result.csv를 읽어서 결과값들 출력

기능 요약
 로그기록을 가져와 모든 사용자가 어느 위험ip경로로 가는지 프로그램을 통해  ip를 자동으로 알 수 있고 인터페이스 사용이 쉽고 명령 없이 자동으로 VIRUS TOTAL API에 분석해주게 한다




3.2	상위 설계
3.2.1 내부 시스템별 모듈 설계

-실시간 목적지 IP주소 VIEW
●Dump버튼 클릭
-덤프버튼 클릭시  목적지 경로 ip를 가져온다->Destination ip view창에 출력
-destination ip 자동 덤프후 log.txt에저장  
●Destination view
-Dump버튼을 클릭시 log.txt에 저장된 내용을 출력 기능 
-Network Traffic view graph
●Graph Button
-Graph Button 클릭시 네트워크 트래픽 그래프 띄워주기
-VIRUSTOTAL Result view
●Result Button
Result버튼 클릭 시 바이러스 토탈 과 연동하여 Destination IP 가 저장된 log.txt를 읽어서 보내고 결과값을 result.csv에 저장
●View Button
View Button 클릭시 유해한 ip인지 확인 한 결과값이 저장된 result.csv를 읽어들여 result view 창에 출력
●result view
바이러스 토탈 결과값이 저장된 result.csv파일을 읽어서 출력 


3.2.2전체적인 UI 설계

	                   <로그인 창 기본틀 GUI>



	                   <로그인 후 실행시 GUI 화면>
	         
3.2.3로그 기록 저장 파일 
-log.txt 저장 내용: 목적지 IP
			<log.txt 저장 내용>




-VIRUS TOTAL API Result 값 저장 파일
파일형식:result.csv
저장내용
 ●스캔 날짜 및 시간
●목적지 IP
●발견된 악성코드 갯수
●총 스캔한 회사
●상세정보 링크주소
-result.csv 출력내용


3.3	상세 설계
3.3.1클래스 다이어그램


-관리자 계정 로그인 GUI
구현언어:python3.7,pyqt5
구현내용:ID,PW일치시 전체 GUI프로그램으로 이동
-네트워크 패킷 캡쳐 덤프 GUI
구현 언어:python3.7,pyqt5
구현내용:·Destination IP 덤프후 IP값을 가져와 log.txt파일에 써서 저장
	   ·log.txt에 저장된 IP값을 출력하여 보여준다.
그래프기능:네트워크 트래픽을 초당 다운 속도를 기준으로 하여 그래프를 그려준다.(1sec 당 00MB)
virus total api:log.txt에 저장된 IP주소 값을 읽어서 바이러스 토탈 서버에 전송하여 유해한 IP와 통신을 했는지 결과값을 result.csv에 저장
-버튼클릭시 결과값이 저장되어 있는 result.csv을 읽어서 출력

3.4기능별 설계
3.4.1로그인 폼 알고리즘


1.setting ID& Password(ID:admin &password:admin)
2. 로그인버튼:if admin ID & Password correct ->connect GUI

3.4.2 GUI 기능별 알고리즘

●실시간 목적지 IP주소 View

1.덤프 버튼 클릭
2.실시간 목적지 경로 ip를 가져와서 log.txt파일에 저장
3.저장된 log.txt 파일을 GUI view에 순서대로 출력한다.




●Network Traffic view Graph



1.네트워크 트래픽 그래프 보기 버튼을 클릭
2.클릭 시 실시간 네트워크 트래픽 그래프와 초당 속도를 기준으로한 그래프를 띄워준다.
●VirusTotal Result view
	<log.txt값 보내기>		<VTAPI결과값 result.csv 파일 읽기>

1.덤프파일을 눌러 실시간으로 실행되어 목적지 IP가 저장되는 log.txt 파일을 가져와서 결과 보내기 버튼 클릭 시 바이러스 토탈 API를 통해 IP 값들을 보내준다.(15초에 IP 1개)
2. 나온 결과값들을 result.csv파일에 저장해 준다.
3.결과값 보기 버튼 클릭 시 result.csv파일을 읽어 결과값들을 출력해 준다.



4.구현 및 테스트
4.1 개발 환경
- Python3.7, qt designer
4.2 동작 시스템 환경
- Windows 10
4.3 구현결과
- Login 화면

- 메인 화면







-그래프 화면



그래프 버튼 클릭 시 네트워크 트래픽 초당 다운로드 속도를 보여주는 그래프를 보여준다

4.4 기능별 시험 결과
1. DUMP버튼 실행

- Dump버튼을 클릭시 네트워크 패킷 덤프한 내용(목적지 IP주소를log.txt에 저장)된 내용을 출력






2. Graph버튼 실행

- Graph Button 클릭시 네트워크 트래픽 그래프 띄워주기

3. Result버튼 실행

- Result버튼 클릭 시 바이러스 토탈과 연동하여 Destination IP 가 저장된 log.txt를 읽어서 보내고 결과값을 result.csv에 저장




4.VIRUS TOTAL 결과값 출력


- View Button 클릭시 유해한 ip인지 확인 한 결과값이 저장된 result.csv를 읽어들여 result view 창에 출력




















5. 프로그램 기대 효과



위 프로그램 사용시 얻는 기대효과
프로그램 실행시 자동으로 목적지 IP를 덤프하여 분석하여준다.
한 눈에 네트워크 실시간 그래프와 그와 동시에 네트워크 패킷과 위험 ip를 사용자가 버튼 클릭으로 알 수 있다.



