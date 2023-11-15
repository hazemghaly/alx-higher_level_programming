#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (h > 0 && w > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      let row = '';
      for (let j = 0; j < this.width; j++) {
        row += 'X';
      }
      console.log(row);
    }
  }

  rotate () {
    let a;
    a = this.height;
    this.height = this.width;
    this.width = a;
  }

  double () {
    this.height = this.height * 2;
    this.width = this.width * 2;
  }
};
