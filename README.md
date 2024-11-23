# 실행 방법
```sh
# clone
git clone git@github.com:aiotp-skycastle/control-panel.git
cd control-panel

# run postgres
mkdir data
docker compose up -d

# init django
python -m venv ./venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate

# run django
python manage.py runserver 0.0.0.0:8001
```

# 진행 상황
## 10주차
- 라즈베리파이간 통신 규약 문서 정의하기  
  <img width="500" alt="Screen Shot 2024-11-06 at 4 43 13 PM" src="https://github.com/user-attachments/assets/cedbce72-d837-48ba-b199-48cbd992d308">
- 백엔드 구현 1 (의자상태, 호출상태, 조도, 온도, 기압, 서보모터)
- 프론트 구현 1 (템플릿 생성, 서보모터 조작)
## 11주차
- HLS를 이용한 카메라 스트리밍 구현 (로컬에서)  
  <img width="400" alt="Screenshot 2024-11-18 at 17 10 20" src="https://github.com/user-attachments/assets/88648e5b-4bba-4209-ac8b-4f50a222e1d1">
- 수기로 작성했던 API 구현 계획을 Swagger로 옮겨 문서를 보고 테스트하기 용이하게 함 (https://skycastle.cho0h5.org/api/swagger/)  
  <img width="400" alt="Screenshot 2024-11-18 at 18 18 03" src="https://github.com/user-attachments/assets/00530603-5f40-4c0c-883a-d5b8b4625674">
## 12주차
- 켜질 때 자동으로 Django와 DB가 켜지도록 설정
- 책상 모듈의 카메라를 위한 UI 추가
- 방 모듈과 책상 모듈로부터 카메라 스트리밍을 받는 API 구현
- 백엔드 구현 2 (부저상태, 공부시간 산출)
- 프론트 구현 2 (경고 api 구현, 공부시간 출력)
# 계획
## 13주차
- 조도, 온도, 기압을 시계열 데이터베이스에 저장하도록 변경하기
## 14주차 
- 프론트 구현 3 (조도, 온도, 기압 그래프)
## 15주차 
- 하드웨어 구현 (호출 당했을 때 LED와 부저도 울리도록)
