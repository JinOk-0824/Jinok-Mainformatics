from system_class_define import Component
from ex_test import *
from function import *
from gate_generate import *
from make_BE import *

def main():
    
    print("\n==== 1. Initial Components ====\n")
    # Define components of the model
    components = kns_EX_3pump()
    

    # 1. Initial Components
    consol_file = "consol_file.txt"
    with open(consol_file, "w", encoding="utf-8") as f:
        f.write("\n==== 1. Initial Components ====\n")
        for comp_id, comp in components.items():
            # print(comp)
            # print("-" * 60)
            f.write(str(comp) + "\n")  # comp 객체를 문자열로 변환해서 쓰기
            f.write("-" * 60 + "\n")
            

    # 2. generate initial basic event gate
    print("\n==== 2. create_basic_event_gates ====\n")
    create_basic_event_gates(components)

    with open(consol_file, "a", encoding="utf-8") as f:
        f.write("\n==== 2. create_basic_event_gates ====\n")
        for comp_id, comp in components.items():
            # print(comp)
            # print("-" * 60)
            f.write(str(comp) + "\n")  # comp 객체를 문자열로 변환해서 쓰기
            f.write("-" * 60 + "\n")


    # 3. create_parallel_gate_and_update
    print("\n==== 3. create_parallel_gate_and_update ====\n")
    create_parallel_gate_and_update(components)

    with open(consol_file, "a", encoding="utf-8") as f:
        f.write("\n==== 3. create_parallel_gate_and_update ====\n")
        for comp_id, comp in components.items():
            # print(comp)
            # print("-" * 60)
            f.write(str(comp) + "\n")  # comp 객체를 문자열로 변환해서 쓰기
            f.write("-" * 60 + "\n")


    # 4. create_no_flow_gates
    print("\n==== 4. create_no_flow_gates ====\n")
    create_no_flow_gates(components)
    with open(consol_file, "a", encoding="utf-8") as f:
        f.write("\n==== 4. create_no_flow_gates ====\n")
        for comp_id, comp in components.items():
            # print(comp)
            # print("-" * 60)
            f.write(str(comp) + "\n")  # comp 객체를 문자열로 변환해서 쓰기
            f.write("-" * 60 + "\n")


    # 5. Parent 2개 정리
    print("\n==== 5. remove_from_b_type_parents ====\n")
    remove_from_b_type_parents(components)  
    with open(consol_file, "a", encoding="utf-8") as f:
        f.write("\n==== 5. remove_from_b_type_parents ====\n")
        for comp_id, comp in components.items():
            # print(comp)
            # print("-" * 60)
            f.write(str(comp) + "\n")  # comp 객체를 문자열로 변환해서 쓰기
            f.write("-" * 60 + "\n")      


    # 6. create BE
    print("\n==== 6. create_basic_event ====\n")
    create_basic_event(components)  
    with open(consol_file, "a", encoding="utf-8") as f:
        f.write("\n==== 6. create_basic_event ====\n")
        for comp_id, comp in components.items():
            # print(comp)
            # print("-" * 60)
            f.write(str(comp) + "\n")  # comp 객체를 문자열로 변환해서 쓰기
            f.write("-" * 60 + "\n")      


    # numbering
    print("\n==== assign_top_priority_numbers ====\n")
    assign_top_priority_numbers(components)

    with open(consol_file, "a", encoding="utf-8") as f:
        f.write("\n==== assign_top_priority_numbers ====\n")
        for comp_id, comp in components.items():
            # print(comp)
            # print("-" * 60)
            f.write(str(comp) + "\n")  # comp 객체를 문자열로 변환해서 쓰기
            f.write("-" * 60 + "\n")




    # ----------------------------------- 
    result = format_tree_all_nodes(components) # 가장 상위 component인 TOP에서 로직 연산
    lines = write_top_children_structure(components)
    # ----------------------------------- 


    
    # 로직 연산 테스트 한 것 확인하는 파일 생성
    logicfile = "./kft/logic check.txt"
    with open(logicfile, "w", encoding="utf-8") as f:
        f.write(result)
        f.write('\n')
        f.writelines(lines)
    print("TOP component info written to file.")
    # ----------------------------------- 



    # Aims 전용 KFT 파일 생성 
    # Define the .kft filename
    filename = "./kft/kns_EX.kft"
    # Generate initial .kft file
    make_init_kft(filename)

    # # Aims test 경로에 생성하는 것
    # filename = "../test/Base/kns_EX.kft"
    # # Generate initial .kft file
    # make_init_kft(filename)
    
    # Generate Components
    insert_components_after_xeventdata(filename, components)
    # 로직파일 kft 파일에 이식
    insert_logic_after_treelogic(filename, logicfile)
    # ----------------------------------- 
    

if __name__ == "__main__":
    main()
