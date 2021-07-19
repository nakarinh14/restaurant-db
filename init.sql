CREATE TABLE "user"
(
    user_id  SERIAL PRIMARY KEY,
    username TEXT UNIQUE NOT NULL,
    password TEXT        NOT NULL
);

CREATE TABLE user_profile
(
    user_profile_id SERIAL PRIMARY KEY,
    user_id         INT REFERENCES "user" (user_id) ON DELETE CASCADE NOT NULL,
    firstname       TEXT        NOT NULL,
    lastname        TEXT        NOT NULL,
    phone_contact   TEXT NOT NULL
);

CREATE TABLE restaurant
(
    restaurant_id SERIAL PRIMARY KEY,
    user_owner_id INT REFERENCES "user" (user_id) NOT NULL,
    name          TEXT UNIQUE NOT NULL,
    phone_contact VARCHAR(10) NOT NULL,
    address       TEXT UNIQUE NOT NULL,
    created_on    TIMESTAMP   NOT NULL DEFAULT CURRENT_TIMESTAMP,
    is_open       BOOLEAN     NOT NULL DEFAULT TRUE,
    img_url       TEXT
);

CREATE TABLE menu_type
(
    menu_type_id SERIAL PRIMARY KEY,
    name         TEXT UNIQUE NOT NULL
);

CREATE TABLE menu
(
    menu_id       SERIAL PRIMARY KEY,
    restaurant_id INT REFERENCES restaurant (restaurant_id) NOT NULL ,
    menu_type_id  INT REFERENCES menu_type (menu_type_id) NOT NULL,
    name          TEXT NOT NULL,
    list_pricing  DECIMAL NOT NULL,
    img_url       TEXT,
    UNIQUE(name, menu_type_id, restaurant_id)
);

CREATE TABLE rating
(
    rating_id SERIAL PRIMARY KEY,
    score     DECIMAL NOT NULL
);

CREATE TABLE review
(
    review_id       SERIAL PRIMARY KEY,
    user_profile_id INT REFERENCES user_profile (user_profile_id) NOT NULL,
    restaurant_id   INT REFERENCES restaurant (restaurant_id) NOT NULL,
    rating_id       INT REFERENCES rating (rating_id)  NOT NULL,
    description     TEXT,
    created_on      TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE tag (
    tag_id SERIAL PRIMARY KEY,
    description TEXT UNIQUE NOT NULL
);

CREATE TABLE restaurant_tag (
    restaurant_tag_id SERIAL PRIMARY KEY,
    tag_id INT REFERENCES tag(tag_id) NOT NULL,
    restaurant_id INT REFERENCES restaurant(restaurant_id) NOT NULL
);



INSERT INTO "user"(username, password)
VALUES ('user1', '5f4dcc3b5aa765d61d8327deb882cf99'), -- Password is 'password'
       ('user2', '5f4dcc3b5aa765d61d8327deb882cf99'),
       ('reviewer1', '5f4dcc3b5aa765d61d8327deb882cf99'),
       ('reviewer2', '5f4dcc3b5aa765d61d8327deb882cf99'),
       ('reviewer3', '5f4dcc3b5aa765d61d8327deb882cf99'),
       ('reviewer4', '5f4dcc3b5aa765d61d8327deb882cf99'),
       ('reviewer5', '5f4dcc3b5aa765d61d8327deb882cf99');

INSERT INTO user_profile(user_id, firstname, lastname, phone_contact)
VALUES (1, 'Sam', 'Smith', '0814280345'),
       (2, 'Somchai', 'Jaemsai', '0894382918'),
       (3, 'Good', 'Reviewer', '5555555555'),
       (4, 'John', 'Doe', '5555555555'),
       (5, 'Wills', 'Heimstein', '5555555555'),
       (6, 'Ken', 'Hector', '5555555555'),
       (7, 'Tae', 'Noooooo', '5555555555');

INSERT INTO restaurant(name, phone_contact, address, created_on, user_owner_id)
VALUES ('Jojo Pizzeria', 7124707705, '4925 Pin Oak Drive Benton Iowa', '2016-06-22'::timestamp, 1),
       ('Bubble Seafood', 4154072066, '4295 Locust View Drive San Francisco California', '1999-07-23'::timestamp, 1),
       ('Seven Heaven Bar', 7085744652, '4546 Star Route Bridgeview Illinois', '2010-02-13'::timestamp, 2),
       ('Hudson Kitchen', 3202661407, '4849 Newton Street Saint Cloud Minnesota', '2018-05-22'::timestamp, 2),
       ('8MilePi Detroit Style Pizza', 4158535342, '60 Morris St Mission Bay', '2018-05-22'::timestamp, 1),
       ('Cuisine of Nepal', 4156472222, '3486 Mission St Bernal Heights', '2018-05-22'::timestamp, 1),
       ('Fable', 4155902404, '558 Castro St Castro', '2018-05-22'::timestamp, 1);

INSERT INTO menu_type(name)
VALUES ('Appetizers'),
       ('Salad/Soup'),
       ('Entrees'),
       ('Sides'),
       ('Dessert'),
       ('Drink');

INSERT INTO menu(restaurant_id, menu_type_id, name, list_pricing)
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
       (4, 5, 'Sticky Toffee Pudding', 20),
       (5, 4, 'BBQ Style Chicken Wings', 9.75),
       (5, 3, '3 Cheese Red Top Pizza', 24.75),
       (5, 3, 'Pepperoni Pie Pizza', 26.75),
       (5, 3, 'Fun Guy Forno Pizza', 28.75),
       (5, 3, 'BBQ Chicken Pizza', 28.75);

INSERT INTO tag(description)
VALUES ('Fast food'),
       ('Vegan'),
       ('Japanese'),
       ('Italian'),
       ('Steakhouse'),
       ('Casual'),
       ('Formal'),
       ('Sit-down dining'),
       ('Delivery'),
       ('Takeout'),
       ('Indoor dining'),
       ('Indoor & Outdoor dining'),
       ('Seafood');

INSERT INTO rating(score)
VALUES (0.0),
       (0.5),
       (1.0),
       (1.5),
       (2.0),
       (2.5),
       (3.0),
       (3.5),
       (4.0),
       (4.5),
       (5.0);

INSERT INTO review(user_profile_id, restaurant_id, rating_id, description)
VALUES (4, 5, 8, 'Lorem ipsum dolor sit amet, consectetur adipiscing elit sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.'),
       (4, 5, 7, 'Being a Windsor resident, I''m a real big Detroit pizza buff. Was massively pleased with 8-mile pizza and how much their quality, accuracy, and authenticity hit the spot on the head...'),
       (4, 6, 10, 'My husband and I dropped in on a whim for lunch today and had an incredible meal and unlimited real-brewed masala chai to wash it all down. The owner was very friendly and provided...'),
       (4, 7, 9, 'Our party of six had a great evening. We had reservations for a late Saturday evening. We sat in the back/outdoors which had a pretty relaxing vibe. The food...'),
       (5, 5, 10, 'Lorem ipsum dolor sit amet, consectetur adipiscing elit sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.'),
       (6, 5, 4, 'Lorem ipsum dolor sit amet, consectetur adipiscing elit sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.'),
       (7, 5, 6, 'Lorem ipsum dolor sit amet, consectetur adipiscing elit sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.');
