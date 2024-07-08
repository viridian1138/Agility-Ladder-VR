


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



import iRenderGen
import RetainedMode
import Vec3




#
# IRenderGen subclass for a single-color tetrahedron
#
class SingleColorTetrahedron(iRenderGen.IRenderGen):
    
    def __init__(self):
        self.posn = Vec3.Vec3()
        self.size = Vec3.Vec3()
        self.color = Vec3.Vec3()
        self.rotation = Vec3.Vec3()
    
        self.posn.x = 0.0
        self.posn.y = 1.0
        self.posn.z = 0.0
    
        self.size = 1.0
    
        self.color.x = 1.0
        self.color.y = 0.0
        self.color.z = 1.0


    def setFixedPosn(self, fixed : bool ):
        self.posn.setFixedPosn(fixed)


    def getFixedPosn(self ):
        return self.posn.getFixedPosn()

    
    def genPrev(self, gen : RetainedMode.RetainedMode ):
    
        gen.storeVertexLength()
    
    
        self.vec0 = gen.allocVertex()
        self.vec0.set( -( 0.5 * self.size ) , -( 0.5 * self.size ) , -( 0.5 * self.size ) )
        self.vec0.add( self.posn )
        self.vec0.setFixedPosn( self.posn.getFixedPosn() )
        
        
        self.vec1 = gen.allocVertex()
        self.vec1.set( +( 0.5 * self.size ), +( 0.5 * self.size ), -( 0.5 * self.size ) )
        self.vec1.add( self.posn )
        self.vec1.setFixedPosn( self.posn.getFixedPosn() )
        
        
        self.vec2 = gen.allocVertex()
        self.vec2.set( +( 0.5 * self.size ), -( 0.5 * self.size ), +( 0.5 * self.size ) )
        self.vec2.add( self.posn )
        self.vec2.setFixedPosn( self.posn.getFixedPosn() )
        
        
        self.vec3 = gen.allocVertex()
        self.vec3.set( -( 0.5 * self.size ), +( 0.5 * self.size ), +( 0.5 * self.size ) )
        self.vec3.add( self.posn )
        self.vec3.setFixedPosn( self.posn.getFixedPosn() )
        
        
        
        face0 = gen.allocFace()
        face0.faceColor = self.color
        face0.normal.calcNormal(self.vec0, self.vec1, self.vec2)
        face0.normal = face0.normal.checkNormal( self.vec0 , self.posn )
        
        
        face1 = gen.allocFace()
        face1.faceColor = self.color
        face1.normal.calcNormal(self.vec0, self.vec1, self.vec3)
        face1.normal = face1.normal.checkNormal( self.vec0 , self.posn )
        
        
        
        face2 = gen.allocFace()
        face2.faceColor = self.color
        face2.normal.calcNormal(self.vec0, self.vec2, self.vec3)
        face2.normal = face2.normal.checkNormal( self.vec0 , self.posn )
        
        
        
        face3 = gen.allocFace()
        face3.faceColor = self.color
        face3.normal.calcNormal(self.vec1, self.vec2, self.vec3)
        face3.normal = face3.normal.checkNormal( self.vec1 , self.posn )
        
        
        indices = [
            0, 1, 2,
            0, 1, 3,
            0, 2, 3,
            1, 2, 3
            ]
        
        
        gen.allocIndices( indices )


    
    def dynamicSetPosn(self, x : float , y : float , z : float , lst : list ):
    
        self.posn.set( x , y , z )
        
    
        self.vec0.set( -( 0.5 * self.size ) , -( 0.5 * self.size ) , -( 0.5 * self.size ) )
        self.vec0.add( self.posn )
        lst.append( self.vec0 )
        
        
        self.vec1.set( +( 0.5 * self.size ), +( 0.5 * self.size ), -( 0.5 * self.size ) )
        self.vec1.add( self.posn )
        lst.append( self.vec1 )
        
        
        self.vec2.set( +( 0.5 * self.size ), -( 0.5 * self.size ), +( 0.5 * self.size ) )
        self.vec2.add( self.posn )
        lst.append( self.vec2 )
        
        
        self.vec3.set( -( 0.5 * self.size ), +( 0.5 * self.size ), +( 0.5 * self.size ) )
        self.vec3.add( self.posn )
        lst.append( self.vec3 )
        
      
      
