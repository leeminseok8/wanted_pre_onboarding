# 원티드 프리온보딩 선발 과제

## 👉 서비스 개요
- 본 서비스는 기업의 채용을 위한 웹 서비스입니다.
- 회사는 채용공고를 생성하고, 이에 사용자는 지원합니다.

## 👉 필수 기술요건
- ORM 사용하여 구현.
- RDBMS 사용 (SQLite, PostgreSQL 등).

---

## 👉 프로젝트 기간
- 2022.08.22 ~ 2022.08.24

## 👉 구현 사항
-  **채용 공고 등록**
-  **채용 공수 수정**
-  **채용 공고 삭제**
-  **채용 공고 목록**
    - **채용 공고 검색 기능 구현 (선택사항 및 가산점요소)**

-  **채용 상세 페이지**
    - **해당 회사가 올린 다른 채용공고 추가적으로 포함 (선택사항 및 가산점요소)**
-  **사용자 채용 공고 지원 (선택사항 및 가산점요소)**

---

## 👉 모델링
<img width="821" alt="스크린샷 2022-08-24 오후 6 24 44" src="https://user-images.githubusercontent.com/93478318/186382817-5abef497-862f-43da-80a5-4424c5ad2a25.png">


## 👉 사용 기술 및 패키지
<img width="241" alt="스크린샷 2022-08-24 오후 6 05 16" src="https://user-images.githubusercontent.com/93478318/186378277-614ce6aa-9319-44a7-b769-230160190e38.png">

---

## 👉 API 명세서

-  **채용 공고 등록**
<img width="497" alt="스크린샷 2022-08-24 오후 6 27 36" src="https://user-images.githubusercontent.com/93478318/186383169-4f0f47b0-a4cc-43c6-a716-e8128f1f65f0.png">

    - 회사 정보는 임의 DB로 미리 등록하고 추가적인 채용 공고에 대한 정보만 요청받아서 처리하도록 구성했습니다.

---

-  **채용 공수 수정**
<img width="552" alt="스크린샷 2022-08-24 오후 6 29 57" src="https://user-images.githubusercontent.com/93478318/186383637-22d95932-53a1-4e32-856b-5bd62537f661.png">
<img width="1243" alt="스크린샷 2022-08-24 오후 6 31 33" src="https://user-images.githubusercontent.com/93478318/186383995-ab077ad6-2aef-429d-a4ca-5caab367520c.png">
<img width="257" alt="스크린샷 2022-08-24 오후 6 32 46" src="https://user-images.githubusercontent.com/93478318/186384324-ea415bef-603c-4ccd-aec6-2beb18105118.png">

---

-  **채용 공고 삭제**
<img width="598" alt="스크린샷 2022-08-24 오후 6 37 22" src="https://user-images.githubusercontent.com/93478318/186385334-accfb96f-7107-4a1f-ac7e-8e422bc83ef8.png">


    - 인증 절차는 구현하지 않으므로 body에 id를 담아 권한을 부여하였습니다.

---

-  **채용 공고 목록**
    - **채용 공고 검색 기능 구현 (선택사항 및 가산점요소)**
    <img width="583" alt="스크린샷 2022-08-24 오후 6 38 54" src="https://user-images.githubusercontent.com/93478318/186385689-dbf98436-fbd6-4338-90c7-c26e48a73402.png">

    - 채용 공고 검색할 수 있는 키워드를 모두 포함하였습니다. 
    <img width="620" alt="스크린샷 2022-08-24 오후 6 43 28" src="https://user-images.githubusercontent.com/93478318/186386721-9cc48017-f352-4ca7-8f64-a84baf940685.png">


---

-  **채용 상세 페이지**
    - **해당 회사가 올린 다른 채용공고 추가적으로 포함 (선택사항 및 가산점요소)**
    <img width="639" alt="스크린샷 2022-08-24 오후 6 40 29" src="https://user-images.githubusercontent.com/93478318/186386082-60e8badc-20c5-4c42-8bc6-6793b8013c29.png">

    - 현재 보고있는 공고를 제외한 다른 공고의 id만 호출하도록 작성하였습니다.
    <img width="515" alt="스크린샷 2022-08-24 오후 6 43 52" src="https://user-images.githubusercontent.com/93478318/186386811-628fc1e1-0522-4cee-9810-f499fba66b05.png">


---

-  **사용자 채용 공고 지원 (선택사항 및 가산점요소)**
<img width="640" alt="스크린샷 2022-08-24 오후 6 41 45" src="https://user-images.githubusercontent.com/93478318/186386395-4fc998ce-b1e0-4b03-8076-4e71a96c85bf.png">


    - 사용자 당 1회의 지원만 가능하므로 지원한 회사가 존재한다면 더 이상 지원할 수 없도록 작성하였습니다.
