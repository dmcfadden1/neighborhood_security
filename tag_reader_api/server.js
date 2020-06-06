const express = require('express')
const logger = require('morgan')
const bodyParser = require('body-parser')
const cors = require('cors')

const plates = require('./app/plates')

const app = express()

app.use(cors())
app.use(logger('dev'))
app.use(bodyParser.json({limit: '2mb'}))
app.use(bodyParser.urlencoded({ extended: false }))

app.use('/plates', plates)
app.listen(8000, () => {})

// catch 404 and forward to error handler
app.use((req, res, next) => {
  const err = new Error('Not Found')
  err.status = 404
  next(err)
})

// error handlers

// development error handler
// will print stacktrace
if (app.get('env') === 'development') {
  app.use((err, req, res, next) => {
    res.status(err.status || 500)
    res.send()
  })
}

// production error handler
// no stacktraces leaked to user
app.use(function (err, req, res, next) {
  res.status(err.status || 500)
  res.send()
})

module.exports = app
