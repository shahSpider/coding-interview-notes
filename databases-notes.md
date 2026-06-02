# DATABASE NOTES
---

## ✅ **1. SQL (Structured Query Language)**

- **Type:** Relational Database (RDBMS)
- **Examples:** MySQL, PostgreSQL, SQLite, MS SQL Server
- **Structure:** Tables (rows & columns), with predefined schemas
- **Queries:** Use SQL (e.g., `SELECT * FROM users WHERE age > 18`)
- **ACID Compliance:** Strong consistency, transactions supported

### 💡 Use Cases:
- Banking systems
- Inventory systems
- ERP, CRM
- Applications with complex relationships and structured data

---

## ✅ **2. NoSQL (Not Only SQL)**

- **Type:** Non-relational databases
- **Examples:** MongoDB, Cassandra, Redis, Firebase, CouchDB
- **Structure:**
  - **Document-based** (MongoDB: JSON-like)
  - **Key-Value** (Redis)
  - **Wide-Column** (Cassandra)
  - **Graph** (Neo4j)

### 💥 Why NoSQL?
- Handles **unstructured / semi-structured data**
- Great for **scalability** (horizontal scaling, big data)
- Designed for **speed and flexibility**
- No fixed schema — dynamic documents
- Good with **real-time** applications (like chat apps, analytics, IoT)

---

## ⚖️ SQL vs NoSQL (Comparison Table)

| Feature             | SQL                            | NoSQL                              |
|---------------------|--------------------------------|-------------------------------------|
| Data Structure      | Tables                         | Documents, Key-Value, etc.          |
| Schema              | Fixed schema                   | Flexible / schema-less              |
| Scaling             | Vertical (big server)          | Horizontal (many cheap servers)     |
| Best for            | Structured data, complex joins | Large data, real-time, fast dev     |
| Transactions        | ACID (yes)                     | BASE (eventual consistency often)   |
| Example DBs         | MySQL, PostgreSQL              | MongoDB, Cassandra, Redis           |

---

## 🔧 When to Use Which?

- **SQL** if:
  - You need strong data integrity
  - Structured data
  - Complex joins/relations
  - Banking, ERP, HRMS, etc.

- **NoSQL** if:
  - Rapid development / prototyping
  - High-speed reads/writes
  - Big data, real-time analytics
  - Chat apps, social media, logs, IoT

---

### 🧠 TL;DR
- **SQL** = Structured, Reliable, Relationships
- **NoSQL** = Fast, Flexible, Big/Unstructured Data

---

Want a quick hands-on query example for both SQL (like PostgreSQL) and NoSQL (like MongoDB)?



--------------------------------------------------------------------------------------------
DATABASE NORMALIZATION

1. First Normal Form (1NF) Rules:
  i-    Using row order to convey information is not permitted
  ii-   Mixing data types within the same column is not permitted
  iii-  Having a table without a primary key is not permitted
  iv-   Storing a repeating group of data items on a single row is not permitted

2. Second Normal Form (2NF) Rules:
  i-    Each non-key attribute must depend on the entire primary key
        Not just on the partial part of the primary key

3. Third Normal Form (3NF):
    Every non-key attribute in a table should depend the key,
    the whole key, and nothing but the key

      There are no transitive dependencies
        Every non-key attribute depends:
          - on the key
          - on the whole key
          - and nothing but the key

| Normal Form | Removes               |
| ----------- | --------------------- |
| 1NF         | Repeating groups      |
| 2NF         | Partial dependency    |
| 3NF         | Transitive dependency |


## MYSQL VS POSTGRESQL WHEN AND WHICH ONE TO SELECT
  + both are Relational Database Management Systems (RDBMS) : Organize data into tables
  + both support Structured Query Language (SQL) and Javascript Object Notation (JSON)

### MYSQL
  + Early established and fast choice for web applications as it's easy to use and setup
  + Small scale SME applications that don't need higher complexity like enterprise level apps do
  + High speed

### POSTGRESQL
  + Most compliant, stable and reliable relational database
  + Enterprise grade level applications use OTLP Like e-commerce, CRMs and Financial Ledgers
  + Higher performance
  + Multi Version Concurrency Control (MVCC) supporting simultaneous read/write operations


PostgreSQL is a feature-rich, enterprise-grade relational database that supports complex queries, strong concurrency through MVCC, and advanced data types, making it ideal for financial systems, analytics, and large-scale enterprise applications.

MySQL is simpler, lightweight, and optimized for fast performance in small to medium-sized web applications, making it popular for blogs, CMS systems, and general web development.