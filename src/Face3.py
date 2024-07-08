


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


class Face3(object):
    
    def __init__(self):
        self.normal = Vec3.Vec3()
        self.faceColor = Vec3.Vec3()
        self.faceColor.set( 1.0 , 1.0 , 0.0 )
        self.specularColor = Vec3.Vec3()
        self.specularColor.set( 0x11 / 255.0 , 0x11 / 255.0 , 0x11 / 255.0 )
        self.ambientColor = Vec3.Vec3()
        self.ambientColor.set( 0.0 , 0.0 , 0.0 )
        self.shininess = 30.0 # Specular exponent
 
