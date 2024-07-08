#!/bin/env python



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



from openvr.gl_renderer import OpenVrGlRenderer
from openvr.color_cube_actor import ColorCubeActor
from openvr.glframework.wx_app import WxApp

import openvr

import AgilityLadderActor


"""
AgilityLadder (Full Body Track) VR
"""


if __name__ == "__main__":
	# Show an OpenGL window
	actor = AgilityLadderActor.AgilityLadderActor()
	
	renderer0 = OpenVrGlRenderer(actor, (800,600))
	
	with WxApp(renderer0, "AgilityLadder (Full Body Track) VR") as app:
		
		print( "VR System" )
		print( renderer0.vr_system )
		hmd = renderer0.vr_system
		
		actor.hmd = hmd
		
		for td in range( openvr.k_unTrackedDeviceIndex_Hmd , openvr.k_unMaxTrackedDeviceCount ) :
			
			NO_ID = -7777
			
			td_class = hmd.getTrackedDeviceClass( td )
			
			if td_class == openvr.TrackedDeviceClass_Controller :
				
				if actor.ID_RightHand_Red == NO_ID :
					
					actor.ID_RightHand_Red = td
					print( "Right Hand Recognized" )
				
				elif actor.ID_LeftHand_Green == NO_ID :
					
					actor.ID_LeftHand_Green = td
					print( "Left Hand Recognized" )
		
			if td_class == openvr.TrackedDeviceClass_GenericTracker :
				
				if actor.ID_LeftFoot_Green == NO_ID :
					
					actor.ID_LeftFoot_Green = td
					print( "Left Foot Recognized" )
				
				elif actor.ID_RightFoot_Red == NO_ID :
					
					actor.ID_RightFoot_Red = td
					print( "Right Foot Recognized" )
		
		app.run_loop()

