var MongoClient = require('mongodb').MongoClient;
var url = "mongodb+srv://user:pass@cluster0-rhzye.mongodb.net/test";
var fs = require('fs');
var objects = JSON.parse(fs.readFileSync('ike.json', 'utf8'));

// Provide the file name and pass in the collection name
MongoClient.connect(url, function(err, db) {
  if (err) throw err;
  var dbo = db.db("test");
  dbo.collection('ikes').insertMany(objects, function(err, res){
    if(err) throw err;
    db.close()
  })
  // objects.forEach(element => {
  //   // console.log(element)
  //   dbo.collection("ikes").insertOne(element, function(err, res) {
  //     if (err) throw err;
  //     // console.log("1 document inserted");
  //     db.close();
  //   });

  // });


}); 