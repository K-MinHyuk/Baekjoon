-- 코드를 작성해주세요
WITH CLASSES AS (
    SELECT ID, NTILE(4) OVER(ORDER BY SIZE_OF_COLONY DESC) AS CLASS
    FROM ECOLI_DATA
),
CLASSIFICATION AS (
    SELECT ID, CASE
                WHEN CLASS = 1
                THEN 'CRITICAL'
                WHEN CLASS = 2
                THEN 'HIGH'
                WHEN CLASS = 3
                THEN 'MEDIUM'
                WHEN CLASS = 4
                THEN 'LOW'
                END AS COLONY_NAME
    FROM CLASSES
)
SELECT ID, COLONY_NAME
FROM CLASSIFICATION
ORDER BY ID