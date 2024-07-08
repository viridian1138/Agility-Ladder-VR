


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
import SingleColorFlatXY
import Vec3




#
# A spatially fixed instance of a seven segment display
#
class SevenSegmentFixed(iRenderGen.IRenderGen):
    
    def __init__(self):
        self.segment0 = SingleColorFlatXY.SingleColorFlatXY()
        self.segment1 = SingleColorFlatXY.SingleColorFlatXY()
        self.segment2 = SingleColorFlatXY.SingleColorFlatXY()
        self.segment3 = SingleColorFlatXY.SingleColorFlatXY()
        self.segment4 = SingleColorFlatXY.SingleColorFlatXY()
        self.segment5 = SingleColorFlatXY.SingleColorFlatXY()
        self.segment6 = SingleColorFlatXY.SingleColorFlatXY()


    def init(self, cntrPosn : Vec3.Vec3 , colorGlslPrefix : str ):
        
        segSize = 0.16;
        
        longAxisSegSize = 4 * segSize
        
        segSizeGeomHoriz = Vec3.Vec3()
        segSizeGeomHoriz.set(
           longAxisSegSize,
           segSize,
           segSize
         );
        
        segSizeGeomVert = Vec3.Vec3()
        segSizeGeomVert.set(
           segSize,
           longAxisSegSize,
           segSize
         );
         
        self.segment0.posn.set(cntrPosn.x, cntrPosn.y + 5.0 * segSize, cntrPosn.z)
        self.segment0.color = Vec3.Vec3()
        self.segment0.color.set( 0.0 , 1.0 , 0.0 )
        self.segment0.color.glslColorString = colorGlslPrefix + "0"
        self.segment0.size = segSizeGeomHoriz
        
        self.segment1.posn.set(cntrPosn.x - 2.5 * segSize, cntrPosn.y + 2.5 * segSize, cntrPosn.z)
        self.segment1.color = Vec3.Vec3()
        self.segment1.color.set( 0.0 , 1.0 , 0.0 )
        self.segment1.color.glslColorString = colorGlslPrefix + "1"
        self.segment1.size = segSizeGeomVert
        
        self.segment2.posn.set(cntrPosn.x + 2.5 * segSize, cntrPosn.y + 2.5 * segSize, cntrPosn.z)
        self.segment2.color = Vec3.Vec3()
        self.segment2.color.set( 0.0 , 1.0 , 0.0 )
        self.segment2.color.glslColorString = colorGlslPrefix + "2"
        self.segment2.size = segSizeGeomVert
        
        self.segment3.posn.set(cntrPosn.x, cntrPosn.y + 0.0 * segSize, cntrPosn.z)
        self.segment3.color = Vec3.Vec3()
        self.segment3.color.set( 0.0 , 1.0 , 0.0 )
        self.segment3.color.glslColorString = colorGlslPrefix + "3"
        self.segment3.size = segSizeGeomHoriz
        
        self.segment4.posn.set(cntrPosn.x - 2.5 * segSize, cntrPosn.y + (-2.5) * segSize, cntrPosn.z)
        self.segment4.color = Vec3.Vec3()
        self.segment4.color.set( 0.0 , 1.0 , 0.0 )
        self.segment4.color.glslColorString = colorGlslPrefix + "4"
        self.segment4.size = segSizeGeomVert
        
        self.segment5.posn.set(cntrPosn.x + 2.5 * segSize, cntrPosn.y + (-2.5) * segSize, cntrPosn.z)
        self.segment5.color = Vec3.Vec3()
        self.segment5.color.set( 0.0 , 1.0 , 0.0 )
        self.segment5.color.glslColorString = colorGlslPrefix + "5"
        self.segment5.size = segSizeGeomVert
        
        self.segment6.posn.set(cntrPosn.x, cntrPosn.y + (-5.0) * segSize, cntrPosn.z)
        self.segment6.color = Vec3.Vec3()
        self.segment6.color.set( 0.0 , 1.0 , 0.0 )
        self.segment6.color.glslColorString = colorGlslPrefix + "6"
        self.segment6.size = segSizeGeomHoriz
        
        
        
        self.segment0.setFixedPosn( True )
        self.segment1.setFixedPosn( True )
        self.segment2.setFixedPosn( True )
        self.segment3.setFixedPosn( True )
        self.segment4.setFixedPosn( True )
        self.segment5.setFixedPosn( True )
        self.segment6.setFixedPosn( True )



    
    def genPrev(self, gen : RetainedMode.RetainedMode ):
    
        self.segment0.genPrev(gen)
        self.segment1.genPrev(gen)
        self.segment2.genPrev(gen)
        self.segment3.genPrev(gen)
        self.segment4.genPrev(gen)
        self.segment5.genPrev(gen)
        self.segment6.genPrev(gen)


    
    def dynamicSetPosn(self, x : float , y : float , z : float , lst : list ):
    
        raise Exception( "Not Applicable" )
        
      
      
