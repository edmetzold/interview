import sqlite3

connection = sqlite3.connect("interview.db")
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE std_member_info(
    member_id INTEGER PRIMARY KEY,
    member_first_name TEXT,
    member_last_name TEXT,
	date_of_birth TEXT,
	main_address TEXT,
	city TEXT,
	state TEXT,
	zip_code INTEGER,
	payer TEXT);
""")

cursor.execute("""
INSERT INTO std_member_info
SELECT
	Person_Id,
	First_Name,
	Last_Name,
	CASE
		WHEN Dob LIKE '__/__/____'
			THEN (substr(Dob,7,4)||'-'||substr(Dob,1,2)||'-'||substr(Dob,4,2))
		ELSE Dob
	END Dob,
	Street_Address,
	CASE
		WHEN State = 'CA'
			THEN 'California'
		ELSE State
	END State,
	City,
	Zip,
	payer
FROM roster_1
WHERE
	CASE
		WHEN eligibility_start_date LIKE '__/__/____'
			THEN (substr(eligibility_start_date,7,4)||'-'||substr(eligibility_start_date,1,2)||'-'||substr(eligibility_start_date,4,2))
		ELSE eligibility_start_date
	END < "2022-05-01"
	AND
	CASE
		WHEN eligibility_end_date LIKE '__/__/____'
			THEN (substr(eligibility_end_date,7,4)||'-'||substr(eligibility_end_date,1,2)||'-'||substr(eligibility_end_date,4,2))
		ELSE eligibility_end_date
	END > "2022-03-31"
UNION
SELECT
	Person_Id,
	First_Name,
	Last_Name,
	CASE
		WHEN Dob LIKE '__/__/____'
			THEN (substr(Dob,7,4)||'-'||substr(Dob,1,2)||'-'||substr(Dob,4,2))
		ELSE Dob
	END Dob,
	Street_Address,
	CASE
		WHEN State = 'CA'
			THEN 'California'
		ELSE State
	END State,
	City,
	Zip,
	payer
FROM roster_2
WHERE
	CASE
		WHEN eligibility_start_date LIKE '__/__/____'
			THEN (substr(eligibility_start_date,7,4)||'-'||substr(eligibility_start_date,1,2)||'-'||substr(eligibility_start_date,4,2))
		ELSE eligibility_start_date
	END < "2022-05-01"
	AND
	CASE
		WHEN eligibility_end_date LIKE '__/__/____'
			THEN (substr(eligibility_end_date,7,4)||'-'||substr(eligibility_end_date,1,2)||'-'||substr(eligibility_end_date,4,2))
		ELSE eligibility_end_date
	END > "2022-03-31"
UNION
SELECT
	Person_Id,
	First_Name,
	Last_Name,
	CASE
		WHEN Dob LIKE '__/__/____'
			THEN (substr(Dob,7,4)||'-'||substr(Dob,1,2)||'-'||substr(Dob,4,2))
		ELSE Dob
	END Dob,
	Street_Address,
	CASE
		WHEN State = 'CA'
			THEN 'California'
		ELSE State
	END State,
	City,
	Zip,
	payer
FROM roster_3
WHERE
	CASE
		WHEN eligibility_start_date LIKE '__/__/____'
			THEN (substr(eligibility_start_date,7,4)||'-'||substr(eligibility_start_date,1,2)||'-'||substr(eligibility_start_date,4,2))
		ELSE eligibility_start_date
	END < "2022-05-01"
	AND
	CASE
		WHEN eligibility_end_date LIKE '__/__/____'
			THEN (substr(eligibility_end_date,7,4)||'-'||substr(eligibility_end_date,1,2)||'-'||substr(eligibility_end_date,4,2))
		ELSE eligibility_end_date
	END > "2022-03-31"
UNION
SELECT
	Person_Id,
	First_Name,
	Last_Name,
	CASE
		WHEN Dob LIKE '__/__/____'
			THEN (substr(Dob,7,4)||'-'||substr(Dob,1,2)||'-'||substr(Dob,4,2))
		ELSE Dob
	END Dob,
	Street_Address,
	CASE
		WHEN State = 'CA'
			THEN 'California'
		ELSE State
	END State,
	City,
	Zip,
	payer
FROM roster_4
WHERE
	CASE
		WHEN eligibility_start_date LIKE '__/__/____'
			THEN (substr(eligibility_start_date,7,4)||'-'||substr(eligibility_start_date,1,2)||'-'||substr(eligibility_start_date,4,2))
		ELSE eligibility_start_date
	END < "2022-05-01"
	AND
	CASE
		WHEN eligibility_end_date LIKE '__/__/____'
			THEN (substr(eligibility_end_date,7,4)||'-'||substr(eligibility_end_date,1,2)||'-'||substr(eligibility_end_date,4,2))
		ELSE eligibility_end_date
	END > "2022-03-31"
UNION
SELECT
	Person_Id,
	First_Name,
	Last_Name,
	CASE
		WHEN Dob LIKE '__/__/____'
			THEN (substr(Dob,7,4)||'-'||substr(Dob,1,2)||'-'||substr(Dob,4,2))
		ELSE Dob
	END Dob,
	Street_Address,
	CASE
		WHEN State = 'CA'
			THEN 'California'
		ELSE State
	END State,
	City,
	Zip,
	payer
FROM roster_5
WHERE
	CASE
		WHEN eligibility_start_date LIKE '__/__/____'
			THEN (substr(eligibility_start_date,7,4)||'-'||substr(eligibility_start_date,1,2)||'-'||substr(eligibility_start_date,4,2))
		ELSE eligibility_start_date
	END < "2022-05-01"
	AND
	CASE
		WHEN eligibility_end_date LIKE '__/__/____'
			THEN (substr(eligibility_end_date,7,4)||'-'||substr(eligibility_end_date,1,2)||'-'||substr(eligibility_end_date,4,2))
		ELSE eligibility_end_date
	END > "2022-03-31"
;
""")

################################################
# How many distinct members are eligible in April 2022?
################################################
cursor.execute("""
SELECT COUNT(*) FROM
(SELECT DISTINCT member_id
FROM std_member_info);
""")

print("How many distinct members are eligible in April 2022?")
print(cursor.fetchone()[0])
print()

################################################
# How many members were included more than once?
################################################
cursor.execute("""
SELECT COUNT(*) FROM
(SELECT Person_Id, COUNT(*) FROM
(SELECT Person_Id FROM roster_1
UNION ALL
SELECT Person_Id FROM roster_2
UNION ALL
SELECT Person_Id FROM roster_3
UNION ALL
SELECT Person_Id FROM roster_4
UNION ALL
SELECT Person_Id FROM roster_5
ORDER BY Person_Id)
GROUP BY Person_Id
HAVING COUNT(*) > 1);
""")

print("How many members were included more than once?")
print(cursor.fetchone()[0])
print()

################################################
# What is the breakdown of members by payer?
################################################
cursor.execute("""
SELECT payer, count(*) FROM std_member_info
GROUP BY payer;
""")

print("What is the breakdown of members by payer?")
for row in cursor.fetchall():
	print(row[0] + ": " + str(row[1]))
print()

################################################
# How many members live in a zip code with a food_access_score lower than 2?
################################################
cursor.execute("""
SELECT COUNT(*) FROM
(SELECT std_member_info.member_id, std_member_info.zip_code, model_scores_by_zip.food_access_score
FROM std_member_info
INNER JOIN model_scores_by_zip ON std_member_info.zip_code = model_scores_by_zip.zcta
WHERE model_scores_by_zip.food_access_score < 2
ORDER BY model_scores_by_zip.food_access_score);
""")

print("How many members live in a zip code with a food_access_score lower than 2?")
print(cursor.fetchone()[0])
print()

################################################
# What is the average social isolation score for the members?
################################################
cursor.execute("""
SELECT AVG(model_scores_by_zip.social_isolation_score)
FROM std_member_info
INNER JOIN model_scores_by_zip ON std_member_info.zip_code = model_scores_by_zip.zcta;
""")

print("What is the average social isolation score for the members?")
print(cursor.fetchone()[0])
print()

################################################
# Which members live in the zip code with the highest algorex_sdoh_composite_score?
################################################
cursor.execute("""
SELECT zcta, MAX(algorex_sdoh_composite_score)
FROM model_scores_by_zip;
""")

highest_zip = cursor.fetchone()[0]

print("highest zip = ",highest_zip)

cursor.execute("""
SELECT *
FROM std_member_info
WHERE zip_code = ?;
""",
(highest_zip,))

print("Which members live in the zip code with the highest algorex_sdoh_composite_score?")
for row in cursor.fetchall():
	print(row[1] + " " + row[2])
print()

################################################

connection.close()