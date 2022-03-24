# TEST-TASK

*1. Consider influenza epidemics for 2-person families. The probability is 21% that at least one has disease. The probability that the husband has contracted influenza is 15% while the probability that both the wife and husband have contracted the disease is 10%. What is the probability that the wife has influenza?*
---
First option:
------
```
A - wife is sick
B - husband is sick

There are 4 outcomes:
- a1: A and B - both are sick
- a2: A^ and B - wife is not sick
- a3: A and B^ - husband is not sick
- a4: A^ and B^ - both are not sick

a1 + a2 = 0.15 - husband is sick
a1 + a2 + a3 = 0.21 - at least one is sick
a1 = 0.1 - both are sick
a1 + a3 = ? - wife is sick 

0.15 + a3 = 0.21; a3 = 0.06 => 0.1 + 0.06 = 0.16 - wife is sick
```

Second option:
------
```
A - wife is sick
B - husband is sick

A⋂B - both are sick
A⋃B - at least one is sick

P(A⋃B) = P(A) + P(B) - P(A⋂B)
0.21 = P(A) + 0.15 - 0.1
0.21 = P(A) + 0.05
P(A) = 0.16 - wife is sick
```

*2. Write a PostgreSQL query to find the following: How many tons worth of fruit does an average seller have? How many sellers have at least one client who purchased their fruit?* 
---

<img width="323" alt="Снимок экрана 2022-03-24 в 11 43 44" src="https://user-images.githubusercontent.com/44771725/159888525-3b978522-d088-491b-a223-73154bf19531.png">

---

**Creating tables:**

```
create table seller_info (seller_id integer, fruit_id integer, fruit_weight integer);
		insert into seller_info (seller_id, fruit_id, fruit_weight) values (1, 256, 10);
		insert into seller_info (seller_id, fruit_id, fruit_weight) values (2, 123, 5);
		insert into seller_info (seller_id, fruit_id, fruit_weight) values (3, 345, 6);
		select * from seller_info;

create table consumption_info (fruit_id integer, seller_id integer, client_id integer, quantity_purchased_fruit float);
		insert into consumption_info (fruit_id, seller_id, client_id, quantity_purchased_fruit) values (256, 1, 111, 10);
		insert into consumption_info (fruit_id, seller_id, client_id, quantity_purchased_fruit) values (123, 2, 222, 5);
    		insert into consumption_info (fruit_id, seller_id, client_id, quantity_purchased_fruit) values (345, 3, 333, 1);
    		insert into consumption_info (fruit_id, seller_id, client_id, quantity_purchased_fruit) values (345, 3, 444, 2);
		select * from consumption_info;
```
    
**Requests:**

1. ```SELECT seller_id, SUM(fruit_weight) AS all_fruit_weight FROM seller_info GROUP BY seller_id;```
2. ```SELECT seller_id, COUNT(client_id) as count_client FROM consumption_info GROUP BY seller_id HAVING COUNT(client_id) >= 1;```

*3. Solution in lucky.py file*
---

*4. Completed all tasks in weather_processing.py file*
---
Some tasks have been merged into one or the order of execution has been changed because, in my opinion, it is more logical.

*5. Solution in sum_in_array.py file*
---
