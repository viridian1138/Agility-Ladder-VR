


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



class Vec3(object):
    
    def __init__(self):
        self.x = 0.0
        self.y = 0.0
        self.z = 0.0
        self.uniformIndex = None
        self.fixedPosn = False
        self.glslColorString = None

    def add(self, inA ):
        self.x = self.x + inA.x
        self.y = self.y + inA.y
        self.z = self.z + inA.z

    def sub(self, inA ):
        self.x = self.x - inA.x
        self.y = self.y - inA.y
        self.z = self.z - inA.z

    def negate(self ):
        self.x = - self.x
        self.y = - self.y
        self.z = - self.z

    def set(self, x : float , y : float , z : float ):
        self.x = x
        self.y = y
        self.z = z

    def crossProduct(self, a, b ):
        self.x = a.y * b.z - a.z * b.y
        self.y = a.z * b.x - a.x * b.z
        self.z = a.x * b.y - a.y * b.z

    def dotProduct(self, a ):
        return self.x * a.x + self.y * a.y + self.z * a.z

    def calcNormal(self, a, b, c ):
        deltaA = Vec3()
        deltaB = Vec3()
        deltaA.set( b.x , b.y , b.z )
        deltaB.set( c.x , c.y , c.z )
        deltaA.sub( a )
        deltaB.sub( b )
        self.crossProduct( deltaA , deltaB )
        
    def checkNormal(self, ptA, cntr):
        delta = Vec3()
        delta.set( ptA.x , ptA.y , ptA.z )
        delta.sub( cntr )
        ret = Vec3()
        ret.set( self.x , self.y , self.z )
        dotVal = ret.dotProduct( delta )
        if dotVal < 0.0 :
            ret.negate()
        return ret

    def setUniformIndex(self, index : int ):
        self.uniformIndex = index

    def getUniformIndex(self ):
        return self.uniformIndex

    def setFixedPosn(self, fixed : bool ):
        self.fixedPosn = fixed

    def getFixedPosn(self ):
        return self.fixedPosn

    def retainedStr( self ) :
        if not ( self.uniformIndex is None ) :
            return "uniformVector" + str( self.uniformIndex )
        elif not( self.glslColorString is None ) :
            return self.glslColorString
        else :
            return "vec3(" + str(self.x) + "," + str(self.y) + "," + str(self.z) + ")"
 
 
