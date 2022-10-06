-- Table: public.telecom_zipcode_population

-- DROP TABLE IF EXISTS public.telecom_zipcode_population;

CREATE TABLE IF NOT EXISTS public.telecom_zipcode_population
(
    zipcode integer NOT NULL,
    population integer NOT NULL,
    CONSTRAINT telecom_zipcode_population_pkey PRIMARY KEY (zipcode)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.telecom_zipcode_population
    OWNER to lzftwtpxmfhkqh;