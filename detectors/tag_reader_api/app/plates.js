const router = require('express').Router()
const base64Img = require('base64-img')
const path = require('path')
const uniqid = require('uniqid')
const validator = require('validator')

const fs = require('fs')
const exec = require('child_process').exec

const uploadPath = path.join(__dirname, '../tmp')

const version = '1.0.3'

router.post('/', (req, res, next) => {
  const imagedata = req.body.image
  const country_code = (req.body.country_code) ? validator.escape(req.body.country_code) : 'eu'
  const pattern_code = (req.body.pattern_code) ? '-p ' + validator.escape(req.body.pattern_code) : ''

  /* Validate input */
  if (!imagedata || validator.isBase64(imagedata)) {
    return res.status(500).json({
      error: 'No image sent',
      version: version
    })
  }

  /* Create upload area if not exists */
  if (!fs.existsSync(uploadPath)) {
    fs.mkdirSync(uploadPath)
  }

  base64Img.img(imagedata, uploadPath, uniqid(), (err, filepath) => {
    if (err) {
      return res.json({
        error: JSON.stringify(err)
      })
    }
    exec(`alpr -c ${country_code} ${pattern_code} -j ${filepath}`, (error, stdout, stderr) => {
      if (error) {
        return res.status(500).json({
          error: JSON.stringify(error)
        })
      } else {
        const result = JSON.parse(stdout)
        console.log(result)
        fs.unlink(filepath, () => {
          if (result.results.length < 1) {
            return res.status(500).json({
              error: 'No plates found in image'
            })
          }
          return res.json({
            results: result.results,
            width: result.img_width,
            height: result.img_height
          })
        })
      }
    })

  })
})

module.exports = router
