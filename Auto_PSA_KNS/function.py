from system_class_define import *  # class import
from ex_test import *
from gate_generate import *
from typing import Dict, List, Union, Optional
from make_BE import *
from typing import Dict, List, Iterable, Optional, Union


# Library import
import textwrap



# component no에 넘버링 (TOP 먼저)
def assign_top_priority_numbers(components: dict):
    """
    Assigns 'no' values starting from:
    1. TOP component (status == 'TOP') gets no = 1
    2. Its children get no = 2, 3, ...
    3. All remaining non-exception components get sequential no values
    """
    # Reset all no values first
    for comp in components.values():
        comp.no = None

    # 1. Find the TOP component
    top_comp = next((c for c in components.values() if c.status == 'TOP' and not c.exception), None)
    if not top_comp:
        print("No TOP component found.")
        return

    current_no = 1
    top_comp.no = current_no
    current_no += 1

    # 2. Assign numbers to TOP's children (if not exception)
    for child in top_comp.child:
        if not child.exception:
            child.no = current_no
            current_no += 1

    # 3. Assign numbers to remaining components
    for comp in sorted(components.values(), key=lambda c: c.id):
        if comp.no is None and not comp.exception:
            comp.no = current_no
            current_no += 1


### Logic 연산

# --- 안전 해석 헬퍼들 ---
def _resolve_node(node: Union['Component', str, None],
                  components: Dict[str, 'Component']) -> Optional['Component']:
    if node is None:
        return None
    if isinstance(node, str):
        return components.get(node)
    return node

def _resolve_children(comp: 'Component',
                      components: Dict[str, 'Component']) -> List['Component']:
    out: List['Component'] = []
    for ch in getattr(comp, "child", []):
        obj = _resolve_node(ch, components)
        if obj is not None:
            out.append(obj)
    return out

def _no_or_id(comp: 'Component') -> str:
    return str(comp.no) if getattr(comp, "no", None) is not None else str(comp.id)

# --- TOP부터 하위 트리 전체 출력 ---
def format_tree_all_nodes(components: Dict[str, 'Component']) -> str:
    output_lines: List[str] = []

    # 1) TOP 찾기
    top = next((c for c in components.values() if getattr(c, "status", "") == "TOP"), None)
    if not top:
        return "No TOP component found."

    visited = set()

    def dfs(node: 'Component'):
        nid = getattr(node, "id", None) or id(node)
        if nid in visited:
            return
        visited.add(nid)

        children = _resolve_children(node, components)
        # 첫 줄: 노드 no(or id), "type", 자식 수
        output_lines.append(f'{_no_or_id(node)},"{node.type}",{len(children)}')
        # 다음 줄들: 자식 no(or id)
        for ch in children:
            output_lines.append(_no_or_id(ch))

        # 자식들 재귀
        for ch in children:
            dfs(ch)

    # TOP 포함해서 전체 내려가기
    dfs(top)

    return "\n".join(output_lines)

# TOP의 child compnent에서 로직 연산
def write_top_children_structure(components: dict) -> list:
    output_lines = []

    # 1. Find the TOP component
    top_comp = next((comp for comp in components.values() if comp.status == "TOP"), None)
    if not top_comp:
        print("No component with status 'TOP' found.")
        return []

    # 2. Iterate over each child of TOP
    for child in top_comp.child:
        # Skip if child is marked as exception
        if child.exception:
            continue

        # 2-1. Append header line: ID, "type", number of children
        output_lines.append(f'{child.no},"{child.type}",{len(child.child)}\n')

        # 2-2. Append each child ID in new line
        for sub_child in child.child:
            if not sub_child.exception:
                output_lines.append(f'{sub_child.no}\n')

    return output_lines



### aims

def make_init_kft(filename: str):
    # Define the initial content of the .kft file
    text = textwrap.dedent("""\
        "#KIRAP_TREE Version 3.5"
        "Title=",""
        "UserName=","isa"
        "DataFileName=",""
        "RecoveryFileName=",""
        "Comments=",""
        "#NoXEvent=",
        "#XEventData"
        "#TreeLogic"
        -1,"?",0
        " "
        "Continue"
        "#NoPage=",-1
        " "
        "Continue"
        "NoEventOmega=",-1
        "NoEventPhi=",-1
        " "
        "End"
    """)

    with open(filename, 'w', encoding='utf-8') as file:
        file.write(text)
    print(f"파일이 생성되었습니다: {filename}")

def insert_components_after_xeventdata(filename: str, components: dict):
    # 1. Read all lines from the file
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # 2. Filter valid components (exception == False)
    valid_components = [comp for comp in components.values() if not comp.exception]
    count = len(valid_components)

    # 3. Update the "#NoXEvent=" line to be like: "#NoXEvent=",62
    for i, line in enumerate(lines):
        if line.strip().startswith('"#NoXEvent="'):
            lines[i] = f'"#NoXEvent=",{count}\n'
            break

    # 4. Find the index right after "#XEventData"
    insert_index = None
    for i, line in enumerate(lines):
        if line.strip().strip('"') == "#XEventData":
            insert_index = i + 1
            break

    if insert_index is None:
        print('"#XEventData" not found in the file.')
        return

    # 5. Create lines for each valid component (sorted by comp.no)
    new_lines = []
    for comp in sorted(valid_components, key=lambda c: c.no):
        new_lines.append(f'{comp.no},"{comp.name}","{comp.type}",0,0\n')
        new_lines.append(f'0,0,{comp.lamda},0,0,"L",0,"","",{comp.factor},0,0\n')
        new_lines.append(f'"{comp.description}"\n')
        new_lines.append(f'""\n')

    # 6. Insert and write back to file
    updated_lines = lines[:insert_index] + new_lines + lines[insert_index:]
    with open(filename, 'w', encoding='utf-8') as f:
        f.writelines(updated_lines)

    print(f"#NoXEvent={count} and component data (sorted by no) inserted into '{filename}'.")

# 작성한 로직 파일을 kft 파일에 삽입하는 코드
def insert_logic_after_treelogic(base_file: str, logic_file: str):
    with open(base_file, 'r', encoding='utf-8') as f:
        base_lines = f.readlines()

    with open(logic_file, 'r', encoding='utf-8') as f:
        logic_lines = f.readlines()

    # '#TreeLogic'을 포함하는 줄을 찾아도 매칭되게 수정
    insert_index = None
    for i, line in enumerate(base_lines):
        if "#TreeLogic" in line:  # 부분 문자열로 비교
            insert_index = i + 1
            break

    if insert_index is None:
        print('"#TreeLogic" not found in the base file.')
        return

    updated_lines = base_lines[:insert_index] + logic_lines + base_lines[insert_index:]

    with open(base_file, 'w', encoding='utf-8') as f:
        f.writelines(updated_lines)

    print(f'Inserted content of "{logic_file}" after "#TreeLogic" in "{base_file}".')



def save_output_to_file(output: str, filename: str):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(output)


def create_basic_event(components: dict):
    create_pump_status_gates(components)
    create_valve_status_gates(components)
    create_tank_status_gates(components)
    create_grouped_ccf_components(components)
