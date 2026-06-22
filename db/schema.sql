PRAGMA foreign_keys = ON;

CREATE TABLE companies (
    id TEXT PRIMARY KEY,
    company_name TEXT,
    website TEXT
);

CREATE TABLE profitandloss (
    company_id TEXT,
    year INTEGER,
    sales REAL,
    profit REAL,
    PRIMARY KEY(company_id, year),
    FOREIGN KEY(company_id) REFERENCES companies(id)
);

CREATE TABLE balancesheet (
    company_id TEXT,
    year INTEGER,
    assets REAL,
    liabilities REAL,
    PRIMARY KEY(company_id, year),
    FOREIGN KEY(company_id) REFERENCES companies(id)
);

CREATE TABLE cashflow (
    company_id TEXT,
    year INTEGER,
    operating_cf REAL,
    investing_cf REAL,
    financing_cf REAL,
    PRIMARY KEY(company_id, year),
    FOREIGN KEY(company_id) REFERENCES companies(id)
);

CREATE TABLE analysis (
    company_id TEXT PRIMARY KEY,
    about_company TEXT,
    FOREIGN KEY(company_id) REFERENCES companies(id)
);

CREATE TABLE documents (
    company_id TEXT PRIMARY KEY,
    annual_report TEXT,
    FOREIGN KEY(company_id) REFERENCES companies(id)
);

CREATE TABLE prosandcons (
    company_id TEXT PRIMARY KEY,
    pros TEXT,
    cons TEXT,
    FOREIGN KEY(company_id) REFERENCES companies(id)
);

CREATE TABLE sectors (
    company_id TEXT PRIMARY KEY,
    sector TEXT,
    FOREIGN KEY(company_id) REFERENCES companies(id)
);

CREATE TABLE stock_prices (
    company_id TEXT,
    price_date DATE,
    close_price REAL,
    PRIMARY KEY(company_id, price_date),
    FOREIGN KEY(company_id) REFERENCES companies(id)
);

CREATE TABLE financial_ratios (
    company_id TEXT,
    year INTEGER,
    roe REAL,
    roce REAL,
    PRIMARY KEY(company_id, year),
    FOREIGN KEY(company_id) REFERENCES companies(id)
);

CREATE TABLE peer_groups (
    company_id TEXT,
    peer_company TEXT
);