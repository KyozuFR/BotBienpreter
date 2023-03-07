# BotBienpreter
Solves the problem of "Bienpreter.com" project openings at a defined time. With this you can put your investment orders a few hours in advance.

## requirement
install python
install selenium (pip install selenium)
install firefox and the latest geckodriver (**!!!geckodriver should be put at the root of the program**)

## functioning
Create a file "mdp.txt" and put your ID at the top of the document with this syntax:


e-mail|password


No spaces, no line breaks.
Then put the link of the project "bienpreter.com" and the amount with this syntax:


link|amount


here you can put as many links as you want, the script will use them in order.

**!!!Be careful, the website has a timeout (which I don't know) so launch the script a reasonable time in advance. I tried to launch it a day before and the bot got disconnected.**


### Copyright
***BotBienpreter Copyright (C) 2023  Linares Julien***

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
