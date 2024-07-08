


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

import pygame



class SoundServices(object):
    '''
    classdocs
    '''


    def init(self) :
        pygame.mixer.init()
        NUM_STRT_SOURCES = 15;
        self.counter = 0;
        self.strtSources = [ None ] * NUM_STRT_SOURCES
#        self.strtSources[ 0 ] = openal.oalOpen("AgilityLadderClip.wav")
#        self.strtSources[ 1 ] = openal.oalOpen("AgilityLadderClip2.wav")
        for cnt in range( len( self.strtSources ) ) :
            self.strtSources[ cnt ] = pygame.mixer.Sound("AgilityLadderClip.wav")
            
    def initiatePlay(self, x : float , y : float , z : float ):
        NUM_STRT_SOURCES = 15;
        self.counter = self.counter + 1
        count = self.counter % NUM_STRT_SOURCES
        source = self.strtSources[ count ]
        dist = math.sqrt( x * x + y * y + z * z )
        if dist < 0.000001 :
            dist = 0.000001
        sqrt2 = math.sqrt( 2 )
        xx = x / dist
        # yy = y / dist
        zz = z / dist
        left_volume = ( abs( zz ) - xx ) / sqrt2
        right_volume = ( abs( zz ) + xx ) / sqrt2
        channel = pygame.mixer.find_channel(False)
        channel.set_volume( left_volume , right_volume );
        channel.play(source)
        
        