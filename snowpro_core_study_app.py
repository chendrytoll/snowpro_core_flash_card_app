import streamlit as st

st.title("SnowPro Core Exam Flash Cards")
st.markdown("""
This interactive study app provides a breakdown for each key item from the SnowPro Core study guide. 
Select a domain from the sidebar and click on each flash card to see detailed explanations, background context, 
practical importance, and relevant Snowflake commands and examples.
""")

# An exhaustive mapping of each item to detailed explanations without bullet symbols
flash_cards = {
    "Domain 1.0: Snowflake AI Data Cloud Features and Architecture": {
        "Elastic Storage": (
            "Elastic Storage is the backbone of Snowflake’s data management, allowing storage to scale automatically as data volume increases.\n\n"
            "Concept & Architecture: Data is stored in a columnar format on cloud storage (such as AWS S3, Azure Blob Storage, or Google Cloud Storage). The system abstracts physical storage details so that users do not have to manage partitions or disks.\n\n"
            "Benefits: This separation of storage from compute means you only pay for the storage you use, with virtually limitless capacity. It also allows for high durability and availability with built‐in redundancy and replication across data centers.\n\n"
            "Usage: There is no direct SQL command to ‘enable’ elastic storage—it is inherent to the Snowflake architecture. Understanding this concept is crucial when planning for cost optimization and scalability."
        ),
        "Elastic Compute": (
            "Elastic Compute refers to the dynamic provisioning of compute resources via Snowflake’s virtual warehouses.\n\n"
            "Concept & Architecture: Compute resources can scale up or down automatically based on workload demands. Each virtual warehouse operates independently, meaning that multiple warehouses can run concurrently without resource contention.\n\n"
            "Benefits: This elasticity ensures consistent query performance and cost efficiency because you can pause or scale resources as needed.\n\n"
            "Commands & Examples:\n"
            "  - Create a warehouse: `CREATE WAREHOUSE my_warehouse WITH WAREHOUSE_SIZE = 'MEDIUM' AUTO_SUSPEND = 300 AUTO_RESUME = TRUE;`\n"
            "  - Modify a warehouse: `ALTER WAREHOUSE my_warehouse SET WAREHOUSE_SIZE = 'LARGE';`"
        ),
        "Snowflake’s Three Distinct Layers": (
            "Snowflake’s architecture is divided into three independent layers, each of which scales separately:\n\n"
            "Storage Layer: Manages all persistent data in a highly optimized, columnar format.\n"
            "Compute Layer: Consists of virtual warehouses that execute queries and process data.\n"
            "Cloud Services Layer: Provides infrastructure services including metadata management, authentication, security, and query optimization.\n\n"
            "Benefits: This separation allows each layer to be independently scaled and optimized, providing high performance and flexibility.\n\n"
            "Usage: Although these layers work behind the scenes, understanding their roles helps in troubleshooting and tuning performance."
        ),
        "Cloud Partner Categories": (
            "Snowflake’s multi-cloud strategy is built on partnerships with major cloud providers.\n\n"
            "Partners: Typically includes AWS, Microsoft Azure, and Google Cloud Platform.\n\n"
            "Benefits: This multi-cloud approach offers flexibility in terms of geographic availability, pricing, and integration with native cloud services.\n\n"
            "Implementation: The underlying integration is managed by Snowflake. Users select their cloud provider during account provisioning, and the platform optimizes its performance based on that provider’s infrastructure."
        ),
        "Overview of Snowflake Editions": (
            "Snowflake offers several editions—such as Standard, Enterprise, and Business Critical—each with a set of features tailored to different business needs.\n\n"
            "Features & Differences: Higher editions typically include enhanced security, better performance features, additional data protection capabilities, and more extensive support options.\n\n"
            "Benefits: Choosing the appropriate edition helps align the platform’s capabilities with organizational requirements for compliance, scalability, and cost management.\n\n"
            "Usage: The edition is selected at the time of account setup and influences available options, rather than being something configured via SQL."
        ),
        "Snowsight": (
            "Snowsight is Snowflake’s modern web-based user interface that offers an intuitive environment for query building, data visualization, and monitoring.\n\n"
            "Features: It allows users to write and execute queries, create dashboards, and explore data without needing specialized SQL clients.\n\n"
            "Benefits: Simplifies data interaction for users of all skill levels and provides rich graphical representations for analytics.\n\n"
            "Usage: Accessed via your browser without additional installation. It is the go-to tool for interactive data exploration."
        ),
        "SnowSQL": (
            "SnowSQL is the official command-line client provided by Snowflake for interacting with the platform.\n\n"
            "Features: Enables script-based interactions, automation of queries, and batch processing.\n\n"
            "Benefits: It is essential for administrative tasks, debugging, and automation within CI/CD pipelines.\n\n"
            "Commands & Examples:\n"
            "  - Basic query: `snowsql -q \"SELECT CURRENT_TIMESTAMP();\"`\n"
            "  - Connecting to a specific account: `snowsql -a <account> -u <user>`"
        ),
        "Snowflake Connectors": (
            "Connectors are libraries available for multiple programming languages (e.g., Python, Java, Node.js) that allow developers to integrate Snowflake with their applications.\n\n"
            "Features: They provide functions and methods to execute SQL commands, fetch results, and manage connections programmatically.\n\n"
            "Benefits: Simplify the integration of Snowflake into data pipelines, machine learning workflows, and application backends.\n\n"
            "Usage: Install via package managers (e.g., pip for Python) and use in your application code to interact with Snowflake seamlessly."
        ),
        "Snowflake Drivers": (
            "Drivers such as ODBC and JDBC enable third-party applications, business intelligence tools, and ETL platforms to connect to Snowflake.\n\n"
            "Features: These drivers support real-time querying, metadata operations, and secure data transfers between applications and Snowflake.\n\n"
            "Benefits: They facilitate integration with enterprise tools, enabling a smooth flow of data across systems.\n\n"
            "Usage: Configuration typically involves setting up connection strings and installing the appropriate driver on the client machine."
        ),
        "Snowpark": (
            "Snowpark is a developer framework that extends Snowflake’s capabilities to languages like Python, Java, and Scala.\n\n"
            "Features: Provides DataFrame APIs, user-defined functions, and methods to perform complex data transformations within Snowflake.\n\n"
            "Benefits: Enables developers to write custom data applications without moving data out of Snowflake, thereby maintaining security and performance.\n\n"
            "Usage: Integrate Snowpark into your development environment and leverage its API to perform operations such as data cleansing, aggregation, and machine learning."
        ),
        "SnowCD": (
            "SnowCD refers to continuous delivery practices within the Snowflake ecosystem aimed at streamlining deployments and updates of data pipelines and SQL code.\n\n"
            "Concept: It integrates with modern CI/CD tools to automate testing and deployment processes, ensuring that changes to code and configuration are delivered rapidly and reliably.\n\n"
            "Benefits: Reduces manual intervention and errors, thereby accelerating innovation and ensuring consistency across environments.\n\n"
            "Usage: While there is no direct SQL command for SnowCD, it relies on external automation tools configured to work with Snowflake’s APIs and SQL endpoints."
        ),
        "Databases": (
            "In Snowflake, a database is a logical container for schemas, tables, views, and other database objects.\n\n"
            "Concept: It provides a way to logically group related data and manage access and security at a higher level.\n\n"
            "Benefits: Helps organize data, simplify backup and recovery, and enforce security policies across related objects.\n\n"
            "Commands & Examples:\n"
            "  - Create a database: `CREATE DATABASE my_database;`\n"
            "  - Drop a database: `DROP DATABASE my_database;`"
        ),
        "Stages": (
            "Stages are named locations in Snowflake (either internal or external) where data files are stored temporarily for loading or unloading.\n\n"
            "Concept: They act as intermediaries between raw data in cloud storage and Snowflake tables.\n\n"
            "Benefits: Facilitate data ingestion and extraction while abstracting the underlying storage details.\n\n"
            "Commands & Examples:\n"
            "  - Create an internal stage: `CREATE STAGE my_stage;`\n"
            "  - List files in a stage: `LIST @my_stage;`"
        ),
        "Schema Types": (
            "Schemas provide a further subdivision within databases, allowing objects to be organized into logical groups.\n\n"
            "Concept: They help in applying granular access controls and organizing objects based on functionality or department.\n\n"
            "Benefits: Enhance security and manageability by segregating objects into different namespaces.\n\n"
            "Commands & Examples:\n"
            "  - Create a schema: `CREATE SCHEMA my_schema;`"
        ),
        "Table Types": (
            "Snowflake supports multiple table types—permanent, transient, and temporary—each with distinct properties regarding data retention and cost.\n\n"
            "Concept: Permanent tables offer full data protection and Time Travel, transient tables are optimized for temporary data with lower costs, and temporary tables exist only for the duration of a session.\n\n"
            "Benefits: Choosing the right table type helps optimize storage costs and performance based on use case.\n\n"
            "Commands & Examples:\n"
            "  - Create a permanent table: `CREATE TABLE my_table (id INT, name STRING);`\n"
            "  - Create a transient table: `CREATE TRANSIENT TABLE temp_table (id INT, data STRING);`"
        ),
        "View Types": (
            "Views are virtual tables defined by SQL queries that present data from one or more underlying tables.\n\n"
            "Concept: They provide a layer of abstraction, allowing users to query complex data structures without accessing the base tables directly.\n\n"
            "Benefits: Enhance security by limiting data exposure and simplifying complex joins or aggregations into a single queryable object.\n\n"
            "Commands & Examples:\n"
            "  - Create a view: `CREATE VIEW my_view AS SELECT id, name FROM my_table;`"
        ),
        "Data Types": (
            "Snowflake supports a wide range of data types including numeric, string, date/time, and semi-structured types such as VARIANT, OBJECT, and ARRAY.\n\n"
            "Concept: Correct data type selection ensures data integrity, optimal performance, and efficient storage.\n\n"
            "Benefits: Using the appropriate data type can lead to better compression, faster query execution, and more accurate results.\n\n"
            "Usage: Data types are specified during table creation and cannot be arbitrarily changed without altering the table structure."
        ),
        "User Defined Functions (UDFs)": (
            "User Defined Functions (UDFs) let you extend Snowflake’s built-in functionality by creating custom scalar functions in SQL or JavaScript.\n\n"
            "Concept: UDFs encapsulate business logic or repetitive calculations so that they can be reused across multiple queries.\n\n"
            "Benefits: Simplify complex operations and ensure consistency by centralizing logic in a single function that can be updated when needed.\n\n"
            "Commands & Examples:\n"
            "  - Create a UDF:\n"
            "    ```sql\n"
            "    CREATE OR REPLACE FUNCTION my_udf(x NUMBER)\n"
            "    RETURNS NUMBER\n"
            "    LANGUAGE SQL\n"
            "    AS 'x * 2';\n"
            "    ```"
        ),
        "User Defined Table Functions (UDTFs)": (
            "UDTFs return a table (a set of rows) rather than a single scalar value.\n\n"
            "Concept: They are useful when you need to transform one row of input data into multiple rows of output data, such as splitting a delimited string into individual elements.\n\n"
            "Benefits: Enhance data transformation capabilities by integrating custom logic that outputs relational data directly usable in queries.\n\n"
            "Commands & Examples:\n"
            "  - Create a UDTF:\n"
            "    ```sql\n"
            "    CREATE OR REPLACE TABLE FUNCTION my_udtf(input STRING)\n"
            "    RETURNS TABLE (word STRING)\n"
            "    LANGUAGE SQL\n"
            "    AS $$\n"
            "      SELECT VALUE AS word FROM TABLE(FLATTEN(INPUT => SPLIT(input, ' ')));\n"
            "    $$;\n"
            "    ```"
        ),
        "Stored Procedures": (
            "Stored procedures allow you to encapsulate complex procedural logic and control flow within Snowflake.\n\n"
            "Concept: They support conditional logic, loops, and error handling, enabling automation of multi-step processes or data transformations.\n\n"
            "Benefits: Ideal for automating repetitive tasks, performing batch processing, or orchestrating complex workflows, all executed on the server side.\n\n"
            "Commands & Examples:\n"
            "  - Create a stored procedure:\n"
            "    ```sql\n"
            "    CREATE OR REPLACE PROCEDURE my_procedure()\n"
            "    RETURNS STRING\n"
            "    LANGUAGE JAVASCRIPT\n"
            "    AS $$\n"
            "      // your procedural logic here\n"
            "      return 'Procedure executed';\n"
            "    $$;\n"
            "    ```"
        ),
        "Streams": (
            "Streams in Snowflake track changes (inserts, updates, deletes) in a table for change data capture purposes.\n\n"
            "Concept: They record data modifications so that only the incremental changes can be processed in downstream tasks, rather than reprocessing the entire table.\n\n"
            "Benefits: Improve efficiency in data pipelines, reduce processing time, and facilitate real-time analytics.\n\n"
            "Commands & Examples:\n"
            "  - Create a stream: `CREATE STREAM my_stream ON TABLE my_table;`"
        ),
        "Tasks": (
            "Tasks are used to schedule and automate the execution of SQL statements or stored procedures.\n\n"
            "Concept: They allow you to define recurring jobs that can refresh materialized views, load data incrementally, or perform routine maintenance.\n\n"
            "Benefits: Automate repetitive processes and ensure that data stays current without manual intervention.\n\n"
            "Commands & Examples:\n"
            "  - Create a task:\n"
            "    ```sql\n"
            "    CREATE OR REPLACE TASK my_task\n"
            "    WAREHOUSE = my_warehouse\n"
            "    SCHEDULE = 'USING CRON 0 * * * *'\n"
            "    AS\n"
            "    CALL my_procedure();\n"
            "    ```"
        ),
        "Pipes": (
            "Pipes are integral to Snowpipe, the continuous data ingestion service.\n\n"
            "Concept: A pipe defines a continuous loading process by linking a stage (where files are dropped) with a target table. It monitors the stage and automatically triggers the load process when new data files are detected.\n\n"
            "Benefits: Minimizes latency between data arrival and availability for querying, and automates the ingestion of streaming or near-real-time data.\n\n"
            "Commands & Examples:\n"
            "  - Create a pipe:\n"
            "    ```sql\n"
            "    CREATE OR REPLACE PIPE my_pipe AS\n"
            "    COPY INTO my_table\n"
            "    FROM @my_stage\n"
            "    FILE_FORMAT = (FORMAT_NAME = 'my_format');\n"
            "    ```"
        ),
        "Shares": (
            "Shares allow you to securely expose data stored in Snowflake to other Snowflake accounts without physically copying the data.\n\n"
            "Concept: Data sharing is achieved by creating a share object that specifies which databases, schemas, or tables are available to external consumers.\n\n"
            "Benefits: Enables collaboration and data monetization while maintaining complete control over access permissions.\n\n"
            "Commands & Examples:\n"
            "  - Create a share: `CREATE SHARE my_share;`\n"
            "  - Grant access: `GRANT USAGE ON DATABASE my_database TO SHARE my_share;`"
        ),
        "Sequences": (
            "Sequences generate unique, sequential numeric values often used to populate primary key columns.\n\n"
            "Concept: They are maintained independently of table data, ensuring that generated values are unique and do not require locking or table scanning.\n\n"
            "Benefits: Facilitate the creation of surrogate keys and support incremental value generation for large datasets.\n\n"
            "Commands & Examples:\n"
            "  - Create a sequence: `CREATE SEQUENCE my_sequence START WITH 1 INCREMENT BY 1;`"
        ),
        "Micro-partitions": (
            "Micro-partitions are the fundamental units of data storage in Snowflake.\n\n"
            "Concept: When data is loaded into a table, it is automatically divided into contiguous, immutable micro-partitions that contain between 50 MB and 500 MB of uncompressed data.\n\n"
            "Benefits: This design allows for efficient compression, faster query performance through partition pruning, and automatic data organization without user intervention.\n\n"
            "Usage: While there is no command to manage micro-partitions directly, understanding their role helps in optimizing queries and comprehending storage costs."
        ),
        "Data Clustering": (
            "Data clustering organizes table data based on specified columns to improve query performance.\n\n"
            "Concept: By specifying clustering keys, Snowflake can physically co-locate similar data in the same micro-partitions.\n\n"
            "Benefits: Reduces the amount of data scanned during queries, especially when filtering on the clustered columns, leading to faster response times and lower compute costs.\n\n"
            "Commands & Examples:\n"
            "  - Define clustering on table creation: `CREATE TABLE my_table (col1 INT, col2 STRING) CLUSTER BY (col1);`"
        ),
        "Data Storage Monitoring": (
            "Snowflake provides extensive monitoring tools to track storage usage, performance, and growth trends.\n\n"
            "Concept: Administrative views (such as those in the INFORMATION_SCHEMA or ACCOUNT_USAGE schemas) display details about data storage consumption, partition usage, and query performance.\n\n"
            "Benefits: Enables proactive management of storage costs, identification of performance bottlenecks, and informed decision-making regarding data lifecycle management.\n\n"
            "Usage: Regularly review views such as TABLE_STORAGE_METRICS and QUERY_HISTORY to monitor system performance and optimize resource allocation."
        )
    },
    "Domain 2.0: Account Access and Security": {
        "Network Security and Policies": (
            "Network security in Snowflake is enforced by configuring IP whitelists and network policies that restrict which IP addresses can access your account.\n\n"
            "Concept & Architecture: Limiting access to trusted networks reduces the attack surface and ensures that only authorized users can connect to your Snowflake instance.\n\n"
            "Benefits: Enhances overall account security and mitigates risks from unauthorized access attempts.\n\n"
            "Commands & Examples:\n"
            "  - Modify network policy: `ALTER NETWORK POLICY my_policy SET ALLOWED_IP_LIST = ('192.168.1.0/24');`"
        ),
        "Multi-Factor Authentication (MFA)": (
            "Multi-Factor Authentication (MFA) requires users to provide additional verification (such as a one-time code) beyond just a password.\n\n"
            "Concept: MFA introduces a second layer of defense, making it significantly harder for attackers to gain unauthorized access even if a password is compromised.\n\n"
            "Benefits: Provides robust protection against phishing and password theft, ensuring that access is granted only after successful verification of multiple credentials.\n\n"
            "Usage: Configured via the Snowflake web interface and integrated with third-party authentication apps."
        ),
        "Federated Authentication": (
            "Federated authentication integrates external identity providers (such as Okta or Azure AD) with Snowflake, allowing for Single Sign-On (SSO).\n\n"
            "Concept: This approach leverages corporate identity systems so that users can authenticate with their existing credentials.\n\n"
            "Benefits: Centralizes user management, reduces password fatigue, and improves security by relying on trusted external authentication systems.\n\n"
            "Usage: Setup is handled through the Snowflake UI and your identity provider’s configuration; no specific SQL command is required."
        ),
        "Key Pair Authentication": (
            "Key pair authentication uses a public/private cryptographic key pair to secure connections to Snowflake.\n\n"
            "Concept: Instead of relying solely on passwords, the user holds a private key while the corresponding public key is stored in Snowflake.\n\n"
            "Benefits: Provides strong, certificate-based authentication that is particularly useful for automated processes where interactive password entry is not feasible.\n\n"
            "Usage: Keys are generated externally and then registered with Snowflake via account settings."
        ),
        "Single Sign-On (SSO)": (
            "Single Sign-On (SSO) simplifies user access by allowing a single set of credentials to authenticate across multiple applications, including Snowflake.\n\n"
            "Concept: It centralizes user authentication, reducing the need to remember multiple passwords and streamlining the login process.\n\n"
            "Benefits: Enhances security through centralized identity management and improves user experience.\n\n"
            "Usage: SSO is typically configured through an external identity provider and integrated into Snowflake’s login process without any direct SQL commands."
        ),
        "Overview of Access Control Frameworks": (
            "Snowflake employs a role-based access control (RBAC) model to manage permissions across all objects.\n\n"
            "Concept: Instead of granting permissions directly to users, privileges are assigned to roles. Roles can be hierarchically organized so that higher-level roles inherit permissions from subordinate roles.\n\n"
            "Benefits: This simplifies administration, ensures consistency in permission management, and makes it easier to audit access controls.\n\n"
            "Usage: Use GRANT and REVOKE commands to manage privileges across roles and users."
        ),
        "Access Control Privileges": (
            "Privileges in Snowflake determine what actions a user or role can perform on database objects such as tables, views, and schemas.\n\n"
            "Concept: Privileges include actions like SELECT, INSERT, UPDATE, DELETE, and more specialized operations.\n\n"
            "Benefits: Fine-grained privilege management ensures that users have exactly the level of access required, enhancing data security and compliance.\n\n"
            "Commands & Examples:\n"
            "  - Grant a privilege: `GRANT SELECT ON TABLE my_table TO ROLE analyst;`"
        ),
        "How Privileges Can Be Granted and Revoked": (
            "Privileges are managed dynamically in Snowflake using the GRANT and REVOKE commands.\n\n"
            "Concept: Administrators can grant specific privileges to roles or users, and revoke them as needed.\n\n"
            "Benefits: This flexibility allows rapid adaptation to changing security requirements and business needs while maintaining tight control over data access.\n\n"
            "Commands & Examples:\n"
            "  - Grant privilege: `GRANT INSERT ON DATABASE mydb TO ROLE data_loader;`\n"
            "  - Revoke privilege: `REVOKE INSERT ON DATABASE mydb FROM ROLE data_loader;`"
        ),
        "Role Hierarchy and Privilege Inheritance": (
            "In Snowflake’s RBAC system, roles can be arranged in a hierarchy where higher-level roles inherit permissions from subordinate roles.\n\n"
            "Concept: This structured design means that a single role can encompass a broad set of permissions without having to list each one explicitly.\n\n"
            "Benefits: It simplifies user management, reduces administrative overhead, and ensures consistent security policies across an organization."
        ),
        "Accounts": (
            "A Snowflake account is the primary container that holds all data, users, roles, and configuration settings for your organization.\n\n"
            "Concept: It serves as the top-level administrative boundary and is where global policies, billing, and resource allocations are managed.\n\n"
            "Benefits: Consolidates data governance, security, and administrative functions under a single management umbrella, facilitating centralized control."
        ),
        "Organizations": (
            "Organizations allow for the grouping of multiple Snowflake accounts, which is particularly useful for large enterprises or multi-regional deployments.\n\n"
            "Concept: They provide a means to centrally manage policies, consolidated billing, and governance across all associated accounts.\n\n"
            "Benefits: Streamlines administration and enables standardized security and compliance practices across diverse business units."
        ),
        "Secure Views": (
            "Secure views are specialized views that hide the underlying SQL logic and sensitive data from end users.\n\n"
            "Concept: They are created using CREATE SECURE VIEW and ensure that both the query logic and the resulting data are protected from unauthorized access.\n\n"
            "Benefits: Provide an additional layer of security for exposing only the necessary data to users while safeguarding proprietary business logic."
        ),
        "Secure Functions": (
            "Secure functions encapsulate logic while protecting the underlying code from exposure.\n\n"
            "Concept: Created with CREATE SECURE FUNCTION, they prevent users from viewing the source code even when executing the function.\n\n"
            "Benefits: Essential for protecting sensitive business rules and intellectual property embedded in custom functions."
        ),
        "Information Schemas": (
            "Information schemas are system-defined views that provide metadata about objects within a Snowflake account.\n\n"
            "Concept: They include details about tables, columns, privileges, and query histories, and are critical for auditing and monitoring.\n\n"
            "Benefits: Empower administrators and developers to understand the structure and usage of database objects, aiding in troubleshooting and performance tuning."
        ),
        "Access History (Tracking Read/Write Operations)": (
            "Snowflake automatically logs access and modification operations on data, which can be reviewed via system views such as ACCESS_HISTORY.\n\n"
            "Concept: This historical data includes who accessed what and when, which is essential for security audits and forensic investigations.\n\n"
            "Benefits: Provides transparency and accountability in data access, enabling compliance with regulatory standards."
        ),
        "Row/Column-Level Security": (
            "Row and column-level security allows you to restrict access to specific subsets of data within a table.\n\n"
            "Concept: Often implemented via secure views or masking policies, this granular control ensures that users see only the data they are permitted to access.\n\n"
            "Benefits: Enhances data protection and privacy by enforcing strict boundaries within shared datasets."
        ),
        "Object Tags": (
            "Object tags are metadata labels that you can assign to database objects for categorization, cost tracking, or security classification.\n\n"
            "Concept: Tags help administrators quickly filter, search, and manage large numbers of objects within a complex environment.\n\n"
            "Benefits: Instrumental in applying consistent governance policies and tracking resource usage across the organization."
        )
    },
    "Domain 3.0: Performance Concepts": {
        "Explain Plans": (
            "Explain plans provide a detailed outline of how a SQL query will be executed, including join orders, filter operations, and data access paths.\n\n"
            "Concept: Using the EXPLAIN command, Snowflake generates a step-by-step execution plan that helps identify bottlenecks or inefficient operations.\n\n"
            "Benefits: By analyzing explain plans, you can optimize query performance and make informed decisions about indexing, clustering, or rewriting queries.\n\n"
            "Commands & Examples:\n"
            "  - `EXPLAIN SELECT * FROM my_table;` shows the execution strategy for the query."
        ),
        "Data Spilling": (
            "Data spilling occurs when the data being processed exceeds the memory available in a virtual warehouse, causing intermediate results to be written to disk.\n\n"
            "Concept: Although Snowflake handles spilling automatically, frequent spills can signal that a warehouse is undersized or that a query could be optimized.\n\n"
            "Benefits: Recognizing data spilling allows you to adjust warehouse sizing or rewrite queries to minimize disk I/O, thereby improving overall performance."
        ),
        "Use of the Data Cache": (
            "Snowflake automatically caches query results in memory so that if the same query is executed repeatedly, the cached result is returned immediately.\n\n"
            "Concept: The result cache significantly reduces response times for recurring queries and lowers compute costs by avoiding redundant processing.\n\n"
            "Benefits: Enhances performance transparently without requiring additional configuration from the user."
        ),
        "Micro-partition Pruning": (
            "Micro-partition pruning is the process by which Snowflake automatically skips over micro-partitions that do not contain data relevant to a query.\n\n"
            "Concept: When a query includes filters, Snowflake examines metadata about each micro-partition to determine whether it needs to be scanned.\n\n"
            "Benefits: This reduces the volume of data read from storage, thereby accelerating query execution and lowering compute usage."
        ),
        "Query History": (
            "Query history logs every query executed in Snowflake along with performance metrics, execution times, and resource consumption details.\n\n"
            "Concept: Accessed via system views like QUERY_HISTORY, this log helps in tracking performance trends and troubleshooting slow queries.\n\n"
            "Benefits: Provides essential insights for performance tuning and capacity planning."
        ),
        "Types of Warehouses": (
            "Virtual warehouses in Snowflake are clusters of compute resources that process queries.\n\n"
            "Concept: They come in various sizes (from X-SMALL to 6X-LARGE) and are designed to handle different workloads.\n\n"
            "Benefits: Selecting the appropriate warehouse type ensures an optimal balance between performance and cost.\n\n"
            "Commands & Examples:\n"
            "  - Create a warehouse: `CREATE WAREHOUSE my_wh WITH WAREHOUSE_SIZE = 'MEDIUM';`"
        ),
        "Multi-clustering Warehouses (Scaling Policies & Modes)": (
            "Multi-clustering enables a virtual warehouse to automatically add or remove clusters to handle varying levels of concurrency.\n\n"
            "Concept: With scaling policies configured, Snowflake can dynamically adjust the number of clusters based on the number of queued queries.\n\n"
            "Benefits: Provides consistent query performance during peak times without manual intervention.\n\n"
            "Commands & Examples:\n"
            "  - Adjust a warehouse’s multi-cluster settings: `ALTER WAREHOUSE my_wh SET MIN_CLUSTER_COUNT = 1, MAX_CLUSTER_COUNT = 3;`"
        ),
        "Warehouse Sizing": (
            "Warehouse sizing determines the compute power available for query execution.\n\n"
            "Concept: Larger warehouses can process more data in parallel, which is important for compute-intensive tasks, while smaller warehouses reduce costs for lighter workloads.\n\n"
            "Benefits: Proper sizing is key to achieving the right balance between performance and cost.\n\n"
            "Commands & Examples:\n"
            "  - Resize a warehouse: `ALTER WAREHOUSE my_wh SET WAREHOUSE_SIZE = 'LARGE';`"
        ),
        "Warehouse Settings and Access": (
            "Warehouse settings such as auto-suspend, auto-resume, and resource limits control how and when compute resources are used.\n\n"
            "Concept: These settings help to optimize cost efficiency by automatically suspending idle warehouses and resuming them when needed.\n\n"
            "Benefits: Ensures that compute resources are used only when necessary, reducing unnecessary costs while maintaining performance.\n\n"
            "Commands & Examples:\n"
            "  - Set auto-suspend: `ALTER WAREHOUSE my_wh SET AUTO_SUSPEND = 300;`\n"
            "  - Enable auto-resume: `ALTER WAREHOUSE my_wh SET AUTO_RESUME = TRUE;`"
        ),
        "Monitoring Warehouse Loads": (
            "Monitoring tools in Snowflake allow administrators to view the workload on virtual warehouses in real time.\n\n"
            "Concept: System views and dashboards (found in ACCOUNT_USAGE and INFORMATION_SCHEMA) display metrics like query concurrency, execution times, and credit consumption.\n\n"
            "Benefits: Helps in identifying performance bottlenecks, planning capacity, and ensuring that warehouses are optimally sized for the workload."
        ),
        "Scaling Up vs. Scaling Out": (
            "Scaling up (vertical scaling) increases the size of a warehouse, while scaling out (horizontal scaling) adds additional clusters to process more queries concurrently.\n\n"
            "Concept: Each method addresses different performance challenges—scaling up improves the speed of individual queries, whereas scaling out enhances overall throughput.\n\n"
            "Benefits: Understanding the difference allows administrators to tailor their approach to meet the specific demands of their workload.\n\n"
            "Usage: Both methods can be managed via ALTER WAREHOUSE commands."
        ),
        "Resource Monitors": (
            "Resource monitors are configured to track and limit the amount of compute credits consumed by virtual warehouses.\n\n"
            "Concept: They help prevent runaway costs by triggering alerts or suspending warehouses when credit usage exceeds predefined thresholds.\n\n"
            "Benefits: Provide cost control and ensure that resources are not over-utilized.\n\n"
            "Commands & Examples:\n"
            "  - Create a resource monitor: `CREATE RESOURCE MONITOR my_monitor WITH CREDIT_QUOTA = 100;`"
        ),
        "Query Acceleration Service": (
            "The Query Acceleration Service (QAS) is an automated feature that dynamically allocates extra resources to long-running queries.\n\n"
            "Concept: Although it operates behind the scenes, QAS can significantly reduce query execution times by temporarily boosting compute power.\n\n"
            "Benefits: Improves user experience by reducing latency for resource-intensive queries without requiring manual scaling adjustments."
        ),
        "Materialized Views": (
            "Materialized views store the precomputed results of complex queries to enable faster retrieval on subsequent executions.\n\n"
            "Concept: They are especially useful for repetitive, resource-intensive queries, as the results are stored and only refreshed when the underlying data changes.\n\n"
            "Benefits: Dramatically reduce query response times and lower compute costs.\n\n"
            "Commands & Examples:\n"
            "  - Create a materialized view: `CREATE MATERIALIZED VIEW my_mv AS SELECT col1, COUNT(*) FROM my_table GROUP BY col1;`"
        ),
        "Specific SELECT Commands": (
            "Advanced SELECT commands, including query hints and optimizations, can further improve performance in specific scenarios.\n\n"
            "Concept: While many performance improvements are automatic, fine-tuning SELECT statements can help optimize execution plans in certain cases.\n\n"
            "Benefits: Provides an additional layer of control for expert users to optimize critical queries."
        ),
        "Clustering": (
            "Clustering refers to the physical organization of data based on specified columns to improve query performance.\n\n"
            "Concept: By using clustering keys, Snowflake can more effectively prune irrelevant micro-partitions, reducing the amount of data scanned during queries.\n\n"
            "Benefits: Speeds up queries that filter on clustered columns, thereby lowering compute costs.\n\n"
            "Commands & Examples:\n"
            "  - Define clustering when creating a table: `CREATE TABLE my_table (col1 INT, col2 STRING) CLUSTER BY (col1);`"
        ),
        "Search Optimization Service": (
            "The Search Optimization Service creates and maintains indexes on large tables to accelerate point lookups and ad hoc search queries.\n\n"
            "Concept: It is especially beneficial for tables with high cardinality and frequent search operations, ensuring that query performance remains high even as data volume grows.\n\n"
            "Benefits: Reduces latency and improves responsiveness for search-heavy workloads.\n\n"
            "Usage: Configured through the Snowflake interface and account settings, with no direct SQL command required."
        ),
        "Persisted Query Results": (
            "Persisted query results are automatically cached by Snowflake so that if the same query is executed again, the results can be returned quickly without re-computation.\n\n"
            "Concept: This feature leverages in-memory caches and other optimizations to reduce query latency.\n\n"
            "Benefits: Improves performance for repetitive queries and reduces overall compute costs."
        ),
        "Metadata Cache": (
            "Snowflake maintains a metadata cache that stores information about database objects, table statistics, and schema details.\n\n"
            "Concept: This cache reduces the overhead of repeatedly querying system tables and metadata during query planning.\n\n"
            "Benefits: Speeds up query compilation and execution by minimizing redundant metadata lookups."
        ),
        "Result Cache": (
            "The result cache stores the outputs of queries so that if an identical query is issued, the cached result can be returned instantly.\n\n"
            "Concept: This feature is completely transparent and requires no additional configuration.\n\n"
            "Benefits: Significantly improves response times and reduces compute load for frequently executed queries."
        ),
        "Warehouse Cache": (
            "The warehouse cache refers to data temporarily stored in the memory of virtual warehouses.\n\n"
            "Concept: It is used to store frequently accessed data, reducing the need to repeatedly fetch data from disk or remote storage.\n\n"
            "Benefits: Enhances query performance by lowering data access latency during high-concurrency operations."
        )
    },
    "Domain 4.0: Data Loading and Unloading": {
        "Stages and Stage Types": (
            "Stages in Snowflake are defined locations for temporarily storing data files during load (ingest) and unload (export) operations.\n\n"
            "Concept: They can be internal (managed by Snowflake) or external (using cloud storage like S3, Azure Blob, or GCP Storage).\n\n"
            "Benefits: Staging allows for efficient data ingestion by decoupling file storage from table loading, handling large volumes of data seamlessly.\n\n"
            "Commands & Examples:\n"
            "  - Create an internal stage: `CREATE STAGE my_stage;`\n"
            "  - Create an external stage: `CREATE STAGE my_ext_stage URL='s3://mybucket/path' CREDENTIALS=(AWS_KEY_ID='...', AWS_SECRET_KEY='...');`"
        ),
        "File Size and Formats": (
            "Selecting the appropriate file size and format is critical for optimizing data load performance.\n\n"
            "Concept: Snowflake supports multiple file formats including CSV, JSON, Avro, Parquet, and ORC.\n\n"
            "Benefits: Correctly formatted and appropriately sized files reduce load times, improve parsing accuracy, and minimize errors during ingestion.\n\n"
            "Commands & Examples:\n"
            "  - Define a file format: `CREATE FILE FORMAT my_csv_format TYPE = 'CSV' FIELD_DELIMITER = ',' SKIP_HEADER = 1;`"
        ),
        "Folder Structures": (
            "Organizing data files into logical folder structures (or prefixes in cloud storage) aids in managing and processing large data loads.\n\n"
            "Concept: A well-organized folder hierarchy simplifies file discovery, batching, and error handling.\n\n"
            "Benefits: Improves load efficiency by allowing targeted file processing and easier troubleshooting when files are not processed as expected."
        ),
        "Ad hoc/Bulk Loading": (
            "Ad hoc loading is used for smaller, one-time data loads, whereas bulk loading leverages parallel processing to ingest large volumes of data.\n\n"
            "Concept: Bulk loading typically uses the COPY INTO command, which can process multiple files concurrently from a stage.\n\n"
            "Benefits: Ensures that even massive data sets can be ingested quickly, reliably, and with built-in error handling."
        ),
        "Snowpipe": (
            "Snowpipe is Snowflake’s continuous data ingestion service that automatically loads data as soon as files appear in a designated stage.\n\n"
            "Concept: It uses event notifications from the cloud storage provider to trigger data loads, ensuring near-real-time data availability.\n\n"
            "Benefits: Reduces latency between data arrival and query availability, making it ideal for streaming or near-real-time applications.\n\n"
            "Commands & Examples:\n"
            "  - Create a pipe for Snowpipe:\n"
            "    ```sql\n"
            "    CREATE OR REPLACE PIPE my_pipe AS\n"
            "    COPY INTO my_table FROM @my_stage FILE_FORMAT = (FORMAT_NAME = 'my_csv_format');\n"
            "    ```"
        ),
        "CREATE STAGE": (
            "The CREATE STAGE command defines a stage that acts as a temporary storage location for data files.\n\n"
            "Concept: Stages abstract the physical file storage details and allow Snowflake to interface seamlessly with external or internal storage.\n\n"
            "Benefits: Simplifies data loading processes by providing a managed point of integration between external data and Snowflake tables.\n\n"
            "Example: `CREATE STAGE my_stage;`"
        ),
        "CREATE FILE FORMAT": (
            "The CREATE FILE FORMAT command creates a reusable definition that specifies how data files should be parsed during loading or unloading.\n\n"
            "Concept: It includes details such as file type (CSV, JSON, etc.), field delimiters, escape characters, and header row options.\n\n"
            "Benefits: Ensures consistency and accuracy in how data is interpreted during ingestion or export.\n\n"
            "Example: `CREATE FILE FORMAT my_format TYPE = 'CSV' FIELD_DELIMITER = ',';`"
        ),
        "CREATE PIPE": (
            "A pipe in Snowflake automates the continuous loading of data using Snowpipe.\n\n"
            "Concept: It links a stage to a target table and specifies the loading command that should be executed when new files are detected.\n\n"
            "Benefits: Enables near real-time data ingestion without manual intervention.\n\n"
            "Example: `CREATE PIPE my_pipe AS COPY INTO my_table FROM @my_stage FILE_FORMAT = (FORMAT_NAME = 'my_format');`"
        ),
        "CREATE EXTERNAL TABLE": (
            "External tables allow you to query data stored in external locations directly, without first loading it into Snowflake.\n\n"
            "Concept: They reference data stored in a stage and use a file format definition to parse the data on the fly.\n\n"
            "Benefits: Ideal for ad hoc analysis of large datasets stored externally, reducing the need for data duplication.\n\n"
            "Example: `CREATE EXTERNAL TABLE my_ext_table (col1 INT, col2 STRING) LOCATION = '@my_ext_stage/path' FILE_FORMAT = (FORMAT_NAME = 'my_format');`"
        ),
        "COPY INTO (Loading)": (
            "The COPY INTO command is used to load data from a stage into a target table.\n\n"
            "Concept: It supports various options such as file format, error handling, and data transformation during the load process.\n\n"
            "Benefits: Efficiently ingests data in parallel from one or more files, while providing robust options for validation and error management.\n\n"
            "Example: `COPY INTO my_table FROM @my_stage FILE_FORMAT = (FORMAT_NAME = 'my_format');`"
        ),
        "INSERT/INSERT OVERWRITE": (
            "INSERT commands add new rows to a table, while INSERT OVERWRITE replaces existing data with new data.\n\n"
            "Concept: They are used for ad hoc data additions or for completely refreshing table contents.\n\n"
            "Benefits: Provide flexibility in how data is integrated into tables, whether as incremental updates or full refreshes.\n\n"
            "Examples:\n"
            "  - Insert: `INSERT INTO my_table VALUES (1, 'data');`\n"
            "  - Insert Overwrite: Typically implemented via a combination of DELETE and INSERT in Snowflake."
        ),
        "PUT": (
            "The PUT command uploads local data files to an internal stage in Snowflake.\n\n"
            "Concept: It transfers files from your local file system to a Snowflake stage so they can then be loaded using COPY INTO.\n\n"
            "Benefits: Facilitates quick testing and one-off data loads without needing to manage external cloud storage manually.\n\n"
            "Example: `PUT file://path/to/data.csv @my_stage;`"
        ),
        "VALIDATE": (
            "The VALIDATE command checks the data files in a stage against the specified file format to ensure they meet the load criteria.\n\n"
            "Concept: It is used as a pre-load check to identify errors or inconsistencies in the data files before running a full load.\n\n"
            "Benefits: Saves time and compute resources by catching issues early in the data ingestion process.\n\n"
            "Example: `VALIDATE @my_stage FILE_FORMAT = (FORMAT_NAME = 'my_format');`"
        ),
        "File Size and Formats (Compression Methods)": (
            "When unloading data from Snowflake, it is important to choose the appropriate file sizes, formats, and compression methods.\n\n"
            "Concept: These parameters impact the speed and efficiency of data export as well as subsequent file handling.\n\n"
            "Benefits: Optimizes data transfer and storage costs, and ensures that the unloaded data is in a readily consumable format.\n\n"
            "Usage: Defined in the file format used during the COPY INTO (unload) operation."
        ),
        "Empty Strings and NULL Values": (
            "Handling empty strings and NULL values appropriately is critical during data unload operations.\n\n"
            "Concept: The file format definition can be configured to specify how these values should be represented, ensuring that data integrity is maintained.\n\n"
            "Benefits: Avoids data misinterpretation in downstream applications and maintains consistency in data exports."
        ),
        "Unloading to a Single File": (
            "In some scenarios, it is desirable to unload data into a single consolidated file.\n\n"
            "Concept: While Snowflake normally outputs data in multiple files for parallel processing, options exist to merge these into one file.\n\n"
            "Benefits: Simplifies file management and downstream processing when a single file is required.\n\n"
            "Usage: Typically controlled via parameters in the COPY INTO command during unload."
        ),
        "Unloading Relational Tables": (
            "Unloading data from relational tables uses the same COPY INTO command as loading but in reverse.\n\n"
            "Concept: It exports table data to an external location (such as an S3 bucket) using the specified file format and compression options.\n\n"
            "Benefits: Provides a reliable method for data backup, migration, or integration with other systems while preserving table structure and data types."
        ),
        "GET": (
            "The GET command is used to download files from an internal stage to a local directory.\n\n"
            "Concept: It provides a way to retrieve exported data files for local analysis or backup.\n\n"
            "Benefits: Simplifies the process of moving data from Snowflake’s internal storage to your local environment.\n\n"
            "Example: `GET @my_stage file://local_directory;`"
        ),
        "LIST": (
            "The LIST command displays all files present in a specified stage.\n\n"
            "Concept: It is used to verify the contents of a stage before initiating a load or unload operation.\n\n"
            "Benefits: Provides quick insight into which files are available, their sizes, and status."
        ),
        "COPY INTO (Unloading)": (
            "The COPY INTO command is also used for unloading data from a Snowflake table to an external location.\n\n"
            "Concept: It supports options for file formatting, compression, and output file splitting.\n\n"
            "Benefits: Enables the export of data in a controlled manner, ensuring that the unloaded files meet specific requirements.\n\n"
            "Example: `COPY INTO 's3://mybucket/path' FROM my_table FILE_FORMAT = (FORMAT_NAME = 'my_format');`"
        ),
        "CREATE STAGE (for Unloading)": (
            "When unloading data, you may define a stage as the destination for the exported files using the CREATE STAGE command.\n\n"
            "Concept: This allows you to manage and monitor where unloaded files are stored before they are transferred to an external system.\n\n"
            "Benefits: Provides a controlled environment for export operations, similar to data loading."
        ),
        "CREATE FILE FORMAT (for Unloading)": (
            "A dedicated file format for unloading can be created to ensure that the exported data conforms to required standards for structure and compression.\n\n"
            "Concept: It is defined using the same CREATE FILE FORMAT command used for loading, but tailored for the export process.\n\n"
            "Benefits: Guarantees that the unloaded files are in the correct format for downstream consumption."
        )
    },
    "Domain 5.0: Data Transformations": {
        "Estimation Functions": (
            "Estimation functions in Snowflake provide approximate calculations on large datasets, which is useful for exploratory analysis and performance optimization.\n\n"
            "Concept: Functions like APPROX_COUNT_DISTINCT() allow you to estimate the number of unique values quickly without the overhead of a full distinct count.\n\n"
            "Benefits: They provide a balance between accuracy and speed, enabling fast insights on very large data sets where exact counts are less critical.\n\n"
            "Usage: Example: `SELECT APPROX_COUNT_DISTINCT(user_id) FROM events;`"
        ),
        "Sampling": (
            "Sampling enables you to work with a representative subset of your data for testing, analytics, or performance tuning.\n\n"
            "Concept: Snowflake supports sampling using the SAMPLE command or the TABLESAMPLE clause, allowing you to specify a percentage or fixed number of rows.\n\n"
            "Benefits: Reduces resource consumption and accelerates query times during exploratory analysis.\n\n"
            "Usage: Example: `SELECT * FROM my_table TABLESAMPLE (10);` retrieves approximately 10% of the rows."
        ),
        "Supported Function Types": (
            "Snowflake supports multiple function types including system functions, table functions, external functions, and user-defined functions (UDFs).\n\n"
            "Concept: This diversity allows you to extend native capabilities with custom logic, perform advanced data transformations, and integrate external services.\n\n"
            "Benefits: Provides flexibility to perform complex data manipulations and business logic directly in SQL.\n\n"
            "Usage: Custom UDFs can be created using commands such as CREATE FUNCTION or CREATE TABLE FUNCTION."
        ),
        "Stored Procedures": (
            "Stored procedures in Snowflake enable the encapsulation of complex logic and control flow, allowing multi-step processes to be executed on the server side.\n\n"
            "Concept: They support procedural programming constructs like loops, conditionals, and error handling.\n\n"
            "Benefits: Ideal for automating repetitive tasks, performing batch operations, or orchestrating complex workflows.\n\n"
            "Usage: Refer to the stored procedure example provided in Domain 1.0 under Stored Procedures."
        ),
        "Streams": (
            "Streams provide a mechanism for change data capture by tracking the changes (inserts, updates, deletes) made to a table.\n\n"
            "Concept: They allow for efficient incremental processing, so that only the new or modified data is processed in downstream operations.\n\n"
            "Benefits: Essential for building real-time data pipelines and reducing the overhead of full table scans.\n\n"
            "Usage: Example: `CREATE STREAM my_stream ON TABLE my_table;`"
        ),
        "Tasks": (
            "Tasks automate the scheduling and execution of SQL statements or stored procedures.\n\n"
            "Concept: They can be set up to run on a schedule or triggered by specific events, enabling periodic data transformations or maintenance tasks.\n\n"
            "Benefits: Reduce manual intervention and ensure that data remains current and consistent.\n\n"
            "Usage: Refer to the task example provided in Domain 1.0 under Tasks."
        ),
        "Supported Data Formats, Data Types, and Sizes": (
            "Snowflake supports a wide variety of data formats—from structured to semi-structured—allowing you to ingest and store JSON, Avro, Parquet, and more.\n\n"
            "Concept: The VARIANT data type, along with OBJECT and ARRAY, provides flexibility to store and query data without requiring a fixed schema.\n\n"
            "Benefits: Enables the integration of disparate data sources and supports agile data modeling as requirements evolve."
        ),
        "VARIANT Column": (
            "The VARIANT data type is designed to hold semi-structured data such as JSON, XML, or Avro.\n\n"
            "Concept: It allows you to store data without a predefined schema, enabling rapid ingestion and flexible querying.\n\n"
            "Benefits: Facilitates the analysis of data from diverse sources and supports schema-on-read, reducing upfront data modeling effort."
        ),
        "Flattening the Nested Structure": (
            "Flattening transforms nested semi-structured data into a tabular format so that it can be queried using standard SQL.\n\n"
            "Concept: The FLATTEN function and the LATERAL FLATTEN clause enable you to convert arrays and nested objects into rows and columns.\n\n"
            "Benefits: Simplifies data analysis by making complex, nested data structures accessible and queryable in a relational format.\n\n"
            "Usage: Example: `SELECT value FROM TABLE(FLATTEN(input => my_variant_column));`"
        ),
        "Semi-structured Data Functions": (
            "Snowflake offers a rich set of functions for manipulating semi-structured data stored in VARIANT columns.\n\n"
            "Concept: Functions such as TO_VARIANT(), OBJECT_CONSTRUCT(), and ARRAY_AGG() enable you to parse, transform, and aggregate semi-structured data.\n\n"
            "Benefits: Allow you to perform complex transformations directly within SQL, reducing the need for external processing."
        ),
        "Directory Tables": (
            "Directory tables allow you to query metadata about files stored in external stages.\n\n"
            "Concept: They provide a structured view of unstructured data files, including attributes like file names, sizes, and modification dates.\n\n"
            "Benefits: Useful for pre-processing or validating data before a load operation, ensuring that file organization meets expectations."
        ),
        "SQL File Functions": (
            "SQL file functions in Snowflake are designed to work with data stored in files, enabling operations such as reading file contents or extracting metadata.\n\n"
            "Concept: These functions can be used in conjunction with stages and external tables to seamlessly integrate file-based data with SQL queries.\n\n"
            "Benefits: Enhance the flexibility of data ingestion and analysis by allowing direct interaction with unstructured data sources."
        ),
        "Purpose of UDFs for Data Analysis": (
            "User Defined Functions (UDFs) for data analysis extend Snowflake’s native functionality by allowing you to implement custom logic for data transformation, aggregation, or filtering.\n\n"
            "Concept: They encapsulate complex operations into callable functions that can be reused across queries and applications.\n\n"
            "Benefits: Simplify code maintenance, promote reuse, and enable tailored analysis that meets specific business needs."
        )
    },
    "Domain 6.0: Data Protection and Data Sharing": {
        "Time Travel": (
            "Time Travel is a unique feature in Snowflake that allows you to query and even restore data as it existed at a previous point in time.\n\n"
            "Concept: By specifying a past timestamp or an offset using an AT or BEFORE clause, you can retrieve historical data.\n\n"
            "Benefits: Provides an effective mechanism for recovering from accidental data loss, running audits, and comparing data changes over time.\n\n"
            "Usage: Example: `SELECT * FROM my_table AT (TIMESTAMP => '2024-09-01 00:00:00');`"
        ),
        "Fail-safe": (
            "Fail-safe is an additional data recovery mechanism that Snowflake provides beyond the Time Travel window.\n\n"
            "Concept: Once Time Travel expires, data enters a fail-safe period during which Snowflake retains a copy for recovery in the event of catastrophic failures.\n\n"
            "Benefits: Offers extra protection against data loss, ensuring that even permanently deleted data can be recovered within a defined period (managed entirely by Snowflake)."
        ),
        "Data Encryption": (
            "Data encryption in Snowflake is applied automatically to all data at rest and in transit.\n\n"
            "Concept: Using industry-standard encryption protocols, Snowflake ensures that sensitive data remains secure throughout its lifecycle without requiring manual configuration.\n\n"
            "Benefits: Provides robust security and compliance with regulatory standards, reducing risk and safeguarding data integrity."
        ),
        "Cloning": (
            "Cloning allows you to create a zero-copy duplicate of databases, schemas, or tables.\n\n"
            "Concept: Because clones share the same underlying storage as the source, they can be created almost instantly and without consuming additional storage until changes are made.\n\n"
            "Benefits: Ideal for testing, development, or backup scenarios where you need an exact replica of your data without the overhead of full duplication.\n\n"
            "Commands & Examples:\n"
            "  - Clone a table: `CREATE TABLE my_table_clone CLONE my_table;`"
        ),
        "Replication": (
            "Replication in Snowflake enables the copying of data across different accounts or regions for high availability and disaster recovery.\n\n"
            "Concept: It is configured via replication policies and account settings, allowing you to maintain a synchronized copy of your data in a secondary location.\n\n"
            "Benefits: Minimizes downtime in the event of a regional failure and supports business continuity by ensuring data redundancy."
        ),
        "Account Types": (
            "Snowflake offers different account types designed to meet varying needs in terms of performance, security, and scalability.\n\n"
            "Concept: The account type chosen during provisioning determines the range of features and configurations available, including security and resource isolation.\n\n"
            "Benefits: Ensures that organizations can select an account configuration that aligns with their operational and compliance requirements."
        ),
        "Snowflake Marketplace": (
            "The Snowflake Marketplace is a platform where organizations can share, monetize, or access third-party data sets.\n\n"
            "Concept: It integrates directly into the Snowflake ecosystem, allowing seamless data sharing and collaboration without moving data out of Snowflake.\n\n"
            "Benefits: Expands the range of data available for analysis, accelerates time to insight, and opens up new business opportunities."
        ),
        "Data Exchange": (
            "Data Exchange in Snowflake provides a secure framework for sharing data with external partners.\n\n"
            "Concept: It leverages Snowflake’s data sharing capabilities along with robust access controls to ensure that shared data is both secure and accessible only to authorized parties.\n\n"
            "Benefits: Facilitates collaboration and data monetization while preserving strict data governance and security."
        ),
        "DDL Commands to Create and Manage Shares": (
            "Sharing data in Snowflake is accomplished through DDL commands that define share objects and manage access.\n\n"
            "Concept: Commands such as CREATE SHARE, GRANT USAGE ON SHARE, and REVOKE allow administrators to expose specific data objects to external accounts in a controlled manner.\n\n"
            "Benefits: Enables secure, efficient, and auditable data sharing without physically copying the data."
        ),
        "Privileges Required for Working with Shares": (
            "Managing data shares requires elevated privileges—typically those held by the ACCOUNTADMIN role.\n\n"
            "Concept: Ensuring that only authorized users can create, modify, or delete shares is critical for maintaining data security and compliance.\n\n"
            "Benefits: Prevents unauthorized data access and maintains strict control over which data can be shared externally."
        ),
        "Secure Data Sharing": (
            "Secure data sharing allows organizations to share data without moving it, leveraging Snowflake’s inherent security features to ensure that only authorized users can access shared data.\n\n"
            "Concept: It combines secure views, role-based access controls, and dedicated sharing commands to expose data in a read-only, fully auditable manner.\n\n"
            "Benefits: Facilitates collaboration with external partners while minimizing the risk of data leakage and ensuring compliance with data protection regulations."
        )
    }
}

# Sidebar for domain selection
selected_domain = st.sidebar.selectbox("Select Domain", list(flash_cards.keys()))
st.header(selected_domain)

# Display each flash card as an expander with the item as the title and exhaustive details inside
for item, explanation in flash_cards[selected_domain].items():
    with st.expander(item):
        st.write(explanation)
