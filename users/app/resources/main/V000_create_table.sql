 /* CREATE TABLE */
CREATE TABLE IF NOT EXISTS users.it_company(
id SERIAL PRIMARY KEY,
corporate_number bigint,
location VARCHAR( 100 ),
name VARCHAR( 100 ),
employee_number bigint,
company_size_male bigint,
company_size_female bigint,
company_url VARCHAR( 100 ),
average_age bigint,
month_average_predetermined_overtime_hours bigint,
average_continuous_service_years_Male bigint,
average_continuous_service_years_Female bigint,
shohyo bigint,
tokkyo bigint,
others bigint
);


