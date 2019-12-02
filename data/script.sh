#!/bin/bash
#mongod
while !(nc -z localhost 27017) ; do
    sleep 2
    echo "Waiting for mongo to initialize..."
done
echo 'db.createUser({user: "mongodb", pwd: "mongodb", roles: ["readWrite", "dbAdmin"]});' > file.js
mongo admin file.js
mongoimport --db intelygenz --collection restaurant --authenticationDatabase admin --username mongodb --password mongodb --file ./restaurant.json