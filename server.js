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
const calcDb = "calculations"
const playersCollection = "players"
const database = client.db(dbName);
const calcDatabase = client.db(calcDb);
var startDate = "2023-03-23";
var endDate = "2023-03-24";

const graphStartDate = "2023-03-01";
const graphEndDate = "2023-03-28";

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
    console.log(req.query.date);
    startDate = new Date(req.query.date);
    endDate = new Date(startDate.valueOf() + 1000*3600*24);
    console.log(startDate);
    console.log(endDate);
    console.log(endDate-startDate);
  
    try {
        calcMap = {}
        calcDatabase.collection(req.query.stat).find({date: { $gte: (startDate), $lt: (endDate)}}).toArray().then(
            (items) => {
                items.forEach(item => {
                    calcMap[item.data.name] = item.probability;
                });
            },
            (err) => {
                return err
            }
        )

        database.collection(req.query.stat).find({date: { $gte: new Date(startDate), $lt: new Date(endDate)}}).toArray().then(
            (items) => {
                for (let i = 0; i < items.length; i++) {
                    if (items[i].data.name in playerMap) {
                        items[i].image = playerMap[items[i].data.name]
                        items[i].probability = calcMap[items[i].data.name]
                    };
                }
                res.send(items);
                // console.log(items);
            },
            (err) => {
                return err
            }
        )
    } catch (err) {
        console.error(`Something went wrong trying to find one document: ${err}\n`);
    }
})

app.get('/probabilities', (req, res) => {
    try {
        console.log(req.query)
        calcDatabase.collection(req.query.stat).find({date: { $gte: new Date(req.query.startDate), $lt: new Date(req.query.endDate)}, "data.name": req.query.name}).toArray().then(
            (items) => {
                console.log(items);
                dates = []
                probabilities = []
                graphData = []
                // for (let i = 0; i < items.length; i++) {
                //     // dates.push(items[i].date)
                //     // probabilities.push(items[i].probability)
                //     graphData.push({x: items[i].date, y: items[i].probability})
                // }
                // console.log(typeof(items))
                dates = items?.map(a => a.date);
                probabilities = items?.map(a => a.probability);
                graphData = dates?.map((v, i) => [v, probabilities[i]]).map(([x, y]) => ({x, y}));
                console.log(graphData);
                res.send(graphData);
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
    console.log('Server is running');
})