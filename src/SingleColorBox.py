


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
# IRenderGen subclass for a single-color box
#
class SingleColorBox(iRenderGen.IRenderGen):
    
    def __init__(self):
        self.posn = Vec3.Vec3()
        self.size = Vec3.Vec3()
        self.color = Vec3.Vec3()
        self.rotation = Vec3.Vec3()

        self.posn.x = 0.0
        self.posn.y = 1.0
        self.posn.z = 0.0

        self.size.x = 1.0
        self.size.y = 1.0
        self.size.z = 1.0

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
        self.vec0.set( -( 0.5 * self.size.x ) , -( 0.5 * self.size.y ) , -( 0.5 * self.size.z ) )
        self.vec0.add( self.posn )
        self.vec0.setFixedPosn( self.posn.getFixedPosn() )
        
        
        self.vec1 = gen.allocVertex()
        self.vec1.set( +( 0.5 * self.size.x ), -( 0.5 * self.size.y ), -( 0.5 * self.size.z ) )
        self.vec1.add( self.posn )
        self.vec1.setFixedPosn( self.posn.getFixedPosn() )
        
        
        self.vec2 = gen.allocVertex()
        self.vec2.set( -( 0.5 * self.size.x ), +( 0.5 * self.size.y ), -( 0.5 * self.size.z ) )
        self.vec2.add( self.posn )
        self.vec2.setFixedPosn( self.posn.getFixedPosn() )
        
        
        self.vec3 = gen.allocVertex()
        self.vec3.set( +( 0.5 * self.size.x ), +( 0.5 * self.size.y ), -( 0.5 * self.size.z ) )
        self.vec3.add( self.posn )
        self.vec3.setFixedPosn( self.posn.getFixedPosn() )
        
        
        self.vec4 = gen.allocVertex()
        self.vec4.set( -( 0.5 * self.size.x ), -( 0.5 * self.size.y ), +( 0.5 * self.size.z ) )
        self.vec4.add( self.posn )
        self.vec4.setFixedPosn( self.posn.getFixedPosn() )
        
        
        self.vec5 = gen.allocVertex()
        self.vec5.set( +( 0.5 * self.size.x ), -( 0.5 * self.size.y ), +( 0.5 * self.size.z ) )
        self.vec5.add( self.posn )
        self.vec5.setFixedPosn( self.posn.getFixedPosn() )
        
        
        self.vec6 = gen.allocVertex()
        self.vec6.set( -( 0.5 * self.size.x ), +( 0.5 * self.size.y ), +( 0.5 * self.size.z ) )
        self.vec6.add( self.posn )
        self.vec6.setFixedPosn( self.posn.getFixedPosn() )
        
        
        self.vec7 = gen.allocVertex()
        self.vec7.set( +( 0.5 * self.size.x ), +( 0.5 * self.size.y ), +( 0.5 * self.size.z ) )
        self.vec7.add( self.posn )
        self.vec7.setFixedPosn( self.posn.getFixedPosn() )
        
        
        
        face0 = gen.allocFace()
        face0.faceColor = self.color
        face0.normal.set( 0.0, 0.0, -1.0 )
        face0.normal = face0.normal.checkNormal( self.vec0 , self.posn )
        
        
        face1 = gen.allocFace()
        face1.faceColor = self.color
        face1.normal.set( 0.0, 0.0, -1.0 )
        face1.normal = face1.normal.checkNormal( self.vec0 , self.posn )
        
        
        
        face2 = gen.allocFace()
        face2.faceColor = self.color
        face2.normal.set( 0.0, 0.0, 1.0 )
        face2.normal = face2.normal.checkNormal( self.vec4 , self.posn )
        
        
        
        face3 = gen.allocFace()
        face3.faceColor = self.color
        face3.normal.set( 0.0, 0.0, 1.0 )
        face3.normal = face3.normal.checkNormal( self.vec4 , self.posn )
        
        
        
        face4 = gen.allocFace()
        face4.faceColor = self.color
        face4.normal.set( 1.0, 0.0, 0.0 )
        face4.normal = face4.normal.checkNormal( self.vec0 , self.posn )
        
        
        
        face5 = gen.allocFace()
        face5.faceColor = self.color
        face5.normal.set( 1.0, 0.0, 0.0 )
        face5.normal = face5.normal.checkNormal( self.vec0 , self.posn )
        
        
        
        face6 = gen.allocFace()
        face6.faceColor = self.color
        face6.normal.set( -1.0, 0.0, 0.0 )
        face6.normal = face6.normal.checkNormal( self.vec1 , self.posn )
        
        
        
        face7 = gen.allocFace()
        face7.faceColor = self.color
        face7.normal.set( -1.0, 0.0, 0.0 )
        face7.normal = face7.normal.checkNormal( self.vec1 , self.posn )
        
        
        
        face8 = gen.allocFace()
        face8.faceColor = self.color
        face8.normal.set( 0.0, 1.0, 0.0 )
        face8.normal = face8.normal.checkNormal( self.vec2 , self.posn )
        
        
        
        face9 = gen.allocFace()
        face9.faceColor = self.color
        face9.normal.set( 0.0, 1.0, 0.0 )
        face9.normal = face9.normal.checkNormal( self.vec2 , self.posn )
        
        
        
        face10 = gen.allocFace()
        face10.faceColor = self.color
        face10.normal.set( 0.0, -1.0, 0.0 )
        face10.normal = face10.normal.checkNormal( self.vec0 , self.posn )
        
        
        
        face11 = gen.allocFace()
        face11.faceColor = self.color
        face11.normal.set( 0.0, -1.0, 0.0 )
        face11.normal = face11.normal.checkNormal( self.vec0 , self.posn )
        
        
        indices = [
            0, 1, 2, 2, 1, 3, # front
            4, 6, 5, 6, 5, 7, # back
            0, 2, 4, 4, 2, 6, # left
            1, 3, 5, 5, 3, 7, # right
            2, 6, 3, 6, 3, 7, # top
            0, 1, 4, 4, 1, 5  # bottom
            ]
        
        
        gen.allocIndices( indices )


    
    def dynamicSetPosn(self, x : float , y : float , z : float , lst : list ):
    
        self.posn.set( x , y , z )
        
    
        self.vec0.set( -( 0.5 * self.size.x ) , -( 0.5 * self.size.y ) , -( 0.5 * self.size.z ) )
        self.vec0.add( self.posn )
        lst.append( self.vec0 )
        
        
        self.vec1.set( +( 0.5 * self.size.x ), -( 0.5 * self.size.y ), -( 0.5 * self.size.z ) )
        self.vec1.add( self.posn )
        lst.append( self.vec1 )
        
        
        self.vec2.set( -( 0.5 * self.size.x ), +( 0.5 * self.size.y ), -( 0.5 * self.size.z ) )
        self.vec2.add( self.posn )
        lst.append( self.vec2 )
        
        
        self.vec3.set( +( 0.5 * self.size.x ), +( 0.5 * self.size.y ), -( 0.5 * self.size.z ) )
        self.vec3.add( self.posn )
        lst.append( self.vec3 )
        
        
        self.vec4.set( -( 0.5 * self.size.x ), -( 0.5 * self.size.y ), +( 0.5 * self.size.z ) )
        self.vec4.add( self.posn )
        lst.append( self.vec4 )
        
        
        self.vec5.set( +( 0.5 * self.size.x ), -( 0.5 * self.size.y ), +( 0.5 * self.size.z ) )
        self.vec5.add( self.posn )
        lst.append( self.vec5 )
        
        
        self.vec6.set( -( 0.5 * self.size.x ), +( 0.5 * self.size.y ), +( 0.5 * self.size.z ) )
        self.vec6.add( self.posn )
        lst.append( self.vec6 )
        
        
        self.vec7.set( +( 0.5 * self.size.x ), +( 0.5 * self.size.y ), +( 0.5 * self.size.z ) )
        self.vec7.add( self.posn )
        lst.append( self.vec7 )
        
      
      
