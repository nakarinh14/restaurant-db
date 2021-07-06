-- Sample, add more table stuff in here.

CREATE TABLE restaurants (
	restaurant_id serial PRIMARY KEY,
	name TEXT UNIQUE NOT NULL,
	phone_contact VARCHAR ( 10 ) NOT NULL,
	address TEXT UNIQUE NOT NULL,
	created_on TIMESTAMP NOT NULL,
	is_open BOOLEAN NOT NULL
);

CREATE TABLE menus (
	menu_id serial PRIMARY KEY,
	restaurant_id serial,
	menu_type_id serial,
	name TEXT UNIQUE NOT NULL,
	list_pricing INT NOT NULL,
	FOREIGN KEY (restaurant_id) REFERENCES restaurants(restaurant_id),
	FOREIGN KEY (menu_type_id) REFERENCES menu_types(menu_type_id)
);

CREATE TABLE menu_types (
	menu_type_id serial PRIMARY KEY,
	name TEXT UNIQUE NOT NULL
);

CREATE TABLE user_profiles (
	user_profile_id serial PRIMARY KEY,
	user_id serial,
	firstname TEXT NOT NULL,
	lastname TEXT NOT NULL,
	phone_contact VARCHAR ( 10 ) NOT NULL,
	FOREIGN KEY (user_id) REFERENCES users(user_id)
);

CREATE TABLE users (
	user_id serial PRIMARY KEY,
	username TEXT UNIQUE NOT NULL,
	password TEXT NOT NULL
);

CREATE TABLE reviews (
	review_id serial PRIMARY KEY,
	user_profile_id serial,
	restaurant_id serial,
	rating_id serial,
	description TEXT,
	created_on TIMESTAMP NOT NULL,
	FOREIGN KEY (user_profile_id) REFERENCES user_profiles(user_profile_id),
	FOREIGN KEY (restaurant_id) REFERENCES restaurants(restaurant_id),
	FOREIGN KEY (rating_id) REFERENCES ratings(rating_id)
);

CREATE TABLE ratings (
	rating_id serial PRIMARY KEY,
	score INT NOT NULL
);
