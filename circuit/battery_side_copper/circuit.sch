EESchema Schematic File Version 4
EELAYER 30 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 1 1
Title ""
Date ""
Rev ""
Comp ""
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
$Comp
L power:VSS #PWR01
U 1 1 61E33281
P 4500 4050
F 0 "#PWR01" H 4500 3900 50  0001 C CNN
F 1 "VSS" H 4515 4223 50  0000 C CNN
F 2 "" H 4500 4050 50  0001 C CNN
F 3 "" H 4500 4050 50  0001 C CNN
	1    4500 4050
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR02
U 1 1 61E336BF
P 4500 4450
F 0 "#PWR02" H 4500 4200 50  0001 C CNN
F 1 "GND" H 4505 4277 50  0000 C CNN
F 2 "" H 4500 4450 50  0001 C CNN
F 3 "" H 4500 4450 50  0001 C CNN
	1    4500 4450
	1    0    0    -1  
$EndComp
Text GLabel 4500 4450 0    50   Input ~ 0
GND
Text GLabel 4500 4050 0    50   Input ~ 0
VSS
$Comp
L Mechanical:MountingHole_Pad H1
U 1 1 61E34F8C
P 5150 3800
F 0 "H1" H 5250 3849 50  0000 L CNN
F 1 "MountingHole_Pad" H 5250 3758 50  0000 L CNN
F 2 "MountingHole:MountingHole_3.2mm_M3_DIN965_Pad_TopBottom" H 5150 3800 50  0001 C CNN
F 3 "~" H 5150 3800 50  0001 C CNN
	1    5150 3800
	1    0    0    -1  
$EndComp
$Comp
L Mechanical:MountingHole_Pad H2
U 1 1 61E358B3
P 5150 4250
F 0 "H2" H 5250 4299 50  0000 L CNN
F 1 "MountingHole_Pad" H 5250 4208 50  0000 L CNN
F 2 "MountingHole:MountingHole_3.2mm_M3_DIN965_Pad_TopBottom" H 5150 4250 50  0001 C CNN
F 3 "~" H 5150 4250 50  0001 C CNN
	1    5150 4250
	1    0    0    -1  
$EndComp
Wire Wire Line
	5150 4450 4500 4450
Wire Wire Line
	4500 4050 5150 4050
Wire Wire Line
	5150 4050 5150 3900
Wire Wire Line
	5150 4450 5150 4350
$EndSCHEMATC
