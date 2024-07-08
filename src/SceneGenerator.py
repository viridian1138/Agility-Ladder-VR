


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



import math

import RetainedMode
import iRenderGen
import SingleColorBox
import SingleColorTetrahedron
import SevenSegmentFixed
import Target
import Vec3


FACE_LIMIT = RetainedMode.FACE_LIMIT



FACE_VECT = RetainedMode.FACE_VECT

FACE_VECT_STR = RetainedMode.FACE_VECT_STR



FACE_INDEX = RetainedMode.FACE_INDEX

FACE_INDEX_STR = RetainedMode.FACE_INDEX_STR




INDEX_MAX = RetainedMode.INDEX_MAX




class SceneGenerator(object):
    
    def __init__(self):
        
        self.deltaTimeIndex = 98
        
        self.hmdLocn = Vec3.Vec3()
        
        self.bucketL2Height = 3
        self.bucketL2YPos = self.bucketL2Height - 2
        
        self.dumbbellHeight = 5.75;
        self.pushKickTopHeight = 2.0;
        self.pushKickMiddleHeight = 1.25;
        self.pushKickBottomHeight = 0.5;
        self.legHeight = 2.5;
        self.uppercutHeight = 7.0;
        self.hookHeadHeight = 7.666;
        self.solarplexHeight = 6.0;
        self.abdomenHeight = 5.0;
        self.uppercutJumpHeight = 8.0;
        self.hammerStrikeHeight = 8.0;
        self.idealHumanHeadHeights = 8.0;
        self.dumbbellHits = 0;
        self.prevDumbbellHits = -1;
        self.jumpHurdleHits = 0;
        self.prevJumpHurdleHits = -1;
        self.rightPunchHits = 0;
        self.prevRightPunchHits = -1;
        self.leftPunchHits = 0;
        self.prevLeftPunchHits = -1;
        self.rightKickHits = 0;
        self.leftKickHits = 0;
        self.masterFontSizeMultiplier = 0.0125;
        self.fontSizeMultiplierScoring = 0.75;
        self.jumpHurdleHeight = 0.05;
        self.dodgeColumnHeight = self.bucketL2YPos
        self.updateDumbbellHits = True;
        self.updateLeftPunchHits = True;
        self.updateRightPunchHits = True;
        self.backDistBucket = -7;
        self.bucketXOffset = 3.8;

        self.difficultyValue = 47.0;

        if True :
            difficulty = self.difficultyValue;
            self.referenceTimeSplit = int( ( difficulty / 50.0 ) * 250 / 2.1);
            self.randomStrategyTimeSplit = int( ( difficulty / 50.0 ) * 500 / 2);
            split2 = self.referenceTimeSplit;
            self.flightTime = int(split2 * 5 * 1.6);
            self.flightTimeKick = int(split2 * 5 * 1.6 * 1.2);
            self.flightTimeStraightPunch = int(split2 * 5 * 1.6 * 0.8);
            self.flightTimeDumbbell = int(split2 * 5 * 1.6 * 0.8);
            self.jumpingKickDelay = 1.5 * split2;
    
        self.playerHeightFeetValue = 6.0;
        self.playerHeightInchesValue = 2.0;

        cubeSize = 4;
        self.cubeSizeGeom = Vec3.Vec3()
        self.cubeSizeGeom.set( cubeSize,
            cubeSize,
            cubeSize)
        
        self.bucketL2Width = 1.0
        self.bucketL2SizeGeom = Vec3.Vec3()
        self.bucketL2SizeGeom.set( self.bucketL2Width,
            self.bucketL2Height,
            self.bucketL2Width)
        
        INCHES_TO_CENTIMETERS = 2.54;
        CENTIMETERS_TO_METERS = 0.01;
        FEET_TO_INCHES = 12;
        
        markerXLength = 8.0 * FEET_TO_INCHES * INCHES_TO_CENTIMETERS * CENTIMETERS_TO_METERS
            
        markerXZOffset = 10 * INCHES_TO_CENTIMETERS * CENTIMETERS_TO_METERS
    
    
        markerHeight = 0.02;
        markerDepth = 0.04;
        
        self.markerXSizeGeom = Vec3.Vec3()
        self.markerXSizeGeom.set(
            markerXLength,
            markerHeight,
            markerDepth # 10.0
        );
        
        self.marker2SizeGeom = Vec3.Vec3()
        self.marker2SizeGeom.set(
            markerDepth,
            markerHeight,
            2.0 * markerXZOffset
        );
    
        # create the target geometry
        self.targetPunchSize = 0.16;
        self.targetPunchSizeGeom = Vec3.Vec3()
        self.targetPunchSizeGeom.set(
           self.targetPunchSize,
           self.targetPunchSize,
           self.targetPunchSize
         );

        # create the target geometry
        self.targetKickSize = 0.16;

        # create the dumbbell geometry
        self.dumbbellSize = 0.16;
        self.dumbbellSizeGeom = Vec3.Vec3()
        self.dumbbellSizeGeom.set(
            self.dumbbellSize,
            self.dumbbellSize,
            self.dumbbellSize
        );

        # create the jump hurdle geometry
        self.jumpHurdleSizeY = 0.16;
        self.jumpHurdleSizeXZ = 0.46;
        self.jumpHurdleSizeGeom = Vec3.Vec3()
        self.jumpHurdleSizeGeom.set(
            self.jumpHurdleSizeXZ,
            self.jumpHurdleSizeY,
            self.jumpHurdleSizeXZ
        );

        # create the dodge column geometry
        self.dodgeColumnWidth = 0.64;
        self.dodgeColumnSizeGeom = Vec3.Vec3()
        self.dodgeColumnSizeGeom.set(
            self.dodgeColumnWidth,
            self.bucketL2Height,
            self.dodgeColumnWidth
        );

        # Ground Plane

        

        self.cubeColor = Vec3.Vec3()
        self.cubeColor.set( 0xff / 255.0 , 0xc0 / 255.0 , 0xcb / 255.0 )

        self.bucketL2Color = Vec3.Vec3()
        self.bucketL2Color.set( 0xf1 / 255.0 , 0xed / 255.0 , 0xc2 / 255.0 )

        self.markerColor = Vec3.Vec3()
        self.markerColor.set( 0x55 / 255.0 , 0x00 / 255.0 , 0xbb / 255.0 )

        self.targetAColor = Vec3.Vec3()
        self.targetAColor.set( 0xe4 / 255.0 , 0x6a / 255.0 , 0x54 / 255.0 )

        self.targetBColor = Vec3.Vec3()
        self.targetBColor.set( 0xb4 / 255.0 , 0xec / 255.0 , 0xbb / 255.0 )

        self.dumbbellAColor = Vec3.Vec3()
        self.dumbbellAColor.set( 0x25 / 255.0 , 0x27 / 255.0 , 0x29 / 255.0 )

        self.jumpHurdleAColor = Vec3.Vec3()
        self.jumpHurdleAColor.set( 0xf1 / 255.0 , 0xed / 255.0 , 0xc2 / 255.0 )

        self.textColor = Vec3.Vec3()
        self.textColor.set( 0xff / 255.0 , 0xc0 / 255.0 , 0x00 / 255.0 )

        self.dodgeColumnColorA = self.bucketL2Color;
        
        

        self.endTime = -5000;
        self.nextSequence = None;



        # Ground Plane Geometry and Font



        self.bucketHypotenuse = math.sqrt(
            self.backDistBucket * self.backDistBucket +
            self.bucketXOffset * self.bucketXOffset
        );

        self.bucketCosine = - self.backDistBucket / self.bucketHypotenuse;

        self.bucketSine = self.bucketXOffset / self.bucketHypotenuse;

        self.bucketDistRatio = - self.bucketHypotenuse / self.backDistBucket;



        
        # MESHES
        
        
        self.cube = SingleColorBox.SingleColorBox()
        self.cube.posn.set(-(cubeSize + 1), cubeSize + 1, 0)
        self.cube.color = self.cubeColor
        self.cube.size = self.cubeSizeGeom
        
        self.bucketL2 = SingleColorBox.SingleColorBox()
        self.bucketL2.posn.set(0, self.bucketL2YPos, self.backDistBucket)
        self.bucketL2.setFixedPosn( True )
        self.bucketL2.color = self.bucketL2Color
        self.bucketL2.size = self.bucketL2SizeGeom
        
        self.marker2 = SingleColorBox.SingleColorBox()
        self.marker2.posn.set(-0, 0, 0)
        self.marker2.setFixedPosn( True )
        self.marker2.color = self.markerColor
        self.marker2.size = self.marker2SizeGeom
        
        self.markerX1 = SingleColorBox.SingleColorBox()
        self.markerX1.posn.set(-0, 0, -markerXZOffset)
        self.markerX1.setFixedPosn( True )
        self.markerX1.color = self.markerColor
        self.markerX1.size = self.markerXSizeGeom
        
        self.markerX2 = SingleColorBox.SingleColorBox()
        self.markerX2.posn.set(-0, 0, +markerXZOffset)
        self.markerX2.setFixedPosn( True )
        self.markerX2.color = self.markerColor
        self.markerX2.size = self.markerXSizeGeom

        self.maxTargets = 13; # 18; # 15 # 10 # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        self.maxKickTargets = 9;
        self.maxDumbbels = 6;
        self.maxJumpHurdles = 6;
        self.maxDodgeColumns = 2;
        self.utimeStrt = -5500.0;
        self.utimeEnd = -5000.0;
        self.targetFarDist = -10.0;
        
        
        
        
        segSize = 0.16;
        
        
        
        
        
        
        
        
        
        self.minuteSegment1 = SevenSegmentFixed.SevenSegmentFixed()
        minuteSegment1Posn = Vec3.Vec3()
        minuteSegment1Posn.set( self.bucketXOffset - ( 9 * 4 ) * segSize, 5 , self.backDistBucket )
        self.minuteSegment1.init( minuteSegment1Posn , "minuteSegment1_segment" )
        
        
        
        self.minuteSegment2 = SevenSegmentFixed.SevenSegmentFixed()
        minuteSegment2Posn = Vec3.Vec3()
        minuteSegment2Posn.set( self.bucketXOffset - ( 9 * 3 ) * segSize, 5 , self.backDistBucket )
        self.minuteSegment2.init( minuteSegment2Posn , "minuteSegment2_segment" )
        
        
        
        
        self.secondSegment1 = SevenSegmentFixed.SevenSegmentFixed()
        secondSegment1Posn = Vec3.Vec3()
        secondSegment1Posn.set( self.bucketXOffset - ( 9 * 1 ) * segSize, 5 , self.backDistBucket )
        self.secondSegment1.init( secondSegment1Posn , "secondSegment1_segment" )

        
        
        
        self.secondSegment2 = SevenSegmentFixed.SevenSegmentFixed()
        secondSegment2Posn = Vec3.Vec3()
        secondSegment2Posn.set( self.bucketXOffset - ( 9 * 0 ) * segSize, 5 , self.backDistBucket )
        self.secondSegment2.init( secondSegment2Posn , "secondSegment2_segment" )

        
        
        
        
        
        


        self.targetsKickA = [None] * self.maxKickTargets;
        for cnt in range( len( self.targetsKickA ) ) :
            self.targetsKickA[cnt] = Target.Target();
            tobj = self.targetsKickA[cnt];
            tobj.strtPos.set(0, 1.5, self.targetFarDist);
            tobj.endPos.set(0, 1.5, self.targetFarDist);
            tobj.mesh = SingleColorTetrahedron.SingleColorTetrahedron()
            tobj.mesh.posn.set(0, 0, self.targetFarDist)
            tobj.mesh.color = self.targetAColor
            tobj.mesh.size = self.targetKickSize
            tobj.rotationRate = 0.01;
            tobj.strtTime = self.utimeStrt;
            tobj.endTime = self.utimeEnd;
            tobj.timeEnabled = False;
            tobj.audioDefined = False;
            tobj.audioPlay = False;
            tobj.collided = False;
        # for

        self.targetsKickB = [None] * self.maxKickTargets;
        for cnt in range( len( self.targetsKickB ) ) :
            self.targetsKickB[cnt] = Target.Target();
            tobj = self.targetsKickB[cnt];
            tobj.strtPos.set(0, 1.5, self.targetFarDist);
            tobj.endPos.set(0, 1.5, self.targetFarDist);
            tobj.mesh = SingleColorTetrahedron.SingleColorTetrahedron()
            tobj.mesh.posn.set(0, 0, self.targetFarDist)
            tobj.mesh.color = self.targetBColor
            tobj.mesh.size = self.targetKickSize
            tobj.rotationRate = 0.01;
            tobj.strtTime = self.utimeStrt;
            tobj.endTime = self.utimeEnd;
            tobj.timeEnabled = False;
            tobj.audioDefined = False;
            tobj.audioPlay = False;
            tobj.collided = False;
        # for

        self.dumbbelsA = [None] * self.maxDumbbels;
        for cnt in range( len( self.dumbbelsA ) ) :
            self.dumbbelsA[cnt] = Target.Target();
            tobj = self.dumbbelsA[cnt];
            tobj.strtPos.set(0, 1.5, self.targetFarDist);
            tobj.endPos.set(0, 1.5, self.targetFarDist);
            tobj.mesh = SingleColorBox.SingleColorBox()
            tobj.mesh.posn.set(0, 0, self.targetFarDist)
            tobj.mesh.color = self.dumbbellAColor
            tobj.mesh.size = self.dumbbellSizeGeom
            tobj.rotationRate = 0.01;
            tobj.strtTime = self.utimeStrt;
            tobj.endTime = self.utimeEnd;
            tobj.timeEnabled = False;
            tobj.audioDefined = False;
            tobj.audioPlay = False;
            tobj.collided = False;
        # for

        self.jumpHurdlesA = [None] * self.maxJumpHurdles;
        for cnt in range( len( self.jumpHurdlesA ) ) :
            self.jumpHurdlesA[cnt] = Target.Target();
            tobj = self.jumpHurdlesA[cnt];
            tobj.strtPos.set(0, 1.5, self.targetFarDist);
            tobj.endPos.set(0, 1.5, self.targetFarDist);
            tobj.mesh = SingleColorBox.SingleColorBox()
            tobj.mesh.posn.set(0, 0, self.targetFarDist)
            tobj.mesh.color = self.jumpHurdleAColor
            tobj.mesh.size = self.jumpHurdleSizeGeom
            tobj.rotationRate = 0.01;
            tobj.strtTime = self.utimeStrt;
            tobj.endTime = self.utimeEnd;
            tobj.timeEnabled = False;
            tobj.audioDefined = False;
            tobj.audioPlay = False;
            tobj.collided = False;
        # for

        self.dodgeColumnsA = [None] * self.maxDodgeColumns;
        for cnt in range( len( self.dodgeColumnsA ) ) :
            self.dodgeColumnsA[cnt] = Target.Target();
            tobj = self.dodgeColumnsA[cnt];
            tobj.strtPos.set(0, 1.5, self.targetFarDist);
            tobj.endPos.set(0, 1.5, self.targetFarDist);
            tobj.mesh = SingleColorBox.SingleColorBox()
            tobj.mesh.posn.set(0, 0, self.targetFarDist)
            tobj.mesh.color = self.dodgeColumnColorA
            tobj.mesh.size = self.dodgeColumnSizeGeom
            tobj.rotationRate = 0.00;
            tobj.strtTime = self.utimeStrt;
            tobj.endTime = self.utimeEnd;
            tobj.timeEnabled = False;
            tobj.audioDefined = False;
            tobj.audioPlay = False;
            tobj.collided = False;
        # for
        
        
        ladderRungOffset = 18 * INCHES_TO_CENTIMETERS * CENTIMETERS_TO_METERS
        
        maxLadderRungsFromZero = 2
        self.ladderRungsA = [None] * 2 * maxLadderRungsFromZero
        for cnt in range( maxLadderRungsFromZero ) : 
            index0 = 2 * cnt
            index1 = index0 + 1
            offsetX = ( cnt + 1 ) * ladderRungOffset
        
            self.ladderRungsA[index0] = SingleColorBox.SingleColorBox()
            self.ladderRungsA[index0].posn.set(-offsetX, 0, 0)
            self.ladderRungsA[index0].setFixedPosn( True )
            self.ladderRungsA[index0].color = self.markerColor
            self.ladderRungsA[index0].size = self.marker2SizeGeom
        
            self.ladderRungsA[index1] = SingleColorBox.SingleColorBox()
            self.ladderRungsA[index1].posn.set(+offsetX, 0, 0)
            self.ladderRungsA[index1].setFixedPosn( True )
            self.ladderRungsA[index1].color = self.markerColor
            self.ladderRungsA[index1].size = self.marker2SizeGeom



        self.stTimeA = -5;

        self.stTimeB = -5;



        
        
        
        
        
        
        
        
        self.controllerBaseSize = 0.1
        
        self.controllerSize = Vec3.Vec3()
        self.controllerSize.set( self.controllerBaseSize , self.controllerBaseSize , self.controllerBaseSize )
        
        self.controller0Color = Vec3.Vec3()
        self.controller0Color.set( 1.0 , 0.0 , 0.0 )
        
        self.controller1Color = Vec3.Vec3()
        self.controller1Color.set( 0.0 , 1.0 , 0.0 )
        
        self.controller2Color = Vec3.Vec3()
        self.controller2Color.set( 1.0 , 0.0 , 0.0 )
        
        self.controller3Color = Vec3.Vec3()
        self.controller3Color.set( 0.0 , 1.0 , 0.0 )
        
        self.controller0 = SingleColorBox.SingleColorBox()
        self.controller0.posn.set(0.0, -5.0, 0.0)
        self.controller0.color = self.controller0Color
        self.controller0.size = self.controllerSize
        
        self.controller1 = SingleColorBox.SingleColorBox()
        self.controller1.posn.set(0.0, -5.0, 0.0)
        self.controller1.color = self.controller1Color
        self.controller1.size = self.controllerSize
        
        self.controller2 = SingleColorTetrahedron.SingleColorTetrahedron()
        self.controller2.posn.set(0.0, -5.0, 0.0)
        self.controller2.color = self.controller1Color
        self.controller2.size = self.controllerBaseSize
        
        self.controller3 = SingleColorTetrahedron.SingleColorTetrahedron()
        self.controller3.posn.set(0.0, -5.0, 0.0)
        self.controller3.color = self.controller0Color
        self.controller3.size = self.controllerBaseSize
        
        
        # Strategies moved to AgilityLadderActor
 
        
        # self.now
        self.curSecs = -5
        
        
        
    def generate(self):
        
        ret = RetainedMode.RetainedMode()
    
        
    
        self.cube.genPrev(ret)
    
        self.bucketL2.genPrev(ret)
    
        self.markerX1.genPrev(ret)
    
        self.markerX2.genPrev(ret)
    
        self.marker2.genPrev(ret)
        
        
        
        
        
        self.minuteSegment1.genPrev(ret)
        
        self.minuteSegment2.genPrev(ret)
        
        self.secondSegment1.genPrev(ret)
        
        self.secondSegment2.genPrev(ret)

        
        
        
        
        
        for cnt in range( len( self.ladderRungsA ) ) :
            self.ladderRungsA[cnt].genPrev(ret)
        # for
        
        
        
        
               
        

        for cnt in range( len( self.targetsKickA ) ) :
            self.targetsKickA[cnt].mesh.genPrev(ret)
        # for
        
        

        for cnt in range( len( self.targetsKickB ) ) :
            self.targetsKickB[cnt].mesh.genPrev(ret)
        # for
        
        

        for cnt in range( len( self.dumbbelsA ) ) :
            self.dumbbelsA[cnt].mesh.genPrev(ret)
        # for
        
        

        for cnt in range( len( self.jumpHurdlesA ) ) :
            self.jumpHurdlesA[cnt].mesh.genPrev(ret)
        # for

        for cnt in range( len( self.dodgeColumnsA ) ) :
            self.dodgeColumnsA[cnt].mesh.genPrev(ret)
        # for
                
        
    
        self.controller0.genPrev(ret)
    
        self.controller1.genPrev(ret)
    
        self.controller2.genPrev(ret)
    
        self.controller3.genPrev(ret)
    
        return ret



    # Checks whether a dumbbell has collided with a cylinder under the player view.
    # NOTE: The algorithm used for collision checking is fairly dumb.
    def checkDumbbellCollision(self, tobj : Target.Target ) :
        if not (tobj.collided) : 
            cameraPos = self.hmdLocn
            dumbbellPos = tobj.mesh.posn;
            # Dumbbell size plus viewer head size
            sizeConstraint = self.dumbbellSize * 0.5 + (0.15 * 0.5);

            collidedX = abs(dumbbellPos.x - cameraPos.x) <= sizeConstraint;

            collidedY = dumbbellPos.y <= (cameraPos.y + 0.03);

            collidedZ = abs(dumbbellPos.z - cameraPos.z) <= sizeConstraint;
            
            collided = collidedX and collidedY and collidedZ;
            if (collided) :
                self.dumbbellHits = self.dumbbellHits + 1;
                tobj.collided = True;
        # if not collided
    # checkDumbbellCollision



    # Checks whether a dodge column has collided with a cylinder through the player view.
    # NOTE: The algorithm used for collision checking is fairly dumb.
    def checkDodgeColumnCollision(self, tobj : Target.Target ) :
        if not (tobj.collided) : 
            cameraPos = self.hmdLocn
            dumbbellPos = tobj.mesh.posn;
            # Dumbbell size plus viewer head size
            sizeConstraint = self.dodgeColumnWidth * 0.5 + (0.15 * 0.5);

            collidedX = abs(dumbbellPos.x - cameraPos.x) <= sizeConstraint;
            
            collidedZ = abs(dumbbellPos.z - cameraPos.z) <= sizeConstraint;

            collided = collidedX and collidedZ;
            if (collided) :
                # Just call it a dumbbell hit for now
                self.dumbbellHits = self.dumbbellHits + 1;
                tobj.collided = True;
        # if not collided
    # checkDodgeColumnCollision



    # Checks whether a controller has punched the correct target.
    # NOTE: The algorithm used for collision checking is fairly dumb.
    def checkControllerCollision(self, controllerMesh : iRenderGen.IRenderGen , tobj : Target.Target ):
        collided = False;
        if not (tobj.collided) : 
            controllerPos = controllerMesh.posn
            targetPos = tobj.mesh.posn;

            sizeConstraint = (self.controllerBaseSize) * 0.5 + (self.targetPunchSize) * 0.5;

            collidedX = abs(targetPos.x - controllerPos.x) <= sizeConstraint;

            collidedY = abs(targetPos.y - controllerPos.y) <= sizeConstraint;

            collidedZ = abs(targetPos.z - controllerPos.z) <= sizeConstraint;

            collided = collidedX and collidedY and collidedZ;
            if (collided) :
                tobj.collided = True;
        # if not collided
        return collided;
    # checkControllerCollision



    # Checks whether a foot controller has collided with a hurdle.
    # NOTE: The algorithm used for collision checking is fairly dumb.
    def checkFootHurdleCollision(self, controllerMesh : iRenderGen.IRenderGen , tobj : Target.Target ):
        collided = False;
        if not (tobj.collided) : 
            controllerPos = controllerMesh.posn
            targetPos = tobj.mesh.posn;

            sizeConstraintXZ = (self.controllerBaseSize) * 0.5 + (self.jumpHurdleSizeXZ) * 0.5;

            sizeConstraintY = (self.controllerBaseSize) * 0.5 + (self.jumpHurdleSizeY) * 0.5;

            collidedX = abs(targetPos.x - controllerPos.x) <= sizeConstraintXZ;

            collidedY = abs(targetPos.y - controllerPos.y) <= sizeConstraintY;

            collidedZ = abs(targetPos.z - controllerPos.z) <= sizeConstraintXZ;

            collided = collidedX and collidedY and collidedZ;
            if (collided) :
                tobj.collided = True;
        # if not collided
        return collided;
    # checkControllerCollision




scene = SceneGenerator()


retm = scene.generate()


uniformLayoutStr = retm.uniformLayoutStr()


vertexStr = retm.vertexStr()


faceColorStr1 = retm.faceColorStr1()


faceColorStr2 = retm.faceColorStr2()


faceUnitNormalStr1 = retm.faceUnitNormalStr1()


faceUnitNormalStr2 = retm.faceUnitNormalStr2()


faceIndexStr1 = retm.faceIndexStr1()


faceIndexStr2 = retm.faceIndexStr2()


with open( "gen.txt" , "w" ) as outf :

    outf.write( str( retm ) )

    outf.write( uniformLayoutStr )

    outf.write( vertexStr )

    outf.write( faceColorStr1 )

    outf.write( faceColorStr2 )

    outf.write( faceUnitNormalStr1 )

    outf.write( faceUnitNormalStr2 )

    outf.write( faceIndexStr1 )

    outf.write( faceIndexStr2 )


allocationSize = 3 * len( retm.vertices ) + 2 * 3 * ( FACE_VECT ) + FACE_INDEX

print( "allocation size" )
print( allocationSize )



