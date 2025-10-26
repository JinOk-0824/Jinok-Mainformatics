from system_class_define import Component  # class import
from typing import Dict, List
from system_class_define import *
from ex_test import *
from typing import Union




def create_basic_event_gates(components: Dict[str, 'Component']) -> Dict[str, 'Component']:
    """
    1. type == 'B'인 Component를 대상으로
    2. 'GAF_' + component.id로 새로운 gate 컴포넌트를 생성하고 type='*'로 설정
    3. 원래 컴포넌트의 parent를 새로운 gate의 id로 교체
    4. 원래 parent 컴포넌트의 child에서 원래 컴포넌트는 제거, 새로운 gate는 추가
    """
    new_components = {}
    existing_ids = set(components.keys())

    for comp in list(components.values()):
        if comp.type == "B":
            # 1. 새 Gate 컴포넌트 ID/이름
            gate_id = f"GAF_{comp.id}"
            gate_name = gate_id

            if gate_id in existing_ids or gate_id in new_components:
                continue  # 중복 방지

            # 2. 새 컴포넌트 생성 (원본 복사 + type만 '+')
            gate_comp = Component(
                id=gate_id,
                name=gate_name,
                parent=comp.parent.copy(),
                child=[comp],
                type="+",
                component="",
                status="",
                failtype="",
                performance=0.0,
                description=f"Basic event gate for {comp.id}",
                lamda=0.0,
                factor=0.0,
                ccf=False,
                exception=False
            )

            # 3. 원래 컴포넌트의 parent를 gate로 교체
            comp.parent = [gate_comp]

            # 4. gate의 parent 컴포넌트(child에서 comp 제거, gate 추가)
            for parent_comp in gate_comp.parent:
                if comp in parent_comp.child:
                    parent_comp.child.remove(comp)
                if gate_comp not in parent_comp.child:
                    parent_comp.child.append(gate_comp)

            # 5. 등록
            new_components[gate_id] = gate_comp

            # 디버깅 출력 (선택)
            print(f"Created Basic Gate: {gate_id} for Component: {comp.id}")

    # 원래 components에 병합
    components.update(new_components)
    return components


# 병렬 게이트 만들기
def create_parallel_gate_and_update(components: Dict[str, 'Component']) -> Dict[str, 'Component']:
    """
    1. child가 2개 이상인 component 찾기
    2. 'GP_' + child 이름들로 새 component 생성
    3. child의 부모 ID가 모두 같으면 → 새 컴포넌트의 parent로 설정
       아니라면 warning 출력, 원래 child는 제외하고 새 gate만 child에 넣음
    4. child의 type이 B가 아닌 경우, 그 하위의 B까지 내려가면서 performance 누적
       누적합이 100 초과되는 n번째 위치를 게이트 type에 기록
    """
    new_components = {}
    existing_ids = set(components.keys())

    for comp in list(components.values()):
        if len(comp.child) < 2:
            continue

        try:
            child_names = [child.name for child in comp.child]
        except AttributeError:
            print(f"Skipping invalid child in component {comp.id}")
            continue

        gate_id = "GP_" + "_".join(child_names)
        gate_name = gate_id

        if gate_id in existing_ids or gate_id in new_components:
            print(f"Gate {gate_id} already exists. Skipping.")
            continue

        # 부모 ID 수집
        parent_ids = [p.id for c in comp.child for p in getattr(c, 'parent', []) if isinstance(p, Component)]
        unique_parents = list(set(parent_ids))
        gate_parent = [components[unique_parents[0]]] if len(unique_parents) == 1 else []

        if not gate_parent:
            print(f"⚠️ Children of component {comp.id} have different parents: {unique_parents}")

        # 💡 Performance 누적 계산
        performance_sum = 0
        threshold_index = None

        for idx, ch in enumerate(comp.child, start=1):
            target = ch

            # B-type이 될 때까지 내려가기
            while target and target.type != "B":
                if target.child:
                    target = target.child[0]
                else:
                    break  # 더 이상 child 없음

            if target and hasattr(target, 'performance'):
                performance_sum += target.performance
                if performance_sum >= 100 and threshold_index is None:
                    threshold_index = idx

        gate_type = str(threshold_index) if threshold_index else "+"

        # 새 게이트 컴포넌트 생성
        gate_comp = Component(
            id=gate_id,
            name=gate_name,
            parent=gate_parent,
            child=comp.child.copy(),
            type=gate_type,
            component="",
            status="GP",
            failtype="",
            performance=0.0,
            description=f"Parallel gate for children of {comp.id}",
            lamda=0.0,
            factor=0.0,
            ccf=False,
            exception=False
        )

        # 원래 컴포넌트의 child를 새 게이트로 교체
        comp.child = [gate_comp]

        # 디버깅 출력
        print(f"🔄 Updated Component: {comp.id}")
        print(f"🆕 Created Parallel Gate: {gate_id} with type: {gate_type}")

        new_components[gate_id] = gate_comp

    components.update(new_components)
    return components

# def create_parallel_gate_and_update(components: Dict[str, 'Component']) -> Dict[str, 'Component']:
#     """
#     1. child가 2개 이상인 component 찾기
#     2. 'GP_' + child 이름들로 새 component 생성
#     3. child의 부모 ID가 모두 같으면 → 새 컴포넌트의 parent로 설정
#        아니라면 warning 출력, 원래 child는 제외하고 새 gate만 child에 넣음
#     4. 변경된 컴포넌트 ID, 새 gate ID 출력
#     """
#     new_components = {}
#     existing_ids = set(components.keys())

#     for comp in list(components.values()):
#         if len(comp.child) < 2:
#             continue

#         try:
#             child_names = [child.name for child in comp.child]
#             child_ids = [child.id for child in comp.child]
#         except AttributeError:
#             print(f"Skipping invalid child in component {comp.id}")
#             continue

#         gate_name = "GP_" + "_".join(child_names)
#         gate_id = gate_name

#         if gate_id in existing_ids or gate_id in new_components:
#             print(f"Gate {gate_id} already exists. Skipping.")
#             continue

#         # 부모 ID 수집
#         parent_ids = [p.id for c in comp.child for p in getattr(c, 'parent', []) if isinstance(p, Component)]
#         unique_parents = list(set(parent_ids))

#         if len(unique_parents) == 1:
#             gate_parent = [components[unique_parents[0]]]
#         else:
#             print(f"Children of component {comp.id} have different parents: {unique_parents}")
#             gate_parent = []

#         # 새 게이트 컴포넌트 생성
#         gate_comp = Component(
#             id=gate_id,
#             name=gate_name,
#             parent=gate_parent,
#             child=comp.child.copy(),
#             type="+",
#             component="",
#             status="GP",
#             failtype="",
#             performance=0.0,
#             description=f"Parallel gate for children of {comp.id}",
#             lamda=0.0,
#             factor=0.0,
#             ccf=False,
#             exception=False
#         )

#         # 원래 컴포넌트의 child를 새 게이트로 교체
#         comp.child = [gate_comp]

#         # 출력
#         print(f"Updated Component: {comp.id}")
#         print(f"Created Parallel Gate: {gate_id}")

#         new_components[gate_id] = gate_comp

#     components.update(new_components)
#     return components



# No flow gate

def create_no_flow_gates(components: Dict[str, 'Component']) -> Dict[str, 'Component']:
    """
    Generate 'No flow' gates starting from the TOP component.
    Recursively creates GAF_No_flow_X components until no valid B-type child is found.
    """
    no_flow_counter = 1
    new_components = {}

    # 1. TOP component 찾기
    top_comp = next((comp for comp in components.values() if comp.status == "TOP"), None)
    if not top_comp:
        print("No TOP component found.")
        return components

    current_parent = top_comp

    while True:
        if not current_parent.child:
            print(f"No more children to process under {current_parent.id}. Stopping.")
            break

        # 여러 자식이 있을 경우를 위해 복사
        children = current_parent.child[:]
        valid_gate_created = False  # 이번 반복에서 게이트 생성 여부

        for child in children:
            walker = child

            # 4. type == "B"가 나올 때까지 탐색
            while walker and walker.type != "B":
                if not walker.child:
                    walker = None
                    break
                walker = walker.child[0]

            if not walker or not walker.child:
                print(f"No valid B-type component with children found under {child.id}")
                continue

            # 2. GAF_No_flow_X 컴포넌트 생성
            gate_id = f"GAF_No_flow_{no_flow_counter}"
            gate_name = gate_id
            gate_comp = Component(
                id=gate_id,
                name=gate_name,
                parent=[current_parent],
                child=walker.child.copy(),
                type="+",
                component="",
                status="",
                failtype="",
                performance=0.0,
                description=f"No Flow Gate {no_flow_counter}",
                lamda=0.0,
                factor=0.0,
                ccf=False,
                exception=False
            )

            # 3. walker의 child -> gate로 이동, walker는 child 비우기
            for ch in gate_comp.child:
                if walker in ch.parent:
                    ch.parent.remove(walker)
                ch.parent.append(gate_comp)

            walker.child = []

            # 4. 기존 parent의 child에서 walker 제거, gate 추가
            if walker in current_parent.child:
                current_parent.child.remove(walker)
            current_parent.child.append(gate_comp)

            # 등록
            new_components[gate_id] = gate_comp
            print(f"Created No Flow Gate: {gate_id}")
            no_flow_counter += 1

            # 다음 반복에 이 gate를 parent로 사용
            current_parent = gate_comp
            valid_gate_created = True
            break  # 한 번에 하나의 게이트만 처리

        if not valid_gate_created:
            print(f"Finished: No more valid B-type children from {current_parent.id}")
            break

    # 병합
    components.update(new_components)
    return components


def remove_from_b_type_parents(components: Dict[str, 'Component']) -> Dict[str, 'Component']:
    """
    Remove components from parents whose type is 'B'.
    If a component has multiple parents, and any parent has type 'B',
    it removes the component from that parent's child list.
    """
    removed_count = 0

    # 1. 모든 컴포넌트 탐색
    for comp in components.values():
        # 2. parent가 2개 이상인 경우만 검사
        if len(comp.parent) >= 2:
            for parent in comp.parent[:]:  # 복사본으로 순회
                if parent.type == "B":
                    # 3. 부모(parent)의 child에서 현재 컴포넌트(comp) 제거
                    if comp in parent.child:
                        parent.child.remove(comp)
                        removed_count += 1
                        print(f"Removed {comp.id} from B-type parent {parent.id}")

    print(f"Cleaned {removed_count} invalid parent-child connections.")
    return components
