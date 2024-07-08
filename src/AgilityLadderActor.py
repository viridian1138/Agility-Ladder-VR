


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



import time
import random

from textwrap import dedent

from OpenGL.GL import *  # @UnusedWildImport # this comment squelches an IDE warning
from OpenGL.GL.shaders import compileShader, compileProgram

from openvr.glframework import shader_string

import openvr


import Vec3
import Target
import RetainedMode
import SceneGenerator
import SoundServices
from glfw import TRUE, FALSE


FACE_LIMIT = RetainedMode.FACE_LIMIT



FACE_VECT = RetainedMode.FACE_VECT

FACE_VECT_STR = RetainedMode.FACE_VECT_STR



FACE_INDEX = RetainedMode.FACE_INDEX

FACE_INDEX_STR = RetainedMode.FACE_INDEX_STR




INDEX_MAX = RetainedMode.INDEX_MAX




class AgilityLadderActor(object):

    
    def __init__(self):
        NO_ID = -7777
        self.shader1 = 0
        self.shader2 = 0
        self.vao = None
        self.ID_LeftHand_Green = NO_ID
        self.ID_RightHand_Red = NO_ID
        self.ID_LeftFoot_Green = NO_ID
        self.ID_RightFoot_Red = NO_ID
        self.hmd = None
        self.retained = None
        self.scene = None
        self.ctime = -1.0
        self.initialTime = -1.0
        self.gInitialized = False
        self.hmdLocn = Vec3.Vec3()
    
    
    def init_gl(self):
        
        print( "Running Scene Generator A !!!!!!!!!!!!!!!!!!!!!!" )
        
        scene = SceneGenerator.SceneGenerator()
        self.scene = scene
        
        
        
        self.soundServices = SoundServices.SoundServices()
        
        self.soundServices.init()
        
        scene.soundServices = self.soundServices
        
        
        
        
        
        
        
        
        




      
        
        
        



        retm = scene.generate()
        self.retained = retm
        
        
        uniformLayoutStr = retm.uniformLayoutStr()


        vertexStr = retm.vertexStr()


        faceColorStr1 = retm.faceColorStr1()


        faceColorStr2 = retm.faceColorStr2()


        faceUnitNormalStr1 = retm.faceUnitNormalStr1()


        faceUnitNormalStr2 = retm.faceUnitNormalStr2()


        faceIndexStr1 = retm.faceIndexStr1()


        faceIndexStr2 = retm.faceIndexStr2()

        
        compileShaderString1 = ( "\n" +
"            // Adapted from @jherico's RiftDemo.py in pyovr \n" +
"             \n" +
"            layout(location = 0) uniform mat4 Projection = mat4(1); \n" +
"            layout(location = 4) uniform mat4 ModelView = mat4(1); \n" +
"            layout(location = 8) uniform float Size = 1.0; \n" +
"            layout(location = " + str( scene.deltaTimeIndex ) + ") uniform float deltaTimeIndex = 0.0; \n" +
"             \n" +
"             \n" +
"             // Calculate the current hour, minute, and second based on the elapsed time\n" +
"             int hours = int(deltaTimeIndex / 3600);\n" +
"             int minutes = int((deltaTimeIndex - hours * 3600) / 60);\n" +
"             int seconds = int(mod(deltaTimeIndex, 60));\n" +
"             \n" +
"             \n" +
"             // The number of digits in base 10\n" +
"             const int NUM_DIGITS = 10;\n" +
"             \n" +
"             \n" +
"             // Convert to single digits\n" +
"             int hour_digit2 = hours % NUM_DIGITS;\n" +
"             int minute_digit1 = minutes / NUM_DIGITS;\n" +
"             int minute_digit2 = minutes % NUM_DIGITS;\n" +
"             int second_digit1 = seconds / NUM_DIGITS;\n" +
"             int second_digit2 = seconds % NUM_DIGITS;\n" +
"             \n" +
"             \n" +
"             struct SevenSegment\n" +
"             {\n" +
"                    bool segments[7];\n" +
"             };\n" +
"             \n" +
"             \n" +
"             struct DigitSegments\n" +
"             {\n" +
"                    SevenSegment digits[NUM_DIGITS];\n" +
"             };\n" +
"             \n" +
"             \n" +
"             const SevenSegment segment0 = SevenSegment( bool[7]( \n" +
"                                       true,\n" +
"                                true,           true,\n" +
"                                       false,\n" +
"                                true,           true,\n" +
"                                       true   ) );\n" +
"             \n" +
"             \n" +
"             const SevenSegment segment1 = SevenSegment( bool[7]( \n" +
"                                       false,\n" +
"                                false,          true,\n" +
"                                       false,\n" +
"                                false,          true,\n" +
"                                       false  ) );\n" +
"             \n" +
"             \n" +
"             const SevenSegment segment2 = SevenSegment( bool[7]( \n" +
"                                       true,\n" +
"                                false,          true,\n" +
"                                       true,\n" +
"                                true,           false,\n" +
"                                       true  ) );\n" +
"             \n" +
"             \n" +
"             const SevenSegment segment3 = SevenSegment( bool[7]( \n" +
"                                       true,\n" +
"                                false,          true,\n" +
"                                       true,\n" +
"                                false,          true,\n" +
"                                       true  ) );\n" +
"             \n" +
"             \n" +
"             const SevenSegment segment4 = SevenSegment( bool[7]( \n" +
"                                       false,\n" +
"                                true,           true,\n" +
"                                       true,\n" +
"                                false,          true,\n" +
"                                       false  ) );\n" +
"             \n" +
"             \n" +
"             const SevenSegment segment5 = SevenSegment( bool[7]( \n" +
"                                       true,\n" +
"                                true,           false,\n" +
"                                       true,\n" +
"                                false,          true,\n" +
"                                       true  ) );\n" +
"             \n" +
"             \n" +
"             const SevenSegment segment6 = SevenSegment( bool[7]( \n" +
"                                       true,\n" +
"                                true,           false,\n" +
"                                       true,\n" +
"                                true,           true,\n" +
"                                       true  ) );\n" +
"             \n" +
"             \n" +
"             const SevenSegment segment7 = SevenSegment( bool[7]( \n" +
"                                       true,\n" +
"                                false,          true,\n" +
"                                       false,\n" +
"                                false,          true,\n" +
"                                       false  ) );\n" +
"             \n" +
"             \n" +
"             const SevenSegment segment8 = SevenSegment( bool[7]( \n" +
"                                       true,\n" +
"                                true,           true,\n" +
"                                       true,\n" +
"                                true,           true,\n" +
"                                       true  ) );\n" +
"             \n" +
"             \n" +
"             const SevenSegment segment9 = SevenSegment( bool[7]( \n" +
"                                       true,\n" +
"                                true,           true,\n" +
"                                       true,\n" +
"                                false,          true,\n" +
"                                       true  ) );\n" +
"             \n" +
"             \n" +
"             const DigitSegments digitSegments = DigitSegments( SevenSegment[NUM_DIGITS]( \n" +
"                                segment0, \n" +
"                                segment1, \n" +
"                                segment2, \n" +
"                                segment3, \n" +
"                                segment4, \n" +
"                                segment5, \n" +
"                                segment6, \n" +
"                                segment7, \n" +
"                                segment8, \n" +
"                                segment9 ) ); \n" +
"             \n" +
"             \n" +
"             \n" +
"             SevenSegment hourSegment2 = digitSegments.digits[ hour_digit2 ];\n" +
"             \n" +
"             SevenSegment minuteSegment2 = digitSegments.digits[ minute_digit2 ];\n" +
"             \n" +
"             SevenSegment minuteSegment1 = digitSegments.digits[ minute_digit1 ];\n" +
"             \n" +
"             SevenSegment secondSegment2 = digitSegments.digits[ second_digit2 ];\n" +
"             \n" +
"             SevenSegment secondSegment1 = digitSegments.digits[ second_digit1 ];\n" +
"             \n" +
"             \n" +
"             \n" +
"             const vec3 SEGMENT_ON_COLOR = vec3(1.0, 0xc0 / 255.0 , 0.0);\n" +
"             \n" +
"             const vec3 SEGMENT_OFF_COLOR = vec3( 0x67 / 255.0 , 0xa5 / 255.0 , 0xee / 255.0 );\n" +
"             \n" +
"             \n" +
"             \n" +
"             \n" +
"             \n" +
"             \n" +
"             vec3 hourSegment2_segment0 = ( hourSegment2.segments[ 0 ] ) ? SEGMENT_ON_COLOR : SEGMENT_OFF_COLOR;\n" +
"             \n" +
"             vec3 hourSegment2_segment1 = ( hourSegment2.segments[ 1 ] ) ? SEGMENT_ON_COLOR : SEGMENT_OFF_COLOR;\n" +
"             \n" +
"             vec3 hourSegment2_segment2 = ( hourSegment2.segments[ 2 ] ) ? SEGMENT_ON_COLOR : SEGMENT_OFF_COLOR;\n" +
"             \n" +
"             vec3 hourSegment2_segment3 = ( hourSegment2.segments[ 3 ] ) ? SEGMENT_ON_COLOR : SEGMENT_OFF_COLOR;\n" +
"             \n" +
"             vec3 hourSegment2_segment4 = ( hourSegment2.segments[ 4 ] ) ? SEGMENT_ON_COLOR : SEGMENT_OFF_COLOR;\n" +
"             \n" +
"             vec3 hourSegment2_segment5 = ( hourSegment2.segments[ 5 ] ) ? SEGMENT_ON_COLOR : SEGMENT_OFF_COLOR;\n" +
"             \n" +
"             vec3 hourSegment2_segment6 = ( hourSegment2.segments[ 6 ] ) ? SEGMENT_ON_COLOR : SEGMENT_OFF_COLOR;\n" +
"             \n" +
"             \n" +
"             \n" +
"             \n" +
"             \n" +
"             \n" +
"             vec3 minuteSegment2_segment0 = ( minuteSegment2.segments[ 0 ] ) ? SEGMENT_ON_COLOR : SEGMENT_OFF_COLOR;\n" +
"             \n" +
"             vec3 minuteSegment2_segment1 = ( minuteSegment2.segments[ 1 ] ) ? SEGMENT_ON_COLOR : SEGMENT_OFF_COLOR;\n" +
"             \n" +
"             vec3 minuteSegment2_segment2 = ( minuteSegment2.segments[ 2 ] ) ? SEGMENT_ON_COLOR : SEGMENT_OFF_COLOR;\n" +
"             \n" +
"             vec3 minuteSegment2_segment3 = ( minuteSegment2.segments[ 3 ] ) ? SEGMENT_ON_COLOR : SEGMENT_OFF_COLOR;\n" +
"             \n" +
"             vec3 minuteSegment2_segment4 = ( minuteSegment2.segments[ 4 ] ) ? SEGMENT_ON_COLOR : SEGMENT_OFF_COLOR;\n" +
"             \n" +
"             vec3 minuteSegment2_segment5 = ( minuteSegment2.segments[ 5 ] ) ? SEGMENT_ON_COLOR : SEGMENT_OFF_COLOR;\n" +
"             \n" +
"             vec3 minuteSegment2_segment6 = ( minuteSegment2.segments[ 6 ] ) ? SEGMENT_ON_COLOR : SEGMENT_OFF_COLOR;\n" +
"             \n" +
"             \n" +
"             \n" +
"             vec3 minuteSegment1_segment0 = ( minuteSegment1.segments[ 0 ] ) ? SEGMENT_ON_COLOR : SEGMENT_OFF_COLOR;\n" +
"             \n" +
"             vec3 minuteSegment1_segment1 = ( minuteSegment1.segments[ 1 ] ) ? SEGMENT_ON_COLOR : SEGMENT_OFF_COLOR;\n" +
"             \n" +
"             vec3 minuteSegment1_segment2 = ( minuteSegment1.segments[ 2 ] ) ? SEGMENT_ON_COLOR : SEGMENT_OFF_COLOR;\n" +
"             \n" +
"             vec3 minuteSegment1_segment3 = ( minuteSegment1.segments[ 3 ] ) ? SEGMENT_ON_COLOR : SEGMENT_OFF_COLOR;\n" +
"             \n" +
"             vec3 minuteSegment1_segment4 = ( minuteSegment1.segments[ 4 ] ) ? SEGMENT_ON_COLOR : SEGMENT_OFF_COLOR;\n" +
"             \n" +
"             vec3 minuteSegment1_segment5 = ( minuteSegment1.segments[ 5 ] ) ? SEGMENT_ON_COLOR : SEGMENT_OFF_COLOR;\n" +
"             \n" +
"             vec3 minuteSegment1_segment6 = ( minuteSegment1.segments[ 6 ] ) ? SEGMENT_ON_COLOR : SEGMENT_OFF_COLOR;\n" +
"             \n" +
"             \n" +
"             \n" +
"             \n" +
"             \n" +
"             \n" +
"             vec3 secondSegment2_segment0 = ( secondSegment2.segments[ 0 ] ) ? SEGMENT_ON_COLOR : SEGMENT_OFF_COLOR;\n" +
"             \n" +
"             vec3 secondSegment2_segment1 = ( secondSegment2.segments[ 1 ] ) ? SEGMENT_ON_COLOR : SEGMENT_OFF_COLOR;\n" +
"             \n" +
"             vec3 secondSegment2_segment2 = ( secondSegment2.segments[ 2 ] ) ? SEGMENT_ON_COLOR : SEGMENT_OFF_COLOR;\n" +
"             \n" +
"             vec3 secondSegment2_segment3 = ( secondSegment2.segments[ 3 ] ) ? SEGMENT_ON_COLOR : SEGMENT_OFF_COLOR;\n" +
"             \n" +
"             vec3 secondSegment2_segment4 = ( secondSegment2.segments[ 4 ] ) ? SEGMENT_ON_COLOR : SEGMENT_OFF_COLOR;\n" +
"             \n" +
"             vec3 secondSegment2_segment5 = ( secondSegment2.segments[ 5 ] ) ? SEGMENT_ON_COLOR : SEGMENT_OFF_COLOR;\n" +
"             \n" +
"             vec3 secondSegment2_segment6 = ( secondSegment2.segments[ 6 ] ) ? SEGMENT_ON_COLOR : SEGMENT_OFF_COLOR;\n" +
"             \n" +
"             \n" +
"             \n" +
"             vec3 secondSegment1_segment0 = ( secondSegment1.segments[ 0 ] ) ? SEGMENT_ON_COLOR : SEGMENT_OFF_COLOR;\n" +
"             \n" +
"             vec3 secondSegment1_segment1 = ( secondSegment1.segments[ 1 ] ) ? SEGMENT_ON_COLOR : SEGMENT_OFF_COLOR;\n" +
"             \n" +
"             vec3 secondSegment1_segment2 = ( secondSegment1.segments[ 2 ] ) ? SEGMENT_ON_COLOR : SEGMENT_OFF_COLOR;\n" +
"             \n" +
"             vec3 secondSegment1_segment3 = ( secondSegment1.segments[ 3 ] ) ? SEGMENT_ON_COLOR : SEGMENT_OFF_COLOR;\n" +
"             \n" +
"             vec3 secondSegment1_segment4 = ( secondSegment1.segments[ 4 ] ) ? SEGMENT_ON_COLOR : SEGMENT_OFF_COLOR;\n" +
"             \n" +
"             vec3 secondSegment1_segment5 = ( secondSegment1.segments[ 5 ] ) ? SEGMENT_ON_COLOR : SEGMENT_OFF_COLOR;\n" +
"             \n" +
"             vec3 secondSegment1_segment6 = ( secondSegment1.segments[ 6 ] ) ? SEGMENT_ON_COLOR : SEGMENT_OFF_COLOR;\n" +
"             \n" +
"             \n" +
"             \n" +
"             \n" +
"             \n" +
"             \n" +
             uniformLayoutStr +
"             \n" +
"            // Minimum Y value is zero, so cube sits on the floor in room scale \n" +
             vertexStr +
"             \n" +
             faceUnitNormalStr1 +
"             \n" +
             faceColorStr1 +
"             \n" +
             faceIndexStr1 +
"             \n" +
"            out vec3 _color; \n" +
"            out vec3 _pixEye; \n" +
"            out vec3 _pixLight; \n" +
"            out vec3 _pixNormal; \n" +
"             \n" +
"            const vec3 lightPosn = vec3( 20.0 * cos( deltaTimeIndex ) , 20.0 * sin( deltaTimeIndex ) , 30.0 ); \n" +
"             \n" +
"            void main() { \n" +
"              _color = vec3(1.0, 0.0, 0.0); \n" +
"\n"
"              int vertexIndex = FACE_INDICES[gl_VertexID] ; \n" +
"\n"
"              int normalIndex = gl_VertexID / 3; \n" +
"               \n" +
"              _color = FACE_COLORS[normalIndex]; \n" +
"              if (any(lessThan(_color, vec3(0.0)))) { \n" +
"                  _color = vec3(1.0) + _color; \n" + 
"              } \n" +
"              vec3 wVertex = VERTEX_ARR[vertexIndex]; \n" + 
"              vec3 wNormal = FACE_UNIT_NORMALS[normalIndex]; \n" +  
"              vec3 wNormalPosn = wNormal + wVertex; \n" + 
"             \n" +
"              gl_Position = Projection * ModelView * vec4(VERTEX_ARR[vertexIndex] * Size, 1.0); \n" +
"              vec4 vertexPosition = ModelView * vec4(VERTEX_ARR[vertexIndex] * Size, 1.0); \n" +
"              _pixEye = - vertexPosition.xyz; \n" +
"              vec4 lightPosition = ModelView * vec4(lightPosn * Size, 1.0); \n" +
"              _pixLight = lightPosition.xyz - vertexPosition.xyz; \n" +
"              vec4 normalPosition = ModelView * vec4(wNormalPosn * Size, 1.0); \n" +
"              _pixNormal = normalPosition.xyz - vertexPosition.xyz; \n" +
"            } \n" +
            "\n" )

        
        
        compileShaderString2 = ( "\n" +
"            // Adapted from @jherico's RiftDemo.py in pyovr \n" +
"             \n" +
"            layout(location = 0) uniform mat4 Projection = mat4(1); \n" +
"            layout(location = 4) uniform mat4 ModelView = mat4(1); \n" +
"            layout(location = 8) uniform float Size = 1.0; \n" +
"            layout(location = " + str( scene.deltaTimeIndex ) + ") uniform float deltaTimeIndex = 0.0; \n" +
"             \n" +
"             \n" +
"             // Calculate the current hour, minute, and second based on the elapsed time\n" +
"             int hours = int(deltaTimeIndex / 3600);\n" +
"             int minutes = int((deltaTimeIndex - hours * 3600) / 60);\n" +
"             int seconds = int(mod(deltaTimeIndex, 60));\n" +
"             \n" +
"             \n" +
"             // The number of digits in base 10\n" +
"             const int NUM_DIGITS = 10;\n" +
"             \n" +
"             \n" +
"             // Convert to single digits\n" +
"             int hour_digit2 = hours % NUM_DIGITS;\n" +
"             int minute_digit1 = minutes / NUM_DIGITS;\n" +
"             int minute_digit2 = minutes % NUM_DIGITS;\n" +
"             int second_digit1 = seconds / NUM_DIGITS;\n" +
"             int second_digit2 = seconds % NUM_DIGITS;\n" +
"             \n" +
"             \n" +
"             struct SevenSegment\n" +
"             {\n" +
"                    bool segments[7];\n" +
"             };\n" +
"             \n" +
"             \n" +
"             struct DigitSegments\n" +
"             {\n" +
"                    SevenSegment digits[NUM_DIGITS];\n" +
"             };\n" +
"             \n" +
"             \n" +
"             const SevenSegment segment0 = SevenSegment( bool[7]( \n" +
"                                       true,\n" +
"                                true,           true,\n" +
"                                       false,\n" +
"                                true,           true,\n" +
"                                       true   ) );\n" +
"             \n" +
"             \n" +
"             const SevenSegment segment1 = SevenSegment( bool[7]( \n" +
"                                       false,\n" +
"                                false,          true,\n" +
"                                       false,\n" +
"                                false,          true,\n" +
"                                       false  ) );\n" +
"             \n" +
"             \n" +
"             const SevenSegment segment2 = SevenSegment( bool[7]( \n" +
"                                       true,\n" +
"                                false,          true,\n" +
"                                       true,\n" +
"                                true,           false,\n" +
"                                       true  ) );\n" +
"             \n" +
"             \n" +
"             const SevenSegment segment3 = SevenSegment( bool[7]( \n" +
"                                       true,\n" +
"                                false,          true,\n" +
"                                       true,\n" +
"                                false,          true,\n" +
"                                       true  ) );\n" +
"             \n" +
"             \n" +
"             const SevenSegment segment4 = SevenSegment( bool[7]( \n" +
"                                       false,\n" +
"                                true,           true,\n" +
"                                       true,\n" +
"                                false,          true,\n" +
"                                       false  ) );\n" +
"             \n" +
"             \n" +
"             const SevenSegment segment5 = SevenSegment( bool[7]( \n" +
"                                       true,\n" +
"                                true,           false,\n" +
"                                       true,\n" +
"                                false,          true,\n" +
"                                       true  ) );\n" +
"             \n" +
"             \n" +
"             const SevenSegment segment6 = SevenSegment( bool[7]( \n" +
"                                       true,\n" +
"                                true,           false,\n" +
"                                       true,\n" +
"                                true,           true,\n" +
"                                       true  ) );\n" +
"             \n" +
"             \n" +
"             const SevenSegment segment7 = SevenSegment( bool[7]( \n" +
"                                       true,\n" +
"                                false,          true,\n" +
"                                       false,\n" +
"                                false,          true,\n" +
"                                       false  ) );\n" +
"             \n" +
"             \n" +
"             const SevenSegment segment8 = SevenSegment( bool[7]( \n" +
"                                       true,\n" +
"                                true,           true,\n" +
"                                       true,\n" +
"                                true,           true,\n" +
"                                       true  ) );\n" +
"             \n" +
"             \n" +
"             const SevenSegment segment9 = SevenSegment( bool[7]( \n" +
"                                       true,\n" +
"                                true,           true,\n" +
"                                       true,\n" +
"                                false,          true,\n" +
"                                       true  ) );\n" +
"             \n" +
"             \n" +
"             const DigitSegments digitSegments = DigitSegments( SevenSegment[NUM_DIGITS]( \n" +
"                                segment0, \n" +
"                                segment1, \n" +
"                                segment2, \n" +
"                                segment3, \n" +
"                                segment4, \n" +
"                                segment5, \n" +
"                                segment6, \n" +
"                                segment7, \n" +
"                                segment8, \n" +
"                                segment9 ) ); \n" +
"             \n" +
"             \n" +
"             \n" +
"             SevenSegment hourSegment2 = digitSegments.digits[ hour_digit2 ];\n" +
"             \n" +
"             SevenSegment minuteSegment2 = digitSegments.digits[ minute_digit2 ];\n" +
"             \n" +
"             SevenSegment minuteSegment1 = digitSegments.digits[ minute_digit1 ];\n" +
"             \n" +
"             SevenSegment secondSegment2 = digitSegments.digits[ second_digit2 ];\n" +
"             \n" +
"             SevenSegment secondSegment1 = digitSegments.digits[ second_digit1 ];\n" +
"             \n" +
"             \n" +
"             \n" +
"             const vec3 SEGMENT_ON_COLOR = vec3(1.0, 0xc0 / 255.0 , 0.0);\n" +
"             \n" +
"             const vec3 SEGMENT_OFF_COLOR = vec3( 0x67 / 255.0 , 0xa5 / 255.0 , 0xee / 255.0 );\n" +
"             \n" +
"             \n" +
"             \n" +
"             \n" +
"             \n" +
"             \n" +
"             vec3 hourSegment2_segment0 = ( hourSegment2.segments[ 0 ] ) ? SEGMENT_ON_COLOR : SEGMENT_OFF_COLOR;\n" +
"             \n" +
"             vec3 hourSegment2_segment1 = ( hourSegment2.segments[ 1 ] ) ? SEGMENT_ON_COLOR : SEGMENT_OFF_COLOR;\n" +
"             \n" +
"             vec3 hourSegment2_segment2 = ( hourSegment2.segments[ 2 ] ) ? SEGMENT_ON_COLOR : SEGMENT_OFF_COLOR;\n" +
"             \n" +
"             vec3 hourSegment2_segment3 = ( hourSegment2.segments[ 3 ] ) ? SEGMENT_ON_COLOR : SEGMENT_OFF_COLOR;\n" +
"             \n" +
"             vec3 hourSegment2_segment4 = ( hourSegment2.segments[ 4 ] ) ? SEGMENT_ON_COLOR : SEGMENT_OFF_COLOR;\n" +
"             \n" +
"             vec3 hourSegment2_segment5 = ( hourSegment2.segments[ 5 ] ) ? SEGMENT_ON_COLOR : SEGMENT_OFF_COLOR;\n" +
"             \n" +
"             vec3 hourSegment2_segment6 = ( hourSegment2.segments[ 6 ] ) ? SEGMENT_ON_COLOR : SEGMENT_OFF_COLOR;\n" +
"             \n" +
"             \n" +
"             \n" +
"             \n" +
"             \n" +
"             \n" +
"             vec3 minuteSegment2_segment0 = ( minuteSegment2.segments[ 0 ] ) ? SEGMENT_ON_COLOR : SEGMENT_OFF_COLOR;\n" +
"             \n" +
"             vec3 minuteSegment2_segment1 = ( minuteSegment2.segments[ 1 ] ) ? SEGMENT_ON_COLOR : SEGMENT_OFF_COLOR;\n" +
"             \n" +
"             vec3 minuteSegment2_segment2 = ( minuteSegment2.segments[ 2 ] ) ? SEGMENT_ON_COLOR : SEGMENT_OFF_COLOR;\n" +
"             \n" +
"             vec3 minuteSegment2_segment3 = ( minuteSegment2.segments[ 3 ] ) ? SEGMENT_ON_COLOR : SEGMENT_OFF_COLOR;\n" +
"             \n" +
"             vec3 minuteSegment2_segment4 = ( minuteSegment2.segments[ 4 ] ) ? SEGMENT_ON_COLOR : SEGMENT_OFF_COLOR;\n" +
"             \n" +
"             vec3 minuteSegment2_segment5 = ( minuteSegment2.segments[ 5 ] ) ? SEGMENT_ON_COLOR : SEGMENT_OFF_COLOR;\n" +
"             \n" +
"             vec3 minuteSegment2_segment6 = ( minuteSegment2.segments[ 6 ] ) ? SEGMENT_ON_COLOR : SEGMENT_OFF_COLOR;\n" +
"             \n" +
"             \n" +
"             \n" +
"             vec3 minuteSegment1_segment0 = ( minuteSegment1.segments[ 0 ] ) ? SEGMENT_ON_COLOR : SEGMENT_OFF_COLOR;\n" +
"             \n" +
"             vec3 minuteSegment1_segment1 = ( minuteSegment1.segments[ 1 ] ) ? SEGMENT_ON_COLOR : SEGMENT_OFF_COLOR;\n" +
"             \n" +
"             vec3 minuteSegment1_segment2 = ( minuteSegment1.segments[ 2 ] ) ? SEGMENT_ON_COLOR : SEGMENT_OFF_COLOR;\n" +
"             \n" +
"             vec3 minuteSegment1_segment3 = ( minuteSegment1.segments[ 3 ] ) ? SEGMENT_ON_COLOR : SEGMENT_OFF_COLOR;\n" +
"             \n" +
"             vec3 minuteSegment1_segment4 = ( minuteSegment1.segments[ 4 ] ) ? SEGMENT_ON_COLOR : SEGMENT_OFF_COLOR;\n" +
"             \n" +
"             vec3 minuteSegment1_segment5 = ( minuteSegment1.segments[ 5 ] ) ? SEGMENT_ON_COLOR : SEGMENT_OFF_COLOR;\n" +
"             \n" +
"             vec3 minuteSegment1_segment6 = ( minuteSegment1.segments[ 6 ] ) ? SEGMENT_ON_COLOR : SEGMENT_OFF_COLOR;\n" +
"             \n" +
"             \n" +
"             \n" +
"             \n" +
"             \n" +
"             \n" +
"             vec3 secondSegment2_segment0 = ( secondSegment2.segments[ 0 ] ) ? SEGMENT_ON_COLOR : SEGMENT_OFF_COLOR;\n" +
"             \n" +
"             vec3 secondSegment2_segment1 = ( secondSegment2.segments[ 1 ] ) ? SEGMENT_ON_COLOR : SEGMENT_OFF_COLOR;\n" +
"             \n" +
"             vec3 secondSegment2_segment2 = ( secondSegment2.segments[ 2 ] ) ? SEGMENT_ON_COLOR : SEGMENT_OFF_COLOR;\n" +
"             \n" +
"             vec3 secondSegment2_segment3 = ( secondSegment2.segments[ 3 ] ) ? SEGMENT_ON_COLOR : SEGMENT_OFF_COLOR;\n" +
"             \n" +
"             vec3 secondSegment2_segment4 = ( secondSegment2.segments[ 4 ] ) ? SEGMENT_ON_COLOR : SEGMENT_OFF_COLOR;\n" +
"             \n" +
"             vec3 secondSegment2_segment5 = ( secondSegment2.segments[ 5 ] ) ? SEGMENT_ON_COLOR : SEGMENT_OFF_COLOR;\n" +
"             \n" +
"             vec3 secondSegment2_segment6 = ( secondSegment2.segments[ 6 ] ) ? SEGMENT_ON_COLOR : SEGMENT_OFF_COLOR;\n" +
"             \n" +
"             \n" +
"             \n" +
"             vec3 secondSegment1_segment0 = ( secondSegment1.segments[ 0 ] ) ? SEGMENT_ON_COLOR : SEGMENT_OFF_COLOR;\n" +
"             \n" +
"             vec3 secondSegment1_segment1 = ( secondSegment1.segments[ 1 ] ) ? SEGMENT_ON_COLOR : SEGMENT_OFF_COLOR;\n" +
"             \n" +
"             vec3 secondSegment1_segment2 = ( secondSegment1.segments[ 2 ] ) ? SEGMENT_ON_COLOR : SEGMENT_OFF_COLOR;\n" +
"             \n" +
"             vec3 secondSegment1_segment3 = ( secondSegment1.segments[ 3 ] ) ? SEGMENT_ON_COLOR : SEGMENT_OFF_COLOR;\n" +
"             \n" +
"             vec3 secondSegment1_segment4 = ( secondSegment1.segments[ 4 ] ) ? SEGMENT_ON_COLOR : SEGMENT_OFF_COLOR;\n" +
"             \n" +
"             vec3 secondSegment1_segment5 = ( secondSegment1.segments[ 5 ] ) ? SEGMENT_ON_COLOR : SEGMENT_OFF_COLOR;\n" +
"             \n" +
"             vec3 secondSegment1_segment6 = ( secondSegment1.segments[ 6 ] ) ? SEGMENT_ON_COLOR : SEGMENT_OFF_COLOR;\n" +
"             \n" +
"             \n" +
"             \n" +
"             \n" +
"             \n" +
"             \n" +
             uniformLayoutStr +
"             \n" +
"            // Minimum Y value is zero, so cube sits on the floor in room scale \n" +
             vertexStr +
"             \n" +
             faceUnitNormalStr2 +
"             \n" +
             faceColorStr2 +
"             \n" +
             faceIndexStr2 +
"             \n" +
"            out vec3 _color; \n" +
"            out vec3 _pixEye; \n" +
"            out vec3 _pixLight; \n" +
"            out vec3 _pixNormal; \n" +
"             \n" +
"            const vec3 lightPosn = vec3( 20.0 * cos( deltaTimeIndex ) , 20.0 * sin( deltaTimeIndex ) , 30.0 ); \n" +
"             \n" +
"            void main() { \n" +
"              _color = vec3(1.0, 0.0, 0.0); \n" +
"\n"
"              int vertexIndex = FACE_INDICES[gl_VertexID] ; \n" +
"\n"
"              int normalIndex = ( gl_VertexID ) / 3; \n" +
"               \n" +
"              _color = FACE_COLORS[normalIndex]; \n" +
"              if (any(lessThan(_color, vec3(0.0)))) { \n" +
"                  _color = vec3(1.0) + _color; \n" + 
"              } \n" +
"              vec3 wVertex = VERTEX_ARR[vertexIndex]; \n" + 
"              vec3 wNormal = FACE_UNIT_NORMALS[normalIndex]; \n" +  
"              vec3 wNormalPosn = wNormal + wVertex; \n" + 
"             \n" +
"              gl_Position = Projection * ModelView * vec4(VERTEX_ARR[vertexIndex] * Size, 1.0); \n" +
"              vec4 vertexPosition = ModelView * vec4(VERTEX_ARR[vertexIndex] * Size, 1.0); \n" +
"              _pixEye = - vertexPosition.xyz; \n" +
"              vec4 lightPosition = ModelView * vec4(lightPosn * Size, 1.0); \n" +
"              _pixLight = lightPosition.xyz - vertexPosition.xyz; \n" +
"              vec4 normalPosition = ModelView * vec4(wNormalPosn * Size, 1.0); \n" +
"              _pixNormal = normalPosition.xyz - vertexPosition.xyz; \n" +
"            } \n" +
            "\n" )
        
        
        with open( "shade1.txt" , "w" ) as outf :
            outf.write( compileShaderString1 )
        with open( "shade2.txt" , "w" ) as outf : 
            outf.write( compileShaderString2 )
            
        vertex_shader1 = compileShader(
            shader_string( compileShaderString1 ), 
            GL_VERTEX_SHADER)
        # vertex_shader2 = compileShader(
        #    shader_string( compileShaderString2 ), 
        #    GL_VERTEX_SHADER)
        fragment_shader = compileShader(
            shader_string("""
            in vec3 _color;
            in vec3 _pixEye;
            in vec3 _pixLight;
            in vec3 _pixNormal;
            out vec4 FragColor;
            
            void main() {
              float ambientIntensity = 0.2;
              float directionalIntensity = 0.7;
              float shininess = 30.0;
              vec3 specularColorInput = vec3( 17 / 255.0 , 17 / 255.0 , 17 / 255.0 );
              vec3 eyeVector = normalize( _pixEye );
              vec3 lightVector = normalize( _pixLight );
              vec3 normal = normalize( _pixNormal );
              vec3 ambientColor = ambientIntensity * _color;
              float lambertTerm = dot( normal , lightVector );
              if( lambertTerm < 0.0 )
              {
                  lambertTerm = 0.0;
              }
              vec3 diffuseColor = directionalIntensity * lambertTerm * _color;
              vec3 R = reflect( -lightVector , normal );
              float specularDot = dot( R , eyeVector );
              if( specularDot < 0.0 )
              {
                  specularDot = 0.0;
              }
              float specular = directionalIntensity * pow( specularDot , shininess );
              vec3 specularColor = specular * specularColorInput;
              FragColor = vec4( ambientColor + diffuseColor + specularColor , 1.0);
            }
            """), 
            GL_FRAGMENT_SHADER)
        try :
            print( "@@@@ Stats : " )
            print( "Indices : " + str( len( retm.indices ) ) )
            print( "Vertices : " + str( len( retm.vertices ) ) )
            print( "Uniforms : " + str( retm.numUniforms ) )
            print( "Faces : " + str( len( retm.indices ) / 3 ) )
            self.shader1 = compileProgram(vertex_shader1, fragment_shader, validate=False)
            # self.shader2 = compileProgram(vertex_shader2, fragment_shader, validate=False)
        except Exception as e :
            raise e
        #
        self.vao = glGenVertexArrays(1)
        glBindVertexArray(self.vao)
        print( "Max Uniform Locations : " + str( glGetIntegerv( GL_MAX_UNIFORM_LOCATIONS ) ) )
        glEnable(GL_DEPTH_TEST)
    
    
        
    def processTobjAudioPlay(self , scene : SceneGenerator.SceneGenerator , tobj : Target.Target ) :   
        
        if tobj.initialStart :
            tobj.initialStart = False;
            # Convert world coordinates to view coordinates
            modelview = self.modelview
            viewX = ( ( tobj.strtPos.x * modelview[0][0] ) +
                ( tobj.strtPos.y * modelview[1][0] ) +
                ( tobj.strtPos.z * modelview[2][0] ) +
                modelview[3][0] );
            viewY = ( ( tobj.strtPos.x * modelview[0][1] ) +
                ( tobj.strtPos.y * modelview[1][1] ) +
                ( tobj.strtPos.z * modelview[2][1] ) +
                modelview[3][1] );
            viewZ = ( ( tobj.strtPos.x * modelview[0][2] ) +
                ( tobj.strtPos.y * modelview[1][2] ) +
                ( tobj.strtPos.z * modelview[2][2] ) +
                modelview[3][2] );
            scene.soundServices.initiatePlay( viewX , viewY , viewZ ); 
        if tobj.collided and tobj.collisionEnable : 
            tobj.collisionEnable = False
            # Convert world coordinates to view coordinates
            modelview = self.modelview
            viewX = ( ( tobj.strtPos.x * modelview[0][0] ) +
                ( tobj.strtPos.y * modelview[1][0] ) +
                ( tobj.strtPos.z * modelview[2][0] ) +
                modelview[3][0] );
            viewY = ( ( tobj.strtPos.x * modelview[0][1] ) +
                ( tobj.strtPos.y * modelview[1][1] ) +
                ( tobj.strtPos.z * modelview[2][1] ) +
                modelview[3][1] );
            viewZ = ( ( tobj.strtPos.x * modelview[0][2] ) +
                ( tobj.strtPos.y * modelview[1][2] ) +
                ( tobj.strtPos.z * modelview[2][2] ) +
                modelview[3][2] );
            scene.soundServices.initiatePlay( viewX , viewY , viewZ ); 
    
        
    def display_gl(self, modelview, projection):
        
        NO_ID = -7777
        
        glClearColor( 0x77 / 255.0 , 0xb5 / 255.0 , 0xfe / 255.0 , 1.0 );
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
        
        ctime = time.time()
        self.ctime = ctime
        
        self.modelview = modelview
        self.scene.modelview = modelview
        
        # print( modelview )
        # print( modelview[0] )
        # x = 2.3 * modelview[3][0]
        # print( x ) # Yes
        
        updateLst = []
        
        td_pose = [None] * ( openvr.k_unMaxTrackedDeviceCount )
        
        td_pose = self.hmd.getDeviceToAbsoluteTrackingPose( openvr.TrackingUniverseStanding, 
            0.0, td_pose )
        
        HMD_LOCN = 0
        
        if HMD_LOCN != NO_ID :
            
            td = HMD_LOCN
            
            v = [ td_pose[td].mDeviceToAbsoluteTracking.m[0][3],
                           td_pose[td].mDeviceToAbsoluteTracking.m[1][3],
                           td_pose[td].mDeviceToAbsoluteTracking.m[2][3]];
                           
            # print( "Posn Hmd: " + str( v[0] ) + " , " + str( v[1] ) + " , " + str( v[2] ) )
            self.hmdLocn.set( v[0] , v[1] , v[2] )
            self.scene.hmdLocn = self.hmdLocn
            
        if self.ID_LeftHand_Green != NO_ID :
        
            td = self.ID_LeftHand_Green
            # Fill the position vector with the position of the device (last column of the matrix)
            v = [ td_pose[td].mDeviceToAbsoluteTracking.m[0][3],
                           td_pose[td].mDeviceToAbsoluteTracking.m[1][3],
                           td_pose[td].mDeviceToAbsoluteTracking.m[2][3]];

            # print( "Posn Left Hand: " + str( v[0] ) + " , " + str( v[1] ) + " , " + str( v[2] ) )
            self.scene.controller1.dynamicSetPosn( v[0] , v[1] , v[2] , updateLst )
            
        if self.ID_RightHand_Red != NO_ID :
        
            td = self.ID_RightHand_Red
            # Fill the position vector with the position of the device (last column of the matrix)
            v = [ td_pose[td].mDeviceToAbsoluteTracking.m[0][3],
                           td_pose[td].mDeviceToAbsoluteTracking.m[1][3],
                           td_pose[td].mDeviceToAbsoluteTracking.m[2][3]];

            # print( "Posn Right Hand: " + str( v[0] ) + " , " + str( v[1] ) + " , " + str( v[2] ) )
            self.scene.controller0.dynamicSetPosn( v[0] , v[1] , v[2] , updateLst )
        
        
        # ********************************************************************************************
            
        if self.ID_LeftFoot_Green != NO_ID :
        
            td = self.ID_LeftFoot_Green
            # Fill the position vector with the position of the device (last column of the matrix)
            v = [ td_pose[td].mDeviceToAbsoluteTracking.m[0][3],
                           td_pose[td].mDeviceToAbsoluteTracking.m[1][3],
                           td_pose[td].mDeviceToAbsoluteTracking.m[2][3]];

            # print( "Posn Left Foot: " + str( v[0] ) + " , " + str( v[1] ) + " , " + str( v[2] ) )
            self.scene.controller2.dynamicSetPosn( v[0] , v[1] , v[2] , updateLst )
            
        if self.ID_RightFoot_Red != NO_ID :
        
            td = self.ID_RightFoot_Red
            # Fill the position vector with the position of the device (last column of the matrix)
            v = [ td_pose[td].mDeviceToAbsoluteTracking.m[0][3],
                           td_pose[td].mDeviceToAbsoluteTracking.m[1][3],
                           td_pose[td].mDeviceToAbsoluteTracking.m[2][3]];

            # print( "Posn Right Foot: " + str( v[0] ) + " , " + str( v[1] ) + " , " + str( v[2] ) )
            self.scene.controller3.dynamicSetPosn( v[0] , v[1] , v[2] , updateLst )
        
        
        glUseProgram(self.shader1)
        glUniformMatrix4fv(0, 1, False, projection)
        glUniformMatrix4fv(4, 1, False, modelview)
        glBindVertexArray(self.vao)
        
        triSize1 = self.retained.getIndexSize1()
        
        igInitialized = self.gInitialized
        
        if not igInitialized :
        
            self.initialTime = ctime
            
            self.elapsedTime = 0.0
            
            now = 1000.0 * self.elapsedTime
            
            if True :
            
                INCHES_TO_CENTIMETERS = 2.54;
                CENTIMETERS_TO_METERS = 0.01;
                FEET_TO_INCHES = 12;
        
                heightFeet = int( self.scene.playerHeightFeetValue );
        
                heightInches = int( self.scene.playerHeightInchesValue );

                self.scene.defenseHeight = (heightFeet * FEET_TO_INCHES + heightInches) * INCHES_TO_CENTIMETERS * CENTIMETERS_TO_METERS;
            
            self.scene.dynamicPosnList = updateLst
            
            glUniform1f( self.scene.deltaTimeIndex , self.elapsedTime )
        
            for x in self.retained.vertices :
                if not ( x.getFixedPosn() ) :
                    uniformIndex = x.getUniformIndex()
                    glUniform3f(uniformIndex, x.x , x.y , x.z )
            
            self.gInitialized = True
        
        else :
        
            self.elapsedTime = ctime - self.initialTime
            
            now = 1000.0 * self.elapsedTime
            
            self.scene.dynamicPosnList = updateLst
            
            if now > self.scene.endTime :
                if self.scene.endTime < -3000 :
                    self.scene.endTime = now;
                    
                INCHES_TO_CENTIMETERS = 2.54;
                CENTIMETERS_TO_METERS = 0.01;

                deltaHeight = 6 * INCHES_TO_CENTIMETERS * CENTIMETERS_TO_METERS * random.random();
                
                self.scene.offenseHeight = self.scene.defenseHeight + (-deltaHeight if random.random() < 0.5 else deltaHeight);
            
            
                
                
            for tobj in self.scene.targetsKickA :
                uA = (now - tobj.strtTime) / (tobj.endTime - tobj.strtTime);
                if (uA >= 0.0) and (uA <= 1.0) :
                    tobj.mesh.rotation.x += tobj.rotationRate;
                    tobj.mesh.rotation.y += tobj.rotationRate;
                    tobj.mesh.rotation.z += tobj.rotationRate;

                    tobj.mesh.dynamicSetPosn(
                        (1 - uA) * (tobj.strtPos.x) + uA * (tobj.endPos.x),
                        (1 - uA) * (tobj.strtPos.y) + uA * (tobj.endPos.y),
                        (1 - uA) * (tobj.strtPos.z) + uA * (tobj.endPos.z),
                        updateLst
                        );
                    collided = self.scene.checkControllerCollision(self.scene.controller3, tobj);
                    if collided :
                        self.scene.rightKickHits = self.scene.rightKickHits + 1;
                    self.processTobjAudioPlay(self.scene, tobj);
                elif (uA > 1.0) and (tobj.timeEnabled) :
                    tobj.strtTime = self.scene.utimeStrt;
                    tobj.endTime = self.scene.utimeEnd;
                    tobj.timeEnabled = False;
                    tobj.strtPos.set(0, 1.5, self.scene.targetFarDist);
                    tobj.endPos.set(0, 1.5, self.scene.targetFarDist);
                    tobj.mesh.dynamicSetPosn(0, 0, self.scene.targetFarDist, updateLst);
                #elif ua
            #for cnt
                    
            for tobj in self.scene.targetsKickB :
                uA = (now - tobj.strtTime) / (tobj.endTime - tobj.strtTime);
                if (uA >= 0.0) and (uA <= 1.0) :
                    tobj.mesh.rotation.x += tobj.rotationRate;
                    tobj.mesh.rotation.y += tobj.rotationRate;
                    tobj.mesh.rotation.z += tobj.rotationRate;

                    tobj.mesh.dynamicSetPosn(
                        (1 - uA) * (tobj.strtPos.x) + uA * (tobj.endPos.x),
                        (1 - uA) * (tobj.strtPos.y) + uA * (tobj.endPos.y),
                        (1 - uA) * (tobj.strtPos.z) + uA * (tobj.endPos.z),
                        updateLst
                        );
                    collided = self.scene.checkControllerCollision(self.scene.controller2, tobj);
                    if collided :
                        self.scene.leftKickHits = self.scene.leftKickHits + 1;
                    self.processTobjAudioPlay(self.scene, tobj);
                elif (uA > 1.0) and (tobj.timeEnabled) :
                    tobj.strtTime = self.scene.utimeStrt;
                    tobj.endTime = self.scene.utimeEnd;
                    tobj.timeEnabled = False;
                    tobj.strtPos.set(0, 1.5, self.scene.targetFarDist);
                    tobj.endPos.set(0, 1.5, self.scene.targetFarDist);
                    tobj.mesh.dynamicSetPosn(0, 0, self.scene.targetFarDist, updateLst);
                #elif ua
            #for cnt

            for tobj in self.scene.dumbbelsA :
                uA = (now - tobj.strtTime) / (tobj.endTime - tobj.strtTime);
                if (uA >= 0.0) and (uA <= 1.0) :
                    tobj.mesh.rotation.x += tobj.rotationRate;
                    tobj.mesh.rotation.y += tobj.rotationRate;
                    tobj.mesh.rotation.z += tobj.rotationRate;

                    tobj.mesh.dynamicSetPosn(
                        (1 - uA) * (tobj.strtPos.x) + uA * (tobj.endPos.x),
                        (1 - uA) * (tobj.strtPos.y) + uA * (tobj.endPos.y),
                        (1 - uA) * (tobj.strtPos.z) + uA * (tobj.endPos.z),
                        updateLst
                        );
                    self.scene.checkDumbbellCollision(tobj);
                    self.processTobjAudioPlay(self.scene, tobj);
                elif (uA > 1.0) and (tobj.timeEnabled) :
                    tobj.strtTime = self.scene.utimeStrt;
                    tobj.endTime = self.scene.utimeEnd;
                    tobj.timeEnabled = False;
                    tobj.strtPos.set(0, 1.5, self.scene.targetFarDist);
                    tobj.endPos.set(0, 1.5, self.scene.targetFarDist);
                    tobj.mesh.dynamicSetPosn(0, 0, self.scene.targetFarDist, updateLst);
                #elif ua
            #for cnt
                    
            for tobj in self.scene.jumpHurdlesA :
                uA = (now - tobj.strtTime) / (tobj.endTime - tobj.strtTime);
                if (uA >= 0.0) and (uA <= 1.0) :
                    # Jump hurdles to not rotate

                    tobj.mesh.dynamicSetPosn(
                        (1 - uA) * (tobj.strtPos.x) + uA * (tobj.endPos.x),
                        (1 - uA) * (tobj.strtPos.y) + uA * (tobj.endPos.y),
                        (1 - uA) * (tobj.strtPos.z) + uA * (tobj.endPos.z),
                        updateLst
                        );
                    collided = self.scene.checkFootHurdleCollision(self.scene.controller3, tobj);
                    collided = collided or self.scene.checkFootHurdleCollision(self.scene.controller2, tobj);
                    if collided :
                        self.scene.jumpHurdleHits = self.scene.jumpHurdleHits + 1;
                    self.processTobjAudioPlay(self.scene, tobj);
                elif (uA > 1.0) and (tobj.timeEnabled) :
                    tobj.strtTime = self.scene.utimeStrt;
                    tobj.endTime = self.scene.utimeEnd;
                    tobj.timeEnabled = False;
                    tobj.strtPos.set(0, 1.5, self.scene.targetFarDist);
                    tobj.endPos.set(0, 1.5, self.scene.targetFarDist);
                    tobj.mesh.dynamicSetPosn(0, 0, self.scene.targetFarDist, updateLst);
                #elif ua
            #for cnt
                
            for tobj in self.scene.dodgeColumnsA :
                uA = (now - tobj.strtTime) / (tobj.endTime - tobj.strtTime);
                if (uA >= 0.0) and (uA <= 1.0) :
                    # Jump hurdles to not rotate

                    tobj.mesh.dynamicSetPosn(
                        (1 - uA) * (tobj.strtPos.x) + uA * (tobj.endPos.x),
                        (1 - uA) * (tobj.strtPos.y) + uA * (tobj.endPos.y),
                        (1 - uA) * (tobj.strtPos.z) + uA * (tobj.endPos.z),
                        updateLst
                        );
                    self.scene.checkDodgeColumnCollision(tobj);
                    self.processTobjAudioPlay(self.scene, tobj);
                elif (uA > 1.0) and (tobj.timeEnabled) :
                    tobj.strtTime = self.scene.utimeStrt;
                    tobj.endTime = self.scene.utimeEnd;
                    tobj.timeEnabled = False;
                    tobj.strtPos.set(0, 1.5, self.scene.targetFarDist);
                    tobj.endPos.set(0, 1.5, self.scene.targetFarDist);
                    tobj.mesh.dynamicSetPosn(0, 0, self.scene.targetFarDist, updateLst);
                #elif ua
            #for cnt
                
                        
            self.scene.now = now;
            
            
            
            glUniform1f( self.scene.deltaTimeIndex , self.elapsedTime )
            
            for x in updateLst :
                uniformIndex = x.getUniformIndex()
                glUniform3f( uniformIndex , x.x , x.y , x.z )
        
        glDrawArrays(GL_TRIANGLES, 0, triSize1)
        
        # glUseProgram(self.shader2)
        glUniformMatrix4fv(0, 1, False, projection)
        glUniformMatrix4fv(4, 1, False, modelview)
        glBindVertexArray(self.vao)
        # triSize2 = self.retained.getIndexSize2()
        
        if not igInitialized :
        
            glUniform1f( self.scene.deltaTimeIndex , self.elapsedTime )
        
            for x in self.retained.vertices :
                if not ( x.getFixedPosn() ) :
                    uniformIndex = x.getUniformIndex()
                    glUniform3f(uniformIndex, x.x , x.y , x.z )
        
        else :
            
            glUniform1f( self.scene.deltaTimeIndex , self.elapsedTime )
            
            for x in updateLst :
                uniformIndex = x.getUniformIndex()
                glUniform3f( uniformIndex , x.x , x.y , x.z )
        
        # glDrawArrays(GL_TRIANGLES, 0, triSize2)
    
    
    def dispose_gl(self):
        glDeleteProgram(self.shader1)
        # glDeleteProgram(self.shader2)
        self.shader = 0
        if self.vao:
            glDeleteVertexArrays(1, (self.vao,))
        self.vao = 0
