const { MongoClient } = require('mongodb');
const mongoose = require('mongoose');
const express = require('express');
const cors = require('cors')
const app = express()
const uri = "mongodb+srv://vincent:nbaprizepicks@cs4440.s5kkhzs.mongodb.net/?retryWrites=true&w=majority";

app.use(cors());
app.use(express.json());


const client = new MongoClient(uri);
client.connect();
const dbName = "prizepicks";
const pointsCollection = "points";
const reboundsCollection = "rebounds";
const assistsCollection = "assists";
const playersCollection = "players"
const database = client.db(dbName);
const date = "2023-02-23";

playerMap = {};
try {
    database.collection(playersCollection).find().toArray().then(
        (items) => {
            items.forEach(item => {
                playerMap[item.name] = item.image;
            });
        },
        (err) => {
            return err
        }
    )
} catch (err) {
    console.error(`Something went wrong trying to find one document: ${err}\n`);
}




app.get('/', (req, res) => {
    try {
        database.collection(pointsCollection).find({date: new Date(date)}).toArray().then(
            (items) => {
                for (let i = 0; i < items.length; i++) {
                    if (items[i].data.name in playerMap) {
                        items[i].image = playerMap[items[i].data.name]
                    };
                }
                res.send(items);
            },
            (err) => {
                return err
            }
        ) 
    } catch (err) {
        console.error(`Something went wrong trying to find one document: ${err}\n`);
    }
})

app.listen(3001, function() {
    console.log('server is running');
})



// // Create a MongoClient with a MongoClientOptions object to set the Stable API version
// const client = new MongoClient(uri, {
//   serverApi: {
//     version: ServerApiVersion.v1,
//     strict: true,
//     deprecationErrors: true,
//   }
// });
// async function run() {
//   try {
//     // Connect the client to the server	(optional starting in v4.7)
//     await client.connect();
//     // Send a ping to confirm a successful connection
//     await client.db("admin").command({ ping: 1 });
//     console.log("Pinged your deployment. You successfully connected to MongoDB!");
//   } finally {
//     // Ensures that the client will close when you finish/error
//     await client.close();
//   }
// }
// run().catch(console.dir);