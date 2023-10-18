# DCSC_HWs

This is a repo containing homework's for the Datacenter Scale Computing course

### HW2 - Instructions to Run

##### Executing Docker Compose

-   Start Docker
-   In the **terminal/wsl**, navigate to the folder and make sure the `docker-compose.yml` is within the directory (check using `ls` command)
-   Run the below command

``` bash
docker compose up --build
```

------------------------------------------------------------------------

#### Expected Output

    hw2-etl-1 \| Input data received
    hw2-etl-1 \| ==========
    hw2-etl-1 \| Transforming the Data
    hw2-etl-1 \| Data transformation completed
    hw2-etl-1 \| ==========
    hw2-etl-1 \| Received transformed data.
    hw2-etl-1 \| ==========
    hw2-etl-1 \| Starting up Postgres
    hw2-etl-1 \| Postgres connection successful
    hw2-etl-1 \| Loading Data
    hw2-etl-1 \| ==========
    hw2-etl-1 \| Completed Data Loading!

------------------------------------------------------------------------

**Note:**

The Docker Compose file establishes a mapping between port 5432 in the container image and port 5432 on the local computer. You can confirm the database connection and data loading by manually connecting to the database using the login credentials provided in the docker-compose.yml file under the environment section, through any database management tool such as DBeaver.
