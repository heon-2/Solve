-- 코드를 입력하세요

# 기본키가 무엇이냐에 흔들리지 않고 FLAVOR를 기준으로 GROUP BY
# GROUP BY만 하고 SUM안하면 한번만 결과값이 나옴.
# 예를 들어 520,220 이 딸기면 740이 아니라 520 한 번만 나옴.

SELECT A.FLAVOR
FROM FIRST_HALF AS A
# JULY 테이블에서 'FLAVOR'별로 주문 총액인 'TOTAL_ORDER'을 계산해.
JOIN (SELECT FLAVOR, SUM(TOTAL_ORDER) AS TOTAL_ORDER
      FROM JULY GROUP BY FLAVOR ) AS B
ON A.FLAVOR = B.FLAVOR
ORDER BY (A.TOTAL_ORDER + B.TOTAL_ORDER) DESC
LIMIT 3;