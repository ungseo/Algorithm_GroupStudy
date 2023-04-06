-- 코드를 입력하세요
SELECT PT_NAME, PT_NO, GEND_CD, AGE, IFNULL(TLNO, 'NONE') as TLNO from PATIENT
WHERE AGE <= 12 and GEND_CD like '%W%'
order by age DESC, PT_NAME;
