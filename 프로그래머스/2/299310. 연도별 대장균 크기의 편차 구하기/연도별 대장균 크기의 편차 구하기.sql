-- 코드를 작성해주세요
WITH T AS (
    SELECT YEAR(DIFFERENTIATION_DATE) YEAR, MAX(SIZE_OF_COLONY) MAX_SIZE
    FROM ECOLI_DATA 
    GROUP BY YEAR(DIFFERENTIATION_DATE)
)

SELECT YEAR(DIFFERENTIATION_DATE) YEAR, (T.MAX_SIZE - ECOLI_DATA.SIZE_OF_COLONY) YEAR_DEV, ID
FROM ECOLI_DATA JOIN T  ON YEAR(ECOLI_DATA.DIFFERENTIATION_DATE) = T.YEAR
ORDER BY YEAR ASC, YEAR_DEV
