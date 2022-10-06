-- Table: public.telecom_customer_churn

-- DROP TABLE IF EXISTS public.telecom_customer_churn;

CREATE TABLE IF NOT EXISTS public.telecom_customer_churn
(
    CustomerID character varying(240) COLLATE pg_catalog."default",
    Gender character varying(100) COLLATE pg_catalog."default",
    Age integer,
    Married character varying(15) COLLATE pg_catalog."default",
    Number_of_Dependents integer,
    city character varying(200) COLLATE pg_catalog."default",
    zipcode integer,
    latitude double precision,
    longtitude double precision,
    NumberofReferrals integer,
    tenureinMonths integer,
    offer character varying(100) COLLATE pg_catalog."default",
    phoneservice character varying(15) COLLATE pg_catalog."default",
    AvgMonthlyLongDistanceCharges double precision,
    InternetService character varying(15) COLLATE pg_catalog."default",
    InternetType character varying(250) COLLATE pg_catalog."default",
    AvgMonthlyGBDownload integer,
    OnlineSecurity character varying(15) COLLATE pg_catalog."default",
    OnlineBackup character varying(15) COLLATE pg_catalog."default",
    DeviceProtectionPlan integer,
    premiumTechSupport character varying(15) COLLATE pg_catalog."default",
    StreamingTV character varying(15) COLLATE pg_catalog."default",
    StreamingMovies character varying(15) COLLATE pg_catalog."default",
    streamingmusic character varying(15) COLLATE pg_catalog."default",
    unlimitedData character varying(15) COLLATE pg_catalog."default",
    contract character varying(50) COLLATE pg_catalog."default",
    paperlessBilling character varying(15) COLLATE pg_catalog."default",
    paymentMethod character varying(100) COLLATE pg_catalog."default",
    MonthlyCharge double precision,
    TotalCharges double precision,
    TotalRefunds double precision,
    TotalExtraDataCharges double precision,
    TotalLongDistanceCharges double precision,
    TotalRevenue double precision,
    CustomerStatus character varying(250) COLLATE pg_catalog."default",
    ChurnCategory character varying(250) COLLATE pg_catalog."default"
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.telecom_customer_churn
    OWNER to lzftwtpxmfhkqh;