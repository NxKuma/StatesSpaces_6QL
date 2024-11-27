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
	agent_id		VARCHAR(5) 		NOT NULL,
	member_name		VARCHAR(255) 	NOT NULL,
	PRIMARY KEY(agent_id, member_name),
	FOREIGN KEY (agent_id) REFERENCES agent(agent_id) ON DELETE RESTRICT
);

CREATE TABLE agentbuilding(
	agent_id		VARCHAR(5) 		NOT NULL,
	building_id		VARCHAR(5) 		NOT NULL,
	PRIMARY KEY(agent_id, building_id),
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
	venue_id		VARCHAR(5) 		NOT NULL,
	building_id		VARCHAR(5)		NOT NULL,
	PRIMARY KEY(venue_id),
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
	amenity_id	VARCHAR(5)	NOT NULL,
	venue_id	VARCHAR(5)	NOT NULL,
	PRIMARY KEY(amenity_id, venue_id),
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


