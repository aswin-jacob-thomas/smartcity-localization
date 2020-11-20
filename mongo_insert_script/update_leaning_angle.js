var fs = require('fs');
var MongoClient = require('mongodb').MongoClient;
var url = "mongodb+srv://user:pass@cluster0-rhzye.mongodb.net/test";

var old_pole_data = JSON.parse(fs.readFileSync('old_pole.json', 'utf8'));
var new_pole_data = JSON.parse(fs.readFileSync('new_pole.json', 'utf8'));

i = 0

for(new_data of new_pole_data){
    for(old_data of old_pole_data){
        if(new_data['id'] == old_data['id']){
            old_data['angle_3to21'] = new_data['angle_3to21']
            i+=1;
            break;
        }
    }
}

console.log('Updated!!!')
console.log('Total updated', i)

i = 1
for(old_data of old_pole_data){
    old_data['manual_id'] = i;
    i += 1
}

MongoClient.connect(url, function(err, db) {
    if (err) throw err;
    var dbo = db.db("test");
    dbo.collection('poles').deleteMany({}, function(err, res){
      if(err) throw err;
      db.close()
    })
}); 

MongoClient.connect(url, function(err, db) {
    if (err) throw err;
    var dbo = db.db("test");
    dbo.collection('poles').insertMany(old_pole_data, function(err, res){
      if(err) throw err;
      db.close()
    })
}); 