import os

def search(dirname):
    try:
        filenames = os.listdir(dirname)
        for filename in filenames:
            # os.path.join는 디렉터리와 파일 이름을 이어 주는 함수
            full_filename = os.path.join(dirname, filename)
            # full_filename가 dicrectory일 경우 해당 경로로 재귀 호출
            if os.path.isdir(full_filename):
                search(full_filename)
            else:
                # os.path.splitext는 파일 이름을 확장자를 기준으로 두 부분으로 나누어 준다. 
                ext = os.path.splitext(full_filename)[1]
                if ext == '.py':
                    print(full_filename)
    # 권한이 없는 dicrectory에 접근하는 경우에도 프로그램이 오류로 종료되지 않기 위함                    
    except PermissionError:
        pass

'''
import os
for (path, dir, files) in os.walk("/Users/bjung/bjung_temp"):
    for filename in files:
        ext = os.path.splitext(filename)[1]
        if ext == 'py':
            print("%s%s" % (path, filename))
'''

search("/Users/bjung/bjung_temp")