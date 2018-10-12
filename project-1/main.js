const ramba = require('rambda');
const express = require('express');
const app = express();
app.set('views', __dirname + '/views');
app.set('view engine', 'pug');

function generatePoints(num) {
  return ramba.range(0, num).map(p => {
    return {
      x: Math.random(-1, 1),
      y: Math.random(-1, 1)
    }
  });
}

function getCorrectTeam(point) {
  return (point.x < point.y) ? 1 : 0; 
}

function drawPoints(points) {
  return "<p>Lala</p>";
}

app.get('/', function(req, res) {
  res.render('points');
});

app.listen(8080);
