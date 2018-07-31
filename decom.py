import ait.core.tlm
import csv
import os.path

# Pull the AIT data dictionary
tlmdict = ait.core.tlm.getDefaultDict()
science_pkt = tlmdict['DRE_SCI_DATA']
engineering_pkt = tlmdict['DRE_ENG_DATA']

# Create data path
directory = '/Users/wilczews/Documents/APID0x2FF_0x300_2018_06_26_11.59.00/'

# Read in data from 5 pairs of files
for f in range(5):

    # Initialize array for storing EDR
    edr = []

    # Create the file path
    file_sci = ['APID0x300_2018_06_26_11.58.01.dat', 'APID0x300_2018_06_26_11.58.02.dat', 'APID0x300_2018_06_26_11.58.03.dat', 'APID0x300_2018_06_26_11.58.04.dat', 'APID0x300_2018_06_26_11.58.06.dat']
    file_eng = ['APID0x2FF_2018_06_26_11.58.01.dat', 'APID0x2FF_2018_06_26_11.58.02.dat', 'APID0x2FF_2018_06_26_11.58.03.dat', 'APID0x2FF_2018_06_26_11.58.04.dat', 'APID0x2FF_2018_06_26_11.58.05.dat']

    path_sci = os.path.join(directory, file_sci[f])
    path_eng = os.path.join(directory, file_eng[f])

    # Open file and write data to it
    with open(path_sci, 'r') as source_sci, open(path_eng, 'r') as source_eng:
        for i in range(32):

            # Use AIT routines to read in data from 32 science packets
            data_sci = source_sci.read(270)
            pkt = ait.core.tlm.Packet(science_pkt, data=data_sci)
            time_stamp = pkt.DRE_Time_Stamp
            exposure_number = pkt.DRE_Exposure_Number
            sci_field_1 = pkt.DRE_Science_Data_Field_1
            sci_field_2 = pkt.DRE_Science_Data_Field_2
            sci_field_3 = pkt.DRE_Science_Data_Field_3
            sci_field_4 = pkt.DRE_Science_Data_Field_4
            sci_field_5 = pkt.DRE_Science_Data_Field_5
            sci_field_6 = pkt.DRE_Science_Data_Field_6
            sci_field_7 = pkt.DRE_Science_Data_Field_7
            sci_field_8 = pkt.DRE_Science_Data_Field_8
            sci_field_9 = pkt.DRE_Science_Data_Field_9
            sci_field_10 = pkt.DRE_Science_Data_Field_10
            sci_field_11 = pkt.DRE_Science_Data_Field_11
            sci_field_12 = pkt.DRE_Science_Data_Field_12
            sci_field_13 = pkt.DRE_Science_Data_Field_13
            sci_field_14 = pkt.DRE_Science_Data_Field_14
            sci_field_15 = pkt.DRE_Science_Data_Field_15
            sci_field_16 = pkt.DRE_Science_Data_Field_16
            temp = [time_stamp, exposure_number, sci_field_1, sci_field_2, sci_field_3, sci_field_4, sci_field_5,
                    sci_field_6, sci_field_7, sci_field_8, sci_field_9, sci_field_10, sci_field_11, sci_field_12,
                    sci_field_13, sci_field_14, sci_field_15, sci_field_16]
            edr = edr + temp
            
        # Use AIT routines to read in data from the Engineering Packet
        data_eng = source_eng.read()
        pkt_eng = ait.core.tlm.Packet(engineering_pkt, data=data_eng)

        # Left out Reserved bits
        Time_Stamp = pkt_eng.Eng_Time_Stamp
        FPGA_VER = pkt_eng.FPGA_VER
        CMD_Acc_Cntr = pkt_eng.CMD_Acc_Cntr
        CMD_Rcv_Cntr = pkt_eng.CMD_Rcv_Cntr
        LAST_Acc_Seq_Cnt = pkt_eng.LAST_Acc_Seq_Cnt
        CMD_Err_Cnt1_CRC = pkt_eng.CMD_Err_Cnt1_CRC
        CMD_Err_Cnt1_SEQ = pkt_eng.CMD_Err_Cnt1_SEQ
        CMD_Err_Cnt1_REJ = pkt_eng.CMD_Err_Cnt1_REJ
        CMD_Err_Cnt2_EOP = pkt_eng.CMD_Err_Cnt2_EOP
        CMD_Err_Cnt2_SPI = pkt_eng.CMD_Err_Cnt2_SPI
        CMD_Err_Cnt2_APID = pkt_eng.CMD_Err_Cnt2_APID
        CMD_Err_Cnt2 = pkt_eng.CMD_Err_Cnt2
        LAST_Rej_Seq_Cnt = pkt_eng.LAST_Rej_Seq_Cnt
        TIME_1PPS_Msw = pkt_eng.TIME_1PPS_Msw
        TIME_1PPS_Lsw = pkt_eng.TIME_1PPS_Lsw
        SC_TIME_1PPS_Msw = pkt_eng.SC_TIME_1PPS_Msw
        SC_TIME_1PPS_Lsw = pkt_eng.SC_TIME_1PPS_Lsw
        SRAM_Bit_Status_TEST = pkt_eng.SRAM_Bit_Status_TEST
        SRAM_Bit_Status_BUSY = pkt_eng.SRAM_Bit_Status_BUSY
        SRAM_Bit_Status_ERROR = pkt_eng.SRAM_Bit_Status_ERROR
        SRAM_Bit_Status_TEST_ADD = pkt_eng.SRAM_Bit_Status_TEST_ADD
        SRAM_Bit_Address = pkt_eng.SRAM_Bit_Address
        SRAM_Config_BLOCK = pkt_eng.SRAM_Config_BLOCK
        SRAM_Config_BANK = pkt_eng.SRAM_Config_BANK
        H1RG_Config_CPLIN = pkt_eng.H1RG_Config_CPLIN
        H1RG_Config_LATENCY = pkt_eng.H1RG_Config_LATENCY
        H1RG_Config_AVG = pkt_eng.H1RG_Config_AVG
        H1RG_Config_MODE = pkt_eng.H1RG_Config_MODE
        H1RG_Config_CMD = pkt_eng.H1RG_Config_CMD
        EXP_Num = pkt_eng.EXP_Num
        OBS_Num = pkt_eng.OBS_Num
        INT_Time = pkt_eng.INT_Time
        RST_INT_Time = pkt_eng.RST_INT_Time
        EXP_Pause_Time = pkt_eng.EXP_Pause_Time
        VCLK_Skip1_Start = pkt_eng.VCLK_Skip1_Start
        VCLK_Skip1_Stop = pkt_eng.VCLK_Skip1_Stop
        VCLK_Skip2_Start = pkt_eng.VCLK_Skip2_Start
        VCLK_Skip2_Stop = pkt_eng.VCLK_Skip2_Stop
        VCLK_Skip3_Start = pkt_eng.VCLK_Skip3_Start
        VCLK_Skip3_Stop = pkt_eng.VCLK_Skip3_Stop
        VCLK_Skip4_Start = pkt_eng.VCLK_Skip4_Start
        VCLK_Skip4_Stop = pkt_eng.VCLK_Skip4_Stop
        VCLK_Skip5_Start = pkt_eng.VCLK_Skip5_Start
        VCLK_Skip5_Stop = pkt_eng.VCLK_Skip5_Stop
        VCLK_Skip6_Start = pkt_eng.VCLK_Skip6_Start
        VCLK_Skip6_Stop = pkt_eng.VCLK_Skip6_Stop
        VCLK_Skip7_Start = pkt_eng.VCLK_Skip7_Start
        VCLK_Skip7_Stop = pkt_eng.VCLK_Skip7_Stop
        VCLK_Skip8_Start = pkt_eng.VCLK_Skip8_Start
        VCLK_Skip8_Stop = pkt_eng.VCLK_Skip8_Stop
        Pixel_Sat_Cnt = pkt_eng.Pixel_Sat_Cnt
        DET_DSUB = pkt_eng.DET_DSUB
        DET_Vreset = pkt_eng.DET_Vreset
        DET_VbiasGate = pkt_eng.DET_VbiasGate
        DET_Drain = pkt_eng.DET_Drain
        DET_VbiasPower = pkt_eng.DET_VbiasPower
        DET_Temp = pkt_eng.DET_Temp
        OBox_Temp = pkt_eng.OBox_Temp
        DRE_Temp = pkt_eng.DRE_Temp
        DAC_Tlm_Chan0 = pkt_eng.DAC_Tlm_Chan0
        DAC_Tlm_Chan1 = pkt_eng.DAC_Tlm_Chan1
        DAC_Tlm_Chan2 = pkt_eng.DAC_Tlm_Chan2
        DAC_Tlm_Chan3 = pkt_eng.DAC_Tlm_Chan3
        AFS_Cur_Pos = pkt_eng.AFS_Cur_Pos
        AFS_Cmd_Pos = pkt_eng.AFS_Cmd_Pos
        AFS_Status_CLOSE = pkt_eng.AFS_Status_CLOSE
        AFS_Status_OPEN = pkt_eng.AFS_Status_OPEN
        AFS_Status_DOOR_BUSY = pkt_eng.AFS_Status_DOOR_BUSY
        AFS_Status_PPS = pkt_eng.AFS_Status_PPS
        AFS_Status_LOST = pkt_eng.AFS_Status_LOST
        AFS_Status_CMD_TO = pkt_eng.AFS_Status_CMD_TO
        AFS_Status_CMD_ERR = pkt_eng.AFS_Status_CMD_ERR
        AFS_Status_STEPPER = pkt_eng.AFS_Status_STEPPER
        AFS_Status_CLK_FRQ = pkt_eng.AFS_Status_CLK_FRQ
        AFS_Status_BUSY = pkt_eng.AFS_Status_BUSY
        AFS_Status_STEPPER_HOME = pkt_eng.AFS_Status_STEPPER_HOME
        CRYO_Cmd_Addr_TO = pkt_eng.CRYO_Cmd_Addr_TO
        CRYO_Cmd_Addr_CS = pkt_eng.CRYO_Cmd_Addr_CS
        CRYO_Cmd_Addr_WRITE = pkt_eng.CRYO_Cmd_Addr_WRITE
        CRYO_Cmd_Data = pkt_eng.CRYO_Cmd_Data
        CRYO_Tlm0 = pkt_eng.CRYO_Tlm0
        CRYO_Tlm1 = pkt_eng.CRYO_Tlm1
        CRYO_Tlm2 = pkt_eng.CRYO_Tlm2
        CRYO_Tlm3 = pkt_eng.CRYO_Tlm3
        CRYO_Tlm4 = pkt_eng.CRYO_Tlm4
        CRYO_Tlm5 = pkt_eng.CRYO_Tlm5
        CRYO_Tlm6 = pkt_eng.CRYO_Tlm6
        CRYO_Tlm7 = pkt_eng.CRYO_Tlm7
        CRYO_Tlm8 = pkt_eng.CRYO_Tlm8
        CRYO_Tlm9 = pkt_eng.CRYO_Tlm9
        CRYO_Tlm10 = pkt_eng.CRYO_Tlm10
        CRYO_Tlm11 = pkt_eng.CRYO_Tlm11
        CRYO_Tlm12 = pkt_eng.CRYO_Tlm12
        CRYO_Tlm13 = pkt_eng.CRYO_Tlm13
        CRYO_Tlm14 = pkt_eng.CRYO_Tlm14
        CRYO_Tlm15 = pkt_eng.CRYO_Tlm15
        CRYO_Tlm16 = pkt_eng.CRYO_Tlm16
        CRYO_Tlm17 = pkt_eng.CRYO_Tlm17
        CRYO_Tlm18 = pkt_eng.CRYO_Tlm18
        CRYO_Tlm19 = pkt_eng.CRYO_Tlm19
        CRYO_Tlm20 = pkt_eng.CRYO_Tlm20
        CRYO_Tlm21 = pkt_eng.CRYO_Tlm21
        CRYO_Tlm22 = pkt_eng.CRYO_Tlm22
        DET_ADC_Tlm01_Reg1 = pkt_eng.DET_ADC_Tlm01_Reg1
        DET_ADC_Tlm01_Reg0 = pkt_eng.DET_ADC_Tlm01_Reg0
        DET_ADC_Tlm23_Reg3 = pkt_eng.DET_ADC_Tlm23_Reg3
        DET_ADC_Tlm23_Reg2 = pkt_eng.DET_ADC_Tlm23_Reg2
        DET_ADC_Tlm45_Reg5 = pkt_eng.DET_ADC_Tlm45_Reg5
        DET_ADC_Tlm45_Reg4 = pkt_eng.DET_ADC_Tlm45_Reg4
        DET_ADC_Tlm67_Reg7 = pkt_eng.DET_ADC_Tlm67_Reg7
        DET_ADC_Tlm67_Reg6 = pkt_eng.DET_ADC_Tlm67_Reg6
        DET_ADC_Tlm89_Reg9 = pkt_eng.DET_ADC_Tlm89_Reg9
        DET_ADC_Tlm89_Reg8 = pkt_eng.DET_ADC_Tlm89_Reg8
        DET_ADC_Tlm1011_Reg11 = pkt_eng.DET_ADC_Tlm1011_Reg11
        DET_ADC_Tlm1011_Reg10 = pkt_eng.DET_ADC_Tlm1011_Reg10
        DET_ADC_Tlm1213_Reg13 = pkt_eng.DET_ADC_Tlm1213_Reg13
        DET_ADC_Tlm1213_Reg12 = pkt_eng.DET_ADC_Tlm1213_Reg12
        DET_ADC_Tlm1415_Reg15 = pkt_eng.DET_ADC_Tlm1415_Reg15
        DET_ADC_Tlm1415_Reg14 = pkt_eng.DET_ADC_Tlm1415_Reg14
        DET_ADC_Tlm1617_Reg17 = pkt_eng.DET_ADC_Tlm1617_Reg17
        DET_ADC_Tlm1617_Reg16 = pkt_eng.DET_ADC_Tlm1617_Reg16
        DET_ADC_Tlm1819_Reg19 = pkt_eng.DET_ADC_Tlm1819_Reg19
        DET_ADC_Tlm1819_Reg18 = pkt_eng.DET_ADC_Tlm1819_Reg18
        DET_ADC_Tlm2021_Reg21 = pkt_eng.DET_ADC_Tlm2021_Reg21
        DET_ADC_Tlm2021_Reg20 = pkt_eng.DET_ADC_Tlm2021_Reg20
        DET_ADC_Tlm2223_Reg23 = pkt_eng.DET_ADC_Tlm2223_Reg23
        DET_ADC_Tlm2223_Reg22 = pkt_eng.DET_ADC_Tlm2223_Reg22
        DET_ADC_Tlm2425_Reg25 = pkt_eng.DET_ADC_Tlm2425_Reg25
        DET_ADC_Tlm2425_Reg24 = pkt_eng.DET_ADC_Tlm2425_Reg24
        DET_ADC_Tlm2627_Reg27 = pkt_eng.DET_ADC_Tlm2627_Reg27
        DET_ADC_Tlm2627_Reg26 = pkt_eng.DET_ADC_Tlm2627_Reg26
        DET_ADC_Tlm2829_Reg29 = pkt_eng.DET_ADC_Tlm2829_Reg29
        DET_ADC_Tlm2829_Reg28 = pkt_eng.DET_ADC_Tlm2829_Reg28
        DET_ADC_Tlm3031_Reg31 = pkt_eng.DET_ADC_Tlm3031_Reg31
        DET_ADC_Tlm3031_Reg30 = pkt_eng.DET_ADC_Tlm3031_Reg30
        DET_ADC_Tlm3233_Reg33 = pkt_eng.DET_ADC_Tlm3233_Reg33
        DET_ADC_Tlm3233_Reg32 = pkt_eng.DET_ADC_Tlm3233_Reg32
        DET_ADC_Tlm3435_Reg35 = pkt_eng.DET_ADC_Tlm3435_Reg35
        DET_ADC_Tlm3435_Reg34 = pkt_eng.DET_ADC_Tlm3435_Reg34
        DET_ADC_Tlm3637_Reg37 = pkt_eng.DET_ADC_Tlm3637_Reg37
        DET_ADC_Tlm3637_Reg36 = pkt_eng.DET_ADC_Tlm3637_Reg36
        DET_ADC_Tlm3839_Reg39 = pkt_eng.DET_ADC_Tlm3839_Reg39
        DET_ADC_Tlm3839_Reg38 = pkt_eng.DET_ADC_Tlm3839_Reg38
        DET_ADC_Tlm4041_Reg41 = pkt_eng.DET_ADC_Tlm4041_Reg41
        DET_ADC_Tlm4041_Reg40 = pkt_eng.DET_ADC_Tlm4041_Reg40
        DET_ADC_Tlm4243_Reg43 = pkt_eng.DET_ADC_Tlm4243_Reg43
        DET_ADC_Tlm4243_Reg42 = pkt_eng.DET_ADC_Tlm4243_Reg42
        DET_ADC_Tlm4445_Reg45 = pkt_eng.DET_ADC_Tlm4445_Reg45
        DET_ADC_Tlm4445_Reg44 = pkt_eng.DET_ADC_Tlm4445_Reg44
        DET_ADC_Tlm4647_Reg47 = pkt_eng.DET_ADC_Tlm4647_Reg47
        DET_ADC_Tlm4647_Reg46 = pkt_eng.DET_ADC_Tlm4647_Reg46
        DET_ADC_Tlm4849_Reg49 = pkt_eng.DET_ADC_Tlm4849_Reg49
        DET_ADC_Tlm4849_Reg48 = pkt_eng.DET_ADC_Tlm4849_Reg48
        DET_ADC_Tlm5051_Reg51 = pkt_eng.DET_ADC_Tlm5051_Reg51
        DET_ADC_Tlm5051_Reg50 = pkt_eng.DET_ADC_Tlm5051_Reg50
        DET_ADC_Tlm5253_Reg53 = pkt_eng.DET_ADC_Tlm5253_Reg53
        DET_ADC_Tlm5253_Reg52 = pkt_eng.DET_ADC_Tlm5253_Reg52
        DET_ADC_Tlm5455_Reg55 = pkt_eng.DET_ADC_Tlm5455_Reg55
        DET_ADC_Tlm5455_Reg54 = pkt_eng.DET_ADC_Tlm5455_Reg54
        DET_ADC_Tlm5657_Reg57 = pkt_eng.DET_ADC_Tlm5657_Reg57
        DET_ADC_Tlm5657_Reg56 = pkt_eng.DET_ADC_Tlm5657_Reg56
        DET_ADC_Tlm5859_Reg59 = pkt_eng.DET_ADC_Tlm5859_Reg59
        DET_ADC_Tlm5859_Reg58 = pkt_eng.DET_ADC_Tlm5859_Reg58
        DET_ADC_Tlm6061_Reg61 = pkt_eng.DET_ADC_Tlm6061_Reg61
        DET_ADC_Tlm6061_Reg60 = pkt_eng.DET_ADC_Tlm6061_Reg60
        DET_ADC_Tlm6263_Reg63 = pkt_eng.DET_ADC_Tlm6263_Reg63
        DET_ADC_Tlm6263_Reg62 = pkt_eng.DET_ADC_Tlm6263_Reg62
        AFS_WAVE = pkt_eng.AFS_WAVE
        AFS_RUN_COUNT = pkt_eng.AFS_RUN_COUNT
        AFS_PHASE_DELAY = pkt_eng.AFS_PHASE_DELAY
        DOOR_WAVE = pkt_eng.DOOR_WAVE
        Frame_1_Pixel = pkt_eng.Frame_1_Pixel
        Frame_2_Pixel = pkt_eng.Frame_2_Pixel
        FLATS_SAT_MODE = pkt_eng.FLATS_SAT_MODE
        temp_eng = [Time_Stamp, FPGA_VER, CMD_Acc_Cntr, CMD_Rcv_Cntr, LAST_Acc_Seq_Cnt, CMD_Err_Cnt1_CRC, CMD_Err_Cnt1_SEQ,
                    CMD_Err_Cnt1_REJ, CMD_Err_Cnt2_EOP, CMD_Err_Cnt2_SPI, CMD_Err_Cnt2_APID, CMD_Err_Cnt2,
                    LAST_Rej_Seq_Cnt, TIME_1PPS_Msw, TIME_1PPS_Lsw, SC_TIME_1PPS_Msw,
                    SC_TIME_1PPS_Lsw, SRAM_Bit_Status_TEST, SRAM_Bit_Status_BUSY,
                    SRAM_Bit_Status_ERROR, SRAM_Bit_Status_TEST_ADD, SRAM_Bit_Address, SRAM_Config_BLOCK, SRAM_Config_BANK,
                    H1RG_Config_CPLIN, H1RG_Config_LATENCY, H1RG_Config_AVG, H1RG_Config_MODE, H1RG_Config_CMD, EXP_Num,
                    OBS_Num, INT_Time, RST_INT_Time, EXP_Pause_Time, VCLK_Skip1_Start, VCLK_Skip1_Stop, VCLK_Skip2_Start,
                    VCLK_Skip2_Stop, VCLK_Skip3_Start, VCLK_Skip3_Stop, VCLK_Skip4_Start, VCLK_Skip4_Stop, VCLK_Skip5_Start,
                    VCLK_Skip5_Stop, VCLK_Skip6_Start, VCLK_Skip6_Stop, VCLK_Skip7_Start, VCLK_Skip7_Stop, VCLK_Skip8_Start,
                    VCLK_Skip8_Stop, Pixel_Sat_Cnt, DET_DSUB, DET_Vreset, DET_VbiasGate, DET_Drain, DET_VbiasPower,
                    DET_Temp, OBox_Temp, DRE_Temp, DAC_Tlm_Chan0, DAC_Tlm_Chan1, DAC_Tlm_Chan2, DAC_Tlm_Chan3, AFS_Cur_Pos,
                    AFS_Cmd_Pos, AFS_Status_CLOSE, AFS_Status_OPEN, AFS_Status_DOOR_BUSY, AFS_Status_PPS, AFS_Status_LOST,
                    AFS_Status_CMD_TO, AFS_Status_CMD_ERR, AFS_Status_STEPPER, AFS_Status_CLK_FRQ, AFS_Status_BUSY,
                    AFS_Status_STEPPER_HOME, CRYO_Cmd_Addr_TO, CRYO_Cmd_Addr_CS, CRYO_Cmd_Addr_WRITE, CRYO_Cmd_Data,
                    CRYO_Tlm0, CRYO_Tlm1, CRYO_Tlm2, CRYO_Tlm3, CRYO_Tlm4, CRYO_Tlm5, CRYO_Tlm6, CRYO_Tlm7, CRYO_Tlm8,
                    CRYO_Tlm9, CRYO_Tlm10, CRYO_Tlm11, CRYO_Tlm12, CRYO_Tlm13, CRYO_Tlm14, CRYO_Tlm15, CRYO_Tlm16,
                    CRYO_Tlm17, CRYO_Tlm18, CRYO_Tlm19, CRYO_Tlm20, CRYO_Tlm21, CRYO_Tlm22, DET_ADC_Tlm01_Reg1,
                    DET_ADC_Tlm01_Reg0, DET_ADC_Tlm23_Reg3, DET_ADC_Tlm23_Reg2, DET_ADC_Tlm45_Reg5, DET_ADC_Tlm45_Reg4,
                    DET_ADC_Tlm67_Reg7, DET_ADC_Tlm67_Reg6, DET_ADC_Tlm89_Reg9, DET_ADC_Tlm89_Reg8, DET_ADC_Tlm1011_Reg11,
                    DET_ADC_Tlm1011_Reg10, DET_ADC_Tlm1213_Reg13, DET_ADC_Tlm1213_Reg12, DET_ADC_Tlm1415_Reg15,
                    DET_ADC_Tlm1415_Reg14, DET_ADC_Tlm1617_Reg17, DET_ADC_Tlm1617_Reg16, DET_ADC_Tlm1819_Reg19,
                    DET_ADC_Tlm1819_Reg18, DET_ADC_Tlm2021_Reg21, DET_ADC_Tlm2021_Reg20, DET_ADC_Tlm2223_Reg23,
                    DET_ADC_Tlm2223_Reg22, DET_ADC_Tlm2425_Reg25, DET_ADC_Tlm2425_Reg24, DET_ADC_Tlm2627_Reg27,
                    DET_ADC_Tlm2627_Reg26, DET_ADC_Tlm2829_Reg29, DET_ADC_Tlm2829_Reg28, DET_ADC_Tlm3031_Reg31,
                    DET_ADC_Tlm3031_Reg30, DET_ADC_Tlm3233_Reg33, DET_ADC_Tlm3233_Reg32, DET_ADC_Tlm3435_Reg35,
                    DET_ADC_Tlm3435_Reg34, DET_ADC_Tlm3637_Reg37, DET_ADC_Tlm3637_Reg36, DET_ADC_Tlm3839_Reg39,
                    DET_ADC_Tlm3839_Reg38, DET_ADC_Tlm4041_Reg41, DET_ADC_Tlm4041_Reg40, DET_ADC_Tlm4243_Reg43,
                    DET_ADC_Tlm4243_Reg42, DET_ADC_Tlm4445_Reg45, DET_ADC_Tlm4445_Reg44, DET_ADC_Tlm4647_Reg47,
                    DET_ADC_Tlm4647_Reg46, DET_ADC_Tlm4849_Reg49, DET_ADC_Tlm4849_Reg48, DET_ADC_Tlm5051_Reg51,
                    DET_ADC_Tlm5051_Reg50, DET_ADC_Tlm5253_Reg53, DET_ADC_Tlm5253_Reg52, DET_ADC_Tlm5455_Reg55,
                    DET_ADC_Tlm5455_Reg54, DET_ADC_Tlm5657_Reg57, DET_ADC_Tlm5657_Reg56, DET_ADC_Tlm5859_Reg59,
                    DET_ADC_Tlm5859_Reg58, DET_ADC_Tlm6061_Reg61, DET_ADC_Tlm6061_Reg60, DET_ADC_Tlm6263_Reg63,
                    DET_ADC_Tlm6263_Reg62, AFS_WAVE, AFS_RUN_COUNT, AFS_PHASE_DELAY, DOOR_WAVE, Frame_1_Pixel,
                    Frame_2_Pixel, FLATS_SAT_MODE]

        edr = edr + temp_eng

# Write EDR to a CSV file

target_file = input("where should this data be stored? ")
    
    with open(target_file, 'ab') as target:
        w = csv.writer(target, delimiter=',')
        w.writerow(edr)

print('done!')

 Verification Snippet
# This code does simple verifaction of Lunar Ice-Cube data

##############   READ IN DATA   ############## 
# Don't currently know how to read data or where it comes from

dataSet = open(filename, 'r')

############## CHECK FOR ZEROES ############## 
# Read each byte in the dataset, check for zeros
# Since we don't know where data comes from, the read in is probably wrong
while dataSet.read()
	if dataSet == 0:
		zero_counter = zero_counter + 1

# At this time, the threshhold number of zeros has not been identified
# 10 is a dummy
if zero_counter > 10:
	print('Too many zeroes')

############## CHECK ROUGH SLOPE ############## 
# Group 1 (skip) is 1024*4 bytes
# Groups 2-4 (average each individually) are 1024*8 (8192) bytes each
# Then compare the averaged values. A good result is 2 > 3 > 4

# Read in 8192 bytes in for each group
group2_data = read()
group3_data = read()
group4_data = read()

# Add them together and then divide by 8192 
avg_group2 = (sum(group2_data)/8192)
avg_group3 = (sum(group3_data)/8192)
avg_group4 = (sum(group4_data)/8192)

if avg_group2 > avg_group3:
	# Group 2 should be greater than group 3
	if avg_group3 > avg_group4:
		# Group 3 should be greater than group 4
		print ('Data passes slope check')
	else 
		print ('Data fails slope check')
else 
	print ('Data fails slope check')

print ('Average of group 2 = %r') %avg_group2
print ('Average of group 3 = %r') %avg_group3
print ('Average of group 4 = %r') %avg_group4
