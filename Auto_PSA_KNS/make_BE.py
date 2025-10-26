from system_class_define import Component  # class import
from typing import Dict, List
from system_class_define import *
from ex_test import *
from typing import Union




# CCF 생성
def create_grouped_ccf_components(components: Dict[str, 'Component']) -> Dict[str, 'Component']:
    """
    그룹 기반으로 CCF 컴포넌트를 한 개만 생성 (N개 컴포넌트 -> 1개 게이트)
    """
    new_components = {}
    visited = set()

    for comp in components.values():
        if comp.ccf and comp.id not in visited:
            # BFS로 연결된 CCF 그룹 찾기
            group = set()
            queue = [comp]

            while queue:
                current = queue.pop()
                if current.id in visited:
                    continue
                visited.add(current.id)
                group.add(current)
                for related in current.ccf_re:
                    if related.ccf and related.id not in visited:
                        queue.append(related)

            if len(group) < 2:
                continue  # 혼자면 의미 없음

            group_ids = sorted([c.id for c in group])
            ccf_id = f"CCF_{'_'.join(group_ids)}"

            # parent: 그룹 내 모든 parent들의 union
            parent_set = set()
            for c in group:
                parent_set.update(c.parent)

            # 새 컴포넌트 생성
            ccf_gate = Component(
                id=ccf_id,
                name=ccf_id,
                parent=list(parent_set),
                child=[],
                type="B",
                component="CCF",
                status="",
                failtype="",
                performance=0.0,
                description=f"CCF Gate for {', '.join(group_ids)}",
                lamda=0.0,
                factor=0.0,
                ccf=False,
                ccf_re=[],
                exception=False
            )

            # 각 parent에 자식으로 CCF 게이트 추가
            for p in parent_set:
                if ccf_gate not in p.child:
                    p.child.append(ccf_gate)

            new_components[ccf_id] = ccf_gate
            print(f"Created Grouped CCF Gate: {ccf_id}")
            print(f"  └ Group: {group_ids}")
            print(f"  └ Parent IDs: {[p.id for p in parent_set]}")

    components.update(new_components)
    return components


# Basic Event 생성

def create_pump_status_gates(components: Dict[str, 'Component']) -> Dict[str, 'Component']:
    new_components = {}

    for comp in components.values():
        if comp.type == "B" and comp.component == "pump":
            # 1. 상태에 따라 복제 ID 결정
            if comp.status == "run":
                clone_id = f"{comp.id}_FTR"
            elif comp.status == "stop":
                clone_id = f"{comp.id}_FTS"
            else:
                continue  # 상태가 run 또는 stop이 아닐 경우 건너뜀

            # 이미 존재하면 스킵
            if clone_id in components or clone_id in new_components:
                print(f"Already exists: {clone_id}")
                continue

            # 2. 컴포넌트 복사 생성
            clone_pump = Component(
                id=clone_id,
                name=clone_id,
                parent=comp.parent.copy(),
                child=[],
                type=comp.type,
                component=comp.component,
                status=comp.status,
                failtype=comp.failtype,
                performance=comp.performance,
                description=f"Cloned from {comp.id}",
                lamda=comp.lamda,
                factor=comp.factor,
                ccf=False,
                exception=comp.exception
            )

            new_components[clone_id] = clone_pump
            print(f"Created: {clone_id}")

            # 3. 부모 컴포넌트의 child에 clone 추가
            for parent in comp.parent:
                if clone_pump not in parent.child:
                    parent.child.append(clone_pump)
                    print(f"Added {clone_id} to parent {parent.id}.child")

    # 딕셔너리 병합
    components.update(new_components)
    return components


def create_valve_status_gates(components: Dict[str, 'Component']) -> Dict[str, 'Component']:
    """
    1. component.type == 'B' and component == 'valve'인 컴포넌트를 찾는다.
    2. status == 'open'이면 ID+'_FTO'를, status == 'close'이면 ID+'_FTC' 컴포넌트를 복사 생성한다.
    3. 복사된 컴포넌트의 ID를 해당 컴포넌트의 parent의 child에 추가한다.
    """
    new_components = {}
    existing_ids = set(components.keys())

    for comp in components.values():
        if comp.type == "B" and comp.component.lower() == "valve":
            # 상태에 따른 후속 컴포넌트 ID 결정
            if comp.status.lower() == "open":
                suffix = "_FTO"
            elif comp.status.lower() == "close":
                suffix = "_FTC"
            else:
                print(f"VALVE {comp.id} has unknown status: {comp.status}")
                continue

            clone_id = comp.id + suffix

            if clone_id in existing_ids or clone_id in new_components:
                print(f"Duplicate ID skipped: {clone_id}")
                continue

            # 컴포넌트 복사 (shallow copy + ID/이름만 변경)
            clone_valve = Component(
                id=clone_id,
                name=clone_id,
                parent=comp.parent.copy(),
                child=[],
                type=comp.type,
                component=comp.component,
                status=comp.status,
                failtype=comp.failtype,
                performance=comp.performance,
                description=f"Cloned from {comp.id}",
                lamda=comp.lamda,
                factor=comp.factor,
                ccf=False,
                exception=comp.exception
            )

            # 부모들의 child 리스트에 추가
            for parent in comp.parent:
                if clone_valve not in parent.child:
                    parent.child.append(clone_valve)

            new_components[clone_id] = clone_valve
            print(f"Created VALVE Gate: {clone_id} for {comp.id} [{comp.status}]")

    # 원본 components에 병합
    components.update(new_components)
    return components


def create_tank_status_gates(components: Dict[str, 'Component']) -> Dict[str, 'Component']:
    """
    1. component.type == 'B' and component == 'tank'인 컴포넌트를 찾는다.
    2. ID+'_FTR' 이름을 가진 새로운 컴포넌트를 생성한다.
    3. 생성된 컴포넌트를 원래 컴포넌트의 parent.child에 추가한다.
    """
    new_components = {}
    existing_ids = set(components.keys())

    for comp in components.values():
        if comp.type == "B" and comp.component.lower() == "tank":
            clone_id = comp.id + "_FTR"



            if clone_id in existing_ids or clone_id in new_components:
                print(f"⚠️ Gate ID already exists: {clone_id}")
                continue

            # 새 컴포넌트 생성
            tank_comp = Component(
                id=clone_id,
                name=clone_id,
                parent=comp.parent.copy(),
                child=[],
                type=comp.type,
                component=comp.component,
                status=comp.status,
                failtype=comp.failtype,
                performance=comp.performance,
                description=f"Cloned from {comp.id}",
                lamda=comp.lamda,
                factor=comp.factor,
                ccf=False,
                exception=comp.exception
            )

            # 부모의 child에 이 gate 컴포넌트 추가
            for parent in comp.parent:
                if tank_comp not in parent.child:
                    parent.child.append(tank_comp)

            # 등록
            new_components[clone_id] = tank_comp
            print(f"Created TANK Gate: {clone_id} for {comp.id}")

    # 병합
    components.update(new_components)
    return components