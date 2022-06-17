"""
 * @file DFRobotDFPlayerMini.h
 * @brief DFPlayer - An Arduino Mini MP3 Player From DFRobot
 * @n Header file for DFRobot's DFPlayer
 *
 * @copyright	[DFRobot]( http://www.dfrobot.com ), 2016
 * @copyright	GNU Lesser General Public License
 *
 * @author [Angelo](Angelo.qiao@dfrobot.com)
 * @version  V1.0.3
 * @date  2016-12-07
 */
"""

DFPLAYER_EQ_NORMAL = 0
DFPLAYER_EQ_POP = 1
DFPLAYER_EQ_ROCK = 2
DFPLAYER_EQ_JAZZ = 3
DFPLAYER_EQ_CLASSIC = 4
DFPLAYER_EQ_BASS = 5

DFPLAYER_DEVICE_U_DISK = 1
DFPLAYER_DEVICE_SD = 2
DFPLAYER_DEVICE_AUX = 3
DFPLAYER_DEVICE_SLEEP = 4
DFPLAYER_DEVICE_FLASH = 5

DFPLAYER_RECEIVED_LENGTH = 10
DFPLAYER_SEND_LENGTH = 10

# DEBUG

TimeOut = 0
WrongStack = 1
DFPlayerCardInserted = 2
DFPlayerCardRemoved = 3
DFPlayerCardOnline = 4
DFPlayerPlayFinished = 5
DFPlayerError = 6
DFPlayerUSBInserted = 7
DFPlayerUSBRemoved = 8
DFPlayerUSBOnline = 9
DFPlayerCardUSBOnline = 10
DFPlayerFeedBack = 11

Busy = 1
Sleeping = 2
SerialWrongStack = 3
CheckSumNotMatch = 4
FileIndexOut = 5
FileMismatch = 6
Advertise = 7


Stack_Header = 0
Stack_Version = 1
Stack_Length = 2
Stack_Command = 3
Stack_ACK = 4
Stack_Parameter = 5
Stack_CheckSum = 7
Stack_End = 9