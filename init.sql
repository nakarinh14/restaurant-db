-- Sample, add more table stuff in here.

CREATE TABLE restaurants (
	id serial PRIMARY KEY,
	name TEXT UNIQUE NOT NULL,
	phone_contact VARCHAR ( 10 ) NOT NULL,
	address TEXT UNIQUE NOT NULL,
	created_on TIMESTAMP NOT NULL,
	is_open BOOLEAN NOT NULL
);