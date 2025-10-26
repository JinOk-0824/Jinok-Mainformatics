from system_class_define import Component  # class import

# KNS Example
def kns_EX():
    # 1) 컴포넌트 먼저 생성 (관계는 빈 리스트로 초기화)
    GAF_TOP = Component(
        id="GAF_TOP",
        name="GAF_TOP",
        parent=[],
        child=[],
        type="+",
        component="",
        status="TOP",
        failtype="",
        performance=0.0,
        description="KNS Example",
        lamda=0.0,
        factor=0.0,
        ccf=False,
        ccf_re=[],
        exception=False
    )

    PUMP1 = Component(
        id="PUMP1",
        name="PUMP1",
        parent=[],
        child=[],
        type="B",
        component="pump",
        status="run",
        failtype="",
        performance=0.0,
        description="PUMP1",
        lamda=0.0,
        factor=0.0,
        ccf=True,
        ccf_re=[],
        exception=False
    )

    PUMP2 = Component(
        id="PUMP2",
        name="PUMP2",
        parent=[],
        child=[],
        type="B",
        component="pump",
        status="run",
        failtype="",
        performance=0.0,
        description="PUMP2",
        lamda=0.0,
        factor=0.0,
        ccf=True,
        ccf_re=[],
        exception=False
    )

    VALVE = Component(
        id="VALVE",
        name="VALVE",
        parent=[],
        child=[],
        type="B",
        component="VALVE",
        status="open",
        failtype="",
        performance=0.0,
        description="VALVE",
        lamda=0.0,
        factor=0.0,
        ccf=False,
        ccf_re=[],
        exception=False
    )

    TANK = Component(
        id="TANK",
        name="TANK",
        parent=[],
        child=[],
        type="B",
        component="tank",
        status="",
        failtype="",
        performance=0.0,
        description="TANK",
        lamda=0.0,
        factor=0.0,
        ccf=False,
        ccf_re=[],
        exception=False
    )

    # 2) 부모-자식, CCF 관계 설정
    GAF_TOP.child = [PUMP1, PUMP2]
    PUMP1.parent = [GAF_TOP]
    PUMP2.parent = [GAF_TOP]

    PUMP1.child = [VALVE]
    PUMP2.child = [VALVE]
    VALVE.parent = [PUMP1, PUMP2]

    VALVE.child = [TANK]
    TANK.parent = [VALVE]

    PUMP1.ccf_re = [PUMP2]
    PUMP2.ccf_re = [PUMP1]


    # 3) 필요 시 dict로 반환
    return {
        "GAF_TOP": GAF_TOP,
        "TANK": TANK,
        "VALVE": VALVE,
        "PUMP1": PUMP1,
        "PUMP2": PUMP2
    }


def kns_EX_3pump():
    # 1) 컴포넌트 먼저 생성 (관계는 빈 리스트로 초기화)
    GAF_TOP = Component(
        id="GAF_TOP",
        name="GAF_TOP",
        parent=[],
        child=[],
        type="+",
        component="",
        status="TOP",
        failtype="",
        performance=0.0,
        description="KNS Example",
        lamda=0.0,
        factor=0.0,
        ccf=False,
        exception=False
    )

    PUMP1 = Component(
        id="PUMP1",
        name="PUMP1",
        parent=[],
        child=[],
        type="B",
        component="pump",
        status="run",
        failtype="",
        performance=50,
        description="PUMP1",
        lamda=0.0,
        factor=0.0,
        ccf=True,
        exception=False
    )

    PUMP2 = Component(
        id="PUMP2",
        name="PUMP2",
        parent=[],
        child=[],
        type="B",
        component="pump",
        status="run",
        failtype="",
        performance=50,
        description="PUMP2",
        lamda=0.0,
        factor=0.0,
        ccf=True,
        exception=False
    )

    PUMP3 = Component(
        id="PUMP3",
        name="PUMP3",
        parent=[],
        child=[],
        type="B",
        component="pump",
        status="run",
        failtype="",
        performance=50,
        description="PUMP3",
        lamda=0.0,
        factor=0.0,
        ccf=True,
        exception=False
    )


    VALVE = Component(
        id="VALVE",
        name="VALVE",
        parent=[],
        child=[],
        type="B",
        component="VALVE",
        status="open",
        failtype="",
        performance=0.0,
        description="VALVE",
        lamda=0.0,
        factor=0.0,
        ccf=False,
        exception=False
    )

    TANK = Component(
        id="TANK",
        name="TANK",
        parent=[],
        child=[],
        type="B",
        component="tank",
        status="",
        failtype="",
        performance=0.0,
        description="TANK",
        lamda=0.0,
        factor=0.0,
        ccf=False,
        exception=False
    )

    # 2) 부모-자식 관계 설정
    GAF_TOP.child = [PUMP1, PUMP2, PUMP3]
    PUMP1.parent = [GAF_TOP]
    PUMP2.parent = [GAF_TOP]
    PUMP3.parent = [GAF_TOP]

    PUMP1.child = [VALVE]
    PUMP2.child = [VALVE]
    PUMP3.child = [VALVE]
    VALVE.parent = [PUMP1, PUMP2, PUMP3]

    VALVE.child = [TANK]
    TANK.parent = [VALVE]

    PUMP1.ccf_re = [PUMP2,PUMP3]
    PUMP2.ccf_re = [PUMP1,PUMP3]
    PUMP3.ccf_re = [PUMP1,PUMP2]

    # 3) 필요 시 dict로 반환
    return {
        "GAF_TOP": GAF_TOP,
        "TANK": TANK,
        "VALVE": VALVE,
        "PUMP1": PUMP1,
        "PUMP2": PUMP2,
        "PUMP3": PUMP3
    }


# KNS Example
def kns_EX1():
    # 1) 컴포넌트 먼저 생성(관계는 비워둠)
    GAF_TOP = Component(
        id="GAF_TOP2", 
        name="GAF_TOP2",
        parent=[], 
        child=[],
        type="+", 
        component="", 
        status="TOP",
        failtype="", 
        performance=0.0,
        description="KNS Example",
        lamda=0.0, 
        factor=0.0, 
        ccf=False, 
        exception=False
    )

    TANK = Component(
        id="TANK", 
        name="TANK",
        parent=[], 
        child=[],
        type="B", 
        component="tank", 
        status="",
        failtype="", 
        performance=0.0,
        description="TANK",
        lamda=0.0, 
        factor=0.0, 
        ccf=False, 
        exception=False
    )

    VALVE = Component(
        id="VALVE", 
        name="VALVE",
        parent=[], 
        child=[],
        type="B", 
        component="VALVE", 
        status="open",
        failtype="", 
        performance=0.0,
        description="VALVE",
        lamda=0.0, 
        factor=0.0, 
        ccf=False, 
        exception=False
    )

    PUMP1 = Component(
        id="PUMP1", 
        name="PUMP1",
        parent=[], 
        child=[],
        type="B", 
        component="pump", 
        status="run",
        failtype="", 
        performance=0.0,
        description="PUMP1",
        lamda=0.0, 
        factor=0.0, 
        ccf=False, 
        exception=False
    )

    PUMP2 = Component(
        id="PUMP2", 
        name="PUMP2",
        parent=[], 
        child=[],
        type="B", 
        component="pump", 
        status="run",
        failtype="", 
        performance=0.0,
        description="PUMP2",
        lamda=0.0, 
        factor=0.0, 
        ccf=False, 
        exception=False
    )

    # 2) 관계 연결 (양방향)
    GAF_TOP.child = [TANK]
    TANK.parent = [GAF_TOP]

    TANK.child = [VALVE]
    VALVE.parent = [TANK]

    VALVE.child = [PUMP1, PUMP2]
    PUMP1.parent = [VALVE]
    PUMP2.parent = [VALVE]

    # 3) 필요 시 dict로 반환
    return {
        "GAF_TOP": GAF_TOP,
        "TANK": TANK,
        "VALVE": VALVE,
        "PUMP1": PUMP1,
        "PUMP2": PUMP2,
    }

# Hokkaido Aux feed water system
def hk_AFS():

    # Top event
    GAF_TOP = Component(
        id="GAF_TOP",
        name="GAF_TOP",
        parent=[],
        child=[],
        type="*",
        component="",
        status="TOP",
        failtype="",
        performance=0.0,
        description="Hokkaido Aux Feed Water System",
        lamda=0.0,
        factor=0.0,
        ccf=False,
        exception=False
    )

    # Steam generator A
    GAF_TRA_SG = Component(
        id="GAF_TRA_SG",
        name="GAF_TRA_SG",
        parent=[],
        child=[],
        type="+",
        component="SG",
        status="",
        failtype="",
        performance=0.0,
        description="Steam Generator train A",
        lamda=0.0,
        factor=0.0,
        ccf=False,
        exception=False
    )

    # ------------------------------
    # Steam generator A - components
    V501 = Component(
        id="V501",
        name="V501",
        parent=[],
        child=[],
        type="B",
        component="valve",
        status="open",
        failtype="",
        performance=0.0,
        description="valve 501",
        lamda=0.0,
        factor=0.0,
        ccf=False,
        exception=False
    )

    AV511 = Component(
        id="MCV511",
        name="MCV511",
        parent=[],
        child=[],
        type="B",
        component="MCV",
        status="open",
        failtype="",
        performance=0.0,
        description="Modulating valve 511",
        lamda=0.0,
        factor=0.0,
        ccf=False,
        exception=False
    )

    V521 = Component(
        id="V521",
        name="V521",
        parent=[],
        child=[],
        type="B",
        component="valve",
        status="open",
        failtype="",
        performance=0.0,
        description="valve 521",
        lamda=0.0,
        factor=0.0,
        ccf=False,
        exception=False
    )

    V531 = Component(
        id="V531",
        name="V531",
        parent=[],
        child=[],
        type="B",
        component="valve",
        status="open",
        failtype="",
        performance=0.0,
        description="valve 531 전기가 나가도 open 상태이기 때문에 분석에서 제외함.",
        lamda=0.0,
        factor=0.0,
        ccf=False,
        exception=True
    )

    V561 = Component(
        id="V561",
        name="V561",
        parent=[],
        child=[],
        type="B",
        component="valve",
        status="close",
        failtype="",
        performance=0.0,
        description="valve 561 maintenance용 유로이기 때문에 분석에서 제외함.",
        lamda=0.0,
        factor=0.0,
        ccf=False,
        exception=True
    )

    V571 = Component(
        id="V571",
        name="V571",
        parent=[],
        child=[],
        type="B",
        component="valve",
        status="open",
        failtype="",
        performance=0.0,
        description="valve 571 maintenance용 유로이기 때문에 분석에서 제외함.",
        lamda=0.0,
        factor=0.0,
        ccf=False,
        exception=True
    )      

    PP01A = Component(
        id="PP01A",
        name="PP01A",
        parent=[],
        child=[],
        type="B",
        component="pump",
        status="stop",
        failtype="",
        performance=0.0,
        description="Pump PP01A",
        lamda=0.0,
        factor=0.0,
        ccf=False,
        exception=False
    )

    V541 = Component(
        id="V541",
        name="V541",
        parent=[],
        child=[],
        type="B",
        component="valve",
        status="open",
        failtype="",
        performance=0.0,
        description="valve 541",
        lamda=0.0,
        factor=0.0,
        ccf=False,
        exception=False
    )

    V551 = Component(
        id="V551",
        name="V551",
        parent=[],
        child=[],
        type="B",
        component="valve",
        status="close",
        failtype="",
        performance=0.0,
        description="valve 551",
        lamda=0.0,
        factor=0.0,
        ccf=False,
        exception=True
    )

    AFWST_A = Component(
        id="AFWST_A",
        name="AFWST_A",
        parent=[],
        child=[],
        type="B",
        component="tank",
        status="",
        failtype="",
        performance=0.0,
        description="AFWST_A",
        lamda=0.0,
        factor=0.0,
        ccf=False,
        exception=False
    )

    # ------------------------------
    # Steam generator B - components
    GAF_TRB_SG = Component(
        id="GAF_TRB_SG",
        name="GAF_TRB_SG",
        parent=[],
        child=[],
        type="+",
        component="SG",
        status="",
        failtype="B",
        performance=0.0,
        description="Steam Generator train B",
        lamda=0.0,
        factor=0.0,
        ccf=False,
        exception=False
    )

    V502 = Component(
        id="V502",
        name="V502",
        parent=[],
        child=[],
        type="B",
        component="valve",
        status="open",
        failtype="",
        performance=0.0,
        description="valve 502",
        lamda=0.0,
        factor=0.0,
        ccf=False,
        exception=False
    )

    V512 = Component(
        id="MCV_512",
        name="MCV_512",
        parent=[],
        child=[],
        type="B",
        component="MCV",
        status="open",
        failtype="",
        performance=0.0,
        description="MCV 512",
        lamda=0.0,
        factor=0.0,
        ccf=False,
        exception=False
    )

    V522 = Component(
        id="V522",
        name="V522",
        parent=[],
        child=[],
        type="B",
        component="valve",
        status="open",
        failtype="",
        performance=0.0,
        description="valve 522",
        lamda=0.0,
        factor=0.0,
        ccf=False,
        exception=False
    )

    V532 = Component(
        id="V532",
        name="V532",
        parent=[],
        child=[],
        type="B",
        component="valve",
        status="open",
        failtype="",
        performance=0.0,
        description="전기가 나가도 open 상태라 제외",
        lamda=0.0,
        factor=0.0,
        ccf=False,
        exception=True
    )

    PP02B = Component(
        id="PP02B",
        name="PP02B",
        parent=[],
        child=[],
        type="B",
        component="pump",
        status="stop",
        failtype="",
        performance=0.0,
        description="Pump PP02B",
        lamda=0.0,
        factor=0.0,
        ccf=False,
        exception=False
    )
    
    V562 = Component(
        id="V562",
        name="V562",
        parent=[],
        child=[],
        type="B",
        component="valve",
        status="close",
        failtype="",
        performance=0.0,
        description="Valve V562",
        lamda=0.0,
        factor=0.0,
        ccf=False,
        exception=False
    )

    V572 = Component(
        id="V572",
        name="V572",
        parent=[],
        child=[],
        type="B",
        component="valve",
        status="open",
        failtype="",
        performance=0.0,
        description="Valve V572",
        lamda=0.0,
        factor=0.0,
        ccf=False,
        exception=False
    )

    V542 = Component(
        id="V542",
        name="V542",
        parent=[],
        child=[],
        type="B",
        component="valve",
        status="open",
        failtype="",
        performance=0.0,
        description="Valve V542",
        lamda=0.0,
        factor=0.0,
        ccf=False,
        exception=False
    )
    
    V552 = Component(
        id="V552",
        name="V552",
        parent=[],
        child=[],
        type="B",
        component="valve",
        status="open",
        failtype="",
        performance=0.0,
        description="Valve V552",
        lamda=0.0,
        factor=0.0,
        ccf=False,
        exception=False
    )

    AFWST_B = Component(
        id="AFWST_B",
        name="AFWST_B",
        parent=[],
        child=[],
        type="B",
        component="tank",
        status="",
        failtype="",
        performance=0.0,
        description="AFWST_B",
        lamda=0.0,
        factor=0.0,
        ccf=False,
        exception=False
    )

    # Set relation
    GAF_TOP.child = [GAF_TRA_SG, GAF_TRB_SG]
    GAF_TRA_SG.parent = [GAF_TOP]
    GAF_TRB_SG.parent = [GAF_TOP]

    # Train A
    GAF_TRA_SG.child = [V501]
    V501.parent = [GAF_TRA_SG]
    V501.child = [AV511]
    AV511.parent = [V501]
    AV511.child = [V521]
    V521.parent = [AV511]
    V521.child = [V531]
    V531.parent = [V521]
    V531.child = [PP01A, V561]

    PP01A.parent = [V531]
    PP01A.child = [V541]
    V541.parent = [PP01A]
    V541.child = [V551]
    V551.parent = [V541]
    V551.child = [AFWST_A]

    V561.parent = [V531]
    V561.child = [V571]
    V571.parent = [V561]
    V571.child = [AFWST_A]

    AFWST_A.parent = [V571, V551]


    # Train B    
    GAF_TRB_SG.child = [V502]
    V502.parent = [GAF_TRB_SG]
    V502.child = [V512]
    V512.parent = [V502]
    V512.child = [V522]
    V522.parent = [V512]
    V522.child = [V532]
    V532.parent = [V522]
    V532.child = [PP02B, V562]

    PP02B.parent = [V532]
    PP02B.child = [V542]
    V542.parent = [PP02B]
    V542.child = [V552]
    V552.parent = [V542]
    V552.child = [AFWST_B]

    V562.parent = [V532]
    V562.child = [V572]
    V572.parent = [V562]
    V572.child = [AFWST_B]

    AFWST_B.parent = [V572, V552]


    # dictionary type -> return
    return {
        "GAF_TOP": GAF_TOP,
        "GAF_TRA_SG": GAF_TRA_SG,
        "GAF_TRB_SG": GAF_TRB_SG,
        "V501": V501,
        "AV511": AV511,
        "V521": V521,
        "V531": V531,
        "V541": V541,
        "V551": V551,
        "V561": V561,
        "V571": V571,
        "PP01A": PP01A,
        "AFWST_A": AFWST_Ａ,

        "V502": V502,
        "V512": V512,
        "V522": V522,
        "V532": V532,
        "PP02B": PP02B,
        "V562": V562,
        "V572": V572,
        "V542": V542,
        "V552": V552,
        "AFWST_B": AFWST_B
    }



def hk_SI():
    # 1) 먼저 노드들을 parent/child 비운 상태로 생성
    GAF_SI  = Component(
        id="GAF_SI",  
        name="GAF_SI",
        parent=[],
        child=[],  
        type="*", 
        component="", 
        status="TOP",
        failtype="", 
        performance=0.0, 
        description="Hokkaido Safety Injection System",
        lamda=0.0, 
        factor=0.0, 
        ccf=False, 
        exception=False
    )

    # LEG A
    GAF_LEGA = Component(
        id="GAF_LEGA", 
        name="GAF_LEGA", 
        parent=[],
        child=[],
        type="+", 
        component="", 
        status="",
        failtype="", 
        performance=0.0, 
        description="RCS COLD LEG A",
        lamda=0.0, 
        factor=0.0, 
        ccf=False, 
        exception=False
    )

    V101 = Component(
        id="V101", 
        name="V101",
        parent=[],
        child=[], 
        type="B", 
        component="valve", 
        status="open",
        failtype="", 
        performance=0.0, 
        description="Valve 101",
        lamda=0.0, 
        factor=0.0, 
        ccf=False, 
        exception=False
    )

    V111 = Component(
        id="V111", 
        name="V111",
        parent=[],
        child=[], 
        type="B", 
        component="valve", 
        status="close",
        failtype="", 
        performance=0.0, 
        description="Valve 111",
        lamda=0.0, 
        factor=0.0, 
        ccf=False, 
        exception=False
     )

    V121 = Component(
        id="V121", 
        name="V121",
        parent=[],
        child=[], 
        type="B", 
        component="valve", 
        status="open",
        failtype="", 
        performance=0.0, 
        description="Valve 121",
        lamda=0.0, 
        factor=0.0, 
        ccf=False, 
        exception=False
    )

    PP01A = Component(
        id="PP01A", 
        name="PP01A",
        parent=[],
        child=[], 
        type="B", 
        component="pump", 
        status="",
        failtype="", 
        performance=0.0, 
        description="Pump PP01A",
        lamda=0.0, 
        factor=0.0, 
        ccf=False, 
        exception=False
    )

    V131 = Component(
        id="V131", 
        name="V131",
        parent=[],
        child=[], 
        type="B", 
        component="valve", 
        status="open",
        failtype="", 
        performance=0.0, 
        description="Valve 131",
        lamda=0.0, 
        factor=0.0, 
        ccf=False, 
        exception=False
    )

    V141 = Component(
        id="V141", 
        name="V141",
        parent=[],
        child=[], 
        type="B", 
        component="valve", 
        status="open",
        failtype="", 
        performance=0.0, 
        description="Valve 141",
        lamda=0.0, 
        factor=0.0, 
        ccf=False, 
        exception=False
    )

    V151 = Component(
        id="V151", 
        name="V151",
        parent=[],
        child=[], 
        type="B", 
        component="valve", 
        status="open",
        failtype="", 
        performance=0.0, 
        description="valve 151",
        lamda=0.0, 
        factor=0.0, 
        ccf=False, 
        exception=False
    )

    V161 = Component(
        id="V161", 
        name="V161",
        parent=[],
        child=[], 
        type="B", 
        component="valve", 
        status="open",
        failtype="", 
        performance=0.0, 
        description="valve 161",
        lamda=0.0, 
        factor=0.0, 
        ccf=False, 
        exception=False
    )

    EMSP = Component(
        id="EMSP", 
        name="EMSP",
        parent=[],
        child=[], 
        type="B", 
        component="tank", 
        status="",
        failtype="", 
        performance=0.0, 
        description="tank",
        lamda=0.0, 
        factor=0.0, 
        ccf=False, 
        exception=False
    )


    # LEG B
    GAF_LEGB = Component(
        id="GAF_LEGB", 
        name="GAF_LEGB", 
        parent=[], 
        child=[],
        type="+", 
        component="", 
        status="", 
        failtype="", 
        performance=0.0,
        description="RCS COLD LEG B", 
        lamda=0.0, 
        factor=0.0,
        ccf=False, 
        exception=False
    )

    V102 = Component(
        id="V102", 
        name="V102", 
        parent=[], 
        child=[],
        type="B", 
        component="valve", 
        status="open", 
        failtype="", 
        performance=0.0,
        description="Valve 102", 
        lamda=0.0, 
        factor=0.0,
        ccf=False, 
        exception=False
    )

    V112 = Component(
        id="V112", 
        name="V112", 
        parent=[], 
        child=[],
        type="B", 
        component="valve", 
        status="close", 
        failtype="", 
        performance=0.0,
        description="Valve 112", 
        lamda=0.0, 
        factor=0.0,
        ccf=False, 
        exception=False
    )

    V122 = Component(
        id="V122", 
        name="V122", 
        parent=[], 
        child=[],
        type="B", 
        component="valve", 
        status="open", 
        failtype="", 
        performance=0.0,
        description="Valve 122", 
        lamda=0.0, 
        factor=0.0,
        ccf=False, 
        exception=False
    )

    PP02B = Component(
        id="PP02B", 
        name="PP02B", 
        parent=[], 
        child=[],
        type="B", 
        component="pump", 
        status="", 
        failtype="", 
        performance=0.0,
        description="Pump PP02B", 
        lamda=0.0, 
        factor=0.0,
        ccf=False, 
        exception=False
    )

    V132 = Component(
        id="V132", 
        name="V132", 
        parent=[], 
        child=[],
        type="B", 
        component="valve", 
        status="open", 
        failtype="", 
        performance=0.0,
        description="Valve 132", 
        lamda=0.0, 
        factor=0.0,
        ccf=False, 
        exception=False
    )

    V142 = Component(
        id="V142", 
        name="V142", 
        parent=[], 
        child=[],
        type="B", 
        component="valve", 
        status="open", 
        failtype="", 
        performance=0.0,
        description="Valve 142", 
        lamda=0.0, 
        factor=0.0,
        ccf=False, 
        exception=False)
     

    # 2) 관계 설정 (양방향으로 맞춰줌)
    # train A
    GAF_SI.child = [GAF_LEGA, GAF_LEGB]
    GAF_LEGA.parent = [GAF_SI]

    GAF_LEGA.child = [V101]
    V101.parent = [GAF_LEGA]

    V101.child = [V111]
    V111.parent = [V101]

    V111.child = [V121]
    V121.parent = [V111]

    V121.child = [PP01A]
    PP01A.parent = [V121]

    PP01A.child = [V131]
    V131.parent = [PP01A]

    V131.child = [V141]
    V141.parent = [V131]

    V151.parent = [PP01A]
    PP01A.child = (PP01A.child + [V151]) if V151 not in PP01A.child else PP01A.child # child가 두 명이라 처리
    
    V151.child = [V161]
    V161.parent = [V151]
    
    V161.child = [EMSP]
    EMSP.parent = [V161]

    # train B
    GAF_SI.child = [GAF_LEGB]
    GAF_LEGB.parent = [GAF_SI]
    GAF_LEGB.child = [V102]
    V102.parent = [GAF_LEGB]
    V102.child = [V112]
    V112.parent = [V102]
    V112.child = [V122]
    V122.parent = [V112]
    V122.child = [PP02B]
    PP02B.parent = [V122]
    PP02B.child = [V132]
    V132.parent = [PP02B]
    V132.child = [V142]
    V142.parent = [V132]

    # 3) 사전으로 반환 (필요한 것만 골라 담아도 됨)
    return {
        "GAF_SI": GAF_SI,
        "GAF_LEGA": GAF_LEGA,
        "V101": V101,
        "V111": V111,
        "V121": V121,
        "PP01A": PP01A,
        "V131": V131,
        "V141": V141,
        "V151": V151,
        "V161": V161,
        "EMSP": EMSP,
        "GAF_LEGB": GAF_LEGB,
        "V102": V102,
        "V112": V112,
        "V122": V122,
        "PP02B": PP02B,
        "V132": V132,
        "V142": V142
    }



    