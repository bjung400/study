if has("syntax")
	syntax on
endif "문법 하이라이트
set nu "줄번호
set hlsearch "명령모드에서 ?,/로 문자열 검색시 하이라이트
set autoindent "자동들여쓰기 
set cindent 
set ts=4 "문서의 \t 값을 출력시 몇개의 스페이스로 보여줄지
set sts=4 "tab 눌렀을때 스페이스 개수
set shiftwidth=4 "자동 들여쓰기 할때 스페이스 개수
set laststatus=2 " 마지막창에 status출력
set showmatch "괄호 하이라이트
set smartcase "대문자 검색시 대문자만검색(\c하면 대소문자무시)
"set ignorecase "대소문자 무시하고 검색
set smarttab "ts, sts, sw 값을 참조하여, 탭과 백스페이스의 동작을 보조해준다.
set smartindent "자동 들여쓰기 시 #include 와 같은 전처리 구문을 판단하여 들여쓰기를 하지 않는다.
set ruler "오른쪽 하단에 현재위치 표시
set fileencodings=utf8,euc-kr "윈도우 메모장도 출력가능
set clipboard=unnamed " use OS clipboard
