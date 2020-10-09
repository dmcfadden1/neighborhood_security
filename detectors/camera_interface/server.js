const cv = require('opencv4nodejs');
const wCap = new cv.VideoCapture(devicePort);
const frame = vCap.read();
vCap.readAsync((err, frame) => {
  console.log("reading");
});
