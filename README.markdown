# Kaleidoscope.sugar for Espresso

Kaleidoscope.sugar adds the ability to diff files in [Kaleidoscope](http://kaleidoscopeapp.com/) from [Espresso](http://macrabbit.com/espresso/).

## Installation

**Requires [ShellActions.sugar](https://github.com/onecrayon/ShellActions-sugar)**

1. After you have installed ShellActions.sugar, [download Kaleidoscope.sugar](http://onecrayon.com/downloads/Kaleidoscope.sugar.zip)
2. Decompress the zip (if your browser doesn't do it for you)
3. Double click the Kaleidoscope.sugar file to install

Or, to install with git, run the following commands in Terminal:

    cd ~/Library/Application\ Support/Espresso/Sugars
    git clone git://github.com/onecrayon/Kaleidoscope.sugar.git

## Usage

Select the files you want to compare in your PROJECT FILES sidebar within Espresso and right click (or click the gear button), then choose **Kaleidoscope&rarr;Diff Selected Files**. Make sure you install the `ksdiff` command line utility from within Kaleidoscope first.

You can also compare the contents of the clipboard with a particular file by right clicking that file and choosing **Kaleidoscope&rarr;Diff With Clipboard**.

## MIT License

Copyright (c) 2013 Ian Beck

The Kaleidoscope trademark and associated imagery all rights reserved by [Black Pixel](http://www.blackpixel.com/)

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
