-- Sample, add more table stuff in here.

CREATE DATABASE food_review_db;

CREATE TABLE restaurants
(
    restaurant_id serial PRIMARY KEY,
    name          TEXT UNIQUE NOT NULL,
    phone_contact VARCHAR(10) NOT NULL,
    address       TEXT UNIQUE NOT NULL,
    created_on    TIMESTAMP   NOT NULL,
    is_open       BOOLEAN     NOT NULL
);

CREATE TABLE menu_types
(
    menu_type_id serial PRIMARY KEY,
    name         TEXT UNIQUE NOT NULL
);

CREATE TABLE menus
(
    menu_id       serial PRIMARY KEY,
    restaurant_id serial,
    menu_type_id  serial,
    name          TEXT UNIQUE NOT NULL,
    list_pricing  INT         NOT NULL,
    FOREIGN KEY (restaurant_id) REFERENCES restaurants (restaurant_id),
    FOREIGN KEY (menu_type_id) REFERENCES menu_types (menu_type_id)
);

CREATE TABLE users
(
    user_id  serial PRIMARY KEY,
    username TEXT UNIQUE NOT NULL,
    password TEXT        NOT NULL
);

CREATE TABLE user_profiles (
	user_profile_id serial PRIMARY KEY,
	user_id serial,
	firstname TEXT NOT NULL,
	lastname TEXT NOT NULL,
	phone_contact VARCHAR ( 10 ) NOT NULL,
	FOREIGN KEY (user_id) REFERENCES users(user_id)
);

CREATE TABLE ratings
(
    rating_id serial PRIMARY KEY,
    score     INT NOT NULL
);

CREATE TABLE reviews (
                         review_id       serial PRIMARY KEY,
                         user_profile_id serial,
                         restaurant_id   serial,
                         rating_id       serial,
                         description     TEXT,
                         created_on      TIMESTAMP NOT NULL,
                         FOREIGN KEY (user_profile_id) REFERENCES user_profiles (user_profile_id),
                         FOREIGN KEY (restaurant_id) REFERENCES restaurants (restaurant_id),
                         FOREIGN KEY (rating_id) REFERENCES ratings (rating_id)
);

INSERT INTO restaurants(name, phone_contact, address, created_on, is_open)
VALUES ('Jojo Pizzeria', 7124707705, '4925 Pin Oak Drive Benton Iowa', '2016-06-22'::timestamp, true),
       ('Bubble Seafood', 4154072066, '4295 Locust View Drive San Francisco California', '1999-07-23'::timestamp, true),
       ('Seven Heaven Bar', 7085744652, '4546 Star Route Bridgeview Illinois', '2010-02-13'::timestamp, true),
       ('Hudson Kitchen', 3202661407, '4849 Newton Street Saint Cloud Minnesota', '2018-05-22'::timestamp, true);

INSERT INTO menu_types(name)
VALUES ('Appetizers'),
       ('Salad/Soup'),
       ('Entrees'),
       ('Sides'),
       ('Dessert'),
       ('Drink');

INSERT INTO menus(restaurant_id, menu_type_id, name, list_pricing)
VALUES (1, 1, 'Garlic Bread', 10),
       (1, 1, 'Risotto', 10),
       (1, 2, 'Caesar Salad', 10),
       (1, 3, 'Pepperoni Pizza', 20),
       (1, 3, 'Beef Lasagne', 15),
       (1, 4, 'French Fries', 5),
       (1, 4, 'Onion Ring', 5),
       (1, 5, 'Lemon Cake', 10),
       (1, 6, 'Cola', 1),
       (2, 1, 'Shrimp Cocktail', 10),
       (2, 1, 'Pan Seared Scallops', 10),
       (2, 2, 'Seafood Special Soup', 15),
       (2, 2, 'Fish and Chips', 15),
       (2, 3, 'Crispy Skin Salmon', 25),
       (2, 3, 'Shellfish Platter', 30),
       (2, 5, 'Sea Salt Ice Cream', 5),
       (2, 6, 'Green Soda', 1),
       (2, 6, 'Blue Soda', 1),
       (3, 4, 'Chicken Wings', 5),
       (3, 4, 'Chips', 5),
       (3, 6, 'Beer', 3),
       (3, 6, 'Old Fashioned', 5),
       (3, 6, 'Vesper Martini', 5),
       (3, 6, 'Cosmo Canyon', 5),
       (4, 1, 'Seared Foie Gras', 15),
       (4, 1, 'Wagyu meatballs', 15),
       (4, 2, 'Green Salad', 10),
       (4, 2, 'Onion Soup', 10),
       (4, 3, 'Herb Crusted Rack of Lamb', 25),
       (4, 3, 'Dry Aged Ribeye Steak', 30),
       (4, 3, 'Braised Short Rib', 25),
       (4, 4, 'Mash Potato', 10),
       (4, 4, 'Glaze Wild Mushroom', 10),
       (4, 5, 'Sticky Toffee Pudding', 20);

