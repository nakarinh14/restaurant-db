-- Sample, add more table stuff in here.

CREATE TABLE franchises
(
    franchise_id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    description TEXT NOT NULL
);

CREATE TABLE restaurants
(
    restaurant_id SERIAL PRIMARY KEY,
    franchise_id INT REFERENCES franchises (franchise_id),
    name          TEXT UNIQUE NOT NULL,
    phone_contact VARCHAR(10) NOT NULL,
    address       TEXT UNIQUE NOT NULL,
    created_on    TIMESTAMP   NOT NULL DEFAULT CURRENT_TIMESTAMP,
    is_open       BOOLEAN     NOT NULL
);

CREATE TABLE menu_types
(
    menu_type_id SERIAL PRIMARY KEY,
    name         TEXT UNIQUE NOT NULL
);

CREATE TABLE menus
(
    menu_id       SERIAL PRIMARY KEY,
    restaurant_id INT REFERENCES restaurants (restaurant_id) NOT NULL ,
    menu_type_id  INT REFERENCES menu_types (menu_type_id) NOT NULL,
    name          TEXT NOT NULL,
    list_pricing  INT NOT NULL,
    UNIQUE(name, menu_type_id, restaurant_id)
);

CREATE TABLE users
(
    user_id  SERIAL PRIMARY KEY,
    username TEXT UNIQUE NOT NULL,
    password TEXT        NOT NULL
);

CREATE TABLE user_profiles
(
    user_profile_id SERIAL PRIMARY KEY,
    user_id         INT REFERENCES users (user_id) ON DELETE CASCADE NOT NULL,
    firstname       TEXT        NOT NULL,
    lastname        TEXT        NOT NULL,
    phone_contact   VARCHAR(10) NOT NULL
);

CREATE TABLE ratings
(
    rating_id SERIAL PRIMARY KEY,
    score     INT NOT NULL
);

CREATE TABLE reviews
(
    review_id       SERIAL PRIMARY KEY,
    user_profile_id INT REFERENCES user_profiles (user_profile_id) NOT NULL, 
    restaurant_id   INT REFERENCES restaurants (restaurant_id) NOT NULL,
    rating_id       INT REFERENCES ratings (rating_id)  NOT NULL,
    description     TEXT,
    created_on      TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE tags (
    tag_id SERIAL PRIMARY KEY,
    description TEXT UNIQUE NOT NULL
);

CREATE TABLE restaurant_tags (
    restaurant_tag_id SERIAL PRIMARY KEY,
    tag_id INT REFERENCES tags(tag_id) NOT NULL,
    restaurant_id INT REFERENCES restaurants(restaurant_id) NOT NULL
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

INSERT INTO tags(tag_id,description)
VALUES (1,'Fast Food'),
       (2,'Vegan'),
       (3,'Japanese'),
       (4,'Italian'),
       (5,'Steakhouse'),
       (6,'Casual'),
       (7,'Formal')
