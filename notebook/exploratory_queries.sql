SELECT COUNT(*) FROM companies;

SELECT COUNT(*) FROM profitandloss;

SELECT COUNT(*) FROM balancesheet;

SELECT COUNT(*) FROM cashflow;

SELECT * FROM companies LIMIT 10;

SELECT * FROM stock_prices LIMIT 10;

SELECT company_id, COUNT(*)
FROM profitandloss
GROUP BY company_id;

SELECT company_id, MAX(year)
FROM balancesheet
GROUP BY company_id;

SELECT company_id, AVG(close_price)
FROM stock_prices
GROUP BY company_id;

SELECT COUNT(*) FROM financial_ratios;