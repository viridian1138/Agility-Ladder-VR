


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
import Face3


FACE_LIMIT = 222



FACE_VECT = 3 * FACE_LIMIT

FACE_VECT_STR = str( FACE_VECT )



FACE_INDEX = 3 * FACE_VECT

FACE_INDEX_STR = str( FACE_INDEX )




INDEX_MAX = 2 * FACE_INDEX




class RetainedMode(object):
    
    def __init__(self):
        self.vertices = []
        self.faces = []
        self.indices = []
        self.storedVertexLength = 0
        
    def allocVertex(self):
        vec3 = Vec3.Vec3()
        self.vertices = self.vertices + [ vec3 ]
        return vec3 
        
    def allocFace(self):
        face3 = Face3.Face3()
        self.faces = self.faces + [ face3 ]
        return face3
        
    def storeVertexLength(self):
        self.storedVertexLength = len( self.vertices )
        
    def allocIndices(self, indexList : list ) :
        storedVertexLength = self.storedVertexLength
        prevIndexLength = len( self.indices ) 
        self.indices = self.indices + indexList;
        for cnt in range( prevIndexLength , len( self.indices ) ) :
            self.indices[ cnt ] = self.indices[ cnt ] + storedVertexLength
        
    def uniformLayoutStr(self):
        currentUniformIndex = 100
        sz = str(len(self.vertices))
        ret = "\n"
        for x in range(len(self.vertices)):
            if not ( self.vertices[x].getFixedPosn() ) :
                indexStr = str( currentUniformIndex )
                ret = ret + "layout(location = " + indexStr + ") uniform vec3 uniformVector" + indexStr + "; \n"
                self.vertices[x].setUniformIndex( currentUniformIndex )
                currentUniformIndex = currentUniformIndex + 3
        ret = ret + "\n"
        self.numUniforms = currentUniformIndex - 100
        return ret
        
    def vertexStr(self):
        sz = str(len(self.vertices))
        ret = "const vec3 VERTEX_ARR[" + sz + "] = vec3[" + sz + "]( \n"
        for x in range(len(self.vertices)):
            ret = ret + self.vertices[x].retainedStr()
            if not x == ( len(self.vertices) - 1 ) :
                ret = ret + ","
            ret = ret + "\n"
        ret = ret + "            ); \n"
        return ret
        
    def faceColorStr1(self):
        ret = ""
        
        if len( self.indices ) > ( INDEX_MAX - 1 ) :
           raise Exception( "Internal Error" )
        
        szI = FACE_VECT if FACE_VECT < len( self.faces ) else len( self.faces )
        sz = str(szI)
        ret = ret + "const vec3 FACE_COLORS[" + sz + "] = vec3[" + sz + "]( \n"
        for x in range(szI):
            ret = ret + self.faces[x].faceColor.retainedStr()
            if not x == ( szI - 1 ) :
                ret = ret + ","
            ret = ret + "\n"
        ret = ret + "            ); \n"
        return ret
        
    def faceColorStr2(self):
        ret = ""
        
        if len( self.indices ) > ( INDEX_MAX - 1 ) :
           raise Exception( "Internal Error" )
        
        ret = ret + "\n"
        
        szI = len(self.faces) - FACE_VECT if FACE_VECT < len( self.faces ) else 0
        sz = str(szI)
        ret = ret + "const vec3 FACE_COLORS[" + sz + "] = vec3[" + sz + "]( \n"
        for x in range(szI):
            ret = ret + self.faces[x+FACE_VECT].faceColor.retainedStr()
            if not x == ( szI - 1 ) :
                ret = ret + ","
            ret = ret + "\n"
        ret = ret + "            ); \n"
        return ret
        
    def faceUnitNormalStr1(self):
        ret = ""
        
        if len( self.indices ) > ( INDEX_MAX - 1 ) :
           raise Exception( "Internal Error" )
        
        szI = FACE_VECT if FACE_VECT < len( self.faces ) else len( self.faces )
        sz = str(szI)
        ret = ret = "const vec3 FACE_UNIT_NORMALS[" + sz + "] = vec3[" + sz + "]( \n"
        for x in range(szI):
            ret = ret + self.faces[x].normal.retainedStr()
            if not x == ( szI - 1 ) :
                ret = ret + ","
            ret = ret + "\n"
        ret = ret + "            ); \n"
        return ret
        
    def faceUnitNormalStr2(self):
        ret = ""
        
        if len( self.indices ) > ( INDEX_MAX - 1 ) :
           raise Exception( "Internal Error" )
        
        ret = ret + "\n"
        
        szI = len(self.faces) - FACE_VECT if FACE_VECT < len( self.faces ) else 0
        sz = str(szI)
        ret = ret + "const vec3 FACE_UNIT_NORMALS[" + sz + "] = vec3[" + sz + "]( \n"
        for x in range(szI):
            ret = ret + self.faces[x+FACE_VECT].normal.retainedStr()
            if not x == ( szI - 1 ) :
                ret = ret + ","
            ret = ret + "\n"
        ret = ret + "            ); \n"
        return ret
        
    def faceIndexStr1(self):
        ret = ""
        
        if len( self.indices ) > ( INDEX_MAX - 1 ) :
           raise Exception( "Internal Error" )
        
        if True :
            szI = FACE_INDEX  if FACE_INDEX < len( self.indices ) else len( self.indices )
            sz = str(szI)
            ret = ret + "const int FACE_INDICES[" + sz + "] = int[" + sz + "]( \n"
            for x in range(szI):
                r = self.indices[x]
                ret = ret + str( r )
                if not x == ( szI - 1 ) :
                    ret = ret + ","
                ret = ret + "\n"
            ret = ret + "            ); \n"
        
        return ret
        
    def faceIndexStr2(self):
        ret = ""
        
        if len( self.indices ) > ( INDEX_MAX - 1 ) :
           raise Exception( "Internal Error" )
        
        ret = ret + "\n"
        
        if True :
            szI = len(self.indices) - FACE_INDEX  if FACE_INDEX < len( self.indices ) else 0
            sz = str(szI)
            ret = ret + "const int FACE_INDICES[" + sz + "] = int[" + sz + "]( \n"
            for x in range(szI):
                r = self.indices[x+FACE_INDEX]
                ret = ret + str( r )
                if not x == ( szI - 1 ) :
                    ret = ret + ","
                ret = ret + "\n"
            ret = ret + "            ); \n"
        
        return ret
    
    def getIndexSize1(self):
        return FACE_INDEX
    
    def getIndexSize2(self):
        return len(self.indices) - FACE_INDEX
        
    
  
   
  
    