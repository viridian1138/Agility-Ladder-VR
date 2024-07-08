


#$$strtCprt
"""
* Agility Ladder (Full Body Track) VR
* 
* Copyright (C) 2022-2024 Thornton Green
* 
* This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as
* published by the Free Software Foundation; either version 3 of the License, or (at your option) any later version.
* This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty 
* of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
* You should have received a copy of the GNU General Public License along with this program; if not, 
* see <http://www.gnu.org/licenses>.
* Additional permission under GNU GPL version 3 section 7
*
"""
#$$endCprt



import Vec3


class Target(object):
    
    def __init__(self):
        self.strtPos = Vec3.Vec3();
        self.endPos = Vec3.Vec3();
        self.initialStart = False;
        self.collisionEnable = False;
        self.collided = False
        

    def add(self, inA ):
        self.x = self.x + inA.x
        self.y = self.y + inA.y
        self.z = self.z + inA.z
 
 
