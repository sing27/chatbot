var toWav = require('audiobuffer-to-wav')
var xhr = require('xhr')
var context = new AudioContext()
 
// request the MP3 as binary
xhr({
  uri: './japan.m4a',
  responseType: 'arraybuffer'
}, function (err, body, resp) {
  if (err) throw err
  // decode the MP3 into an AudioBuffer
  audioContext.decodeAudioData(resp, function (buffer) {
    // encode AudioBuffer to WAV
    var wav = toWav(buffer)
    
    // do something with the WAV ArrayBuffer ...
  })
})