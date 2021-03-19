var express = require('express');
var http = require('http');
var bodyParser = require('body-parser')
var app = express();
var server = http.createServer(app);
app.use(bodyParser().json())

const users = [{loginId: 'hello', password: 'world', nickname: 'handstudio', token: '123456'}]

app.get('/', function(req, res){
    res.send('root page');
});

app.get('/login', function(req, res){
    
    res.send('start page');
});

app.get('/user', function(req, res){
    token = req.query.token
    const user = users.find(u => u.token == token)
    if (!user) {return res.status(404).send('Token was not found.')}
    result = {'success':true, 'token': user['token']}
    res.send(result);
});

app.post('/user', function(req, res){
    const loginId = req.body.loginId
    const password = req.body.password
    const nickname = req.body.nickname

    const user = users.find(u=>u.loginId == loginId && u.password == password && u.nickname == nickname)
    if (!user) {return res.status(404).send('user is not exist')}
    result = {'success':true}
    res.status(200).send(result);

})

server.listen(3000, '127.0.0.1', function(){
    console.log('Server listen on port' + server.address().port);
});