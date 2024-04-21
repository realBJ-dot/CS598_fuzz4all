InnoDB is a storage engine for the database management system MySQL and MariaDB.[1] Since the release of MySQL 5.5.5 in 2010, it replaced MyISAM as MySQL's default table type.[2][3] It provides the standard ACID-compliant transaction features, along with foreign key support (declarative referential integrity). It is included as standard in most binaries distributed by MySQL AB, the exception being some OEM versions.

Description
InnoDB became a product of Oracle Corporation after its acquisition of the Finland-based company Innobase in October 2005.[4] The software is dual licensed; it is distributed under the GNU General Public License, but can also be licensed to parties wishing to combine InnoDB in proprietary software.[5]

InnoDB supports:

Both SQL and XA transactions
Tablespaces
Foreign keys
Full text search indexes, since MySQL 5.6 (February 2013)[6] and MariaDB 10.0[7]
Spatial operations, following the OpenGIS standard
Virtual columns, in MariaDB[8]

Table 17.1 InnoDB Storage Engine Features

Feature	Support
B-tree indexes	Yes
Backup/point-in-time recovery (Implemented in the server, rather than in the storage engine.)	Yes
Cluster database support	No
Clustered indexes	Yes
Compressed data	Yes
Data caches	Yes
Encrypted data	Yes (Implemented in the server via encryption functions; In MySQL 5.7 and later, data-at-rest encryption is supported.)
Foreign key support	Yes
Full-text search indexes	Yes (Support for FULLTEXT indexes is available in MySQL 5.6 and later.)
Geospatial data type support	Yes
Geospatial indexing support	Yes (Support for geospatial indexing is available in MySQL 5.7 and later.)
Hash indexes	No (InnoDB utilizes hash indexes internally for its Adaptive Hash Index feature.)
Index caches	Yes
Locking granularity	Row
MVCC	Yes
Replication support (Implemented in the server, rather than in the storage engine.)	Yes
Storage limits	64TB
T-tree indexes	No
Transactions	Yes
Update statistics for data dictionary	Yes