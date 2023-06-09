-- 코드를 입력하세요
SELECT a.PRODUCT_CODE, SUM(a.PRICE * b.SALES_AMOUNT) AS SALES
FROM PRODUCT a JOIN OFFLINE_SALE b ON a.PRODUCT_ID = b.PRODUCT_ID
GROUP BY a.PRODUCT_CODE
ORDER BY SUM(a.PRICE * b.SALES_AMOUNT) DESC, a.PRODUCT_CODE
;

# SELECT P.PRODUCT_CODE, SUM(P.PRICE*OS.SALES_AMOUNT) AS SALES
# FROM PRODUCT P
# JOIN OFFLINE_SALE OS
# ON P.PRODUCT_ID=OS.PRODUCT_ID
# GROUP BY PRODUCT_CODE
# ORDER BY SALES DESC, PRODUCT_CODE ASC