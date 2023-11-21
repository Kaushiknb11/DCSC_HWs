# Data Center Scale Computing

### CSCI-5253 - Fall 2023 - Dr. Alex Yarosh
---

### About the Repository
This is a repo containing all the homework assignments for the Datacenter Scale Computing course

---

### HW3 Airflow -- Instructions to Run

##### Executing Docker Compose

* Instantiate Docker
  
*  Ensure that the 'docker-compose.yml' file is present in the directory by checking with the 'ls' command.

* In the terminal or WSL, execute the following commands:

```bash
docker compose up
```

---

#### Snippets from the actual run

### Visualization of Airflow DAG
![Image 11-20-23 at 7 36 PM](https://github.com/Kaushiknb11/DCSC_HWs/assets/107951993/7940d957-7efc-415f-9234-7268b03bc750)

<img width="1132" alt="Screenshot 2023-11-20 at 7 19 13 PM" src="https://github.com/Kaushiknb11/DCSC_HWs/assets/107951993/a2e9f450-ce6c-427e-837a-eb270b63b2ad">

## Cloud Data Storage - S3 Bucket
<img width="1365" alt="Screenshot 2023-11-20 at 8 05 42 PM" src="https://github.com/Kaushiknb11/DCSC_HWs/assets/107951993/f60663f0-08c6-4b84-928b-adef1ab8ac79">
<img width="1360" alt="Screenshot 2023-11-20 at 8 06 37 PM" src="https://github.com/Kaushiknb11/DCSC_HWs/assets/107951993/f2fb3205-1986-4b66-ad30-cf2657ef7209">
<img width="1371" alt="Screenshot 2023-11-20 at 8 06 46 PM" src="https://github.com/Kaushiknb11/DCSC_HWs/assets/107951993/3a02650e-63d9-4f7f-a900-0a9e66d26f09">
<img width="1363" alt="Screenshot 2023-11-20 at 8 06 56 PM" src="https://github.com/Kaushiknb11/DCSC_HWs/assets/107951993/3ca9b16a-7dda-4128-8494-6c7474e2c61c">

## Cloud Relational Database (Amazon RDS)
<img width="1141" alt="Screenshot 2023-11-20 at 7 23 43 PM" src="https://github.com/Kaushiknb11/DCSC_HWs/assets/107951993/3b57b7f5-cd7a-4693-9878-2b53b86fbb88">

## Database connectivity test with Cloud RDS via DBeaver
<img width="1318" alt="Screen Shot 2023-11-20 at 7 45 25 PM" src="https://github.com/Kaushiknb11/DCSC_HWs/assets/107951993/59305219-4f25-4563-8784-2884c19548fd">

## Data Loading in the ETL Procedure
<img width="1462" alt="Screen Shot 2023-11-20 at 7 46 04 PM" src="https://github.com/Kaushiknb11/DCSC_HWs/assets/107951993/1e40b165-781e-4f4e-98a3-1f96493917a0">

---

### Note on Credentials for Successful Execution

- To run the homework-3 code successfully, go to `/dags/secrets.env`, replace the credential items with your own credentials, and then execute the 'docker-compose.yml'. 
- Additionally, to establish the Primary Key and Foreign Key relationships between the tables, it is recommended to run the `init.sql` file in dbeaver.
