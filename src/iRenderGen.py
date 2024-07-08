


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



from abc import ABCMeta, abstractmethod

import RetainedMode



"""
# Abstract base class defining a common interface for renderable objects
"""
class IRenderGen:
    __metaclass__ = ABCMeta

    """
    # Abstract method that generates the shape definition into the RetainedMode
    # prior to the retained mode being declared to the GL shaders 
    #
    """
    @abstractmethod
    def genPrev(self, gen : RetainedMode.RetainedMode ):
        raise NotImplementedError

    """
    # Abstract method that sets whether the position of the IRenderGen is fixed
    """
    @abstractmethod
    def setFixedPosn(self, fixed : bool ):
        raise NotImplementedError

    """
    # Abstract method that sets whether the position of the IRenderGen is fixed
    """
    @abstractmethod
    def getFixedPosn(self ):
        raise NotImplementedError

    """
    # Abstract method that performs a dynamic set of the position into the list
    """
    @abstractmethod
    def dynamicSetPosn(self, x : float , y : float , z : float , lst : list ):
        raise NotImplementedError

