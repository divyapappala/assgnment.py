import mysql.connector


mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Divya64@",
    database="omnywise",
    auth_plugin="mysql_native_password"
)  
my_cursor =mydb.cursor()
#Which actors have the last name ‘Johansson’
d ="SELECT * from list where l_name = 'Johansson'"
my_cursor.execute(d)
b = my_cursor.fetchall()
print(b)
#Which actors have the first name ‘Scarlett’
c ="SELECT * from list where f_name = 'Scarlett'"
my_cursor.execute(c)
q = my_cursor.fetchall()
print(q)
#How many distinct actors last names are there?
e ="SELECT count(distinct l_name)  from list"
my_cursor.execute(e)
w = my_cursor.fetchall()
print(w)
#Which last names are not repeated?
di = "SELECT l_name from  list GROUP BY l_name HAVING COUNT(*) = 1"
my_cursor.execute(di)
e = my_cursor.fetchall()
print(e)
#Which last names appear more than once?
dv = "SELECT l_name from  list GROUP BY l_name HAVING COUNT(*) >  1"
my_cursor.execute(dv)
p = my_cursor.fetchone()
print(p)
#Which actor has appeared in the most films?
ha = "SELECT actor_id, f_name, l_name, COUNT(films) AS film_count FROM list GROUP BY actor_id, f_name, l_name ORDER BY film_count DESC LIMIT 1"
my_cursor.execute(ha)
f = my_cursor.fetchall()
print(f)
#Is ‘Academy Dinosaur’ available for rent from Store 1?
da = "SELECT * FROM list WHERE films = 'Academy Dinosaur' AND available = 'Store 1'"
my_cursor.execute(da)
m = my_cursor.fetchall()
print(m)
#Insert a record to represent Mary Smith renting ‘Academy Dinosaur’ from Mike Hillyer at Store 1 today .
s = "INSERT INTO list(f_name, l_name, films, available) VALUES ('mary', 'smith', 'Academy Dinosaur', 'store1')"
my_cursor.execute(s)
mydb.commit()

#When is ‘Academy Dinosaur’ due?
sa ="SELECT due from list WHERE films = 'Academy Dinosaur'"
my_cursor.execute(sa)
h = my_cursor.fetchall()
print(h)
#What is that average running time of all the films in the sakila DB?
g = "SELECT AVG(rent) FROM list"
my_cursor.execute(g)
j = my_cursor.fetchall()
print(j)
#What is the average running time of films by category?
u ="select category, avg(rent)as avg_running_time from list group by category"
my_cursor.execute(u)
z=my_cursor.fetchall()
print(z)
my_cursor.close()
mydb.close()