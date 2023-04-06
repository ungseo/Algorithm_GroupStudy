-- 코드를 입력하세요
SELECT DR_NAME, DR_ID, MCDP_CD, date_format(HIRE_YMD, "%Y-%m-%d") from DOCTOR
WHERE MCDP_CD like '%CS%' or MCDP_CD like '%GS%'
ORDER by HIRE_YMD DESC, DR_NAME;