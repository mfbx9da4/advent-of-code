import fs from 'fs'
import os from 'os'
import path from 'path'
import fsExtra from 'fs-extra'

fs.readFile(path.join(__dirname, 'input.txt'), 'utf8', (err, data) => {
  console.log('data: ', data)
})
