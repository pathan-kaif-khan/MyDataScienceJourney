SELECT count(*) FROM public."FactBilling";


CREATE MATERIALIZED VIEW avg_customer_bill (customerid, averagebillamount) AS
(SELECT customerid, avg(billedamount)
from public."FactBilling"
GROUP BY customerid
);

REFRESH MATERIALIZED VIEW avg_customer_bill;

SELECT FROM avg_customer_bill WHERE averagebillamount > 11000;