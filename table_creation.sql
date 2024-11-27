CREATE TABLE building(
	building_id		VARCHAR(5) 		NOT NULL PRIMARY KEY,
	building_name	VARCHAR(255) 	NOT NULL,
	street			VARCHAR(255),
	city			VARCHAR(255) 	NOT NULL
);

CREATE TABLE agent(
	agent_id			VARCHAR(5) 		NOT NULL PRIMARY KEY,
	agent_first_name	VARCHAR(255) 	NOT NULL,
	agent_last_name		VARCHAR(255) 	NOT NULL
);

CREATE TABLE memberassignment(
	member_name		VARCHAR(255) 	NOT NULL PRIMARY KEY,
	agent_id		VARCHAR(5) 		NOT NULL,
	FOREIGN KEY (agent_id) REFERENCES agent(agent_id) ON DELETE RESTRICT
);

CREATE TABLE agentbuilding(
	agent_id		VARCHAR(5) 		NOT NULL PRIMARY KEY,
	building_id		VARCHAR(5) 		NOT NULL,
	FOREIGN KEY (agent_id) REFERENCES agent(agent_id) ON DELETE RESTRICT,
	FOREIGN KEY (building_id) REFERENCES building(building_id) ON DELETE RESTRICT
);

CREATE TABLE venue(
	venue_id			VARCHAR(5) 		NOT NULL PRIMARY KEY,
	venue_name	 		VARCHAR(255)	NOT NULL,
	floor_area			INT				NOT NULL,
	capacity			INT				NOT NULL,
	venue_type			VARCHAR(255)	NOT NULL,
	floor				INT				NOT NULL,
	under_renovation 	BOOLEAN 		DEFAULT FALSE,
	reservation_fee 	INT				NOT NULL
);

CREATE TABLE venuebuilding(
    venue_id    VARCHAR(5)  NOT NULL PRIMARY KEY,
    building_id VARCHAR(5)  NOT NULL,
    FOREIGN KEY(venue_id) REFERENCES venue(venue_id),
    FOREIGN KEY(building_id) REFERENCES building(building_id)
);

CREATE TABLE availablevenue(
	a_venue_id	VARCHAR(5) 	NOT NULL PRIMARY KEY,
	FOREIGN KEY(a_venue_id) REFERENCES venue(venue_id)
);

CREATE TABLE unavailablevenue(
	u_venue_id					VARCHAR(5) 	NOT NULL PRIMARY KEY,
	renovation_date_start		DATE		NOT NULL,
	renovation_date_end			DATE 		NOT NULL,
	FOREIGN KEY(u_venue_id) REFERENCES venue(venue_id)
);

CREATE TABLE amenity(
	amenity_id			VARCHAR(5) 		NOT NULL PRIMARY KEY,
	amenity_type		VARCHAR(255)	NOT NULL,
	description			VARCHAR(255),
	quantity			INT				NOT NULL DEFAULT 1
);

CREATE TABLE amenityvenue(
	amenity_id	VARCHAR(5)	NOT NULL PRIMARY KEY,
	venue_id	VARCHAR(5)	NOT NULL,
	FOREIGN KEY(amenity_id) REFERENCES amenity(amenity_id),
	FOREIGN KEY(venue_id) REFERENCES venue(venue_id)
);

CREATE TABLE customer (
	customer_id 				VARCHAR(5) 		NOT NULL PRIMARY KEY,
	customer_first_name 		VARCHAR(255) 	DEFAULT NULL,
	customer_middle_initial 	VARCHAR(2) 		DEFAULT NULL,
	customer_last_name 			VARCHAR(255) 	NOT NULL,
	birth_date 					DATE 			NOT NULL
);

CREATE TABLE reservation (
	reservation_id 			VARCHAR(5)		NOT NULL PRIMARY KEY,
	customer_id 			VARCHAR(5) 		NOT NULL,
	venue_id 				VARCHAR(5) 		NOT NULL,
	number_of_participants 	INT 			NOT NULL,
	date_start 				DATE 			NOT NULL,
	date_end 				DATE 			NOT NULL,
	FOREIGN KEY (customer_id) REFERENCES customer(customer_id) ON DELETE RESTRICT,
	FOREIGN KEY (venue_id) REFERENCES venue(venue_id) ON DELETE RESTRICT
);


INSERT INTO building (building_id, building_name, street, city)
VALUES
    ('00001', 'Sunset Towers', '123 Sunset Blvd', 'Springfield'),
    ('00002', 'Pinewood Plaza', '456 Pine St', 'Greenfield'),
    ('00003', 'Oak Ridge Center', '789 Oak Dr', 'Lakeside'),
    ('00004', 'Maple Grove', '101 Maple Ave', 'Riverside'),
    ('00005', 'Cedar Heights', '202 Cedar Ln', 'Hillview');

INSERT INTO agent (agent_id, agent_first_name, agent_last_name)
VALUES
    ('00001', 'James', 'Bond'),
    ('00002', 'Perry', 'Dplatypus'),
    ('00003', 'John', 'Wick'),
    ('00004', 'Emily', 'Davis'),
    ('00005', 'Chris', 'Brown'),
    ('00006', 'Sarah', 'Miller'),
    ('00007', 'David', 'Wilson'),
    ('00008', 'Sophia', 'Moore');

INSERT INTO memberassignment (agent_id, member_name)
VALUES
    ('00001', 'Alice Brown'),
    ('00001', 'Bob Smith'),
    ('00002', 'Charlie Davis'),
    ('00002', 'Diana Johnson'),
    ('00003', 'Eve Clark'),
    ('00003', 'Frank Lee'),
    ('00004', 'Grace Taylor'),
    ('00004', 'Henry Miller'),
    ('00005', 'Ivy Wilson'),
    ('00005', 'Jack Moore'),
    ('00006', 'Liam Adams'),
    ('00006', 'Mia Walker'),
    ('00007', 'Noah King'),
    ('00007', 'Olivia Scott'),
    ('00008', 'Parker Harris');

INSERT INTO agentbuilding (agent_id, building_id)
VALUES
    ('00001', '00001'),
    ('00002', '00002'),
    ('00003', '00003'),
    ('00004', '00004'),
    ('00005', '00005'),
    ('00006', '00001'),
    ('00007', '00002'),
    ('00008', '00003');

INSERT INTO venue (venue_id, venue_name, floor_area, capacity, venue_type, floor, under_renovation, reservation_fee)
VALUES
    ('00001', 'Santos Conference Room', 500, 100, 'Conference Room', 1, FALSE, 200),
    ('00002', 'Bristol Banquet Hall', 800, 300, 'Banquet Room', 2, TRUE, 500),
    ('00003', 'Parkview Meeting Room', 150, 30, 'Meeting Room', 1, FALSE, 100),
    ('00004', 'Oakwood Lecture Hall', 400, 80, 'Lecture Hall', 3, FALSE, 150),
    ('00005', 'Riverside Exhibition Hall', 1000, 500, 'Exhibition Space', 2, FALSE, 300),
    ('00006', 'Greenfield Workshop Room', 250, 50, 'Workshop Room', 4, TRUE, 120),
    ('00007', 'Seaside Lounge Area', 200, 40, 'Lounge', 5, FALSE, 80),
    ('00008', 'Mountainview Training Room', 350, 60, 'Training Room', 1, FALSE, 150),
    ('00009', 'Crescent Auditorium', 1200, 800, 'Auditorium', 3, FALSE, 700),
    ('00010', 'Harborview Gallery', 600, 200, 'Gallery', 2, TRUE, 250),
    ('00011', 'Willowbrook Conference Center', 600, 150, 'Conference Room', 1, FALSE, 220),
    ('00012', 'Silverstone Banquet Hall', 1000, 350, 'Banquet Room', 2, TRUE, 550),
    ('00013', 'Eastview Meeting Room', 200, 40, 'Meeting Room', 1, FALSE, 110),
    ('00014', 'Pinecrest Lecture Hall', 450, 100, 'Lecture Hall', 3, FALSE, 180),
    ('00015', 'Sunset Exhibition Hall', 1200, 600, 'Exhibition Space', 2, FALSE, 320),
    ('00016', 'Horizon Workshop Room', 300, 60, 'Workshop Room', 4, TRUE, 130),
    ('00017', 'Lakeside Lounge Area', 250, 50, 'Lounge', 5, FALSE, 90),
    ('00018', 'Riverbend Training Room', 400, 80, 'Training Room', 1, FALSE, 160),
    ('00019', 'Sunrise Auditorium', 1400, 1000, 'Auditorium', 3, FALSE, 750),
    ('00020', 'Oceanview Gallery', 700, 250, 'Gallery', 2, TRUE, 300);

INSERT INTO venuebuilding (venue_id, building_id)
VALUES
    ('00001', '00001'),
    ('00002', '00001'),
    ('00003', '00002'),
    ('00004', '00002'),
    ('00005', '00003'),
    ('00006', '00003'),
    ('00007', '00004'),
    ('00008', '00004'),
    ('00009', '00005'),
    ('00010', '00005'),
    ('00011', '00001'),
    ('00012', '00001'),
    ('00013', '00002'),
    ('00014', '00002'),
    ('00015', '00003'),
    ('00016', '00003'),
    ('00017', '00004'),
    ('00018', '00004'),
    ('00019', '00005'),
    ('00020', '00005');

INSERT INTO availablevenue (a_venue_id)
VALUES
    ('00001'),
    ('00003'),
    ('00004'),
    ('00005'),
    ('00007'),
    ('00008'),
    ('00009'),
    ('00010'),
    ('00011'),
    ('00013'),
    ('00014'),
    ('00015'),
    ('00017'),
    ('00018'),
    ('00019');

INSERT INTO unavailablevenue (u_venue_id, renovation_date_start, renovation_date_end)
VALUES
    ('00002', '2024-11-01', '2024-11-30'),
    ('00006', '2024-12-01', '2024-12-15'),
    ('00012', '2024-11-15', '2024-12-15'),
    ('00016', '2024-11-20', '2024-12-05'),
    ('00020', '2024-12-01', '2024-12-20');

INSERT INTO amenity (amenity_id, amenity_type, description, quantity)
VALUES
    ('00001', 'Projector', 'High-definition projector for presentations', 1),
    ('00002', 'Microphone', 'Wireless microphone for speakers', 1),
    ('00003', 'Chairs', 'Comfortable seating for attendees', 50),
    ('00004', 'Tables', 'Wooden tables for events', 20),
    ('00005', 'Wi-Fi', 'High-speed internet access for participants', 1),
    ('00006', 'Whiteboard', 'Large whiteboard for presentations', 1),
    ('00007', 'Speakers', 'Surround sound speakers for audio', 2),
    ('00008', 'Projector Screen', 'Large projector screen for presentations', 1),
    ('00009', 'Stage', 'Raised platform for events and performances', 1),
    ('00010', 'Lighting', 'Stage lighting for events', 5),
    ('00011', 'Podium', 'Stand for speakers or presentations', 1),
    ('00012', 'Air Conditioning', 'Climate control for comfort', 1),
    ('00013', 'Sound System', 'Full sound system for events', 1),
    ('00014', 'Water Dispensers', 'Water coolers for guests', 2),
    ('00015', 'Refreshment Station', 'Station for drinks and snacks', 1),
    ('00016', 'Projector', 'HD projector for visual presentations', 1),
    ('00017', 'Laptops', 'Laptops for workshops and meetings', 5),
    ('00018', 'Chairs', 'Seating for training sessions', 30),
    ('00019', 'Whiteboard', 'Whiteboard for brainstorming sessions', 1),
    ('00020', 'Podium', 'Podium for speakers during events', 1),
    ('00021', 'Flipchart', 'Easel with flipchart for brainstorming', 1),
    ('00022', 'Projector Screen', 'Retractable projector screen for presentations', 1),
    ('00023', 'Video Conferencing', 'Equipment for remote video meetings', 1),
    ('00024', 'Kitchenette', 'Small kitchenette for refreshments', 1),
    ('00025', 'Soundproofing', 'Soundproof walls for privacy', 1),
    ('00026', 'Refrigerator', 'Mini fridge for drinks and snacks', 1),
    ('00027', 'Microwave', 'Microwave for reheating food', 1),
    ('00028', 'Notebook', 'Notebooks for attendees', 50),
    ('00029', 'Pens', 'Pens for attendees', 50),
    ('00030', 'Projector Stand', 'Stand for placing projector during events', 1);

INSERT INTO amenityvenue (amenity_id, venue_id)
VALUES
    ('00001', '00001'), ('00002', '00001'),
    ('00003', '00002'), ('00004', '00002'),
    ('00005', '00003'),
    ('00006', '00004'),
    ('00007', '00005'), ('00008', '00005'),
    ('00009', '00006'),
    ('00010', '00007'),
    ('00011', '00008'), ('00012', '00008'),
    ('00013', '00009'),
    ('00014', '00010'),
    ('00015', '00011'), ('00016', '00011'),
    ('00017', '00012'), ('00018', '00012'),
    ('00019', '00014'),
    ('00020', '00015'),
    ('00021', '00016'),
    ('00022', '00017'), ('00023', '00017'),
    ('00024', '00018'), ('00025', '00018'),
    ('00026', '00019'), ('00027', '00019'),
    ('00028', '00020'), ('00029', '00020'), ('00030', '00020');

INSERT INTO customer (customer_id, customer_first_name, customer_middle_initial, customer_last_name, birth_date)
VALUES
    ('00001', 'Angelo', 'A', 'Sese', '1985-06-15'),
    ('00002', 'Bal', 'B', 'Valencia', '1990-09-22'),
    ('00003', 'Catle', 'C', 'Espiritu', '1988-11-30');

INSERT INTO reservation (reservation_id, customer_id, venue_id, number_of_participants, date_start, date_end)
VALUES
    ('00001', '00001', '00001', 50, '2024-12-01', '2024-12-03'),
    ('00002', '00001', '00002', 100, '2024-12-10', '2024-12-12'),
    ('00003', '00002', '00003', 30, '2024-12-05', '2024-12-06'),
    ('00004', '00002', '00004', 80, '2024-12-15', '2024-12-17'),
    ('00005', '00003', '00005', 60, '2024-12-02', '2024-12-04'),
    ('00006', '00003', '00006', 150, '2024-12-08', '2024-12-09');
