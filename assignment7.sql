create table list (actor_id int,f_name varchar(255),l_name varchar(255),due int,rent int,films varchar(255),category varchar(255),avialable varchar(255));
select * from list;
insert into list values
	      (1, 'Scarlett', 'Johansson', 10, 5, 'Academy Dinosaur', 'Action','yes'),
		  (2, 'Jane', 'Smith', 15, 7, 'lionking', 'Drama','no'),
          (3, 'Bob', 'Johansson', 8, 4, 'jungle book', 'Comedy','yes'),
          (4,'john','Doe',12,5,'angrybird','violence','no');
#Which actors have the first name ‘Scarlett’
select * from list where f_name = 'Scarlett';
#Which actors have the last name ‘Johansson’
select * from list where l_name = 'johansson';
#How many distinct actors last names are there?
select count(distinct l_name)  from list;
#Which last names are not repeated?
select l_name from  list GROUP BY l_name HAVING COUNT(*) = 1;
#Which last names appear more than once?
select l_name from  list GROUP BY l_name HAVING COUNT(*) >  1;
#Which actor has appeared in the most films?
select  actor_id, f_name, l_name, COUNT(films) AS film_count
FROM list
GROUP BY actor_id, f_name, l_name
ORDER BY film_count DESC
LIMIT 1;
#Is ‘Academy Dinosaur’ available for rent from Store 1?
select * FROM list where films = 'Academy Dinosaur' AND avialable = 'Store 1';
#Insert a record to represent Mary Smith renting ‘Academy Dinosaur’ from Mike Hillyer at Store 1 today .
insert into list(f_name,l_name,films,avialable) values ('mary','smith','Academy Dinosaur','store1'); 
#When is ‘Academy Dinosaur’ due?
select due from list WHERE films = 'Academy Dinosaur';
#What is that average running time of all the films in the sakila DB?
select avg(rent) from list;
#What is the average running time of films by category?
select category, avg(rent)as avg_running_time from list group by category;






