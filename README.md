# Streamlit for Age Prediction

## Deploy Streamlit using Docker
### 전제 조건
- DB와 FastAPI가 동일한 Docker 환경 내에 실행되고 있어야 한다.
```bash
# DB Run
$ sudo docker run -d \
        --name 3rd-t2-mariadb \
        -e MARIADB_USER=3rd \
        --env MARIADB_PASSWORD=1234 \
        --env MARIADB_DATABASE=team2 \
        --env MARIADB_ROOT_PASSWORD=my-secret-pw \
        -p 23306:3306 \
        mariadb:latest
```
```sql
# Create DB Table
CREATE TABLE face_age (
    num INT AUTO_INCREMENT PRIMARY KEY NOT NULL COMMENT 'Serial number',
    origin_name VARCHAR(100) NOT NULL COMMENT '원본 파일명',
    file_path VARCHAR(255) NOT NULL COMMENT '저장 전체 경로 및 변환 파일명',
    request_time CHAR(19) NOT NULL COMMENT '요청시간',
    prediction_result VARCHAR(10) COMMENT '예측 결과',
    prediction_time CHAR(19) COMMENT '예측시간',
    answer VARCHAR(10) COMMENT '실제 정답',
    comments VARCHAR(255) COMMENT '추가사항'
);
```

```bash
# Run FastAPI
$ sudo docker run -d -p 8022:8080 -e DB_IP=<docker_ip> --name api -v /home/ubuntu/images:/home/ubuntu/images seokxkyu/age_pred:2.0.1

# Run Streamlit
$ sudo docker run -d -p 8032:8501 -e EC2_IP=<docker_ip> -e PWD=<admin_pwd> -v /home/ubuntu/images:/home/ubuntu/images --name stream j25ng/streamlit:8.0.0
```

### Streamlit 접속하기
```
http://<your_ip>:8032
```

### 기능
#### User Page
- Upload Image
![image](https://github.com/user-attachments/assets/c6961226-c6c5-4ca5-8218-4790e477e25f)
- View Result
![image](https://github.com/user-attachments/assets/b5a0f868-a6a9-4f84-8de3-c0ecefbc99e4)
- View Chart
![image](https://github.com/user-attachments/assets/032523cd-0578-4483-bb84-02c4e91b3660)
![image](https://github.com/user-attachments/assets/d13f10e0-5c9b-477f-aeed-300609a86443)
![image](https://github.com/user-attachments/assets/5e154209-502c-452f-8d32-d14e51c5fca9)

#### Admin Page
- Input Password : <admin_pwd>로 로그인
![image](https://github.com/user-attachments/assets/f04d9918-3d62-4cab-bac2-615ca6e23760)
- Dashboard
![image](https://github.com/user-attachments/assets/7d8f6b93-68e8-4684-a7eb-350171f08b5f)

