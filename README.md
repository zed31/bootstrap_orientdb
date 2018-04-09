# bootstrap_orientdb
bootstrap orientdb with some script to create a simple database that links user to offer and companies

---

To use the several scripts, you first need to have python3.6 on your distribution
Then you also need to install [Pyorient](https://github.com/mogui/pyorient)

---

All scripts are using the database with localhost as host and root as id, root as password.
There are 3 scripts:

* orient_setup: Setup the database with all the vertexes and edges
* orient_clean: Clean the content of the database (each vertices)
* orient_create_database: Generate all the vertices and their edges to test the database

---

You can make the request thanks to the [Orientdb console](https://orientdb.com/docs/last/Tutorial-Run-the-console.html)
